from discord.ext import commands
import aiocron
import random
from openai import OpenAI

# TODO: Add your own OpenAI Key, then find out the your Discord channel's ID
# TODO: Change prompt, also check TODO on cron scheduling below
OPENAI_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
DISCORD_CHANNEL_ID = 00000000000000000000
CONTINUATION_PROMPT = "The chat has stalled for a period of time. Please restart the conversation somehow. Pretend like you haven't interacted with the user for a while. You might ask the user for a favor, share a joke or interesting fact that reminded you of the conversation or the user, or just prompt the user again to respond. Use your creativity to restart the conversation and show some emotion such as being worried or missing the user."


class CronJobCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.OPENAI_KEY = OPENAI_KEY
        self.client = OpenAI(api_key=self.OPENAI_KEY)
        self.BOT_CHANNELS = DISCORD_CHANNEL_ID
        self.schedule_tasks()

    def schedule_tasks(self):
        # TODO: Choose a different cron job and random check for the bot to randomly reach out to user.  Right now, every 2 days, the bot has a 50% chance of reaching out to user.
        @aiocron.crontab("* * */2 * *")
        async def restart_conversation():
            if random.randrange(0, 10) > 5:
                print("Restarting conversation")

                self.bot.messages.append({
                    "role": "system",
                    "content": CONTINUATION_PROMPT
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
                
                channel = self.bot.get_channel(self.BOT_CHANNELS)
                if channel:
                    await channel.send(content)

async def setup(bot):
    await bot.add_cog(CronJobCog(bot))
