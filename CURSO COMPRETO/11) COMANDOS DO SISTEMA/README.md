# COMANDOS DO SISTEMA
## DESCRIÇÃO:
É um bot de Telegram que executa comandos no sistema operacional quando acionado por um administrador. Aqui está uma breve descrição do que o bot faz:

1. **Inicia o Bot**: Quando você executa o código, ele inicia o bot com o token fornecido.

2. **Verifica Administradores**: Ele verifica se o ID do remetente da mensagem (usuário) corresponde a um ID de administrador especificado na variável `ADMINS`. Se o usuário não for um administrador, ele envia uma mensagem informando que não está autorizado.

3. **Comando /start**: Quando alguém envia o comando `/start`, o bot envia uma mensagem de boas-vindas.

4. **Comando /c**: Quando um administrador envia o comando `/c`, seguido por um comando, o bot executa esse comando no sistema operacional. Ele usa o módulo `subprocess.run` para executar o comando e capturar a saída padrão (stdout) e erros (stderr).

5. **Resposta aos Comandos**: O bot envia a saída do comando de volta ao chat do Telegram. Isso inclui qualquer saída padrão gerada pelo comando, bem como mensagens de erro, se houver.

Lembre-se de que permitir que um bot execute comandos no sistema operacional pode ser arriscado, especialmente se ele for usado em chats públicos ou comandos não verificados. Certifique-se de compartilhar comandos somente com pessoas confiáveis e administração cuidadosa para evitar possíveis problemas de segurança.

Certifique-se de que as configurações de segurança do seu sistema permitam a execução de comandos via `subprocess.run`.