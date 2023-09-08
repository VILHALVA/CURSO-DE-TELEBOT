local config = require 'config'
local u = require 'utilities'
local api = require 'methods'
local JSON = require 'dkjson'

local plugin = {}

local function save_data(filename, data)
    local s = JSON.encode(data, {indent = true})
    local f = io.open(filename, 'w')
    f:write(s)
    f:close()
end

local function load_data(filename)
    local f = io.open(filename)
    if f then
        local s = f:read('*all')
        f:close()
        return JSON.decode(s)
    else
        return {}
    end
end

local function gen_backup(chat_id)
    chat_id = tostring(chat_id)
    local file_path = '/tmp/snap'..chat_id..'.gbb'
    local t = {
        [chat_id] = {
            hashes = {},
            sets = {}
        }
    }
    local hash
    for i=1, #config.chat_hashes do
        hash = ('chat:%s:%s'):format(chat_id, config.chat_hashes[i])
        local content = db:hgetall(hash)
        if next(content) then
            t[chat_id].hashes[config.chat_hashes[i]] = {}
            for key, val in pairs(content) do
                t[chat_id].hashes[config.chat_hashes[i]][key] = val
            end
        end
    end
    for i=1, #config.chat_sets do
    	if config.chat_sets[i] ~= 'mods' then --do not backup the modlist
        	set = ('chat:%s:%s'):format(chat_id, config.chat_sets[i])
        	local content = db:smembers(set)
        	if next(content) then
            t[chat_id].sets[config.chat_sets[i]] = content
        end
    	end
    end
    
    save_data(file_path, t)
    
    return file_path
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

local imported_text = [['Done.
*Important*:
- #extra commands which are associated with a media must be set again if the bot you are using now is different from the bot that originated the backup.
- moderators have been restored too (if there were some moderators when the file has been created)
]]

function plugin.onTextMessage(msg, blocks)
    if msg.from.admin then
        if blocks[1] == 'snap' then
            local key = 'chat:'..msg.chat.id..':lastsnap'
            local last_user = db:get(key)
            if last_user then
                local ttl = db:ttl(key)
                local time_remaining = get_time_remaining(ttl)
                local text = _("<i>I'm sorry, this command has been used for the last time less then 3 days ago by</i> %s (ask him for the file).\nWait [<code>%s</code>] to use it again"):format(last_user, time_remaining)
                api.sendReply(msg, text, 'html')
            else
                local name = u.getname_final(msg.from)
                db:setex(key, 259200, name) --3 days
                local file_path = gen_backup(msg.chat.id)
                api.sendReply(msg, _('*Sent in private*'), true)
                api.sendDocument(msg.from.id, file_path, nil, ('#snap\n%s'):format(msg.chat.title))
            end
        end
        if blocks[1] == 'import' then
		    local text
		    if msg.reply then 
		    	if msg.reply.document then
		    		if msg.reply.document.file_name == 'snap'..msg.chat.id..'.gbb' then
		    			local res = api.getFile(msg.reply.document.file_id)
		    			local download_link = u.telegram_file_link(res)
		    			local file_path, code = u.download_to_file(download_link, '/tmp/'..msg.chat.id..'.json')
		    			if not file_path then
		    				text = _('Download of the file failed with code %s'):format(tostring(code))
		    			else
		    				local data = load_data(file_path)
		    				for chat_id, group_data in pairs(data) do
		    					chat_id = tonumber(chat_id)
		    					if tonumber(chat_id) ~= msg.chat.id then
		    						text = _('Chat IDs don\'t match (%s and %s)'):format(tostring(chat_id), tostring(msg.chat.id))
		    					else
		    					    --restoring sets
		    					    if group_data.sets and next(group_data.sets) then
		    					        for set, content in pairs(group_data.sets) do
		    					            db:sadd(('chat:%d:%s'):format(chat_id, set), table.unpack(content))
		    					        end
		    					    end
		    					    
		    					    --restoring hashes
		    					    if group_data.hashes and next(group_data.hashes) then
		    						    for hash, content in pairs(group_data.hashes) do
		    						        if next(content) then
		    						            --[[for key, val in pairs(content) do
		    						                print('\tkey:', key)
		    						                db:hset(('chat:%d:%s'):format(chat_id, hash), key, val)
		    						            end]]
		    						            db:hmset(('chat:%d:%s'):format(chat_id, hash), content)
		    						        end
	    					            end
	    					        end
		    						text = _(imported_text)
		    					end
	    				    end
		    			end
		    		else
		    			text = _('This is not a valid backup file.\nReason: invalid name (%s)'):format(tostring(msg.reply_to_message.document.file_name))
		    		end
		    	else
		    		text = _('Invalid input. Please reply to a document')
		    	end
		    else
		    	text = _('Invalid input. Please reply to the backup file (/snap command to get it)')
		    end
		    api.sendMessage(msg.chat.id, text)
	    end
	end
end

plugin.triggers = {
	onTextMessage = {
		config.cmd..'(snap)$',
		config.cmd..'(import)$'
	}
}

return plugin