"""Discord screenshot bot. See README.md for setup and usage."""
import asyncio
import io
import os

import discord
import mss
import mss.tools
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]
OWNER_ID = int(os.environ["OWNER_ID"])

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


def grab(monitor_index: int) -> bytes:
    """Return PNG bytes. Index 0 = all monitors combined."""
    with mss.mss() as sct:
        if monitor_index >= len(sct.monitors):
            raise ValueError(f"Only {len(sct.monitors) - 1} monitor(s) found.")
        shot = sct.grab(sct.monitors[monitor_index])
        return mss.tools.to_png(shot.rgb, shot.size)


@bot.command(name="shot")
async def shot(ctx: commands.Context, monitor: int = 0):
    if ctx.author.id != OWNER_ID:
        return  # ignore everyone but you
    try:
        png = await asyncio.to_thread(grab, monitor)
    except ValueError as e:
        await ctx.send(str(e))
        return
    await ctx.send(file=discord.File(io.BytesIO(png), filename="screen.png"))


bot.run(TOKEN)
