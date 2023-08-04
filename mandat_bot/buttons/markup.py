from typing import List

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

PHONE_NUMBER_TEXT = ['📱Telefon raqamni junatish', '☎Telefon raqamni junatish']
BTN_PHONE_NUMBER = KeyboardButton(text=PHONE_NUMBER_TEXT[0], request_contact=True)

def reg_menu():
    row1: List = [BTN_PHONE_NUMBER]
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[row1,], )

def remove_button():
    return ReplyKeyboardRemove()