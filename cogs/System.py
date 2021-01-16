import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from pathlib import Path
import datetime
import psutil
import aiohttp


class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["r", "rl"])
    @commands.is_owner()
    async def reload(self, ctx):
        statusOfReload = ""
        cogs = [x.stem for x in Path('cogs').glob('*.py')]
        for extension in cogs:
            try:
                self.bot.reload_extension(f'cogs.{extension}')
                statusOfReload = statusOfReload + f"<:lemontick:789500300976586802> {extension}\n"
            except Exception as e:
                self.bot.reload_extension(f'cogs.{extension}')
                statusOfReload = statusOfReload + f"<:lemoncross:789500300993495060> {extension}\n{e}\n"
        await ctx.send(statusOfReload)

    @commands.command()
    async def embed(self,ctx,title,description):
        embed=discord.Embed(title=f"{title}", description=description, color=0xFBF514)
        embed.set_footer(text=f"Lemon Studios • Posted by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command()
    async def editembed(self,ctx,msgid:int,title,description):
        embed=discord.Embed(title=f"{title}", description=description, color=0xFBF514)
        embed.set_footer(text=f"Lemon Studios • Posted by {ctx.author.name}")
        msg = await ctx.channel.fetch_message(msgid)
        await msg.edit(embed=embed)

    @commands.command()
    async def poll(self,ctx,optiona,optionb):
        embed=discord.Embed(title=f"A new poll has started! :tada:", description=f":one: {optiona}\n:two: {optionb}", color=0xFBF514)
        embed.set_footer(text=f"Poll created by {ctx.author}")
        message = await ctx.send(embed=embed)
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")

    @commands.command()
    async def how2review(self,ctx):
        embed=discord.Embed(title=f"How to submit a review.", description=f"To leave a review for your freelancer, you can use `!review`.", color=0xFBF514)
        embed.add_field(name=f"__Format:__", value=f"**!review <@Freelancer> <1-10> <Review Message>**", inline=False)
        embed.add_field(name=f"__Here is an example:__", value=f"**!review <@590651977034366976> 10 They did a great job!**", inline=True)
        embed.set_footer(text=f"Lemon Studios")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Administration(bot))