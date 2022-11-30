from tkinter import *
from cryptography.fernet import Fernet
import mysql.connector as connector
import main_passwords
from tkinter import messagebox
import customtkinter

def login():
    login_window = customtkinter.CTk()
    login_window.geometry('1000x800')
    login_window.title('Login')
    login_window.configure(bg='#669bbc')

    welcome = customtkinter.CTkLabel(login_window, text="                     Welcome to Online Bank", width=1200,height=200,
                    bg='#669bbc',fg='#432818')
    welcome.grid(column=0, row=0, columnspan=6)

    spaces = customtkinter.CTkLabel(login_window, text="           ",bg='#669bbc')
    spaces.grid(column=0, row=1)

    welcome = customtkinter.CTkLabel(login_window, text="   Login   ",bg='#669bbc',fg='#432818')
    welcome.grid(column=1, row=1, columnspan=2)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40),bg='#669bbc')
    spaces.grid(column=0, row=1)

    userid_label = customtkinter.CTkLabel(login_window, text="   User ID   ",bg='#669bbc',fg='#e9edc9')
    userid_label.grid(column=1, row=3)

    userid_e = Entry(login_window, borderwidth=5, font=('sans-serif', 20))
    userid_e.grid(column=2, row=3)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40),bg='#669bbc')
    spaces.grid(column=0, row=4)

    pass_label = customtkinter.CTkLabel(login_window, text="Password   ",bg='#669bbc',fg='#e9edc9')
    pass_label.grid(column=1, row=4)

    pass_e_login = Entry(login_window, borderwidth=5, font=('sans-serif', 20), show='*')
    pass_e_login.grid(column=2, row=4)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40),bg='#669bbc')
    spaces.grid(column=0, row=5)
    spaces = Label(login_window, text="             ", font=('sans-serif', 40),bg='#669bbc')
    spaces.grid(column=1, row=5)

    login_button = Button(login_window, text='Login', font=('sans-serif', 24), bg='#e3d5ca',fg='#3a5a40',
                          command=pass_)
    login_button.grid(row=5, column=1, columnspan=2)

    spaces = Label(login_window, text="             ", font=('sans-serif', 40),bg='#669bbc')
    spaces.grid(column=0, row=6)

    frame_admin = LabelFrame(login_window, text='Administrator', font=('sans-serif', 20),bg='#669bbc',fg='#e9edc9')
    frame_admin.grid(column=1, row=6)

    login_button_admin = Button(frame_admin, text='Login', font=('sans-serif', 24), bg='#FF7F50',fg='#e9edc9',
                                command=pass_)
    login_button_admin.grid(row=0, column=0, )

    frame_new = LabelFrame(login_window, text='New Account', font=('sans-serif', 20), padx=5, pady=5,bg='#669bbc',fg='#e9edc9')
    frame_new.grid(column=2, row=6, columnspan=2)

    create_btn = Button(frame_new, text='Create new account', font=('sans-serif', 24), bg='#00008B', fg='white', padx=7,
                        pady=3, command=pass_)
    create_btn.grid(row=5, column=0)

    login_window.mainloop()

def pass_():
   pass

login()