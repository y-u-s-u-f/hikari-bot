import lightbulb
import os
from dotenv import load_dotenv

load_dotenv()

bot = lightbulb.BotApp(token=os.getenv("DISCORD_TOKEN"), prefix="!")

@bot.command
@lightbulb.command("ping", "checks the bot is alive")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
		await ctx.respond("Pong!")

bot.run()
