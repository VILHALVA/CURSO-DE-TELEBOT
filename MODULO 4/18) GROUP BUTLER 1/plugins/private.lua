local function do_keybaord_credits()
	local keyboard = {}
    keyboard.inline_keyboard = {
    	{
    		{text = 'Canal', url = 'https://telegram.me/'..config.channel:gsub('@', '')},
    		{text = 'GitHub', url = 'https://github.com/'},
    		{text = 'Evalúame!', url = 'https://telegram.me/storebot?start='..bot.username},
		}
	}
	return keyboard
end

local action = function(msg, blocks, ln)
    
    if not(msg.chat.type == 'private') then return end
    
	if blocks[1] == 'ping' then
		api.sendMessage(msg.from.id, '*Pong!*', true)
	end
	if blocks[1] == 'strings' then
		if not blocks[2] then
			local file_id = db:get('trfile:EN')
			if not file_id then return end
			api.sendDocumentId(msg.chat.id, file_id, msg.message_id)
		else
			local l_code = blocks[2]
			local exists = is_lang_supported(l_code)
			if exists then
				local file_id = db:get('trfile:'..l_code:upper())
				if not file_id then return end
				api.sendDocumentId(msg.chat.id, file_id, msg.message_id)
			else
				api.sendReply(msg, lang[ln].setlang.error, true)
			end
		end
	end
	if blocks[1] == 'echo' then
		local res, code = api.sendMessage(msg.chat.id, blocks[2], true)
		if not res then
			if code == 118 then
				api.sendMessage(msg.chat.id, lang[ln].bonus.too_long)
			else
				api.sendMessage(msg.chat.id, lang[ln].breaks_markdown, true)
			end
		end
	end
	if blocks[1] == 'c' then
		if msg.chat.type ~= 'private' then
        	return
    	end
    	local text = 'This command *has been replaced!*\n\nNow you can start your message with an ! to communicate with the bot owner. Example:\n_!hello, how are you?_'
    	if config.help_group and config.help_group ~= '' then
    		text = text..'\n\nYou can also join the discussion group to ask your question/report a bug. You can join with [this link]('..config.help_group..')'
    	end
    	api.sendMessage(msg.chat.id, text, true)
    end
    if blocks[1] == '!' then
    	if msg.chat.type ~= 'private' then
        	return
    	end
        local input = blocks[2]
        local receiver = msg.from.id
        
        --allert if not feedback
        if not input and not msg.reply then
            api.sendMessage(msg.from.id, lang[ln].report.no_input)
            return
        end
        
        if msg.reply then
        	msg = msg.reply
        end
	    
	    api.forwardMessage (config.admin.owner, msg.from.id, msg.message_id)
	    api.sendMessage(receiver, lang[ln].report.sent)
	end
	if blocks[1] == 'info' then
		local keyboard = {}
		keyboard = do_keybaord_credits()
		api.sendKeyboard(msg.chat.id, '`v'..config.version..'`\n'..lang[ln].credits, keyboard, true)
	end
	if blocks[1] == 'resolve' then
		local id = res_user_group(blocks[2], msg.chat.id)
		if not id then
			message = lang[ln].bonus.no_user
		else
			message = '*'..id..'*'
		end
		api.sendMessage(msg.chat.id, message, true)
	end
end

return {
	action = action,
	triggers = {
		'^/(ping)$',
		'^/(strings)$',
		'^/(strings) (%a%a)$',
		'^/(echo) (.*)$',
--		'^/(c)%s?',
		'^(!)$',
		'^(!)(.+)',
		'^/(info)$',
		'^/(resolve) (@[%w_]+)$',
	}
}