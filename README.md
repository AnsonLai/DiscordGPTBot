# Discord "Natural" GPT Bot

The goal of this is to create a OpenAI GPT bot accessible through Discord.  The added "natural" behavior is for role-play.  There is a random delay between messages so that the bot doesn't immediately respond all the time.  There is also the ability for the bot to be proactive and reach out to the user from time to time.

## Instructions

You will need your own Discord bot token and OpenAI API key.  There are three files you need to look at, main.py at the root, and cron_cog.py and openai_cog.py in the cogs folder.
You will also need to identify your bot's ID and the channel ID so that your bot can operate.  These should be changed in the same 3 files.
You can look at the two files in the cogs folder, they both have settings to change the delay and proactivity of the bot.
You can adjust the prompts in main.py and each of the cogs.