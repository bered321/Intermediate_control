import datetime
import os
import csv
from data_create import id_number, name_data, text_data, date_data



def input_data():
    print('Введите данные для записи в файл:\n ')
    id = id_number()

    with open(f"data.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=';')
        existing_ids = set(row[0] for row in reader)
        if id in existing_ids:
            print(f"Заметка с номером {id} уже существует.")

            # Поиск максимального номера id
            max_id = max(existing_ids)
            print(f"Последний номер заметки: {max_id}")
            return
        
    name = name_data()
    text = text_data()
    date = date_data()
   
    with open(f"data.csv", "a", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
                [
                    id,
                    name,
                    text,
                    date
                ]
        )    
     

def print_data():    
    if os.path.exists("data.csv"):
        print('Вывод данных из файла: ')
        with open(f"data.csv", 'r', encoding="utf-8") as file:
            list_data = file.readlines()
            for element in list_data:
                print(element)
    else:
        print("Файла не существует!!!")


def filter_data(filter_string):
    filtered_notes = []
    
    filter_date = datetime.datetime.strptime(filter_string, '%Y-%m-%d').date()
    
    with open("data.csv", 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        for element in list_data:
            parts = element.strip().split(';')
            note_date = datetime.datetime.strptime(parts[3], '%Y-%m-%d').date()
            if note_date == filter_date:
                filtered_notes.append(element)
    for element in filtered_notes:
        print(element)

        
def delete_data(delete_string):
    with open(f"data.csv", "r", encoding="utf-8") as file:
        list_data = file.readlines()
        for i in range(len(list_data)):
            if delete_string == int(list_data[i].split(";")[0]):
                list_data.pop(i) 
                break
    with open(f"data.csv", "w", encoding="utf-8") as file:
        for i in range(len(list_data)):
            temp_record = list_data[i].split(";")
            file.write(f"{temp_record[0]};{temp_record[1]};{temp_record[2]};{temp_record[3]}")


def swap_value(id2):
    with open("data.csv", 'r', encoding='utf-8') as file:
        list_data = file.readlines()
        found = False

        for line_i in range(len(list_data)):
            record_list_data = list_data[line_i].strip().split(';')
            if record_list_data[0] == str(id2):
                print(f"Заметка с ID {id2} найдена.")
                print("Выберите часть заметки для редактирования:")
                print("1 - Заголовок")
                print("2 - Текст")
                choice = int(input("Введите номер операции: "))
                if choice == 1:
                    new_title = input("Введите новый заголовок: ")
                    record_list_data[1] = new_title
                    found = True
                    print("Заголовок успешно изменён!")
                elif choice == 2:
                    new_text = input("Введите новый текст: ")
                    record_list_data[2] = new_text
                    found = True
                    print("Текст успешно изменён!")
                else:
                    print("Некорректный выбор.")
                list_data[line_i] = ';'.join(record_list_data) + '\n'
                break

        if not found:
            print(f"Заметка с ID {id2} не найдена.")

    with open("data.csv", 'w', encoding='utf-8') as file:
        for line in list_data:
            file.write(line)


