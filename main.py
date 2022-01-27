import os
import discord
import math
import sympy as sp
import os
import keep_alive
from sympy import integrate, Symbol
import subprocess
from subprocess import PIPE
from PIL import Image
from bs4 import BeautifulSoup
import requests
from dislash import slash_commands, Option, OptionType
from discord.ext import commands
import asyncio
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from inspect import getsource
import sys
from discord_buttons_plugin import *
import logging
import textwrap
import contextlib
import io

import random
import csv
from util.util import clean_code,Pag



chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--lang=en-US')
chrome_options.add_argument('--headless')


driver = webdriver.Chrome(options=chrome_options)

  # Accesss Token Secert





# 接続に必要なオブジェクトを生成
my_secret = os.environ['TOKEN']


client = commands.Bot(command_prefix = "^",intents=discord.Intents.all())

buttons = ButtonsClient(client)

  # change command_prefix='-' to command_prefix=get_prefix for custom prefixes
slash = slash_commands.SlashClient(client)

count_task = None






@client.event
async def on_ready():
    Ca = 917748353264148540
    channel = client.get_channel(Ca)
    print("on ready")
    await channel.send('ready')
    await client.change_presence(activity=discord.Game(name="︎︎︎︎ "))
   # send_message_every_10sec.start()

@buttons.click
async def utf8(ctx):
  await ctx.reply()

@buttons.click
async def ascii(ctx):
	await ctx.reply("このメッセージはあなたにしか見えていません！")


@client.command()
async def test(message,arg):
  await message.channel.send("a")
  return


@slash.command(
    name = 'debug',
    description = 'code',
    options = [
        Option('text', 'nini', OptionType.STRING),
    ],
)
async def debug(inter, text=None):
    try:
      if text is not None:        
        await inter.reply(f'```{eval(text)}```')
    except:
        await inter.reply(f"```{traceback.format_exc()}```")



# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視)

    global count_task
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    print(f'{message.author}\n{message.content}')
    a = message.content[4:]
    embed = discord.Embed(title='削除',description=f'{a}件のメッセージが{message.author.mention}によって消されました')
    if message.content.startswith("/eval "):
      try:
        src = message.content.split(" ", 2)[-1].lstrip()

        await eval(src)
      except:
        await message.channel.send(f"```{traceback.format_exc()}```")
    if message.content[:3]=="enc":
	      await buttons.send(
          content = message.content,
          channel = message.channel.id,
          components = [
			ActionRow([
				Button(
					label="utf-8", 
					style=ButtonType().Primary, 
					custom_id="utf8"
				)
			]),ActionRow([
				Button(
					label="Ephemeral",
					style=ButtonType().Danger,
					custom_id="button_ephemeral"
				)
			])
		]
	)
   
      




    if message.content[:3] == "del":
        await message.channel.purge(limit=int(a))
        await message.channel.send(embed=embed)
    driver = webdriver.Chrome(options=chrome_options)
    if message.content[:2]=="kp":
      try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://kanji.reader.bz/jukugo_2moji/")
        driver.maximize_window()
        driver.find_element(By.NAME,"word").send_keys(message.content[3:])
        driver.find_element(By.XPATH,"//form/input").click()
        el=driver.find_elements(By.XPATH,"//p/a")
        f = open("g.csv","w+",encoding="utf-8")
        a=open("s.csv","w+",encoding="utf-8")
        writer = csv.writer(f) 
        we=csv.writer(a)
        i = 0
        for elm in el:
            i=i+1
            if elm.text[0]==message.content[3:] :
              csvlist=[]
              csvlist.append(elm.text)
              writer.writerow(csvlist)
            if elm.text[1]==message.content[3:]:
              cslist=[]
              cslist.append(elm.text)
              we.writerow(cslist)
            if i > 29:
                break
        f.close()
        a.close()
        dat=open("g.csv","r")
        print(dat.read())
        dat.close()
        b = open("g.csv","r",encoding="utf-8")
        j=open("y.csv","w")
        w=b.readlines()
        txt=str(random.sample(w,2))
        sdf="\[]n',"
        for s in sdf:
          txt=txt.replace(s,"")
        print(txt)
        j.write(txt)
        j.close()
        b.close()
        x=open("s.csv","r",encoding="utf-8")
        m=open("t.csv","w")
        g=x.readlines()
        tx=str(random.sample(g,2))
        h="\[]n',"
        for y in h:
          tx=tx.replace(y,"")
        print(tx)
        m.write(tx)
        m.close()
        x.close()
        e = open("t.csv","r")
        u=e.read()
        r=open("y.csv","r")
        i=r.read()
        await message.channel.send(f"kpcommands\n  {u.split()[0][0]}\n{u.split()[1][0]}□{i.split()[0][1]}\n  {i.split()[1][1]}")
      except:
        await message.channel.send(f"{message.content[3:]}は候補が少なすぎたため、処理を終了しました")
    l=message.content
    m = "•"
    w=l.find(m)
    u=l[w+1:]
    if message.content[:2]=="yt":
      if "•" not in message.content:
        await message.channel.send("動画が約何分かを指定してください")
      else:
        await message.channel.send(f"{3*(int(u)**2)/600}分ほどお待ちください")
        d=message.content[2:w]
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://offliberty.io/")
        driver.maximize_window()
        b=driver.find_element(By.CSS_SELECTOR,"input.track#track")
        b.send_keys(d)
        b.send_keys(Keys.ENTER)
        sleep(3*(int(u)**2)/10)
        c=driver.find_element(By.CSS_SELECTOR,"a.download")
        s=c.get_attribute('href')
        await message.channel.send(s)


    if message.content[:1]=="c":
        await message.channel.send(exec(message.content[1:]))  # 返信メッセージを送信 # 返信する非同期関数を実行
      
    p = message.content
    a = 'c'
    b = 'm'
    c = p.find(a)
    m = p.find(b)
    s = p[c + 1:m]
    nn = p[m + 1:]
    if message.content[:2] == 'ps':
        channel = client.get_channel(int(s))
        await channel.send(nn)
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    z = sp.Symbol('z')
    try:
      if message.content[0] == 'v':
        await message.channel.send(eval(message.content[1:]))
    except:
        await message.channel.send(f"```{traceback.format_exc()}```")
    i = "i"
    s = message.content.find(i)
    num = message.content[2:s]
    digit = message.content[s+1:]
    try:
      if message.content[:2] == "sq":
        
        result = ''
        cnt = added_num = minused_num = 0
        x = Symbol('x')

# 整数部分と小数点数部分で２回ループする
        for i in range(2):

            if int(digit) <= cnt:
               break

            split_num = num.split('.')[i] if i == 0 or '.' in num else ''

            if i == 0:
        # 1週目は整数部分なので最初を0埋め
                 formatted_num = ('0' if len(split_num) % 2 else '') + split_num
            else:
        # 2週目は小数点数部分なので最後を0埋め
                formatted_num = split_num + ('0' if len(split_num) % 2 else '')
                result += '.'

            two_num_list = [int(v + formatted_num[i + 1]) for i, v in enumerate(formatted_num) if i % 2 == 0]

    # 2桁ごとに分割した数字単位でループ
            j = 0
            while int(digit) > cnt:

                if i == 0 and len(two_num_list) <= j:
            # 整数部分を計算したので小数点部分へ行く
                    break

                target_num = int(str(minused_num) + (str(two_num_list[j]) if len(two_num_list) > j else '00'))

                if cnt == 0:
            # 最初の1回だけべき根以下の最大の自然数を取得
                    calc_stacking_num = result_num = sp.floor(sp.sqrt(target_num))
                else:
            # 2週目以降
            #   x*(added_num*10+x) が target_num 以下の最大の自然数を取得
                    result_num = [sp.floor(v) for v in sp.solve(x * (added_num * 10 + x) - target_num, x) if v >= 0][0]
                    calc_stacking_num = int(str(added_num) + str(result_num))

                result += str(result_num)

        # calc_stacking_num と下一桁を足す
                last_num = int(str(calc_stacking_num)[-1])
                added_num = calc_stacking_num + last_num

        # 次の two_digit と合わせるために引いた数を取得しておく
                minused_num = target_num - result_num * calc_stacking_num

                cnt += 1
                j += 1

        await message.channel.send(result)
    except:
        await message.channel.send(f"```{traceback.format_exc()}```")
    o = message.content[2:]
    if message.content[0:2] == 'y.':
        proc = subprocess.check_output(f"{o}", shell=True).decode()
        i = proc.returncode
        await message.channel.send(f"{proc}\n'return'{i}")



@client.event
async def on_message_delete(message):
    Ca = 919487367189004298
    channel = client.get_channel(Ca)
    embed = discord.Embed(
        title="へんしゅー部",
        description=f"{message.author.mention}\n削除されたメッセージ　: {message.content}",
        color=0xff0000)
    if message.author.bot:
        return
    else:
        await channel.send(embed=embed)
        attach_name = message.attachments[0].url
        a = f"ファイルや画像 {attach_name}"
        await channel.send(a)
      

@client.event
async def on_message_edit(before, after):
    Ca = 919487367189004298
    channel = client.get_channel(Ca)
    embed = discord.Embed(
        title="へんしゅう部",
        description=
        f'{before.author.name}\nチャンネル:{before.channel}\n時刻　：　{before.created_at}\n編集前　: {before.content}\n      ⏬\n編集後　: {after.content}\nファイルや画像:{before.attachments}\n{after.jump_url}',
        color=discord.Colour.gold())
    if before.author.bot:
        return
    else:
        await channel.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
  await client.get_channel(917748353264148540).send(f'```{error}```')



@client.event
async def on_slash_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send('You do not have permission to execute this command', hidden=True)
    else:
       await ctx.send('An unexpected error occured. Please contact the bot developer', hidden=True)
       raise error  # this will show some debug print in the console, when debugging
 # command_prefixはコマンドの最初の文字として使うもの。 e.g. !
#サーバー常時起動用
keep_alive.keep_alive()
# Botの起動とDiscordサーバーへの接続
client.run(os.environ["TOKEN"])
