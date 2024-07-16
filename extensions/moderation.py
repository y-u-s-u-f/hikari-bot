import lightbulb
import hikari
import datetime

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


@plugin.command
@lightbulb.option("amount", "The amount of messages to purge", type=int, max_value=100, min_value=1, required=True)
@lightbulb.option("user", "The user to purge messages from", type=hikari.User, required=False)
@lightbulb.option("reason", "The reason for purging messages", type=str, required=False)
@lightbulb.command("purge", "Purges messages from a channel")
@lightbulb.implements(lightbulb.SlashCommand)
async def purge(ctx: lightbulb.SlashContext):
		amount = ctx.options.amount
		user = ctx.options.user
		reason = ctx.options.reason

		# Send an initial response
		await ctx.respond(embed=hikari.Embed(title="Purging messages...", color=hikari.Color.from_rgb(255, 0, 0)), flags=hikari.MessageFlag.EPHEMERAL)

		if not ctx.guild_id:
				await ctx.respond("This command can only be used in a server.", flags=hikari.MessageFlag.EPHEMERAL)
				return

		if amount > 100:
				await ctx.respond(embed=hikari.Embed(
						title="❌ Error", 
						description="You can only purge up to 100 messages at a time.", 
						color=hikari.Color.from_rgb(255, 0, 0)),
						flags=hikari.MessageFlag.EPHEMERAL
				)
				return

		messages = await ctx.app.rest.fetch_messages(ctx.channel_id).take_until(
			lambda m: datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=14) > m.created_at
		).limit(amount)
	
		if messages:
			if user:
					messages = [m for m in messages if m.author == user]
			await ctx.app.rest.delete_messages(ctx.channel_id, messages)
			await ctx.respond(embed=hikari.Embed(
					title="Purged!", 
					description=f"Purged {len(messages)} messages.", 
					color=hikari.Color.from_rgb(0, 255, 0)),
					flags=hikari.MessageFlag.EPHEMERAL
			)
		else:
				await ctx.respond(embed=hikari.Embed(
						title="Error!", 
						description="Could not find any messages younger than 14 days!", 
						color=hikari.Color.from_rgb(255, 0, 0)),
						flags=hikari.MessageFlag.EPHEMERAL
				)


def load(bot):
	bot.add_plugin(plugin)


def unload(bot):
	bot.remove_plugin(plugin)



