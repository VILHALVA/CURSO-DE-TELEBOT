local config = require 'config'
local u = require 'utilities'
local api = require 'methods'
local db = require 'database'
local locale = require 'languages'
local i18n = locale.translate

local plugin = {}

local function is_whitelisted(chat_id, text)
	local set = ('chat:%d:whitelist'):format(chat_id)
	local links = db:smembers(set)
	if links and next(links) then
		for i=1, #links do
			if text:find(links[i]:lower():gsub('%-', '%%-')) then
				return true
			end
		end
	end
end

local function getAntispamWarns(chat_id, user_id)
	local max_allowed = (db:hget('chat:'..chat_id..':antispam', 'warns')) or config.chat_settings['antispam']['warns']
	max_allowed = tonumber(max_allowed)
	local warns_received = (db:hincrby('chat:'..chat_id..':spamwarns', user_id, 1))
	warns_received = tonumber(warns_received)

	return warns_received, max_allowed
end

local humanizations = {
	['ban'] = i18n('banned'),
	['kick'] = i18n('kicked'),
	['mute'] = i18n('muted'),
	['links'] = i18n('telegram.me links'),
	['forwards'] = i18n('Channels messages')
}

function plugin.onEveryMessage(msg)
	if not msg.inline and msg.spam and msg.chat.id < 0 and not msg.cb and not msg.from.admin then
		local status = db:hget('chat:'..msg.chat.id..':antispam', msg.spam)
		if status and status ~= 'alwd' then
			local whitelisted
			if msg.spam == 'links' then
				whitelisted = is_whitelisted(msg.chat.id, msg.text:lower())
			--[[elseif msg.forward_from_chat then
				if msg.forward_from_chat.type == 'channel' then
					whitelisted = is_whitelisted_channel(msg.chat.id, msg.forward_from_chat.id)
				end]]
			end

			if not whitelisted then
				local hammer_text = nil
				local name = u.getname_final(msg.from)
				local warns_received, max_allowed = getAntispamWarns(msg.chat.id, msg.from.id) --also increases the warns counter

				if warns_received >= max_allowed then
					if status == 'del' then
						api.deleteMessage(msg.chat.id, msg.message_id)
					end

					local action = (db:hget('chat:'..msg.chat.id..':antispam', 'action')) or config.chat_settings['antispam']['action']

					local res
					if action == 'ban' then
						res = api.banUser(msg.chat.id, msg.from.id)
					elseif action == 'kick' then
						res = api.kickUser(msg.chat.id, msg.from.id)
					elseif action == 'mute' then
						res = api.muteUser(msg.chat.id, msg.from.id)
					end
					if res then
						db:hdel('chat:'..msg.chat.id..':spamwarns', msg.from.id) --remove spam warns
						api.sendMessage(msg.chat.id,
							i18n('%s %s for <b>spam</b>! (%d/%d)'):format(name, humanizations[action], warns_received, max_allowed), 'html')
					end
				else
					if status == 'del' and warns_received == max_allowed - 1 then
						api.deleteMessage(msg.chat.id, msg.message_id)
						api.sendReply(msg, i18n('%s, spam is not allowed here. The next time you will be restricted'):format(name),
							'html')
					elseif status == 'del' then
						--just delete
						api.deleteMessage(msg.chat.id, msg.message_id)
					elseif status ~= 'del' then
						api.sendReply(msg, i18n('%s, this kind of spam is not allowed in this chat (<b>%d/%d</b>)')
							:format(name, warns_received, max_allowed), 'html')
					end
				end
				local name_pretty = {links = i18n("telegram.me link"), forwards = i18n("message from a channel")}
				u.logEvent('spamwarn', msg,
					{hammered = hammer_text, warns = warns_received, warnmax = max_allowed, spam_type = name_pretty[msg.spam]})
			end
		end
	end

	if msg.edited then return false end
	return true
end

local function toggleAntispamSetting(chat_id, key)
	local hash = 'chat:'..chat_id..':antispam'
	local current = db:hget(hash, key) or config.chat_settings['antispam'][key]

	local next_state = { ['alwd'] = 'warn', ['warn'] = 'del', ['del'] = 'alwd' }
	local new = next_state[current] or 'alwd'
	db:hset(hash, key, new)

	if key == 'forwards' then
		if new == 'alwd' then
			return i18n("forwards are allowed")
		elseif new == 'warn' then
			return i18n("warn for forwards")
		elseif new == 'del' then
			return i18n("forwards will be deleted")
		end
	elseif key == 'links' then
		if new == 'alwd' then
			return i18n("links are allowed")
		elseif new == 'warn' then
			return i18n("warn for links")
		elseif new == 'del' then
			return i18n("links will be deleted")
		end
	end
end

local function changeWarnsNumber(chat_id, action)
	local hash = 'chat:'..chat_id..':antispam'
	local key = 'warns'
	local current = (db:hget(hash, key)) or config.chat_settings['antispam'][key]
	current = tonumber(current)
	if current < 1 then
		current = 1
		db:hset(hash, key, 1)
	end

	if current == 1 and action == 'dim' then
		return i18n("You can't go lower")
	elseif current == 7 and action == 'raise' then
		return i18n("You can't go higher")
	else
		local new
		if action == 'dim' then
			new = db:hincrby(hash, key, -1)
		elseif action == 'raise' then
			new = db:hincrby(hash, key, 1)
		end
		return i18n("New value: %d"):format(new)
	end
end

local function changeAction(chat_id)
	local hash = 'chat:'..chat_id..':antispam'
	local key = 'action'
	local current = (db:hget(hash, key)) or config.chat_settings['antispam'][key]
	local new_action

	if current == 'ban' then new_action = 'kick'
	elseif current == 'kick' then new_action = 'mute'
	elseif current == 'mute' then new_action = 'ban' end

	db:hset(hash, key, new_action)

	return '✅'
end

local function get_alert_text(key)
	if key == 'links' then
		return i18n("Allow/forbid telegram.me links")
	elseif key == 'forwards' then
		return i18n("Allow/forbid forwarded messages from channels")
	elseif key == 'warns' then
		return i18n("Set how many times the bot should warn the user before kick/ban him")
	else
		return i18n("Description not available")
	end
end

local function doKeyboard_antispam(chat_id)
	local keyboard = {inline_keyboard = {}}

	for field, _ in pairs(config.chat_settings['antispam']) do
		if field == 'links' or field == 'forwards' then
			local icon = '✅'
			local status = (db:hget('chat:'..chat_id..':antispam', field)) or config.chat_settings['antispam'][field]
			if status == 'warn' then
				icon = '❌'
			elseif status == 'del' then icon = '🗑' end
			local line = {
				{text = i18n(humanizations[field] or field), callback_data = 'antispam:alert:'..field..':'..locale.language},
				{text = icon, callback_data = 'antispam:toggle:'..field..':'..chat_id}
			}
			table.insert(keyboard.inline_keyboard, line)
		end
	end

	local warns = (db:hget('chat:'..chat_id..':antispam', 'warns')) or config.chat_settings['antispam']['warns']
	local action = (db:hget('chat:'..chat_id..':antispam', 'action')) or config.chat_settings['antispam']['action']

	if action == 'kick' then
		action = i18n("Kick 👞")
	elseif action == 'ban' then
		action = i18n("Ban 🔨")
	elseif action == 'mute' then
		action = i18n("Mute 👁")
	end

	local line = {
		{text = 'Warns: '..warns, callback_data = 'antispam:alert:warns:'..locale.language},
		{text = '➖', callback_data = 'antispam:toggle:dim:'..chat_id},
		{text = '➕', callback_data = 'antispam:toggle:raise:'..chat_id},
		{text = action, callback_data = 'antispam:toggle:action:'..chat_id}
	}

	table.insert(keyboard.inline_keyboard, line)

	--back button
	table.insert(keyboard.inline_keyboard, {{text = '🔙', callback_data = 'config:back:'..chat_id}})

	return keyboard
end

local function get_url(text, entity)
	return text:sub(entity.offset + 1, entity.offset + entity.length)
end

local function urls_table(entities, text)
	local links = {}
	for _, entity in pairs(entities) do
		if entity.type == 'url' then
			local url = get_url(text, entity):gsub(' ', ''):gsub('https?://', ''):gsub('www.', '')
			table.insert(links, url)
		end
	end

	return links
end

function plugin.onCallbackQuery(msg, blocks)

	if blocks[1] == 'alert' then
		if config.available_languages[blocks[3]] then
			locale.language = blocks[3]
		end
		local text = get_alert_text(blocks[2])
		api.answerCallbackQuery(msg.cb_id, text, true, config.bot_settings.cache_time.alert_help)
	else

		local chat_id = msg.target_id
		if not u.is_allowed('config', chat_id, msg.from) then
			api.answerCallbackQuery(msg.cb_id, i18n("You're no longer an admin"))
		else
			local antispam_first = i18n([[*Anti-spam settings*
Choose which kind of spam you want to forbid
• ✅ = *Allowed*
• ❌ = *Not allowed*
• 🗑 = *Delete*
When set on `delete`, the bot doesn't warn users until they are about to be kicked/banned/muted (at the second-to-last warning)
]])

			local keyboard, text

			if blocks[1] == 'toggle' then
				if blocks[2] == 'forwards' or blocks[2] == 'links' then
					text = toggleAntispamSetting(chat_id, blocks[2])
				else
					if blocks[2] == 'raise' or blocks[2] == 'dim' then
						text = changeWarnsNumber(chat_id, blocks[2])
					elseif blocks[2] == 'action' then
						text = changeAction(chat_id, blocks[2])
					end
				end
			end

			keyboard = doKeyboard_antispam(chat_id)
			api.editMessageText(msg.chat.id, msg.message_id, antispam_first, true, keyboard)
			if text then api.answerCallbackQuery(msg.cb_id, text) end
		end
	end
end

local function edit_channels_whitelist(chat_id, list, action)

	local channels = {valid = {}, not_valid ={}}
	local for_entered
	local set = ('chat:%d:chanwhitelist'):format(chat_id)
	local res
	for channel_id in list:gmatch('-%d+') do
		if action == 'add' then
			res = db:sadd(set, channel_id)
		elseif action == 'rem' then
			res = db:srem(set, channel_id)
		end

		if res == 1 then
			table.insert(channels.valid, channel_id)
		elseif res == 0 then
			table.insert(channels.not_valid, channel_id)
		end

		for_entered = true
	end

	return for_entered, channels
end

function plugin.onTextMessage(msg, blocks)
	if u.is_allowed('texts', msg.chat.id, msg.from) then
		if (blocks[1] == 'wl' or blocks[1] == 'whitelist') and blocks[2] then
			if blocks[2] == '-' then
				local set = ('chat:%d:whitelist'):format(msg.chat.id)
				local n = db:scard(set) or 0
				local text
				if n == 0 then
					text = i18n("_The whitelist was already empty_")
				else
					db:del(set)
					text = i18n("*Whitelist cleaned*\n%d links have been removed"):format(n)
				end
				api.sendReply(msg, text, true)
			else
				local text
				if msg.entities then
					local links = urls_table(msg.entities, msg.text)
					if not next(links) then
						text = i18n("_I can't find any url in this message_")
					else
						local new = db:sadd(('chat:%d:whitelist'):format(msg.chat.id), unpack(links))
						text = i18n("%d link(s) will be whitelisted"):format(#links - (#links - new))
						if new ~= #links then
							text = text..i18n("\n%d links were already in the list"):format(#links - new)
						end
					end
				else
					text = i18n("_I can't find any url in this message_")
				end
				api.sendReply(msg, text, true)
			end
		end
		if (blocks[1] == 'wl' or blocks[1] == 'whitelist') and not blocks[2] then
			local links = db:smembers(('chat:%d:whitelist'):format(msg.chat.id))
			if not next(links) then
				api.sendReply(msg, i18n("_The whitelist is empty_.\nUse `/wl [links]` to add some links to the whitelist"), true)
			else
				local text = i18n("Whitelisted links:\n\n")
				for i=1, #links do
					text = text..'• '..links[i]..'\n'
				end
				api.sendReply(msg, text)
			end
		end
		if blocks[1] == 'unwl' or blocks[1] == 'unwhitelist' then
			local text
			if msg.entities then
				local links = urls_table(msg.entities, msg.text)
				if not next(links) then
					text = i18n("_I can't find any url in this message_")
				else
					local removed = db:srem(('chat:%d:whitelist'):format(msg.chat.id), unpack(links))
					text = i18n("%d link(s) removed from the whitelist"):format(removed)
					if removed ~= #links then
						text = text..i18n("\n%d links were already in the list"):format(#links - removed)
					end
				end
			else
				text = i18n("_I can't find any url in this message_")
			end
			api.sendReply(msg, text, true)
		end
		if blocks[1] == 'funwl' then --force the unwhitelist of a link
			db:srem(('chat:%d:whitelist'):format(msg.chat.id), blocks[2])
			api.sendReply(msg, 'Done')
		end
		if blocks[1] == 'wlchan' and not blocks[2] then
			local channels = db:smembers(('chat:%d:chanwhitelist'):format(msg.chat.id))
			if not next(channels) then
				api.sendReply(msg, i18n("_Whitelist of channels empty_"), true)
			else
				api.sendReply(msg, i18n("*Whitelisted channels:*\n%s"):format(table.concat(channels, '\n')), true)
			end
		end
		if blocks[1] == 'wlchan' and blocks[2] then
			local for_entered, channels = edit_channels_whitelist(msg.chat.id, blocks[2], 'add')

			if not for_entered then
				api.sendReply(msg, i18n("_I can't find a channel ID in your message_"), true)
			else
				local text = ''
				if next(channels.valid) then
					text = text..("*Channels whitelisted*: `%s`\n"):format(table.concat(channels.valid, ', '))
				end
				if next(channels.not_valid) then
					text = text..("*Channels already whitelisted*: `%s`\n"):format(table.concat(channels.not_valid, ', '))
				end

				api.sendReply(msg, text, true)
			end
		end
		if blocks[1] == 'unwlchan' then
			local for_entered, channels = edit_channels_whitelist(msg.chat.id, blocks[2], 'rem')

			if not for_entered then
				api.sendReply(msg, i18n("_I can't find a channel ID in your message_"), true)
			else
				local text = ''
				if next(channels.valid) then
					text = text..("*Channels unwhitelisted*: `%s`\n"):format(table.concat(channels.valid, ', '))
				end
				if next(channels.not_valid) then
					text = text..("*Channels not whitelisted*: `%s`\n"):format(table.concat(channels.not_valid, ', '))
				end

				api.sendReply(msg, text, true)
			end
		end
	end
end

plugin.triggers = {
	onCallbackQuery = {
		'^###cb:antispam:(toggle):(%w+):(-?%d+)$',
		'^###cb:antispam:(alert):(%w+):([%w_]+)$',
		'^###cb:(config):antispam:(-?%d+)$'
	},
	onTextMessage = {
		config.cmd..'(wl) (.+)$',
		config.cmd..'(whitelist) (.+)$',
		--config.cmd..'(wlchan) (.+)$',
		config.cmd..'(unwl) (.+)$',
		config.cmd..'(unwhitelist) (.+)$',
		--config.cmd..'(unwlchan) (.+)$',
		config.cmd..'(wl)$',
		config.cmd..'(whitelist)$',
		--config.cmd..'(wlchan)$',
		config.cmd..'(funwl) (.+)'
	}
}

return plugin
