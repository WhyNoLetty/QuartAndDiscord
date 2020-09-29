### Quart And Discord.py

Permitir a comunicação do [discord.py](https://discordpy.readthedocs.io/en/latest/) entre alguma framework asyncronizada (Exemplo [Quart](https://pgjones.gitlab.io/quart/) | [aiohttp.web](https://docs.aiohttp.org/en/stable/web_quickstart.html))

## Instalação

O modulo é somente instalado através do [git](https://git-scm.com)

```py
python -m pip install -U git+https://github.com/WhyNoLetty/QuartAndDiscord
```

## Uso básico ou Seus primeiros passos

Poderá saber mais sobre o Quart clicando [aqui](https://pgjones.gitlab.io/quart/)

```py
# BOT FILE
import discord
from discord.ext import commands

from discord.ext.dashboard import Server

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def on_dash_ready(self):
        print("Dash ready")
    
    async def on_ready(self):
        print("Bot ready")

bot = Bot(command_prefix="!", case_insensitive=True)
dashboard = Server(bot, "localhost", 5000, "secret_key")

@dashboard.route()
async def get_guild_count(data):
    return len(bot.guilds)

if __name__ == "__main__":
    dashboard.start()
    bot.run("Seu token")

```py
# WEB SERVER FILE
from quart import Quart
from discord.ext.dashboard import Client

app = Quart(__name__)
bot = Client("localhost", 5000, "secret_key")

@app.route("/")
async def show_guilds():
    guild_count = await bot.request("get_guild_count")
    return guild_count

if __name__ == "__main__":
    app.run()
```