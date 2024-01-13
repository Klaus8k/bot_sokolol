from aiogram import Bot, Dispatcher, executor, types
import json

with open('db_SokololBot.json', 'r') as f:
    token = json.loads(f.read())['bot_token']

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot=bot)

# Хэндлер ответа
@dp.message_handler(commands=['start', 'help', '1-10'])
async def cmd_start(message: types.Message):
    if message.get_command() == r'/start':
        await message.reply('Get start!@')
    elif message.get_command() == r'/help':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Menu', 'random', 'Order']
        keyboard.add(*buttons)
        await message.answer('Menu:', reply_markup=keyboard)
        
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)