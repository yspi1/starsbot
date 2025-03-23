import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import WebAppInfo

API_TOKEN = '7943452824:AAEgZ6NBnwk9wSpXUarfJSzc2qsdA5SMmPo'

logging.basicConfig(level=logging.INFO)

# Указываем параметры по умолчанию, включая parse_mode
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    # Создаем клавиатуру с кнопкой для открытия Web App
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(
            text="Открыть мини-приложение",
            web_app=WebAppInfo(url="https://ваш-сайт.com")  # Укажите URL вашего Web App
        )]
    ])
    await message.answer("Добро пожаловать! Нажмите кнопку ниже, чтобы открыть мини-приложение.", reply_markup=keyboard)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())