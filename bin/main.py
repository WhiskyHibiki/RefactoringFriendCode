from telebot import TeleBot, types
from telebot.types import Message
from bin.classes.cls_USER import User
from bin.classes.buttons import TelegramButtons
from bin.handlers.register_admin_callbacks import register_admin_callbacks

import json
import os


class TelegramBot(TeleBot):
    """
    Класс бота
    """

    def __init__(self, api_key):
        """
        Инициализация бота
        :param api_key: твой апи ключ бота
        """
        super().__init__(api_key)
        self.add_message_handlers()
        self.cur_admin_users = []

    def add_message_handlers(self):
        """
        ЭТо добавляешь перед каждой функцией, если пишешь её внутри класса, то есть в этом файле: add_message_handlers(self)
        Иначе не будет работать
        """

        @self.message_handler(commands=['start']) # Сам хендлер, селф обязателен
        def send_welcome(message: Message):
            this_user = User(message.from_user.id) # Вызов созднание объекта класса User

            if this_user.is_admin:
                self.reply_to(message, "You are admin")
                self.cur_admin_users.append(User)
                self.admin_panel_msg(message) # Вызов панели админа если админ

            else:
                self.reply_to(message, "Not admin")


    """
    def send_message(self, chat_id, text, **kwargs):
        print(f"[LOG] Sending message: {text} to chat {chat_id}")
        return super().send_message(chat_id, text, **kwargs)
    """

    def admin_panel_msg(self, message):
        """
        Динамическая создание кнопок админ панели, из файла buttons.json

        :param message:
        :return:
        """

        buttons_dict = self.read_json() # Чтение Json
        buttons_list = buttons_dict["admin_buttons"] # Получение данных из Json
        array_buttons = []

        markup = types.InlineKeyboardMarkup()

        for each in buttons_list:
            array_buttons.append(TelegramButtons(each)) # Динамическое создание кнопок с помощью класса TelegramButtons

        for each_btn in array_buttons:
            markup.add(each_btn.make_tg_button()) # Динамическое добавление кнопок в сообщение

        sent = self.send_message(message.chat.id, "text", reply_markup=markup, parse_mode='Markdown') # отправка сообщение, тут ничего сложного


    def read_json(self):
        """
        Чтение данных из файла button.json в дате
        :return: все данные из button.json
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))  # путь к bin/
        json_path = os.path.join(base_dir, '..', 'data', 'button.json')  # выход на уровень выше + data/

        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file) # само чтение файла эти две строки если что (with open...)

        return data



bot = TelegramBot("here need place token")
register_admin_callbacks(bot)
bot.infinity_polling()