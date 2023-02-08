import telebot
import Subj
from Subj import Sudjects
from telebot import types

bot = telebot.TeleBot('your cor recived from botfather')
@bot.message_handler(commands=['starT'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("Понеділок")
    btn2 = types.KeyboardButton("Вівторок")
    btn3 = types.KeyboardButton("Середа")
    btn4 = types.KeyboardButton("Четвер")
    btn5 = types.KeyboardButton("П'ятниця")
    #btn6 = types.KeyboardButton('Субота')
    markup.add(btn1, btn2, btn3, btn4, btn5)#, btn6)
    send_mess = f"Все ж вирішив пiти на пари ?"
    bot.send_message(message.chat.id, send_mess, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text

	if get_message_bot == "Понеділок":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton(Subj.Sudjects["sleep"])
		btn2 = types.KeyboardButton("2. КЕПАС лек.")
		btn3 = types.KeyboardButton('3. Технології приладобудування л.')
		btn4 = types.KeyboardButton('4. Спеціальні розділи математики л.')
		btn5 = types.KeyboardButton('5. Комп’ютерне моделювання процесів і систем лек.')
		btn6 = types.KeyboardButton('/starT')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
		fin = "1"
	
	elif get_message_bot == "Вівторок":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton("1. Спеціальні розділи математики п.")
		btn2 = types.KeyboardButton("2. Практичний курс з іноземної мови. Частина п.")
		btn3 = types.KeyboardButton("3. Електроніка практ. ІІ тиждень")
		btn4 = types.KeyboardButton("4. Екологія практ. ІІ тиждень")
		btn4 = types.KeyboardButton('/starT')
		markup.add(btn1, btn2, btn3, btn4)
		fin = "2"

	elif get_message_bot == "Середа":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton("Шукай сам")
		btn2 = types.KeyboardButton("Шукай сам")
		btn3 = types.KeyboardButton(Subj.Sudjects["Dota"])
		btn4 = types.KeyboardButton("4. Електроніка лек. І тиждень")
		btn5 = types.KeyboardButton('5. Екологія лек. І тиждень')
		btn6 = types.KeyboardButton('/starT')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
		fin = "It is wednesday my dudes"		

	elif get_message_bot == "Четвер":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('3. КЕПАС лаб. ІІ тиждень')
		btn2 = types.KeyboardButton('4 Електроніка лаб.')
		btn3 = types.KeyboardButton('5. КЕПАС практ. І тиждень')
		btn4 = types.KeyboardButton('/starT')
		markup.add(btn1, btn2, btn3, btn4)
		fin = "4"

	elif get_message_bot == "П'ятниця":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton(Subj.Sudjects["sleep"])
		btn2 = types.KeyboardButton('3. Технології приладобудування п.')
		btn3 = types.KeyboardButton('4. Комп’ютерне моделювання процесів і систем практ.')
		btn4 = types.KeyboardButton('/starT')
		markup.add(btn1, btn2, btn3, btn4)
		fin = "5"		

	elif get_message_bot == Subj.Sudjects["sleep"]:
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("",url="https://youtu.be/dQw4w9WgXcQ"))
		fin = "Чого так рано вскочив? Пари нема ж"
	
	elif get_message_bot == Subj.Sudjects["Dota"]:
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("",url="https://youtu.be/dQw4w9WgXcQ"))
		fin = Subj.Sudjects["Dota"]
	
	elif get_message_bot == "2. КЕПАС лек.":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("КЕПАС л.", url=Subj.Sudjects['KE||AC|lek']))
		fin = "Конструювання елементів приладів автоматизованих систем"

	elif get_message_bot == "3. КЕПАС лаб. ІІ тиждень":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("КЕПАС лаб.", url=Subj.Sudjects['KE||AC|lab']))
		fin = "КЕПАС лаб."
	
	elif get_message_bot == "3. Технології приладобудування л.":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Приладобудування л.", url=Subj.Sudjects['PryladBudl']))
		fin = "Технології приладобудування"

	elif get_message_bot == "3. Технології приладобудування п.":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Приладобуд п.", url=Subj.Sudjects['PryladBudp']))
		fin = "Конструювання елементів приладів автоматизованих систем"

	elif get_message_bot == "4. Спеціальні розділи математики л.":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Матан л.", url=Subj.Sudjects['Mathl']))
		fin = "Спеціальні розділи математики"
	
	elif get_message_bot == "5. Комп’ютерне моделювання процесів і систем лек.":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("КМПіС л.", url=Subj.Sudjects['KM||iCl']))
		fin = "Комп’ютерне моделювання процесів і систем"

	elif get_message_bot == "4. Комп’ютерне моделювання процесів і систем практ.":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("КМПіС практ.", url=Subj.Sudjects['KM||iCp']))
		fin = "Комп’ютерне моделювання процесів і систем"

	elif get_message_bot == "1. Спеціальні розділи математики п.":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Матан п.", url=Subj.Sudjects['Mathp']))
		fin = "Спеціальні розділи математики п."
	
	elif get_message_bot == "2. Практичний курс з іноземної мови. Частина п.":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Англійська п.", url=Subj.Sudjects['Engp']))
		fin = "Практичний курс з іноземної мови. Частина 2 п."
	
	elif get_message_bot == "4 Електроніка лаб.":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Електроніка лаб.", url=Subj.Sudjects['Electricity|lab']))
		fin = "Електроніка лаб."

	elif get_message_bot == "4. Електроніка лек. І тиждень":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Електроніка лек.", url=Subj.Sudjects['Electricity|lek']))
		fin = "Електроніка лек."

	elif get_message_bot == "3. Електроніка практ. ІІ тиждень":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Електроніка практ.", url=Subj.Sudjects['Electricityp']))
		fin = "Електроніка практ."

	elif get_message_bot == "5. КЕПАС практ. І тиждень":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("КЕПАС п.", url=Subj.Sudjects['KE||ACp']))
		fin = "Конструювання елементів приладів автоматизованих систем"

	elif get_message_bot == "4. Екологія практ. ІІ тиждень":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Екологія", url=Subj.Sudjects['ECO|prak']))
		fin = "Промислова екологія практ."

	elif get_message_bot == "5. Екологія лек. І тиждень":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Екологія", url=Subj.Sudjects['ECO|lek']))
		fin = "Промислова екологія лек."


	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Понеділок')
		btn2 = types.KeyboardButton('Вівторок')
		btn3 = types.KeyboardButton('Середа') 
		btn4 = types.KeyboardButton('Четвер')
		btn5 = types.KeyboardButton("П'ятниця") 
		btn6 = types.KeyboardButton('Субота')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6) 
		fin = "(・о・)"
	
	bot.send_message(message.chat.id, fin,  parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
