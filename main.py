import telebot
import sqlite3

token = '5842732622:AAGEky1ArqETEuS1hGGzRwHub6h_kgPqeDY'
bot = telebot.TeleBot(token)

con = sqlite3.connect("./fit.db", check_same_thread=False)

@bot.message_handler(commands=['start', 'help'])
def send_info(message):
    text = ('Привет, я чат бот Московского политеха.\n\n'
            'Я могу вывести информацию о проходных баллах, количстве оригиналов, претендентов направления ')
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['web'])
def send_Web(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Веб-технологии'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['sapr'])
def send_SAPR(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Интеграция и программирование в САПР'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['iss'])
def send_ISS(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Программное обеспечение информационных систем'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['cps'])
def send_CPS(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Киберфизические системы'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['spi'])
def send_SPI(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Системная и программная инженерия'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['ac'])
def send_AC(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'АС обработки информации и управления; ИТ в медиандустрии и дизайне; Технологии доп и VR; ПО игровой компьютерной индустрии; ИС умных пространств'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['dt'])
def send_DT(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Цифровая трансформация'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['aipcs'])
def send_AIPCS(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Автоматизированные системы обработки информации и управления'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['cis'])
def send_CIS(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Корпоративные информационные системы'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['big'])
def send_BIG(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Большие и открытые данные'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['itbm'])
def send_ITBM(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Информационные технологии управления бизнесом'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['ib'])
def send_IB(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Информационная безопасность'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

@bot.message_handler(commands=['cas'])
def send_CAS(message):
    cur = con.cursor()
    cur.execute("SELECT * FROM FIT WHERE program = 'Кибербезопасность автоматизированных систем'")
    rows = cur.fetchall()
    for row in rows:
        text = (
            f'Код: {row[1]}\nПрограмма (направление): {row[2]}\nОснова: {row[3]}\nКЦП: {row[4]}  Оригиналов: {row[5]}\n'
            f'Претендентов: {row[6]}\nПроходной балл: {row[7]}\nМаксимальный приоритет: {row[8]} \nСвободно: {row[9]}')
    con.commit()
    bot.send_message(message.chat.id, text=f'{text}')

bot.polling()
