import discord
from discord.ext import commands

class PingCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready")

    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency)

        await ctx.send(f"Pong: {bot_latency} ms")

async def setup(client):
    await client.add_cog(PingCog(client))