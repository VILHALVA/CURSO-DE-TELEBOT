const Telegraf = require('telegraf')
const Extra = require('telegraf/extra')
const Markup = require('telegraf/markup')
const schedule = require('node-schedule')

// Cria uma nova instância do bot
const bot = new Telegraf(process.env.BOT_TOKEN)

// Armazena as mensagens agendadas
const scheduledMessages = {}

// Responde ao comando /schedule
bot.command('schedule', (ctx) => {
  // Obtém a mensagem a ser agendada a partir do argumento do comando
  const message = ctx.message.text.slice(9).trim()

  // Pergunta ao usuário quando a mensagem deve ser enviada
  ctx.reply('Quando você quer que eu envie esta mensagem? Por favor, me diga a data e hora usando o formato "dd/mm/yyyy hh:mm".')

  // Armazena a mensagem e aguarda a resposta do usuário com a data e hora
  scheduledMessages[ctx.from.id] = { message }
  bot.on('text', setDateTime)
})

// Responde à resposta do usuário com a data e hora para agendamento
function setDateTime(ctx) {
  // Obtém a data e hora informada pelo usuário
  const dateTimeStr = ctx.message.text.trim()

  // Tenta converter a data e hora para um objeto Date
  const dateTime = new Date(dateTimeStr)
  if (isNaN(dateTime.getTime())) {
    ctx.reply('Desculpe, não entendi a data e hora. Por favor, tente novamente usando o formato "dd/mm/yyyy hh:mm".')
    return
  }

  // Verifica se a data e hora informada é no futuro
  if (dateTime.getTime() < Date.now()) {
    ctx.reply('Desculpe, não posso agendar uma mensagem para o passado. Por favor, informe uma data e hora futuras.')
    return
  }

  // Armazena a data e hora informada pelo usuário e aguarda a confirmação do grupo
  const scheduledMessage = scheduledMessages[ctx.from.id]
  scheduledMessage.dateTime = dateTime
  ctx.reply(`Ok, vou enviar a mensagem "${scheduledMessage.message}" em ${dateTime.toLocaleString()}. Por favor, confirme o agendamento com o comando /confirm_schedule.`)

  // Remove o handler de data e hora
  bot.off('text', setDateTime)

  // Aguarda a confirmação do grupo
  bot.command('confirm_schedule', confirmSchedule)
}

// Responde ao comando /confirm_schedule
function confirmSchedule(ctx) {
  // Obtém a mensagem agendada e o chat_id do usuário
  const scheduledMessage = scheduledMessages[ctx.from.id]
  const chatId = ctx.chat.id

  // Agenda a mensagem
  const job = schedule.scheduleJob(scheduledMessage.dateTime, () => {
    ctx.telegram.sendMessage(chatId, scheduledMessage.message)
  })

  // Remove a mensagem agendada
  delete scheduledMessages[ctx.from.id]

  // Envia uma mensagem para confirmar o agendamento
  ctx.reply(`A mensagem "${scheduledMessage.message}" será enviada em ${scheduledMessage.dateTime.toLocaleString()}. O agendamento foi confirmado.`)
}

// Para criar um bot do Telegram em JavaScript que permita agendar mensagens usando o seu perfil em grupos, podemos usar a biblioteca node-telegram-bot-api.