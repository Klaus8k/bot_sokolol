from aiogram import Bot, Dispatcher, types, executor

import json
# https://t.me/SokololBot


def file_check(file='db_SokololBot.json', type_open='r', unit=None):
    with open(file=file, mode=type_open) as f:
        if unit == 'token':
            return json.loads(f.read())['bot_token']
        else:
            result_unit = json.loads(f.read())['users']
            return result_unit


def get_user(message: types.Message):
    users_dict = file_check(unit='users')
    request_user = str(message['chat']['id'])
    if request_user in [users_dict[user]['chat_id'] for user in users_dict.keys()]:
        for i in users_dict.keys():
            if users_dict[i]['chat_id'] == request_user:
                return users_dict[i]


bot = Bot(token=file_check(unit='token'), parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot=bot)


# Хэндлер ответа
@dp.message_handler(commands=['start', 'help'])
async def cmd_start(message: types.Message):
    user = get_user(message)
    print('req_mess:', request_message)
    print(f'user {user["first_name"]}:', user)

    if message.get_command() == r'/start':
        await message.reply('Get start!@')
    elif message.get_command() == r'/help':
        await message.answer('Бот помощник')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
