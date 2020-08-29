print("lancement du bot...")
import json
import discord

from discord.utils import get

from discord.ext import commands

from discord.ext.commands import has_permissions


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("bot pret")
    await bot.change_presence(status=discord.Status.idle,
            activity=discord.Game("!commandes"))

@bot.command()
async def regles(ctx):
    await ctx.send("Pas de gros mot/insulte\nPas de pub YouTube/Twitch/Instagram/Twitter\nInterdit d’allez dans un salon filles si on est un garçon et inversement\nParce que apprès ça s'appelle être un PERVERS xD")

@bot.command()
async def epic(ctx):
    await ctx.send("le epic de mon maître suppreme : Varzek_YT xD")

@bot.command()
async def insta(ctx):
    await ctx.send("l'insta de mon maître suppreme : varzek_yt xD")

@bot.command()
async def twitter(ctx):
    await ctx.send("le twitter de mon maître suppreme : @lemegamanyt3 xD")

@bot.command()
async def twitch(ctx):
    await ctx.send("le twitch de mon maître suppreme : varzek_yt xD")

@bot.command()
async def video(ctx):
    await ctx.send("voici la derniere video que mon maîte suppreme a sorti : https://www.youtube.com/watch?v=znBXjcMKcAo")

@bot.command()
async def commandes(ctx):
    await ctx.send("les commandes sont pour l'instant :\n1 !regles : permet de voir les règles\n2 !epic : permet de voir l'epic de varzek\n3 !insta : pareil que l'epic pes pour insta\n4 !twitter : idem mais pour twitter*\n5 !twitch : * mais pour twitch \n6 !video : permet de voir la dèrnière vidéo posté par varzek\n7 !leak : permet de voir les derniers leak de varzek(je dédicace jcbevc parce que c'est lui qui donne quelques leak et non je ne fais pas ça parce que c'est lui qui me programme) *siflotte* :sweat_smile:")

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, membre: discord.Member):
    await membre.send("t'as été ban t'avais cas a faire le gentil toutou, cheh")
    await membre.ban()

@bot.command()
async def leak(ctx):
    await ctx.send("voiçi le dernièr leak de varzek\n\nenfin moi et yanteh")
    await ctx.send("https://www.instagram.com/p/CEdw3RjpoUJ/")


@ban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("frr tas cruy tallais ban des gens comm ça eh vazy tum dégoute j'vais t'ban")

token = "NzQyNjcyMzg2ODU1MjcyNTQw.XzJhjw.eiJVmLTryxsMouPBXNWN6ubr_Kc"

bot.run(token)