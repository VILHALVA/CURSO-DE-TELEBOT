# MODULO 0: CRIANDO BOTS DO ZERO
👨‍⚖️CURSO BÁSICO DE CRIAÇÃO DE BOTS.

[![GitHub Repo stars](https://img.shields.io/badge/VILHALVA-GITHUB-03A9F4?logo=github)](https://github.com/VILHALVA) 
[![GitHub Repo stars](https://img.shields.io/badge/NOSSOS-CURSOS-03A9F4?logo=github)](https://github.com/VILHALVA?tab=repositories&q=CURSO&type=public&language=&sort=) <br>

[![GitHub Repo stars](https://img.shields.io/badge/CURSO%20DE-BOTS-03A9F4?logo=youtube)](https://www.youtube.com/playlist?list=PLheIVUbpfWZ2wDRHulCcuIVF-9lkIvyBi)
[![GitHub Repo stars](https://img.shields.io/badge/VEJA%20A-DOCUMENTAÇÃO-03A9F4?logo=youtube)](https://github.com/eternnoir/pyTelegramBotAPI) <br>

<img src="https://static-s.aa-cdn.net/img/gp/20600015011937/Awi79vd4pDQb-YvVtdgiyecFOuZBezvRScyq5mkBbfkJSG5TlwH9BYq-EuPGKfPmm-8?v=1" align="center" width="280"> <br>

## REQUESITOS:
* [INSTALAR O PYTHON](https://www.python.org/downloads/release/python-3110/)
* [INSTALAR O PY TELEGRAM BOT](https://pypi.org/project/pyTelegramBotAPI/#files)

## AVISO IMPORTANTE:
Esse curso se trata de uma [playlist do Youtube](https://www.youtube.com/playlist?list=PLheIVUbpfWZ2wDRHulCcuIVF-9lkIvyBi). Por isso devo salientar algumas coisas:
* ✅A ordem dos Diretórios está diferente dos demais módulos. Onde cada aula é uma pasta, e cada pasta (aula) tem muitos bots diferentes e indepedentes.
* ✅Em alguns diretórios tem o arquivo `TOKEN.py` você precisa colocar o TOKEN do seu bot. Todos os bots da pasta irão usar esse mesmo TOKEN. Por isso todos os códigos de alguns diretórios tem o comando: 
```python
from TOKEN import *
```

## [CONTEÚDO DO CURSO:](https://www.youtube.com/playlist?list=PLheIVUbpfWZ2wDRHulCcuIVF-9lkIvyBi)
* ✅ BOTÕES DE RESPOSTA
* ✅ BOTÕES INLINE
* ✅ POLLING VS WEBHOOK
* ✅ BARRA DE PROGRESSO
* ✅ MODO LENTO
* ✅ CONTROLE DE GRUPOS
* ✅ CAPTURAR TELA
* ✅ REINICIAR BOT
* ✅ EXECUTAR COMANDOS DO SISTEMA
* ✅ GUARDANDO BACKTUP
* ✅ FOTO COM TEXTO
* ✅ CHATGPT COM HTML
* ✅ BOT COMPARADOR DE PREÇOS

## BOTS NA LINGUAGEM PYTHON:
### INSTALAÇÃO DO PYTHON:
1. **Baixar o Python:** Primeiro, você precisa ter o Python instalado no seu sistema. Se você ainda não tem o Python instalado, siga as instruções abaixo para baixá-lo de acordo com seu sistema operacional:

   - **Windows:** Vá para o site oficial do Python em [python.org](https://www.python.org/downloads/windows/) e baixe a versão mais recente do Python para Windows. Execute o instalador e siga as instruções para instalar o Python.

   - **Linux:** A maioria das distribuições Linux já vem com o Python pré-instalado. No entanto, você pode verificar a versão do Python usando o comando `python3 --version`. Se não estiver instalado, você pode instalá-lo usando o gerenciador de pacotes da sua distribuição (por exemplo, `sudo apt-get install python3` no Ubuntu).

   - **macOS:** O macOS também geralmente inclui o Python pré-instalado. Você pode verificar a versão do Python usando o comando `python3 --version`. Se necessário, você pode instalá-lo usando um gerenciador de pacotes como o Homebrew.

### INSTALAÇÃO DA BIBLIOTECA: `pyTelegramBotAPI`:
Depois de ter o Python instalado, você pode instalar a biblioteca `pyTelegramBotAPI` usando o `pip`, que é o gerenciador de pacotes padrão do Python. Abra o terminal ou prompt de comando e execute o seguinte comando:

```bash
pip install pyTelegramBotAPI
```

Isso instalará a biblioteca `pyTelegramBotAPI` no seu ambiente Python.

Agora, você pode começar a criar seu bot em Python e usar a biblioteca `pyTelegramBotAPI` para interagir com a API do Telegram. Certifique-se de obter um token de acesso do BotFather do Telegram antes de criar seu bot e substitua `"SEU_TOKEN_AQUI"` pelo token real do seu bot no código Python.

Com a biblioteca `pyTelegramBotAPI` instalada e o Python configurado, você está pronto para criar e executar seu bot no Telegram.