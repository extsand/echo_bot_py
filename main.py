import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.dispatcher.filters import Text

#custom import
from app.read_file import get_proverb
from app import app_configure

# print(app_configure.telegram_bot_token)



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

bot_token = app_configure.telegram_bot_token
bot = Bot(token=bot_token)
dp = Dispatcher(bot=bot)

#generate button
# button_hi = KeyboardButton('Hello again')
# greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
# # greet_kb.add(button_hi)
#
# button_location = KeyboardButton('Shared location', request_location=True)
# location_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_location)

def get_welcome_message(username):
    msg = f"Hi {username}\n" \
          f"I glad to see you again.\n" \
          f"My aim - it's an echo. I just i'll send you all, what you i'll " \
          f"sending me.\n\n" \
          f"My commands is:\n" \
          f"/start\n" \
          f"/help\n" \
          f"/a\n" \
          f"/btn\n" \
          f"also, you can work with the telegram buttons " \
          f"below.Do you have any questions? "
    return msg



#create buttons
button_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Echo test')
).add(
    KeyboardButton(text='Send me proverb')
).add(
    KeyboardButton(text='Send phone number', request_contact=True)
).add(
    KeyboardButton(text='Send location', request_location=True)
).add(
    KeyboardButton(text='Help me, Taonga')
)

#handling commands
@dp.message_handler(commands=['btn'])
async def process_start_command(message: types.Message):
    await message.reply("Generate buttons below!", reply_markup=button_markup)

@dp.message_handler(commands=['start', 'help', 'a'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(
        text=get_welcome_message(username=username),
        reply=True
    )

@dp.message_handler(commands=['proverb'])
async def say(message: types.Message):
    await message.reply(
        text=get_proverb(),
        reply=True
    )


@dp.message_handler(Text(equals="Send me proverb"))
async def send_proverb(message: types.Message):
    await message.reply(
        text=get_proverb(),
        reply=True
    )

@dp.message_handler(Text(equals="Help me, Taonga"))
async def send_help(message: types.Message):
    username = message.from_user.username
    await message.reply(
        text=get_welcome_message(username=username),
        reply=True
    )

@dp.message_handler(content_types=types.ContentType.TEXT)
async def do_echo(message: types.Message):
    text = message.text
    if text and not text.startswith('/'):
        await message.reply(text=text)

#bot init
def run_bot():
    #for future
    #send message to owner about bot status
    print('Bot activate')
    executor.start_polling(dispatcher=dp, skip_updates=True)

if __name__ == '__main__':
    run_bot()

