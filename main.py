from tkinter import *
from tkinter import ttk
from tkinter import messagebox

phonebook_file_name = 'phonebook.txt'
phone_book = []
fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

root = Tk()  # создаем корневой объект - окно
root.title("Телефонный справочник")
root.geometry("1024x768")


for column in range(4):
    root.columnconfigure(index=column, weight=1)
for row in range(5):
    root.rowconfigure(index=row, weight=1)


def warning_dialog(text: str):
    messagebox.showinfo('Внимание', text)


def read_all():
    phone_book.clear()
    with open(phonebook_file_name, 'a+', encoding='utf-8') as phb:
        for line in phb:
            phone_book.append(dict(zip(fields, line.split(','))))


def write_record(last_name: str, name: str, phone: str, desc: str):
    with open(phonebook_file_name, 'a', encoding='utf-8') as phb:
        phone_book.append(dict(zip(fields, [last_name, name, phone, desc])))
        phb.write(f'{last_name},{name},{phone},{desc}\n')
    update_listbox(records)


def check_record_exist(text: str) -> bool:
    with open(phonebook_file_name, 'r', encoding='utf-8') as phb:
        if text in phb.read():
            return True
    return False


def add_record(data: tuple):
    print(data[0])
    if len(phone) > 0 and check_record_exist(phone):
        warning_dialog('Такой номер существует')
    if all([len(last_name), len(name), len(phone), len(desc)]):
        write_record(last_name, name, phone, desc)
    else:
        warning_dialog('Одно или несколько из полей пустые.')

def update_listbox(records: Listbox):
    records.delete(0, END)
    for item in phone_book:
        print(item)
        # records.insert(f'{item[0]}\n {item[1]}\n {item[2]}\n {item[3]}')
        records.insert(END, f"|{item.get('Фамилия')} {item.get('Имя')} {item.get('Телефон')} {item.get('Описание')}|")


def create_frame(label_text):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)
    entry = ttk.Entry(frame)
    entry.pack(anchor=NW)
    return frame, entry

def clear_fields():
    last_name.delete(0, END)
    name.delete(0, END)
    phone.delete(0, END)
    description.delete(0, END)

last_name_frame, last_name = create_frame("Фамилия")
last_name_frame.grid(row=0, column=0)

name_frame, name = create_frame("Имя")
name_frame.grid(row=1, column=0)

phone_frame, phone = create_frame("Телефон")
phone_frame.grid(row=2, column=0)

desc_frame, description = create_frame("Описание")
desc_frame.grid(row=3, column=0)


add_rec_butt = ttk.Button(text='Добавить', command=lambda: add_record((last_name.get(), name.get(), phone.get(), description.get())) and clear_fields())
add_rec_butt.grid(row=4, column=0)


# entry.pack(anchor=NW, padx=16, pady=6)

# label = Label(text="Hello METANIT.COM")  # создаем текстовую метку
# label.pack()  # размещаем метку в окне
add_new_button = ttk.Button(text='Обновить', command=lambda: update_listbox(records))
add_new_button.grid(row=1, column=2)

records = Listbox()
records.grid(row=0, column=1, rowspan=5, sticky=NSEW)

read_all()
update_listbox(records)

root.mainloop()
