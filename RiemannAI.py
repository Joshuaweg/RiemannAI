from http.client import responses
import openai
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import json

MAX_MESSAGES = 50
load_dotenv()
f_msg = open("messages.json")
msg=json.loads(f_msg.read())
f_msg.close()
openai.api_key=os.environ.get("OPEN_API_KEY")
def generateResponse(user,cmd,message):
    f_msg = open("messages.json")
    instruct = open(cmd+".txt")
    msg=json.loads(f_msg.read())
    if(user not in msg.keys()):
        msg[user]={}
        msg[user][cmd]=[]
        msg[user][cmd].append({"role":"system","content":instruct.read()})
    if(cmd not in msg[user].keys()):
        msg[user][cmd]=[]
        msg[user][cmd].append({"role":"system","content":instruct.read()})
    instruct.close()
    model="gpt-3.5-turbo"
    msg[user][cmd].append({"role":"user","content":message})
    response = openai.ChatCompletion.create(
            model=model,
            messages=msg[user][cmd]
            )
    msg[user][cmd].append({"role":"assistant","content":response.choices[0].message.content})
    while(len(msg[user][cmd])>MAX_MESSAGES+1):
       del msg[user][cmd][1]
       del msg[user][cmd][1]
    with open("messages.json", "w") as jsonFile:
        json.dump(msg, jsonFile)
    return response
intents = discord.Intents.default()
intents.message_content=True
bot = commands.Bot(command_prefix='!', intents=intents)
def run():
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')
    
        # wait for the bot to be fully loaded
        await bot.wait_until_ready()
    
        print(f'{bot.user.name} is ready to go!')
    @bot.command(name='hello')
    async def hello_command(ctx):
        print("lol")
        await ctx.send('Hello! I am a Discord bot.')

    @bot.command(name='ping')
    async def ping(ctx):
        await ctx.send('pong!')
    @bot.command("musa")
    async def algebra_intent(ctx,* ,arg):
        response=generateResponse(ctx.message.author.name,"musa",arg.replace("!musa",""))
        await ctx.send(response.choices[0].message.content)
    @bot.command("newton")
    async def calculus_intent(ctx,* ,arg):
        response=generateResponse(ctx.message.author.name,"newton",arg.replace("!newton",""))
        await ctx.send(response.choices[0].message.content)
    @bot.command("hip")
    async def trigonometry_intent(ctx,* ,arg):
        response=generateResponse(ctx.message.author.name,"hip",arg.replace("!hip",""))
        await ctx.send(response.choices[0].message.content)
    @bot.command("euclid")
    async def geometry_intent(ctx,* ,arg):
        response=generateResponse(ctx.message.author.name,"euclid",arg.replace("!euclid",""))
        await ctx.send(response.choices[0].message.content)
    @bot.command("cantor")
    async def discrete_intent(ctx,* ,arg):
        response=generateResponse(ctx.message.author.name,"cantor",arg.replace("!cantor",""))
        await ctx.send(response.choices[0].message.content)
    @bot.command("curie")
    async def physics_intent(ctx,* ,arg):
        response=generateResponse(ctx.message.author.name,"curie",arg.replace("!curie",""))
        await ctx.send(response.choices[0].message.content)
    @bot.command("feynman")
    async def quantum_intent(ctx,* ,arg):
        response=generateResponse(ctx.message.author.name,"feynman",arg.replace("!feynman",""))
        await ctx.send(response.choices[0].message.content)
    @bot.command("bayes")
    async def stat_intent(ctx,* ,arg):
        response=generateResponse(ctx.message.author.name,"bayes",arg.replace("!bayes",""))
        await ctx.send(response.choices[0].message.content)
    @bot.command("guass")
    async def stat_intent(ctx,* ,arg):
        response=generateResponse(ctx.message.author.name,"guass",arg.replace("!guass",""))
        await ctx.send(response.choices[0].message.content)
    #Admin Controls

    bot.run(os.environ.get("DISCORD_KEY"))
    
if __name__ == "__main__":
    run()