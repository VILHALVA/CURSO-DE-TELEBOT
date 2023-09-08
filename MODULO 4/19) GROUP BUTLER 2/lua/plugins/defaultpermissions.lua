local config = require 'config'
local u = require 'utilities'
local api = require 'methods'
local db = require 'database'
local locale = require 'languages'
local i18n = locale.translate

local plugin = {}

local function toggle_permissions_setting(chat_id, key)
	local hash = 'chat:'..chat_id..':defpermissions'
	local current = (db:hget(hash, key)) or config.chat_settings['defpermissions'][key]
	local new
	if current == 'true' then new = 'false' else new = 'true' end

		local new_perm = {[key] = new}

		if new == 'true' then
				if key == 'can_send_media_messages' then
						new_perm['can_send_messages'] = 'true'
				elseif key == 'can_send_other_messages' then
						new_perm['can_send_messages'] = 'true'
						new_perm['can_send_media_messages'] = 'true'
				elseif key == 'can_add_web_page_previews' then
						new_perm['can_send_messages'] = 'true'
						new_perm['can_send_media_messages'] = 'true'
				end
		elseif new == 'false' then
				if key == 'can_send_messages' then
						new_perm['can_send_other_messages'] = 'false'
						new_perm['can_send_media_messages'] = 'false'
						new_perm['can_add_web_page_previews'] = 'false'
				elseif key == 'can_send_media_messages' then
						new_perm['can_send_other_messages'] = 'false'
						new_perm['can_add_web_page_previews'] = 'false'
				end
		end

	db:hmset(hash, new_perm)

	return '✅'
end

local function get_alert_text(key)
	if key == 'can_send_messages' then
		return i18n("Permission to send messages. If disabled, the user won't be able to send any kind of message")
	elseif key == 'can_send_media_messages' then
		return i18n(
			[[Permission to send media (audios, documents, photos, videos, video notes and voice notes). Implies the permission to send messages
			]])
	elseif key == 'can_send_other_messages' then
		return i18n(
			[[Permission to send other types of messages (GIFs, games, stickers and use inline bots). Implies the permission to send medias
			]])
	elseif key == 'can_add_web_page_previews' then
		return i18n("When disabled, user's messages with a link won't show the web page preview")
	else
		return i18n("Description not available")
	end
end

local humanizations = {
	['can_send_messages'] = i18n('Send messages'),
	['can_send_media_messages'] = i18n('Send media'),
	['can_send_other_messages'] = i18n('Send other types of media'),
	['can_add_web_page_previews'] = i18n('Show web page preview'),
}

local permissions =
{'can_send_messages', 'can_send_media_messages', 'can_send_other_messages', 'can_add_web_page_previews'}

local function doKeyboard_permissions(chat_id)
	local keyboard = {inline_keyboard = {}}

	local line, status, icon, permission
	--for field, value in pairs(config.chat_settings['defpermissions']) do
		for i=1, #permissions do --pairs() doesn't keep the order of the keys
				permission = permissions[i]
		icon = '✅'
		status = (db:hget('chat:'..chat_id..':defpermissions', permission))
			or config.chat_settings['defpermissions'][permission]
		if status == 'false' then icon = '☑️' end
		line = {
			{
				text = i18n(humanizations[permission] or permission),
				callback_data = 'defpermissions:alert:'..permission..':'..locale.language
			},
			{
				text = icon,
				callback_data = 'defpermissions:toggle:'..permission..':'..chat_id
			}
		}
		table.insert(keyboard.inline_keyboard, line)
	end

	--back button
	table.insert(keyboard.inline_keyboard, {{text = '🔙', callback_data = 'config:back:'..chat_id}})

	return keyboard
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
		if not u.can(chat_id, msg.from.id, 'can_restrict_members') then
			api.answerCallbackQuery(msg.cb_id, i18n("You don't have the permission to restrict members"))
		else
			local msg_text = i18n([[*Deafult permissions*
From this menu you can change the default permissions that will be granted when a new member join.
_Only the administrators with the permission to restrict a member can access this menu._
Tap on the name of a permission for a description of what kind of messages it will influence.
]])

			local reply_markup, popup_text, show_alert

			if blocks[1] == 'toggle' then
				popup_text = toggle_permissions_setting(chat_id, blocks[2])
			end

			reply_markup = doKeyboard_permissions(chat_id)
			local res, code, _, retry_after
			if blocks[2] then
				--if the user tapped on a keybord button, just edit the markup and not the whole message
				res, code, _, retry_after = api.editMessageReplyMarkup(msg.chat.id, msg.message_id, reply_markup)
			else
				res, code, _, retry_after = api.editMessageText(msg.chat.id, msg.message_id, msg_text, true, reply_markup)
			end

			if not res and code == 429 and retry_after then
					popup_text = i18n("Setting saved, but I can't edit the buttons because you are too fast! Wait other %d seconds")
						:format(retry_after)
					show_alert = true
			end
			if popup_text then api.answerCallbackQuery(msg.cb_id, popup_text, show_alert) end
		end
	end
end

plugin.triggers = {
	onCallbackQuery = {
		'^###cb:config:defpermissions:(-%d+)$',
		'^###cb:defpermissions:(toggle):([%w_]+):(-%d+)$',
		'^###cb:defpermissions:(alert):([%w_]+):([%w_]+)$',
	}
}

return plugin
