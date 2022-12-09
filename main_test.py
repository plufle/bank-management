from tkinter import *
from tkinter import messagebox
import mysql.connector as connector
import random
from cryptography.fernet import Fernet
import datetime
import pytz
import sys
import customtkinter
from datetime import date, timedelta
import main_passwords


def pass_():
    print('hi')


def login(x, y):
    userid = int(x)
    password = y

    pin_selector_database = "SELECT * from users where userid = {}".format(userid)
    cursor.execute(pin_selector_database)
    current_user_temp_tuple = cursor.fetchone()
    current_user_temp_list = list(current_user_temp_tuple)
    current_user_temp_list[2] = str(decodeStr(current_user_temp_list[2]))
    if current_user_temp_list[2] == password:
        print('successfully logged to the account')
        messagebox.showinfo("login", "successfully logged in")
        login_window.destroy()
        logged_screen()

    else:
        print('entered password is incorrect\n please try again')
        response = messagebox.askquestion('login', 'password is incorrect...try again')
        if response == 'yes':
            login_window.destroy()
            login_screen()
        else:
            sys.exit('user closed')

    return current_user_temp_list


def logged_screen():
    print('GOOD')


def login_screen():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    global login_window
    login_window = customtkinter.CTk()
    login_window.geometry('800x524')
    login_window.title('Login')

    welcome = customtkinter.CTkLabel(login_window, text="Welcome to Online Bank"
                                     , text_font=('Roboto Mono', 35), text_color='#d7e3fc')
    welcome.pack(pady=10)

    welcome = customtkinter.CTkLabel(login_window, text='''   Login   ''', text_font=('Roboto Mono', 29),
                                     text_color='#d7e3fc')
    welcome.pack()

    spaces = customtkinter.CTkLabel(login_window, text=''' ''', text_font=('Roboto Mono', 20))
    spaces.pack()

    main_frame = customtkinter.CTkFrame(login_window)
    main_frame.pack()

    spaces = customtkinter.CTkLabel(main_frame, text='''     ''', text_font=('Roboto Mono', 20))
    spaces.grid(row=0, column=0)
    spaces = customtkinter.CTkLabel(main_frame, text='''      ''', text_font=('Roboto Mono', 20))
    spaces.grid(row=1, column=3)
    spaces = customtkinter.CTkLabel(main_frame, text='''      ''', text_font=('Roboto Mono', 5))
    spaces.grid(row=3, column=2)
    spaces = customtkinter.CTkLabel(main_frame, text='''      ''', text_font=('Roboto Mono', 5))
    spaces.grid(row=5, column=2)

    spaces = customtkinter.CTkLabel(login_window, text=''' ''', text_font=('Roboto Mono', 20))
    spaces.pack()

    userid_label = customtkinter.CTkLabel(main_frame, text="   User ID   ", text_font=('Roboto Mono', 20))
    userid_label.grid(column=1, row=1)

    userid_e = customtkinter.CTkEntry(main_frame, text_font=('Roboto Mono', 15), width=150, height=35)
    userid_e.grid(column=2, row=1, pady=10)

    pass_label = customtkinter.CTkLabel(main_frame, text="Password   ", text_font=('Roboto Mono', 20))
    pass_label.grid(column=1, row=2)

    pass_e = customtkinter.CTkEntry(main_frame, text_font=('Roboto Mono', 15), show='*', width=150, height=35)
    pass_e.grid(column=2, row=2)

    login_button = customtkinter.CTkButton(main_frame, text='Login', text_font=('Roboto Mono', 25),
                                           command=lambda: login(userid_e.get(), pass_e.get()))
    login_button.grid(row=4, column=1, columnspan=2, ipadx=10, ipady=4)

    frame_admin = customtkinter.CTkFrame(login_window, border_color='White')
    frame_admin.pack(ipadx=10, ipady=10)

    login_button_admin = customtkinter.CTkButton(frame_admin, text='Administrator Login', text_font=('Roboto Mono', 20),
                                                 command=pass_, fg_color='#9ceaef', text_color='#333')
    login_button_admin.grid(row=0, column=0, pady=10, padx=20, ipadx=10, ipady=4)

    create_btn = customtkinter.CTkButton(frame_admin, text=' Create new account', text_font=('Roboto Mono', 20),
                                         command=pass_, fg_color='#ffc2d1', text_color='#333')
    create_btn.grid(row=1, column=0, pady=10, padx=20, ipadx=10, ipady=4)

    login_window.mainloop()


def currenttime():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

    d_string = current_time.strftime("20%y-%m-%d")
    t_string = current_time.strftime("%H:%M:%S")
    time = [d_string, t_string]
    return time


def encodeStr(text):
    global fernet, key
    encryptedText = fernet.encrypt(text.encode()).decode()
    return encryptedText


def decodeStr(text):
    global fernet, key
    decryptedText = fernet.decrypt(text.encode()).decode()
    return decryptedText


try:
    database = connector.connect(host=main_passwords.hosts, database=main_passwords.name,
                                 user=main_passwords.users, password=main_passwords.database_password)

    print('successfully connected to database')
except:
    print('database not connected')

cursor = database.cursor()
key = main_passwords.frenet_key.encode()
fernet = Fernet(key)

login_screen()
