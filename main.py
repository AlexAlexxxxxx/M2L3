
import telebot
from config import token
# Задание 7 - испортируй команду defaultdict
from logic import quiz_questions
from collections import defaultdict
from gpt_ya import gpt


user_responses = {}
status = 1
delete_id = 0

# Задание 8 - создай словарь points для сохранения количества очков пользователя
points = defaultdict()

bot = telebot.TeleBot(token)

def send_question(chat_id):
    global delete_id
    # if delete_id != 0:
    #     bot.delete_message(chat_id, delete_id)
    delete_id = bot.send_message(chat_id, quiz_questions[user_responses[chat_id]].text, reply_markup=quiz_questions[user_responses[chat_id]].gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global status 

    if status == 1: 
        if call.data == "correct":
            bot.answer_callback_query(call.id, "Answer is correct")
            # Задание 9 - добавь очки пользователю за правильный ответ
            points[call.message.chat.id]  += 1 

        elif call.data == "wrong":
            bot.answer_callback_query(call.id,  "Answer is wrong")
        
        # Задание 5 - реализуй счетчик вопросов
        user_responses[call.message.chat.id]  += 1 
        # Задание 6 - отправь пользователю сообщение с количеством его набранных очков, если он ответил на все вопросы, а иначе отправь следующий вопрос
        if user_responses[call.message.chat.id]>=len(quiz_questions):
            status = 0 
            bot.send_message(call.message.chat.id, "The end")
            bot.send_message(call.message.chat.id, f"points = {points[call.message.chat.id]}")

        else:
            send_question(call.message.chat.id)
    else:
        bot.send_message(call.message.chat.id, "viktorinna zakonchilac")



@bot.message_handler(commands=['start'])
def start(message):
    global status
    status = 1
    if message.chat.id not in user_responses.keys():
        user_responses[message.chat.id] = 0
        points[message.chat.id]=0
        send_question(message.chat.id)
        # a = 1
        # if a == 0:
        #     bot.stop_polling()
        # elif a == 1:
        #     bot.polling()
        
    else:
        bot.send_message(message.chat.id, "ugra zapystilac zanovo")
        user_responses[message.chat.id] = 0
        points[message.chat.id]=0
        send_question(message.chat.id)
        # a = 1
        # if a == 0:
        #     bot.stop_polling()
        # elif a == 1:
        #     bot.polling()


    @bot.message_handler(func=lambda message: True)
    def echo_message(message):
        bot.reply_to(message, gpt(message.text))

bot.infinity_polling()
