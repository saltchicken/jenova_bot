from jenova_bot import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
# intents = discord.Intents(members=True, guilds=True)
# intents.members = True  # Enable the Administrator intent
# intents = discord.Intents.default()
bot = JenovaBot(command_prefix='!', intents=intents)
bot.run(TOKEN)

