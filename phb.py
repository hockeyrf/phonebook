def work_with_phonebook():
    choic e =show_menu()
    phone_boo k =read_txt('phon.txt')
    while (choic e! =7):
        if choic e= =1:
            print_result(phone_book)
        elif choic e= =2:
            last_nam e =input('lastname ')
            print(find_by_lastname(phone_book ,last_name))
        elif choic e= =3:
            last_nam e =input('lastname ')
            new_numbe r =input('new  number ')
            print(change_number(phone_book ,last_name ,new_number))
        elif choic e= =4:
            lastnam e =input('lastname ')
            print(delete_by_lastname(phone_book ,lastname))
        elif choic e= =5:
            numbe r =input('number ')
            print(find_by_number(phone_book ,number))
        elif choic e= =6:
            user_dat a =input('new data ')
            add_user(phone_book ,user_data)
            write_txt('phonebook.txt' ,phone_book)
        choic e =show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
    изменить данные
    "5. Сохранить справочник в текстовом формате\n"
    "6. Закончить работу")
    choice = int(input())
    return choice


# Иванов,       Иван ,   111,  описание Иванова
# Петров,      Петр ,    222,  описание Петрова
# Васичкина , Василиса , 333 , описание Васичкиной
# Питонов,    Антон,     777,    умеет в Питон
# Питонов ,Антон ,777,    умеет в Питон


def read_txt(filename):
    phone_boo k =[]
    field s=.     ['Фамилия', 'Имя', 'Телефон', 'Описание']
    line.split(',') = [Питонов,    Антон,     '777',    'умеет в Питон']
    with open(filename ,'r' ,encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
        # dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
            phone_book.append(record)
    return phone_book


def write_txt(filename , phone_book):
    with open(filename ,'w' ,encoding='utf-8') as phout:
        for i in range(len(phone_book)): s=''
            for v in phone_book[i].values():
                s = s + v + ','
                phout.write(f'{s[:-1]}\n')
WA
x = 10
x = x + 5

work_with_phonebook()

























