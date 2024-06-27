from tkinter import *
from tkinter import ttk
from tkinter import messagebox

phonebook_file_name = 'phonebook.txt'
phone_book = []
fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("1024x768")  # устанавливаем размеры окна

def warning_dialog(text: str):
    messagebox.showinfo('Внимание', text)


def read_all():
    phone_book.clear()
    with open(phonebook_file_name, 'r', encoding='utf-8') as phb:
        for line in phb:
            phone_book.append(dict(zip(fields, line.split(','))))


def check_record_exist(text: str) -> bool:
    with open(phonebook_file_name, 'r', encoding='utf-8') as phb:
        if text in phb.read():
            return True
    return False


def write_record(last_name: str, name: str, phone: str, desc: str):
    with open(phonebook_file_name, 'a', encoding='utf-8') as phb:
        phone_book.append(dict(zip(fields, [last_name, name, phone, desc])))
        phb.write(f'{last_name},{name},{phone},{desc}\n')


def add_record(last_name: str, name: str, phone: str, desc: str):
    if len(phone) > 0 and check_record_exist(phone):
        warning_dialog('Такой номер существует')
    if all([len(last_name), len(name), len(phone), len(desc)]):
        write_record(last_name, name, phone, desc)
    else:
        warning_dialog('Одно или несколько из полей пустые.')

def update_listbox(records: Listbox):
    records.delete(0, END)
    for item in phone_book:
        records.insert(item)


for column in range(4):
    root.columnconfigure(index=column, weight=1)
for row in range(5):
    root.rowconfigure(index=row, weight=1)


ttk.Label(text='Фамилия').grid(row=0, column=0)
last_name = ttk.Entry()
last_name.grid(row=0, column=1)


ttk.Label(text='Имя').grid(row=1, column=0)
name = ttk.Entry()
name.grid(row=1, column=1)


ttk.Label(text='Телефон').grid(row=2, column=0)
phone = ttk.Entry()
phone.grid(row=2, column=1)


ttk.Label(text='Описание').grid(row=3, column=0)
description = ttk.Entry()
description.grid(row=3, column=1)

add_rec_butt = ttk.Button(text='Добавить', command=lambda: add_record(last_name.get(), name.get(), phone.get(), description.get()))
add_rec_butt.grid(row=4, column=0)


# entry.pack(anchor=NW, padx=16, pady=6)

# label = Label(text="Hello METANIT.COM")  # создаем текстовую метку
# label.pack()  # размещаем метку в окне
add_new_button = ttk.Button(text='Обновить', command=lambda: update_listbox(records))
add_new_button.grid(row=1, column=2)

records = Listbox()
records.grid(row=0, column=2, rowspan=3, sticky=NSEW)

root.mainloop()
