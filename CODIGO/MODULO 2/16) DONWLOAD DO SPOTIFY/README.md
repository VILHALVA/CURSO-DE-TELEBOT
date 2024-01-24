# Spotify-Download-Telegram-Bot
Bot criado no telegram para fazer downloads de musicas, playlists e discografia de artistas usando o Spotdl -> https://github.com/ritiek/spotify-downloader
##
O Funcionamento é muito simples, envie um link de música, playlist ou discografia do artista e o bot fará o resto, normalmente ele demora um pouco para fazer o download de listas de músicas, por se tratar de muitas músicas.
##
Você pode acessar ele atraves do link dele no Telegram -> https://t.me/Dryrtanbot
##

## O que é preciso para fazer funcionar na sua maquina??
- Primeiro vamos começar instalando as dependencias
```
pip3 install -r requirements.txt
```
- Após isso mudaremos o token (https://t.me/BotFather) do bot do Telegram localizado em config.py
```
TOKEN = 'TOKEN DO BOT AQUI'
```
- Por ultimo você precisa entrar no site https://developer.spotify.com/dashboard/applications e usar a API do Spotify e pegar o Client ID e o Client Secret e dar o comando
```
export SPOTIPY_CLIENT_ID="client id aqui"
export SPOTIPY_CLIENT_SECRET="client secret aqui"
pip3 install --upgrade requests
sudo apt install ffmpeg
```

##
![alt text](https://uploaddeimagens.com.br/images/003/285/772/original/Fluxograma.png?1623486888)

[CÓDIGO FONTE BAIXADO DE DRYRTAN](https://github.com/Dryrtan/Spotify-Download-Telegram-Bot)
