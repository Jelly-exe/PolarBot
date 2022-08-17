import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

chat_filter = []
bypass_list = ["278548721778688010"]

@client.event
async def on_ready():
    print("Bot is online and connected to discord!")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel,"<@%s> Pong!" % (userID))

    if message.content.upper().startswith('!SAY'):
        if message.author.id == "278548721778688010":
            args = message.content.split(" ")
            await client.send_message(message.channel,"%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You don't have permission to run that command!")

    if message.content.upper().startswith('!AMIADMIN'):
        if "386957320879341568" in [role.id for role in message.author.roles]: #Change to PolarCraftMC Discord Role ID
            await client.send_message(message.channel, "You are an admin/mod")
        else:
            await client.send_message(message.channel, "You are not an admin/mod")

    if message.content.upper().startswith('!IP'):
        await client.send_message(message.channel,"The IP is: `Play.PolarCraftMC.Net`")

    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!!** Your not allowed to use that word here!")
                except discord.errors.NotFound:
                    return
                
            else:
                await client.send_message(message.channel, "Your too cool so I won't delete your message, but keep your language to a minimum please!")

    if message.content.upper().startswith('!WELCOME'):
        emb = (discord.Embed(title="Welcome to the PolarCraftMC Official Bot!", description="To get started do !help", colour=0x00ffff))
        emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/428285031828553750/456574247729496064/PolarCraftMC_Logo_2.png")
        emb.set_author(name="Welcome! ", icon_url='https://i.imgur.com/gL2vdHVh.jpg')
        emb.set_footer(text="Made by: qoqʎןןǝſ #6161 and Eartharoid #2006")
        await client.send_message(message.channel,embed=emb)

    if message.content.upper().startswith('!NOTIFYME'):
        user = message.author
        role = discord.utils.get(user.server.roles, name="Notify")
        await client.add_roles(user, role)
        await client.send_message(message.channel,"You now have the `@Notify` Role!")
        
    if message.content.upper().startswith('!DONTNOTIFYME'):
        user = message.author
        role = discord.utils.get(user.server.roles, name="Notify")
        await client.remove_roles(user, role)
        await client.send_message(message.channel,"The `@Notify` Role has now been removed!")

    if message.content.upper().startswith('!ANNOUNCE'):
        if "386957320879341568" in [role.id for role in message.author.roles]: #Change to PolarCraftMC Discord Role ID
            args2 = message.content.split(" ")
            await client.send_message(client.get_channel('315490920764276736'), "<@&445289326872363008> %s" % (" ".join(args2[1:])))#Change to PolarCraftMC Discord Role ID
            await client.send_message(message.channel, "Message sent in <#315490920764276736>!") #Change to PolarCraftMC Discord Channel ID
            
        else:
            await client.send_message(message.channel, "You don't have permission to run that command!")

    #if message.content.upper().startswith('!MUTE'):
     #   try:
      #      args3 = message.content.split(" ")
       #     user = args3[1]
        #    role = discord.utils.get(user.server.roles, name="Muted")
         #   await client.add_roles(user, role)
          #  await client.send_message(message.channel,"%s Has been muted!" % (" ".join(args3[1])))
#
 #       except discord.errors.NotFound:
  #          await client.send_message(message.channel, "There is no user mentioned! `!mute <User>` ")
    if message.content.upper().startswith('!STORE'):
        await client.send_message(message.channel,"The Store Link is: http://polarcraftmcstore.buycraft.net")
        
    if message.content.upper().startswith('!APPLY'):
        await client.send_message(message.channel,"Want to become 1 of our brilliant staff members? Go to: https://goo.gl/forms/Qceo9DBYKxISNMfH3")
        
    if message.content.upper().startswith('!WEBSITE'):
        await client.send_message(message.channel,"Coming Soon!")


 #   if message.content.upper().startswith('!MUTE'):
  #      muteargs = message.content.split(" ")
   #     await client.send_message(message.channel, "\%s" % ("".join(muteargs[1])))
    #    #user = message.author
     #   #role = discord.utils.get(user.server.roles, name="Muted")
      #  #await client.add_roles(user, role)
       # #await client.send_message(message.channel,"You now have the `@Notify` Role!")

   # if message.content.upper().startswith('<@!'):
    #    muteargs2 = message.content.split(" ")
        
client.run("NDU2NDU2MDQ2MzAzNTEwNTI5.DgMTIQ.jbrgBWWAbJwLxjFGIkZXshv30rY")
                                      
