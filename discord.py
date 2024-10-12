TOKEN = "MTI3OTYzODA1MDI1OTA3OTI0OQ.GvwqlB.dHsx3zo2AXwYh1JP6rS0tfMDpvx6Jib_Qrdl5s"

import discord
from discord.ext import commands
from discord import app_commands
import requests
import time
import hashlib
import base64
from urllib.parse import urlparse, parse_qs
import re

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)
platoboost = "https://gateway.platoboost.com/a/8?id="
platoboost2 = "https://gateway.platoboost.com/a/54658?id="
trigonlink = 'https://trigonevo.fun/whitelist/'
fluxusa = 'https://flux.li/android/external/start.php?HWID='
cookies =  dict(cookies_are='i7RymNfipUa88Fnr.b.ynfcZ5AHpLPqpHGpdIZT4oXA-1728494093-1.2.1.1-iRnyJTL2ud2vTRAwRHK3MkFtsstqdlml4q7TL74Wy8aJbXiuQqQBSZH12Ps.4a5pB0PMM3N2pp8zHogKcLUWKNv3Td3aXJhbAI0XbL5SfI.DSr6VZ9CUrPWREZ677oDWkuz3rvgt4brDTTORt7qDvepRQAWtj709tDWhE1oexsrlQn72UKowEV9hV5_RIGXM2vnLuDc0.xHZ29iXK3xH6BH0.2FL2ZRTC.GUl9lXhTYANlRtOdYTxz3Zf1Gvjww0Q5o7nbZX0LhwVA7.WtZzb9vG6SL3aCWZpCmjs.vqiCP3MbyPF8XfqkxUobxHUihQW4ONOm_cWAxwwVMoSXj5SNoH6_p70cw4KqPyNaFb.sZ.t6Hs5q61Fo9CCYnUdaf1J1l2oQ38Y0vqJMKFQ18Ha8ApESv0XXEo7NR53Cygn_s8RrO4emX4zavi2yBl3vk1D7KRw2Io2_ZMQX3lnIKb3Q')
loot_link = ' https://loot-link.com/s?'
pattern = r"(https?://[^\\s]+)"

def time_convert(n):
    hours = n // 60
    minutes = n % 60
    return f"{hours} Hours {minutes} Minutes"

def linkvert(url):
    link = re.sub(r'https://?.*?s=0&r=', '', url)
    link = re.sub(r'%3D', '', link)
    decoded_bytes = base64.urlsafe_b64decode(link + '==')
    decoded_bytes = str(decoded_bytes, 'utf-8')
    return decoded_bytes

def linkvertapi(url):
    link = requests.get('https://api.bypass.vip/bypass?url='+url)
    return link.json()["result"]

def sleep(ms):
    time.sleep(ms / 1000)

def get_turnstile_response():
    time.sleep(1)
    return "turnstile-response"

def Trigon_bypass(url):
    other = r"""Active"""
    response = requests.request('GET',url)
    link = response.content.decode('utf-8')
    if len(re.findall(other, link)) < 2:
        link = re.search(pattern, str(re.findall(r'''onclick="window.location.href=?.*?'">''', link)))
        url = link.group(1)
        response = requests.request('GET',url, allow_redirects=True)
        cooked = linkvertapi(response.url)
        response = requests.request('GET', cooked)
        response.raise_for_status()
        return {
            'True':'enjoy your gameplay on trigon'
        }
    return {
        'failed':"already bypassed XD"
    }


def cokka(real):
    parsed_url = urlparse(real)
    query_params = parse_qs(parsed_url.query)
    id = query_params.get('id', [None])[0]
    if not id:
        raise ValueError("Invalid URL: 'id' parameter is missing")

    payload = {}
    link = f"https://api-gateway.platoboost.com/v1/authenticators/54658/{id}"
    respond = requests.request('GET', link)
    respond.raise_for_status()
    other = respond.json()
    if 'key' in other:
        time_left = time_convert(other['minutesLeft'])
        print(f"\033[32m INFO \033[0m Time left:  \033[32m{time_left}\033[0m - KEY: \033[32m{other['key']}\033[0m")
        return {
                "status": "success",
                "key": other['key'],
                "time_left": time_left
            }
    other2 = other.get('captcha')
    if other2:
        print("\033[32m INFO \033[0m hCaptcha detected! Trying to resolve...")
            # If captcha exists, make sure to solve it before continuing
        response = requests.post(f"https://api-gateway.platoboost.com/v1/sessions/auth/54658/{id}",cookies=cookies,
        json={
                    "captcha": get_turnstile_response(),
                    "type": "Turnstile"
                }
            )
    else:
            # if no captcha, continue without it
        response = requests.post(
        f"https://api-gateway.platoboost.com/v1/sessions/auth/54658/{id}",cookies=cookies,
        json={})

    other = response.json()
    if 'message' in other:
        return {
            'error':'solve the hcaptcha'

        }
    link = other.get('redirect')
    link = linkvert(link)
    response = requests.get(link, allow_redirects=True)
    return response.url

def delta(url):
    start_time = time.time()
    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        id = query_params.get('id', [None])[0]

        if not id:
            raise ValueError("Invalid URL: 'id' parameter is missing")

        response = requests.get(f"https://api-gateway.platoboost.com/v1/authenticators/8/{id}",cookies=cookies)
        response.raise_for_status()
        already_pass = response.json()

        if 'key' in already_pass:
            time_left = time_convert(already_pass['minutesLeft'])
            print(f"\033[32m INFO \033[0m Time left:  \033[32m{time_left}\033[0m - KEY: \033[32m{already_pass['key']}\033[0m")
            return {
                "status": "success",
                "key": already_pass['key'],
                "time_left": time_left
            }

        captcha = already_pass.get('captcha')

        if captcha:
            print("\033[32m INFO \033[0m hCaptcha detected! Trying to resolve...")
            # If captcha exists, make sure to solve it before continuing
            response = requests.post(
                f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{id}",cookies=cookies,
                json={
                    "captcha": get_turnstile_response(),
                    "type": "Turnstile"
                }
            )
        else:
            # if no captcha, continue without it
            response = requests.post(
                f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{id}",cookies=cookies,
                json={}
            )

        if response.status_code != 200:
            security_check_link = f"{platoboost}{id}"

        loot_link = response.json()
        sleep(1000)
        decoded_lootlink = requests.utils.unquote(loot_link['redirect'])
        parsed_loot_url = urlparse(decoded_lootlink)
        r_param = parse_qs(parsed_loot_url.query)['r'][0]
        decoded_base64 = base64.b64decode(r_param).decode('utf-8')
        tk = parse_qs(urlparse(decoded_base64).query)['tk'][0]
        sleep(5000)

        response = requests.put(f"https://api-gateway.platoboost.com/v1/sessions/auth/8/{id}/{tk}",cookies=cookies)
        response.raise_for_status()

        response_plato = requests.get(f"https://api-gateway.platoboost.com/v1/authenticators/8/{id}",cookies=cookies)
        pass_info = response_plato.json()

        if 'key' in pass_info:
            time_left = time_convert(pass_info['minutesLeft'])
            execution_time = time.time() - start_time
            print(f"\033[32m INFO \033[0m Time left:  \033[32m{time_left}\033[0m - KEY: \033[32m{pass_info['key']}\033[0m")
            return {
                "status": "success",
                "key": pass_info['key'],
                
                "time taken": f"{execution_time:.2f} seconds"
            }

    except Exception as error:
        print(f"\033[31m ERROR \033[0m Error: {error}")
        execution_time = time.time() - start_time
        return {
            "status": "error",
            "error": "please solve the hcaptcha nigga",
            "time taken": f"{execution_time:.2f} seconds"
        }

# Main function
async def lootlinkkey(interaction, link):
    await interaction.response.defer(thinking=True)
    link2 = re.sub(r'https://loot-link\.com/s\?.*?&r=', '', link)
    encoded_str = re.sub(r'%3D','',link2)
    decoded_bytes = str(base64.urlsafe_b64decode(encoded_str + '=='), 'utf-8')
    embed=discord.Embed(title="BYPASSED", description="yippe", color=0xd9534f)
    try:
        embed.add_field(name='yay', value = decoded_bytes, inline=False)
    except:
        embed=discord.Embed(title="FAILED", description="NOO :sob:", color=0xd9534f)
    await interaction.followup.send(embed=embed)

headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
	    }

async def linky(interaction, link):
    await interaction.response.defer(thinking=True)
    embed=discord.Embed(title="BYPASSED", description="yippe", color=0xd9534f)
    try:
        url = "https://api.bypass.vip/bypass?url="+link
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        link = response.json()["result"]
        embed.add_field(name='link', value=link, inline=True)
    except:
        embed=discord.Embed(title="FAILED", description=":sob:", color=0xd9534f)
        return 0
    await interaction.followup.send(embed=embed)

async def fluxus(interaction, link):
    await interaction.response.defer(thinking=True)

    embed=discord.Embed(title="[BYPASSED](https://discord.gg/sfR8ebZcsz)", description="yippe", color=0xd9534f)
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/1119671882975821917/78c9f9030e29c9a02c6433ac0c67bf74.webp?size=100')
    link = re.sub(r"https://flux.li/android/external/?.*?HWID=",'',link)
    md5_hash = hashlib.md5()
    md5_hash.update(link.encode())
    key = md5_hash.hexdigest()
    try:
        embed.add_field(name='key:', value=f"```\n{key}\n```", inline=True)
    except:
        embed.add_field(name='key:', value=f"```\nDIED API DUE TO FLUXUS KEY SYSTEM\n```", inline=True)
    try:
        await interaction.followup.send(embed=embed)
    except:
        await interaction.followup.send(content = 'failed')

async def trigon(interaction, link):
    await interaction.response.defer(thinking=True)

    embed=discord.Embed(title="[BYPASSED](https://discord.gg/sfR8ebZcsz)", description="yippe", color=0xd9534f)
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/1119671882975821917/78c9f9030e29c9a02c6433ac0c67bf74.webp?size=100')
    link = Trigon_bypass(link)
    try:
        embed.add_field(name='key:', value=f"```\n{link['True']}\n```", inline=True)
    except:
        embed.add_field(name='key:', value=f"```\n{link['failed']}\n```", inline=True)
    
    try:
        await interaction.followup.send(embed=embed)
    except:
        await interaction.followup.send(content = 'failed')

async def delta_key(interaction, hwid):
    await interaction.response.defer(thinking=True)

    code = delta(hwid)
    embed=discord.Embed(title="[BYPASSED](https://discord.gg/sfR8ebZcsz)", description="yippe", color=0xd9534f)
    try:
        embed.add_field(name='key:', value=f"```\n{code['key']}\n```", inline=True)
    except:
        embed=discord.Embed(title="FAILED", description="no :sob:", color=0xd9534f)
    try:
        if "error" in code:
            embed.add_field(name='error', value = code["error"], inline=False)
        if "time_left" in code:
            embed.add_field(name='time left', value = code["time_left"], inline=True)
        if 'time taken' in code:
            embed.add_field(name='time taken', value = code["time taken"], inline=True)
    except:
        embed=discord.Embed(title="FAILED", description="KEY SYSTEM IS DOWN!", color=0xd9534f)
        await interaction.followup.send(embed=embed)
        return 0
    
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/1119671882975821917/78c9f9030e29c9a02c6433ac0c67bf74.webp?size=100')
    try:
        await interaction.followup.send(embed=embed)
    except:
        await interaction.followup.send(content = 'failed')

async def cokka_key(interaction, hwid):
    await interaction.response.defer(thinking=True)

    code = cokka(hwid)
    embed=discord.Embed(title="[BYPASSED](https://discord.gg/sfR8ebZcsz)", description="yippe", color=0xd9534f)
    try:
        if 'key' in code:
            embed.add_field(name='key:', value=f"```\n{code['key']}\n```", inline=True)
        else:
            embed.add_field(name='link:', value=f"{code}", inline=True)
    except:
        embed=discord.Embed(title="FAILED", description="no :sob:", color=0xd9534f)

    try:
        if 'error' in code:
            embed.add_field(name='error:', value=f"{code}", inline=True)
    except:
        print('ok')
    try:
        if "time_left" in code:
            embed.add_field(name='time left', value = code["time_left"], inline=True)
    except:
        embed=discord.Embed(title="FAILED", description=":sob:", color=0xd9534f)
        await interaction.followup.send(embed=embed)
        return 0
    
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/1119671882975821917/78c9f9030e29c9a02c6433ac0c67bf74.webp?size=100')
    try:
        await interaction.followup.send(embed=embed)
    except:
        await interaction.followup.send(content = 'failed')

#--- Get Delta Key ---#
@bot.tree.command(description="Get delta or platoboost key.")
@app_commands.describe(
    link='Enter your delta, cokka, fluxus or platoboost link'
)
async def key(interaction: discord.Interaction, link: str):
    if link.startswith(platoboost):
        await delta_key(interaction, link)
    elif link.startswith(platoboost2):
        await cokka_key(interaction, link)
    elif link.startswith(fluxusa):
        await fluxus(interaction, link)
    elif link.startswith(trigonlink):
        await trigon(interaction, link)
    else:
        await lootlinkkey(interaction, link)

@bot.tree.command(description="Bypass supported links.")
@app_commands.describe(
    link='Enter your link'
)
async def link(interaction: discord.Interaction, link: str):
    await linky(interaction, link)

#---------- Bot's events ----------#
#--- Log on ---#
@bot.event
async def on_ready():
    #--- Sync commands ---#
    await bot.tree.sync()
    print(f'Logged on as {bot.user}')

#--- Handle command not found ---#
@bot.event
async def on_command_error(ctx, error):
    pass

#---------- Run bot ----------#
bot.run(TOKEN)
