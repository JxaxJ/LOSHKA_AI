import tkinter
from tkinter import *
from tkinter import ttk
import generate
from idlelib.tooltip import Hovertip
import re

def insert_generate():
    generate_text.insert(0.0, generate.generate_poems())


def delete_entry():
    generate_text.delete(0.0, 'end')


def get_leght(lenght):
    generate.save_lengths(lenght)


def apply_all():
    get_leght(lenght_input.get())
    apply_settings.set('*что бы применить настройки перезапустите приложение')


root = Tk()
root.title('Neural_network_demo')
root.geometry('800x600')
root.resizable(width=False, height=True)

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='poems')
tab_control.add(tab2, text='train_model')
tab_control.add(tab3, text='settings')

lb1 = Label(tab1)
lb1.pack()

lb2 = Label(tab2)
lb2.pack()

lb3 = Label(tab3)
lb3.pack()

tab_control.pack(expand=0, fill='both')
lenght_standart = tkinter.IntVar()
lenght_standart.set(generate.set_lengths())

apply_settings = tkinter.StringVar()

m_lb1 = ttk.Label(tab1, text='GENERATE', font=22)
m_lb2 = ttk.Label(tab2, text='GENERATE_FAKE_DATA', font=22)
m_lb3 = ttk.Label(tab3, text='SETTINGS', font=22)
s_lb1 = ttk.Label(tab3, text='SETTINGS', font=22)
s_lb2 = ttk.Label(tab3, text='lenght', font=22)
s_lb3 = ttk.Label(tab3, textvariable=apply_settings, font='Times 9')
lenght_input = Entry(tab3, width=9, textvariable=lenght_standart)
Hovertip(lenght_input, 'Чем больше символов - тем дольше будет генерация (особенно на старых компьютерах)', hover_delay=1000)

btn = ttk.Button(tab1, text='generate', command=insert_generate, width=22)
btn2 = ttk.Button(tab1, text='delete', command=delete_entry, width=22)
btn3 = ttk.Button(tab3, text='apply', command=apply_all, width=22)

generate_text = Text(tab1, width=50, height=20, wrap=WORD)

btn.place(x=24, y=345)
btn2.place(x=628, y=345)
btn3.place(x=320, y=100)
m_lb1.pack()
generate_text.pack()
s_lb1.pack()
s_lb2.place(x=270, y=50)
s_lb3.place(x=450, y=345)
lenght_input.place(x=359, y=50)

root.grid_columnconfigure(0, minsize=70)
root.grid_columnconfigure(1, minsize=70)

root.mainloop()