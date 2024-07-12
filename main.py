import lightbulb
import logging
import os
import hikari
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
											 }, intents=hikari.Intents.ALL)


@bot.command()
@lightbulb.command("ping", "Checks that the bot is alive")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
		"""Checks that the bot is alive"""
		await ctx.respond("Pong!")



bot.run()