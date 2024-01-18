from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode

import asyncio

import json
# https://t.me/SokololBot


def file_check(file='db_SokololBot.json', type_open='r', unit=None):
    with open(file=file, mode=type_open) as f:
        if unit == 'token':
            return json.loads(f.read())['bot_token']
        users = json.loads(f.read())['users']
        if unit in users.keys():
            print(users[unit])
            return users[unit]


bot = Bot(token=file_check(unit='token'), parse_mode="HTML")

dp = Dispatcher()


# Хэндлер ответа
@dp.message(F.text, Command('start', 'help', 'hmi'))
async def cmd_start(message: types.Message):
    user = file_check(unit=str(message.chat.id))
    print('req_mess:', message)
    print(f'user {user["first_name"]}:', user)

    if message.text == r'/start':
        await message.reply("'start', 'help', 'hmi'")
    elif message.text == r'/help':
        await message.answer('Бот помощник')
    elif message.text == r'/hmi':
        await bot.send_message(message.chat.id, user["first_name"])


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())