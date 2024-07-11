import lightbulb
import logging
import os
from dotenv import load_dotenv

load_dotenv()

bot = lightbulb.BotApp(token=os.getenv("DISCORD_TOKEN"),
											 prefix="!",
											 logs={
													 "version": 1,
													 "incremental": True,
													 "loggers": {
															 "hikari": {
																	 "level": "INFO"
															 },
															 "hikari.ratelimits": {
																	 "level": "TRACE_HIKARI"
															 },
															 "lightbulb": {
																	 "level": "INFO"
															 },
													 },
											 })


@bot.command
@lightbulb.command("ping", "checks the bot is alive")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
		await ctx.respond("Pong!")


bot.run()