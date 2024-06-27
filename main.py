from tkinter import *
from tkinter import ttk

global phonebook_file_name, phone_book
phonebook_file_name = 'phonebook.txt'

root = Tk()  # создаем корневой объект - окно
root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
root.geometry("1024x768")  # устанавливаем размеры окна

def read_all():
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(phonebook_file_name ,'r' ,encoding='utf-8') as phb:
        for line in phb:


def add_record():
    window_new = Tk()
    window_new.title("Добавить нового")
    window_new.geometry("250x200")
    label = ttk.Label(window_new, text="Принципиально новое окно")
    label.pack(anchor=CENTER, expand=1)


for column in range(3):
    root.columnconfigure(index=column, weight=1)
for row in range(3):
    root.rowconfigure(index=row, weight=1)

entry = ttk.Entry()
entry.grid(row=0, column=0)
entry2 = ttk.Entry()
entry2.grid(row=1, column=0)
# entry.pack(anchor=NW, padx=16, pady=6)

# label = Label(text="Hello METANIT.COM")  # создаем текстовую метку
# label.pack()  # размещаем метку в окне
add_new_button = ttk.Button(text='Добавить', command=lambda: add_record())
add_new_button.grid(row=1, column=2)

records = Listbox()
records.grid(row=0, column=1, rowspan=3, sticky=NSEW)

records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")
records.insert(END, "Python")
records.insert(END, "C#")



root.mainloop()
