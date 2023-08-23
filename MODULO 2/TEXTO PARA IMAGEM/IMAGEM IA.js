const Telegraf = require('telegraf');
const request = require('request');
const Clarifai = require('clarifai');

const bot = new Telegraf('<SEU_TOKEN_DE_ACESSO>');
const clarifai = new Clarifai.App({
  apiKey: '<SUA_API_KEY_CLARIFAI>',
});

// Configura o bot para receber uma imagem e enviar uma mensagem de texto com a descrição da imagem e uma foto baseada em IA
bot.on('photo', async (ctx) => {
  try {
    const fileId = ctx.update.message.photo[0].file_id;
    const fileUrl = await ctx.telegram.getFileLink(fileId);
    
    // Faz o upload da imagem para o Clarifai
    const imageBytes = await request.get(fileUrl.href, { encoding: null });
    const response = await clarifai.models.predict(Clarifai.GENERAL_MODEL, { base64: imageBytes.toString('base64') });

    // Obtém a descrição da imagem
    const description = response.outputs[0].data.concepts.map((concept) => concept.name).join(', ');

    // Obtém uma imagem relacionada a partir do Clarifai
    const imageSearchResponse = await clarifai.inputs.search({
      concept: {
        name: description,
        type: 'input',
      },
    });
    const imageUrl = imageSearchResponse.hits[0].input.data.image.url;

    // Envia a mensagem de texto com a descrição da imagem e a foto relacionada
    ctx.replyWithPhoto({ url: imageUrl }, { caption: description });
  } catch (err) {
    console.error(err);
    ctx.reply('Ocorreu um erro ao processar a imagem.');
  }
});

bot.launch();

