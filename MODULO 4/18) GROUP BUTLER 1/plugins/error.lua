local action = function(msg, blocks)
if blocks[1] == 'a' then
api.sendReply(msg, make_text '*ERROR*\n`Debes ingresar un texto despúes del comando`.', true)
end
end

return {
     action = action,
     triggers = {
         '^/[Cc]aracolamagic(a)$',
         '^/[Cc]aracol(a)$',
         '^/ser(a)$'
}
}
