import lightbulb
import hikari

plugin = lightbulb.Plugin("Moderation")


@plugin.command
@lightbulb.option('member', 'The member to kick', type=hikari.User)
@lightbulb.option('reason', 'The reason for kicking the member')
@lightbulb.command(name='kick', description='Kick a user from the server.')
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx: lightbulb.SlashContext):
		await ctx.options.member.send(embed=discord.Embed(title='Kicked!', description=f'You have been kicked from MacApps', color=discord.Color.red()))
		await member.kick(reason=reason)
		await interaction.followup.send(embed=discord.Embed(title='Kicked!', description=f'Kicked {member.mention}.', color=discord.Color.green()))


def load(bot):
	bot.add_plugin(plugin)


def unload(bot):
	bot.remove_plugin(plugin)
