from aiogram.types import Message
from data.weather_getter import get_weather_week
from loader import dp

@dp.message(lambda message: message.text == "/haftalik")
async def haftalik_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        await message.answer(get_weather_week())
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")