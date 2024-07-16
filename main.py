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
                       },
                       intents=hikari.Intents.ALL)

bot.load_extensions("extensions.moderation")


# slash command to reload an extension (only available in guild 941744574529957898 and only invokable by the bot owner))
@bot.command
@lightbulb.option("extension", "The extension to reload", type=str)
@lightbulb.command("reload", "Reloads an extension")
@lightbulb.implements(lightbulb.SlashCommand)
async def reload(ctx: lightbulb.SlashContext) -> None:
    if ctx.author.id == 712439467901976660:
        try:
            bot.reload_extensions(f"extensions.{ctx.options.extension}")
            await ctx.respond(embed=hikari.Embed(
                title="Reloaded!",
                description=f"Reloaded extension {ctx.options.extension}",
                color=hikari.Color.from_rgb(0, 255, 0)),
                              flags=hikari.MessageFlag.EPHEMERAL)
        except lightbulb.errors.ExtensionNotLoaded:
           
            await ctx.respond(embed=hikari.Embed(
                title="Error!",
                description=f"Extension {ctx.options.extension} is not loaded!",
                color=hikari.Color.from_rgb(255, 0, 0)),
                              flags=hikari.MessageFlag.EPHEMERAL)


bot.run()
