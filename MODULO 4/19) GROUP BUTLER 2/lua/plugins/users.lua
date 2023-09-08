local config = require 'config'
local u = require 'utilities'
local api = require 'methods'
local db = require 'database'
local locale = require 'languages'
local i18n = locale.translate

local plugin = {}

local permissions = {
	can_change_info = i18n("can't change the chat title/description/icon"),
	can_send_messages = i18n("can't send messages"),
	can_delete_messages = i18n("can't delete messages"),
	can_invite_users = i18n("can't invite users/generate a link"),
	can_restrict_members = i18n("can't restrict members"),
	can_pin_messages = i18n("can't pin messages"),
	can_promote_members = i18n("can't promote new admins"),
	can_send_media_messages = i18n("can't send photos/videos/documents/audios/voice messages/video messages"),
	can_send_other_messages = i18n("can't send stickers/GIFs/games/use inline bots"),
	can_add_web_page_previews = i18n("can't show link previews")
}

local function do_keyboard_cache(chat_id)
	local keyboard = {inline_keyboard = {{{text = i18n("🔄️ Refresh cache"), callback_data = 'recache:'..chat_id}}}}
	return keyboard
end

local function get_time_remaining(seconds)
	local final = ''
	local hours = math.floor(seconds/3600)
	seconds = seconds - (hours*60*60)
	local min = math.floor(seconds/60)
	seconds = seconds - (min*60)

	if hours and hours > 0 then
		final = final..hours..'h '
	end
	if min and min > 0 then
		final = final..min..'m '
	end
	if seconds and seconds > 0 then
		final = final..seconds..'s'
	end

	return final
end

local function get_user_id(msg, blocks)
	if msg.reply then
		return msg.reply.from.id
	elseif blocks[2] then
		if blocks[2]:match('@[%w_]+$') then --by username
			local user_id = u.resolve_user(blocks[2])
			if not user_id then
				print('username (not found)')
				return false
			else
				print('username (found)')
				return user_id
			end
		elseif blocks[2]:match('^%d+$') then --by id
			print('id')
			return blocks[2]
		elseif msg.mention_id then --by text mention
			print('text mention')
			return msg.mention_id
		else
			return false
		end
	end
end

local function do_keyboard_userinfo(user_id)
	local keyboard = {
		inline_keyboard = {
			{{text = i18n("Remove warnings"), callback_data = 'userbutton:remwarns:'..user_id}}
		}
	}

	return keyboard
end

local function get_userinfo(user_id, chat_id)
	local text = i18n([[*User ID*: `%d`
`Warnings`: *%d*
`Media warnings`: *%d*
`Spam warnings`: *%d*
]])
	local warns = (db:hget('chat:'..chat_id..':warns', user_id)) or 0
	local media_warns = (db:hget('chat:'..chat_id..':mediawarn', user_id)) or 0
	local spam_warns = (db:hget('chat:'..chat_id..':spamwarns', user_id)) or 0
	return text:format(tonumber(user_id), warns, media_warns, spam_warns)
end

function plugin.onTextMessage(msg, blocks)
	if blocks[1] == 'id' then --just for debug
		if msg.chat.id < 0 and msg.from.admin then
			api.sendMessage(msg.chat.id, string.format('`%d`', msg.chat.id), true)
		end
	end

	if msg.chat.type == 'private' then return end

	if blocks[1] == 'adminlist' then
		local adminlist = u.getAdminlist(msg.chat.id)
		if not msg.from.admin then
			api.sendMessage(msg.from.id, adminlist, 'html')
		else
			api.sendReply(msg, adminlist, 'html')
		end
	end
	if blocks[1] == 'status' then
		if msg.from.admin then
			if not blocks[2] and not msg.reply then return end
			local user_id, error_tr_id = u.get_user_id(msg, blocks)
			if not user_id then
				api.sendReply(msg, i18n(error_tr_id), true)
			else
				local res = api.getChatMember(msg.chat.id, user_id)

				if not res then
					api.sendReply(msg, i18n("That user has nothing to do with this chat"))
					return
				end
				local status = res.result.status
				local name = u.getname_final(res.result.user)
				local statuses = {
					kicked = i18n("%s is banned from this group"),
					left = i18n("%s left the group or has been kicked and unbanned"),
					administrator = i18n("%s is an admin"),
					creator = i18n("%s is the group creator"),
					unknown = i18n("%s has nothing to do with this chat"),
					member = i18n("%s is a chat member"),
					restricted = i18n("%s is a restricted")
				}
				local denied_permissions = {}
				for permission, str in pairs(permissions) do
					if res.result[permission] ~= nil and res.result[permission] == false then
						table.insert(denied_permissions, str)
					end
				end

				local text = statuses[status]:format(name)
				if next(denied_permissions) then
					text = text..i18n('\nRestrictions: <i>%s</i>'):format(table.concat(denied_permissions, ', '))
				end

				api.sendReply(msg, text, 'html')
			end
		end
	end
	if blocks[1] == 'user' then
		if not msg.from.admin then return end

		if not msg.reply
			and (not blocks[2] or (not blocks[2]:match('@[%w_]+$') and not blocks[2]:match('%d+$')
			and not msg.mention_id)) then
			api.sendReply(msg, i18n("Reply to an user or mention them by username or numerical ID"))
			return
		end

		------------------ get user_id --------------------------
		local user_id = get_user_id(msg, blocks)

		if not user_id then
			api.sendReply(msg, i18n([[I've never seen this user before.
This command works by reply, username, user ID or text mention.
If you're using it by username and want to teach me who the user is, forward me one of his messages]]), true)
			return
		end
		-----------------------------------------------------------------------------

		local keyboard = do_keyboard_userinfo(user_id)

		local text = get_userinfo(user_id, msg.chat.id)

		api.sendMessage(msg.chat.id, text, true, keyboard)
	end
	if blocks[1] == 'cache' then
		if not msg.from.admin then return end
		local hash = 'cache:chat:'..msg.chat.id..':admins'
		local seconds = db:ttl(hash)
		local cached_admins = db:scard(hash)
		local text = i18n("📌 Status: `CACHED`\n⌛ ️Remaining: `%s`\n👥 Admins cached: `%d`")
			:format(get_time_remaining(tonumber(seconds)), cached_admins)
		local keyboard = do_keyboard_cache(msg.chat.id)
		api.sendMessage(msg.chat.id, text, true, keyboard)
	end
	if blocks[1] == 'msglink' then
		if not msg.reply or not msg.chat.username then return end

		local text = string.format('[%s](https://telegram.me/%s/%d)',
			i18n("Message N° %d"):format(msg.reply.message_id), msg.chat.username, msg.reply.message_id)
		if msg.from.admin or not u.is_silentmode_on(msg.chat.id) then
			api.sendReply(msg.reply, text, true)
		else
			api.sendMessage(msg.from.id, text, true)
		end
	end
	if blocks[1] == 'leave' then
		if msg.from.admin then
			u.remGroup(msg.chat.id)
			api.leaveChat(msg.chat.id)
		end
	end
end

function plugin.onCallbackQuery(msg, blocks)
	if not msg.from.admin then
		api.answerCallbackQuery(msg.cb_id, i18n("You are not allowed to use this button")) return
	end

	if blocks[1] == 'remwarns' then
		local removed = {
			normal = db:hdel('chat:'..msg.chat.id..':warns', blocks[2]),
			media = db:hdel('chat:'..msg.chat.id..':mediawarn', blocks[2]),
			spam = db:hdel('chat:'..msg.chat.id..':spamwarns', blocks[2])
		}

		local name = u.getname_final(msg.from)
		local text = i18n("The number of warnings received by this user has been <b>reset</b>, by %s"):format(name)
		api.editMessageText(msg.chat.id, msg.message_id, text:format(name), 'html')
		u.logEvent('nowarn', msg,
			{admin = name, user = ('<code>%s</code>'):format(msg.target_id), user_id = msg.target_id, rem = removed})
	end
	if blocks[1] == 'recache' and msg.from.admin then
		local missing_sec = tonumber(db:ttl('cache:chat:'..msg.target_id..':admins') or 0)
		local wait = 600
		if config.bot_settings.cache_time.adminlist - missing_sec < wait then
			local seconds_to_wait = wait - (config.bot_settings.cache_time.adminlist - missing_sec)
			api.answerCallbackQuery(msg.cb_id,i18n(
					"The adminlist has just been updated. You must wait 10 minutes from the last refresh (wait  %d seconds)"
				):format(seconds_to_wait), true)
		else
			db:del('cache:chat:'..msg.target_id..':admins')
			u.cache_adminlist(msg.target_id)
			local cached_admins = db:smembers('cache:chat:'..msg.target_id..':admins')
			local time = get_time_remaining(config.bot_settings.cache_time.adminlist)
			local text = i18n("📌 Status: `CACHED`\n⌛ ️Remaining: `%s`\n👥 Admins cached: `%d`")
				:format(time, #cached_admins)
			api.answerCallbackQuery(msg.cb_id, i18n("✅ Updated. Next update in %s"):format(time))
			api.editMessageText(msg.chat.id, msg.message_id, text, true, do_keyboard_cache(msg.target_id))
			--api.sendLog('#recache\nChat: '..msg.target_id..'\nFrom: '..msg.from.id)
		end
	end
end

plugin.triggers = {
	onTextMessage = {
		config.cmd..'(id)$',
		config.cmd..'(adminlist)$',
		config.cmd..'(status) (.+)$',
		config.cmd..'(status)$',
		config.cmd..'(cache)$',
		config.cmd..'(msglink)$',
		config.cmd..'(user)$',
		config.cmd..'(user) (.*)',
		config.cmd..'(leave)$'
	},
	onCallbackQuery = {
		'^###cb:userbutton:(remwarns):(%d+)$',
		'^###cb:(recache):'
	}
}

return plugin
