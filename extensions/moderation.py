import lightbulb
import hikari

plugin = lightbulb.Plugin("Moderation")


@plugin.command
@lightbulb.option('member', 'The member to kick', type=hikari.User)
@lightbulb.option('reason', 'The reason for kicking the member')
@lightbulb.command(name='kick', description='Kick a user from the server.')
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx: lightbulb.SlashContext):
		await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE)
		await ctx.options.member.send(embed=hikari.Embed(title='Kicked!', description=f'You have been kicked from {ctx.get_guild().name}', color=hikari.Color.red()))
		await ctx.get_guild().kick_member(user=ctx.options.member, reason=reason)
		await ctx.reply(embed=hikari.Embed(title='Kicked!', description=f'Kicked {member.mention}.', color=discord.Color.green()))


def load(bot):
	bot.add_plugin(plugin)


def unload(bot):
	bot.remove_plugin(plugin)
