from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


menu = [
    [InlineKeyboardButton(text='Mini App', web_app=WebAppInfo())]
]

inline_keybords = InlineKeyboardMarkup(inline_keyboard=menu)