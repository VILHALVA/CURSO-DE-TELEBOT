const { Telegraf } = require('telegraf');

// Configurações
const bot = new Telegraf('5774876922:AAFHemJbJBIIX15DRs7ehpBtlvXj1WcT0xE');
bot.start((ctx) => ctx.reply('Olá, eu sou o GroupHelpBot!'));

// Comando para configurar as regras do grupo
bot.command('setrules', (ctx) => {
  // Verifica se o usuário é um administrador do grupo
  if (ctx.message.from.id !== ctx.message.chat.id) {
    return ctx.reply('Este comando só pode ser usado por administradores do grupo.');
  }

  // Obtém as regras do grupo do argumento do comando
  const rules = ctx.message.text.slice(9);

  // Armazena as regras em um banco de dados ou arquivo
  // Neste exemplo, vamos armazenar em uma variável
  ctx.db.groupRules = rules;

  // Envia uma mensagem confirmando que as regras foram atualizadas
  ctx.reply('As regras do grupo foram atualizadas.');
});

// Comando para obter as regras do grupo
bot.command('rules', (ctx) => {
  const rules = ctx.db.groupRules || 'As regras do grupo não foram definidas ainda.';

  ctx.reply(`As regras do grupo são: \n\n${rules}`);
});

// Comando para denunciar um membro do grupo
bot.command('report', (ctx) => {
  const userId = ctx.message.reply_to_message.from.id;
  const reportedUser = ctx.message.reply_to_message.from.username;

  // Envia uma mensagem para os administradores do grupo
  bot.telegram.sendMessage(ctx.message.chat.id, `O usuário @${reportedUser} (${userId}) foi denunciado por ${ctx.message.from.username}.`);

  // Envia uma mensagem confirmando a denúncia
  ctx.reply(`O usuário @${reportedUser} foi denunciado. Obrigado por nos informar.`);
});

// Ação para detectar a entrada de um novo usuário no grupo
bot.on('new_chat_members', (ctx) => {
  const memberCount = ctx.message.new_chat_members.length;

  // Verifica se há mais de um novo membro
  if (memberCount > 1) {
    ctx.reply(`${memberCount} novos membros entraram no grupo. Por favor, leiam as regras do grupo.`);
  } 
  else {
    ctx.reply(`${ctx.message.new_chat_members[0].first_name} entrou no grupo. Por favor, leia as regras do grupo.`);
  }
});

// Inicia o bot
bot.launch();

