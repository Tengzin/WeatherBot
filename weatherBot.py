from discord.ext.commands import Bot
import requests
from discord import Game
from weather import Weather, Unit

BOT_PREFIX = ("~")
TOKEN = "NTMwMDQ1MTczMzIxODI2MzM0.Dw5q3w.r9jiqllmZNxPjGwNeYLaU--2kEg"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='weather',
                description="Displays the current weather.",
                brief="How's it looking outside?")
async def weather(reqLocation):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(reqLocation)
    condition = location.condition
    forecasts = location.forecast
    today = forecasts[0]
    await client.say(today.text + ", low/high is " + today.low + "/" + today.high + " degrees Celsius.")

client.run(TOKEN)