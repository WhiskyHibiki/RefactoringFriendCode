from telebot import types


class TelegramButtons:
    def __init__(self, button: dict):
        key, value = next(iter(button.items())) # чтение данных из dict, для кнопок
        self.button_name = value
        self.button_callback = key

    def make_tg_button(self):
        return types.InlineKeyboardButton(text=self.button_name, callback_data=self.button_callback) # кнопки создаются тут
