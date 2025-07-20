import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(file_name)
            await ctx.send("Archivo guardado")
            class_name = get_class("keras_model.h5","labels.txt",file_name)
            await ctx.send(class_name)

            try:
                class_name = get_class("keras_model.h5", "labels.txt", file_name)
                if class_name[0] == "Hostil":
                    await ctx.send("Este es un mob hostil, matalo o escapa de el")
                elif class_name[0] == "Pacifico":
                    await ctx.send("Este mob no es hostil, no hay peligro")
            except:
                await ctx.send("La clasificacion a fallado")
    else:
        await ctx.send("No hay archivos adjuntos")
bot.run("")