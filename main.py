import discord
from discord.ext import commands
from Chatbox import Chatbox
import sqlite3
import time
from random import choice
prefix = "!"
client = commands.Bot(command_prefix=prefix)

commands_list = []
conn = sqlite3.connect("database.db")
c = conn.cursor()
print("Database loaded successfully.")

@client.event
async def on_ready():
    # c.execute("""drop table incog""")
    # c.execute("""create table incog(hash integer, incog_name text)""")
    global commands_list
    commands_list = [c.name for c in client.commands]
    # print(commands_list)
    print('We have logged in as {0.user}'.format(client))
    print(client.user)

@client.command()
async def join(ctx):
    author = ctx.author
    if not Chatbox.check(author):
        a = Chatbox(author)
        user = a.join()
        if user == "waiting.":
            await ctx.send("you are added to waiting list. Thank you for your patience :heart:")
        else:
            print(f"{a.author} : {user.author}")
            a_name = user_name = "someone"
            if len(c.execute("select hash from incog where hash == ?",(hash(a.author.id),)).fetchall())==1:
                a_name = c.execute(f"select incog_name from incog where hash == {hash(a.author.id)}").fetchone()[0]
            if len(c.execute("select hash from incog where hash == ?",(hash(user.author.id),)).fetchall())==1:
                user_name = c.execute(f"select incog_name from incog where hash == {hash(user.author.id)}").fetchone()[0]


            user_msg = discord.Embed(title="_WELCOME TO CHATBOT :heart:_", description="", color= 0x2ecc71)
            a_msg = discord.Embed(title="_WELCOME TO CHATBOT :heart:_ ", description="", color= 0x2ecc71)

            user_msg_edit = await user.author.send(embed=user_msg)
            a_msg_edit = await a.author.send(embed=a_msg)
            desc = ""
            while a.running_status and user.running_status:
                msg = await client.wait_for("message")
                if not isinstance(msg.channel, discord.channel.DMChannel):
                    continue
                if msg.content.startswith("!"):
                    if msg.content == "!leave":
                        if msg.author == a.author or msg.author == user.author:
                           a.leave()
                           await a.author.send("Chat Ended")
                           user.leave()
                           await user.author.send("Chat Ended")
                           del a, user
                           break
                    continue

                # if msg.content[1:] in commands_list:
                #    continue

                if msg.author == a.author or msg.author == user.author:
                    message = msg.content
                    if msg.attachments:
                        pass
                        # message = msg.attachments[0].url
                        # if msg.author == a.author:
                            # await user.author.send(f"**{a_name}**: {message}")
                        # else:
                            # await a.author.send(f"**{user_name}**: {message}")
                    else:
                        if msg.author == a.author:
                            desc = desc + f"\n `{a_name}`: {message}"
                            # desc = desc + f"\n `**{a_name}**`: {message}"

                        else:
                            desc = desc + f"\n`{user_name}`: {message}"
                            # desc = desc + f"\n`**{user_name}**`: {message}"

                        user_msg = discord.Embed(title="_WELCOME TO CHATBOT :heart:_", description=desc, color= 0x2ecc71)
                        # a_msg = discord.Embed(title="_WELCOME TO CHATBOT :heart:_ ", description=desc_a, color= choice(colors))

                        temp = await user.author.send(embed=user_msg)
                        await user_msg_edit.delete()
                        user_msg_edit = temp

                        temp = await a.author.send(embed=user_msg)
                        await a_msg_edit.delete()
                        a_msg_edit = temp

    else:
        await ctx.author.send("you are active in chat with someone. or you are in waiting queue. pls wait. :heart:")

@client.command()
async def leave(ctx):
    pass

@client.command()
async def live(ctx):
    await ctx.send(f"live: {Chatbox.live()}")

@client.command()
async def next(ctx):
    pass

@client.command()
async def report(ctx):     #maybe this will be changed to button!
    pass

@client.command(aliases = ("fake", "incog"))
async def anonymous(ctx, *args):
    id = hash(ctx.author.id)
    if args == ():
        names = c.execute(f"select incog_name from incog where hash == {id}").fetchone()
        name = names[0]
        await ctx.author.send(f"Your anonymous_name :skull: is  **{name}**")
    else:
        name = " ".join(args)
        if len(c.execute("select hash from incog where hash == ?",(id,)).fetchall())==1:
            c.execute("delete from incog where hash == ?", (id,))
        c.execute("insert into incog values(?, ?)",(id, name))
        conn.commit()
        await ctx.author.send(f"Your anonymous_name :bust_in_silhouette: is set to --> **{name}**")

@client.command()
async def test(ctx):
    embedVar = discord.Embed(title="_WELCOME TO CHATBOT :heart:_", description="**Hi ra **\npukka", color= choice(colors))
    embedVar1 = discord.Embed(description="**Hi ra ** \n hehe sorry!")
    # embedVar.add_field(name="Field1", value="hi", inline=False)
    # embedVar.add_field(name="Field2", value="hi2", inline=False)
    msg = await ctx.send(embed=embedVar)
    time.sleep(1)
    await msg.edit(embed=embedVar1)
    # x = ctx.author.id.send("STOP messaging me.")
    # if f"{ctx.author}" == f"{ctx.channel}".split(" ")[-1]:
        # await x
        # return
    # y = ctx.send('WORKING.')
    # await x and await y

client.run('MTAwMzMzMzY1MTMwOTgwOTc5Ng.GNKisO.BIK6kKUVAJ_Xe0BxnMEGGxB8F2jHGcTCbXsdIs')