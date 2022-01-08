import discord
import atexit
from discord.ext import commands
from discord.ext.commands.core import has_permissions

activity = discord.Activity(type=discord.ActivityType.watching, name="a movie on Diamond Media")
bot = commands.Bot(command_prefix='!', activity=activity)

@bot.event
async def on_ready():
    print('Logged on as', bot.user)

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     if not message.guild:
#         try:
#             await message.channel.send("sorry I dont chat with hoes kthxbai")
#         except discord.errors.Forbidden:
#             pass
#     else:
#         pass


@bot.command()
async def cleardms(ctx):
    dmchannel = ctx.message.channel #dm channel you want to clear
    async for message in dmchannel.history(limit=100):
        if message.author == bot.user: #client.user or bot.user according to what you have named it
            await message.delete()


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
@has_permissions(administrator=True)
async def fs(ctx, username : str):
    from plexapi.server import PlexServer
    import requests

    PLEX_URL = 'http://PLEX_URL:32400'
    PLEX_TOKEN = 'YOUR_PLEX_TOKEN'

    sess = requests.Session()
    # Ignore verifying the SSL certificate
    sess.verify = False
    if sess.verify is False:
        # Disable the warning that the request is insecure, we know that...
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    plex = PlexServer(PLEX_URL, PLEX_TOKEN, session=sess)

    try:
        plex.myPlexAccount().inviteFriend(user=username, server=plex, allowSync=False, allowCameraUpload=False)
        print(username + ' Invited Succesfully!')
        await ctx.send(username + ' invited to free server succesfully!')
    except Exception as exc:
        print(exc)
        await ctx.send(exc)

@bot.command()
async def listfreeusers(ctx):
    from plexapi.server import PlexServer
    import requests

    PLEX_URL = 'http://PLEX_URL:32400'
    PLEX_TOKEN = 'YOUR_PLEX_TOKEN'

    sess = requests.Session()
    # Ignore verifying the SSL certificate
    sess.verify = False
    if sess.verify is False:
        # Disable the warning that the request is insecure, we know that...
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    plex = PlexServer(PLEX_URL, PLEX_TOKEN, session=sess)
    print('plex initialised')
    users = plex.myPlexAccount().users()
    for user in users:
        print(str(users.index(user) + 1) + '. ' + user.username,user.email)
        await ctx.send(str(users.index(user) + 1) + '. ' + user.username + ' - ' + user.email)

@bot.command()
@has_permissions(administrator=True)
async def freeslots(ctx):
    from plexapi.server import PlexServer
    import requests

    PLEX_URL = 'URL'
    PLEX_TOKEN = 'TOKEN'

    sess = requests.Session()
    # Ignore verifying the SSL certificate
    sess.verify = False
    if sess.verify is False:
        # Disable the warning that the request is insecure, we know that...
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    plex = PlexServer(PLEX_URL, PLEX_TOKEN, session=sess)
    print('plex initialised')
    users = plex.myPlexAccount().users()
    invites = plex.myPlexAccount().pendingInvites(includeSent=True, includeReceived=False)
    freeslots = 100 - len(users) - len(invites)
    print(freeslots)
    print('Free Slots Available : {}'.format(str(freeslots)))
    await ctx.send('Free Slots Available : {}'.format(str(freeslots)))

@bot.command()
@has_permissions(administrator=True)
async def listpsusers(ctx):
    from plexapi.server import PlexServer
    import requests

    PLEX_URL = 'URL'
    PLEX_TOKEN = 'TOKEN'

    sess = requests.Session()
    # Ignore verifying the SSL certificate
    sess.verify = False
    if sess.verify is False:
        # Disable the warning that the request is insecure, we know that...
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    plex = PlexServer(PLEX_URL, PLEX_TOKEN, session=sess)
    print('plex initialised')
    users = plex.myPlexAccount().users()
    for user in users:
        print(str(users.index(user) + 1) + '. ' + user.username,user.email)
        await ctx.send(str(users.index(user) + 1) + '. ' + user.username + ' - ' + user.email)


bot.run('BOT_TOKEN')
