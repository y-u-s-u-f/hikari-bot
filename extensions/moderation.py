import lightbulb
import hikari

plugin = lightbulb.Plugin("Moderation")


@plugin.command
@lightbulb.option("member", "The member to kick", type=hikari.Member)
@lightbulb.option("reason",
                  "The reason for kicking the member",
                  type=str,
                  required=False)
@lightbulb.command(name="kick", description="Kicks a user from the server")
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx: lightbulb.SlashContext) -> None:

	if not ctx.guild_id:
		await ctx.respond("This command can only be used in a guild.")
		return

	await ctx.app.rest.kick_user(ctx.guild_id,
	                             ctx.options.member.id,
	                             reason=ctx.options.reason)


def load(bot):
	bot.add_plugin(plugin)


def unload(bot):
	bot.remove_plugin(plugin)
