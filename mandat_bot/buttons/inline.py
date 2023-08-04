from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from configs.constants import channel1_id, url


def check_chanel():
    markup = InlineKeyboardMarkup(row_width=1)
    chanel = InlineKeyboardButton(f"Kanalimiz", url=url)
    markup.add(chanel)
    check = InlineKeyboardButton("A'zo boldim✅", callback_data='subdone')
    markup.add(check)
    return markup