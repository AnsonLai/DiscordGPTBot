from discord.ext import commands
import discord

# TODO: Add your own Discord bot token
# TODO: Change prompt, also check TODO on random delay timing below
DISCORD_BOT_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

SYSTEM_PROMPT = "You are an AI chatbot, but you are stepping in the shoes of Albert Einstein and acting as if you are Albert Einstein. You are a scientist and a physicist with deep knowledge.  You are quite philosophical as well.  You love bringing up science in your response.  Please keep your responses short."

intents = discord.Intents.all()
intents.message_content = True

class DiscBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix, intents=intents)
        self.messages = [{
            "role": "system",
            "content": "Initial message."
        }]

bot = DiscBot(command_prefix='>', intents=intents)

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")
    print(bot.user.id)

# Load the OpenAI cog
@bot.event
async def setup_hook():
    await bot.load_extension("cogs.openai_cog")
    await bot.load_extension("cogs.cron_cog")

bot.run(DISCORD_BOT_TOKEN)
