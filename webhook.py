import asyncio
import discord
from discord import Webhook
import aiohttp

async def send_webhook(url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(title="Hello from VS Code")
        await webhook.send(embed=embed, username="VS Code")
        
if __name__ == "__main__":

    # webhook URL, generated from a discord server -> server setting -> integration -> webhook
    # TODO replace with a real webhook URL 
    url = "https://discord.com/api/webhooks/xxxx00813148346xxxx/XXXXXXXXXXXXX"
    
    loop = asyncio.new_event_loop()
    loop.run_until_complete(send_webhook(url))
    loop.close()
