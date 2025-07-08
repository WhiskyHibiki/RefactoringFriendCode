from telebot import TeleBot, types

def register_admin_callbacks(bot):

    @bot.callback_query_handler(func=lambda call: call.data == "look_ticket")
    def handle_look_ticket(call):
        tickets = []  # пример пустого списка тикетов

        if not tickets:
            bot.answer_callback_query(call.id, "Тікетів немає!", show_alert=True)
        else:
            bot.send_message(call.message.chat.id, "Ось ваші тікети...")


    @bot.callback_query_handler(func=lambda call: call.data == "announce")
    def handle_look_ticket(call):
        announce = []  # пример пустого списка тикетов

        if not announce:
            bot.answer_callback_query(call.id, "Оголошень немає", show_alert=True)
        else:
            bot.send_message(call.message.chat.id, "Ось ваші announce...")