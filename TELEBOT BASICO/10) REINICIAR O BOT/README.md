# REINICIAR BOT
## DESCRIÇÃO:
1. **Inicia o Bot**: Quando você executa o código, ele inicia o bot com o token fornecido.

2. **Verifica Administradores**: Ele verifica se o ID do remetente da mensagem (usuário) corresponde a um ID de administrador especificado na variável `ADMINS`. Se o usuário não for um administrador, ele envia uma mensagem informando que não está autorizado.

3. **Comando /start**: Quando alguém envia o comando `/start`, o bot envia uma mensagem de boas-vindas.

4. **Comando /restart**: Quando um administrador envia o comando `/restart`, o bot interrompe a atualização (polling) e reinicia-se. Isso permite reiniciar o bot sem parar o programa principal. Após reiniciar, ele envia uma mensagem informando que foi reiniciado.

5. **Comando /reboot**: Quando um administrador envia o comando `/reboot`, o bot reinicia o servidor. Isso é feito usando o comando "shutdown /r" no Windows e "reboot" no Linux. Certifique-se de que o bot tenha as permissões necessárias para executar esses comandos no sistema operacional.

Em resumo, este bot permite reiniciar-se ou reiniciar o servidor (dependendo do comando) quando comandado por um administrador autorizado.

Lembre-se de proteger o acesso aos comandos `/restart` e `/reboot`, pois eles têm o potencial de interromper o funcionamento do bot ou do servidor. Certifique-se de compartilhar esses comandos apenas com os administradores ou pessoas de confiança.

## DOCUMENTAÇÃO:
* [Documentacão oficial OS.EXECV()](https://docs.python.org/es/3/library/os.html#os.execv)