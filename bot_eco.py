import telebot
import random
import os

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("Ваш токен")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот в котором ты сможешь узнать полезные советы по экологии👋(напиши./help для показа команд)!')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Вот список команд:/vred_othodov./gde_utilizirovat./eco_picture.!')

@bot.message_handler(commands=['gde_utilizirovat'])
def send_welcome(message):
    response = '''Несколько организаций, занимающихся утилизацией отходов в Нижнем Новгороде, и их адреса:

«НПО Промэкология». Утилизация отходов, адрес: Яблоневая ул., 26.
«Synergetic». Утилизация отходов, адрес: площадь Революции, 2А, этаж 1.
«Маг Груп». Утилизация отходов, адрес: Сормовское ш., 1Д.
«Мусороперегрузочная станция». Утилизация отходов, адрес: ул. Коминтерна, 53А.
«ПродКапитал». Утилизация отходов, адрес: Электровозная ул., 1Б.
«Промконтракт». Приём и скупка металлолома, адрес: Московское ш., 302А, корп. 2.
«Утилизация техники». Утилизация отходов, адрес: Интернациональная ул., 100, корп. 10.'''
    
    bot.reply_to(message, response)

@bot.message_handler(commands=['vred_othodov'])
def send_welcome(message):
    response = '''  Отходы наносят вред окружающей среде и здоровью человека. 

Это связано с тем, что значительная часть отходов содержит токсичные и опасные компоненты.
Неправильное обращение с отходами (захоронение на свалках, сжигание) приводит к загрязнению почвы, 
водоёмов и атмосферы, а также к негативному воздействию на здоровье человека.
Поэтому я рекомендую утилизировать отходы'''
    
    bot.reply_to(message, response)

@bot.message_handler(commands=['eco_picture'])
def send_mem(message):
    b = (os.listdir('images_eco'))
    gg = random.choice(b)
    with open(f'images_eco/{gg}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

bot.polling()
