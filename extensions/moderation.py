import lightbulb
import hikari

plugin = lightbulb.Plugin("Moderation")


@plugin.command
@lightbulb.option('member', 'The member to kick', type=hikari.User)
@lightbulb.option('reason',
                  'The reason for kicking the member',
                  required=False)
@lightbulb.command(name='kick', description='Kick a user from the server.')
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx: lightbulb.SlashContext):
	await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE)
	await ctx.options.member.send(embed=hikari.Embed(
	    title='Kicked!',
	    description=f'You have been kicked from {ctx.get_guild().name}',
	    color=hikari.Color.from_rgb(255, 0, 0)))
	await ctx.get_guild().kick(ctx.options.member,
	                           reason=ctx.options.reason or hikari.UNDEFINED)
	await ctx.respond(
	    embed=hikari.Embed(title='Kicked!',
	                       description=f'Kicked {ctx.options.member.mention}.',
	                       color=hikari.Color.from_rgb(255, 0, 0)))


@plugin.command
@lightbulb.option('member', 'The member to ban', type=hikari.User)
@lightbulb.option('reason',
                  'The reason for banning the member',
                  required=False)
@lightbulb.command(name='ban', description='Ban a user from the server.')
@lightbulb.implements(lightbulb.SlashCommand)
async def ban(ctx: lightbulb.SlashContext):
	await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE)
	await ctx.options.member.send(embed=hikari.Embed(
	    title='Banned!',
	    description=f'You have been banned from {ctx.get_guild().name}',
	    color=hikari.Color.from_rgb(255, 0, 0)))
	await ctx.get_guild().ban(ctx.options.member,
	                          reason=ctx.options.reason or hikari.UNDEFINED)
	await ctx.respond(
	    embed=hikari.Embed(title='Banned!',
	                       description=f'Banned {ctx.options.member.mention}.',
	                       color=hikari.Color.from_rgb(255, 0, 0)))


@plugin.command
@lightbulb.option('reason', 'The reason for the creation of this ticket')
@lightbulb.command(
    name='ticket',
    description='Create a ticket to get help from the staff team')
@lightbulb.implements(lightbulb.SlashCommand)
async def ticket(ctx: lightbulb.SlashContext):
	await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE,
	                  ephemeral=True)
	# create channel
	# update overwrites
	# send message in newly created channel
	# respond to original interaction


def load(bot):
	bot.add_plugin(plugin)


def unload(bot):
	bot.remove_plugin(plugin)
