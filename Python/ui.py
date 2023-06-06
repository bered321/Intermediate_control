from logger import input_data, print_data, filter_data, delete_data, swap_value



def interface():
    while True:
        print(""" Выберите режим работы:
                1 - Создать новую заметку
                2 - Вывод заметок
                3 - Фильтрация заметок по дате создания
                4 - Удаление заметки
                5 - Редактирование заметки
                6 - Выход
                """)

        operation_number = int(input('Введите номер операции: '))

        if operation_number == 1:
            input_data()
        elif operation_number == 2:
            print_data()
        elif operation_number == 3:
            print("Введите дату в формате 'Год-месяц-число': ")
            filter_string = input()
            filter_data(filter_string)
        elif operation_number == 4:
            delete_string = int(input("Введите номер заметки для удаления: "))
            delete_data(delete_string)
        elif operation_number == 5:
            swap()
        elif operation_number == 6:
            break

def swap():
    id2 = int(input('Введите номер заметки: '))
    swap_value(id2)


