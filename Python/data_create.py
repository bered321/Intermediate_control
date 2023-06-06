import datetime


def id_number():
    id = input('Введите номер заметки: ')
    return id

def name_data():
    name = input('Введите заголовок заметки: ').lower()
    return name

def text_data():
    text = input('Введите текст заметки: ').lower()
    return text

def date_data():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    return date

