from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder
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


# Хэндлер ответа с фото (из папки на компе)
@dp.message(F.text, Command('photo', 'photoURL'))
async def photo_answer(message: types.Message):
    # (из папки на компе)
    file_ids = []
    if message.text == r'/photo':
        image_from_pc = FSInputFile("photo.jpg")
        result = await message.answer_photo(
            image_from_pc, caption="Изображение из файла на компьютере")
        file_ids.append(result.photo[-1].file_id)
    # (по ссылке)
    if message.text == r'/photoURL':
        image_from_url = URLInputFile(
            "https://tipkor.ru/static/tipkor/img/booklet.jpg")
        result = await message.answer_photo(image_from_url,
                                            caption="Изображение по ссылке")

# Обычные кнопки
@dp.message(Command("buttons"))
async def buttons(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="С пюрешкой"),
            types.KeyboardButton(text="Без пюрешки")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи")
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


@dp.message(F.text.lower() == "с пюрешкой")
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!",
                        reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text.lower() == "без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!",
                        reply_markup=types.ReplyKeyboardRemove())

# Кнопки с Keyboard Builder
@dp.message(Command('KB'))
async def kb_func(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(10):
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(3)
    await message.reply(
                        'choose num',
                        reply_markup=builder.as_markup(resize_keyboard=True, one_time_keyboard=True))












# Поиск емейла в произвольном тексте по entities
@dp.message(F.text)
async def any_message(message: types.Message):
    data = {'email': 'N/A'}
    entities = message.entities or []
    for item in entities:
        data[item.type] = item.extract_from(message.text)
    await message.reply("Нашел почту\n"
                        f"E-mail: {data['email']}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())