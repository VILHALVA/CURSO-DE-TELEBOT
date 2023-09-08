local command = 'urbandictionary <query>'
local doc = [[```
/urbandictionary <query>
Returns a definition from Urban Dictionary.
Aliases: /ud, /urban
```]]

local triggers = {
	'^/urbandictionary[@'..bot.username..']*',
	'^/ud[@'..bot.username..']*$',
	'^/ud[@'..bot.username..']* ',
	'^/urban[@'..bot.username..']*'
}

local action = function(msg)

	local input = msg.text:input()
	if not input then
		if msg.reply_to_message and msg.reply_to_message.text then
			input = msg.reply_to_message.text
		else
			sendMessage(msg.chat.id, doc, true, msg.message_id, true)
			return
		end
	end

	local url = 'http://api.urbandictionary.com/v0/define?term=' .. URL.escape(input)

	local jstr, res = HTTP.request(url)
	if res ~= 200 then
		sendReply(msg, config.errors.connection)
		return
	end

	local jdat = JSON.decode(jstr)
	if jdat.result_type == "no_results" then
		sendReply(msg, config.errors.results)
		return
	end

	local output = '*' .. jdat.list[1].word .. '*\n\n' .. jdat.list[1].definition:trim()
	if string.len(jdat.list[1].example) > 0 then
		output = output .. '_\n\n' .. jdat.list[1].example:trim() .. '_'
	end

	output = output:gsub('%[', ''):gsub('%]', '')

	sendMessage(msg.chat.id, output, true, nil, true)

end

return {
	action = action,
	triggers = triggers,
	doc = doc,
	command = command
}
