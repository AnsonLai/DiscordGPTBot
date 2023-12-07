from discord.ext import commands
from openai import OpenAI
import asyncio
import random

import sys

# TODO: Add your own OpenAI Key, then find out the your Discord bot's ID
OPENAI_KEY = "xxxxxxxxxxxxxxxxxxxx"
DISCORD_BOT_ID = 00000000000

class OpenAICog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.OPENAI_KEY = OPENAI_KEY
        self.client = OpenAI(api_key=self.OPENAI_KEY)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.author.id != DISCORD_BOT_ID:
            # TODO: Choose a different random delay for regular responses.  Right now it is set to delay randomly between 3 and 60 seconds.
            await asyncio.sleep(random.randrange(3,60))
            self.bot.messages.append({
                "role": "user",
                "content": message.content
            })
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.bot.messages,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            content = response.choices[0].message.content
            self.bot.messages.append({
                "role": "assistant",
                "content": content
            })
            
            await message.channel.send(content)

async def setup(bot):
    await bot.add_cog(OpenAICog(bot))
