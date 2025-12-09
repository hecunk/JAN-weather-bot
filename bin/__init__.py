import logging
import aiogram
import json

with open('config.json') as config:
    config = json.load(config)

users: dict[int, tuple[float, float]] = {}

logging.basicConfig(level=logging.INFO)

bot = aiogram.Bot(token=config["bot_token"])
dp = aiogram.Dispatcher()

from handlers import *
