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
@lightbulb.option("reason", "The reason for the creation of this ticket")
@lightbulb.command(
    name='ticket',
    description='Create a ticket to get help from the staff team')
@lightbulb.implements(lightbulb.SlashCommand)
async def ticket(ctx: lightbulb.SlashContext):
	await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE,
	                  flags=hikari.MessageFlag.EPHEMERAL)
	overwrite = hikari.PermissionOverwrite(
	    id=ctx.channel_id,
	    type=hikari.PermissionOverwriteType.MEMBER,
	    allow=(hikari.Permissions.VIEW_CHANNEL | hikari.Permissions.SEND_MESSAGES
	           | hikari.Permissions.READ_MESSAGE_HISTORY))
	channel = await ctx.bot.rest.create_guild_text_channel(
	    guild=ctx.guild_id,
	    name=f'{ctx.author.username}-ticket',
	    topic=f'Ticket for {ctx.author.username}',
	    permission_overwrites=[overwrite],
	    category=941744574529957899)

	await ctx.respond(embed=hikari.Embed(
	    title='Ticket created!',
	    description=f'Please go to {channel.mention} to see your ticket!',
	    color=hikari.Color.from_rgb(0, 255, 0)))
	await channel.send(embed=hikari.Embed(
	    title='New Ticket!',
	    description=f'{ctx.author.mention} has created a ticket!',
	    timestamp=datetime.datetime.now(),
	    color=hikari.Color.from_rgb(0, 255, 0)).set_author(
	        name=f'Created by {ctx.author.username}',
	        icon=str(ctx.author.display_avatar_url)))


@plugin.command
@lightbulb.option("amount",
                  "The amount of messages to purge",
                  type=int,
                  max_value=100,
                  min_value=1,
                  required=True)
@lightbulb.option("user",
                  "The user to purge messages from",
                  type=hikari.User,
                  required=False)
@lightbulb.command("purge", "Purges messages from a channel")
@lightbulb.implements(lightbulb.SlashCommand)
async def purge(ctx: lightbulb.SlashContext):
	amount = ctx.options.amount
	user = ctx.options.user

	# Send an initial response
	await ctx.respond(embed=hikari.Embed(title="Purging messages...",
	                                     color=hikari.Color.from_rgb(255, 0, 0)),
	                  flags=hikari.MessageFlag.EPHEMERAL)

	if not ctx.guild_id:
		await ctx.respond("This command can only be used in a server.",
		                  flags=hikari.MessageFlag.EPHEMERAL)
		return

	if amount > 100:
		await ctx.respond(embed=hikari.Embed(
		    title="❌ Error",
		    description="You can only purge up to 100 messages at a time.",
		    color=hikari.Color.from_rgb(255, 0, 0)),
		                  flags=hikari.MessageFlag.EPHEMERAL)
		return

	messages = await ctx.app.rest.fetch_messages(
	    ctx.channel_id
	).take_until(lambda m: datetime.datetime.now(datetime.timezone.utc) -
	             datetime.timedelta(days=14) > m.created_at).limit(amount)

	if messages:
		if user:
			messages = [m for m in messages if m.author == user]
		await ctx.app.rest.delete_messages(ctx.channel_id, messages)
		await ctx.respond(embed=hikari.Embed(
		    title="Purged!",
		    description=f"Purged {len(messages)} messages.",
		    color=hikari.Color.from_rgb(0, 255, 0)),
		                  flags=hikari.MessageFlag.EPHEMERAL)
	else:
		await ctx.respond(embed=hikari.Embed(
		    title="Error!",
		    description="Could not find any messages younger than 14 days!",
		    color=hikari.Color.from_rgb(255, 0, 0)),
		                  flags=hikari.MessageFlag.EPHEMERAL)


@plugin.command
@lightbulb.option("reason",
                  "The reason for locking the thread",
                  type=str,
                  required=False)
@lightbulb.command("lock", "Locks a thread")
@lightbulb.implements(lightbulb.SlashCommand)
async def lock(ctx: lightbulb.SlashContext):
	await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE,
	                  flags=hikari.MessageFlag.EPHEMERAL)


	# command
@plugin.command
@lightbulb.option("thread",
                  "The ID or link of the thread to unlock",
                  type=str,
                  required=False)
@lightbulb.option("reason",
                  "The reason for unlocking the thread",
                  type=str,
                  required=False)
@lightbulb.command("unlock", "Unlocks a thread")
@lightbulb.implements(lightbulb.SlashCommand)
async def unlock(ctx: lightbulb.SlashContext):
	await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE,
	                  flags=hikari.MessageFlag.EPHEMERAL)
	# command


def load(bot):
	bot.add_plugin(plugin)


def unload(bot):
	bot.remove_plugin(plugin)
