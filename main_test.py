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

def login_create():
    login_window.destroy()
    create_account_f()
def create_account_f():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    global create_account
    create_account = customtkinter.CTk()
    create_account.geometry('800x524')
    create_account.title('Create Account')
    spaces = customtkinter.CTkLabel(create_account, text=''' ''', text_font=('Roboto Mono', 20))
    spaces.pack()
    welcome = customtkinter.CTkLabel(create_account, text="Create Account", text_font=('Roboto Mono', 28),
                                     text_color='#d7e3fc')
    welcome.pack(anchor=customtkinter.N)

    create_frame = customtkinter.CTkFrame(master=create_account, width=20, height=250, corner_radius=10)
    create_frame.pack(ipady=5, ipadx=10, expand=True)

    spaces = customtkinter.CTkLabel(create_frame, text=''' ''', text_font=('Roboto Mono', 5))
    spaces.grid(row=1, column=3)
    spaces = customtkinter.CTkLabel(create_frame, text=''' ''', text_font=('Roboto Mono', 5))
    spaces.grid(row=3, column=2)
    spaces = customtkinter.CTkLabel(create_frame, text=''' ''', text_font=('Roboto Mono', 5))
    spaces.grid(row=5, column=2)

    name_label = customtkinter.CTkLabel(create_frame, text='                 name                 ',
                                        text_font=('Roboto Mono', 20))
    name_label.grid(column=1, row=2)
    password_label = customtkinter.CTkLabel(create_frame, text='                 password             ',
                                            text_font=('Roboto Mono', 20))
    password_label.grid(column=1, row=3)
    password_confirm_label = customtkinter.CTkLabel(create_frame, text='                 password confirm ',
                                                    text_font=('Roboto Mono', 20))
    password_confirm_label.grid(column=1, row=4)

    name_entry = customtkinter.CTkEntry(create_frame, text_font=('Roboto Mono', 15), width=150, height=35)
    name_entry.grid(column=2, row=2, pady=10)

    pass_entry = customtkinter.CTkEntry(create_frame, text_font=('Roboto Mono', 15), show='*', width=150, height=35)
    pass_entry.grid(column=2, row=3, pady=10)

    pass_confirm_entry = customtkinter.CTkEntry(create_frame, text_font=('Roboto Mono', 15), show='*', width=150,
                                                height=35)
    pass_confirm_entry.grid(column=2, row=4, pady=10)

    login_button = customtkinter.CTkButton(create_frame, text='create account', text_font=('Roboto Mono', 22),
                                           command=lambda: createaccount(name_entry.get(),pass_entry.get(),
                                                                          pass_confirm_entry.get()))
    login_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4)

    create_account.mainloop()


def createaccount(x,y,z):
    name = x
    userid = random.randint(10002, 100000)
    pin = y
    pin2 = z
    if pin != pin2:
        response = messagebox.askquestion('create account', 'the two passwords does not match,try again')
        if response == 'yes':
            create_account.destroy()
            create_account_f()
        else:
            sys.exit('user closed')

    else:
        balance = 0
        pin_encoded = str(encodeStr(pin))
        print(type(pin_encoded))
        insertstr = "insert into users values('{0}','{1}','{2}','{3}')".format(userid, name, pin_encoded, balance)
        cursor.execute(insertstr)
        database.commit()
        window = customtkinter.CTkToplevel()
        window.geometry("500x300")
        window.title('account created')
        spaces = customtkinter.CTkLabel(window, text=''' ''', text_font=('Roboto Mono', 20))
        spaces.pack()

        welcome = customtkinter.CTkLabel(window, text="Account Created", text_font=('Roboto Mono', 24),
                                         text_color='#d7e3fc')
        welcome.pack(anchor=customtkinter.N)

        frame = customtkinter.CTkFrame(master=window, corner_radius=10)
        frame.pack(ipady=5, ipadx=10, expand=True)

        name_label = customtkinter.CTkLabel(frame, text='name : {} '.format(name),
                                            text_font=('Roboto Mono', 20))
        name_label.grid(column=1, row=2)

        pass_label = customtkinter.CTkLabel(frame, text='password : {} '.format(pin),
                                            text_font=('Roboto Mono', 20))
        pass_label.grid(column=1, row=4, ipadx=20)

        userid_label = customtkinter.CTkLabel(frame, text='userid : {} '.format(userid),
                                              text_font=('Roboto Mono', 20))
        userid_label.grid(column=1, row=3)

        login_button = customtkinter.CTkButton(frame, text='Login', text_font=('Roboto Mono', 22),command= pre_login_screen)
        login_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4, pady=10)

        window.mainloop()



def pre_login_screen():
    create_account.destroy()
    login_screen()
def login(x, y):
    userid = int(x)
    password = y

    pin_selector_database = "SELECT * from users where userid = {}".format(userid)
    cursor.execute(pin_selector_database)
    current_user_temp_tuple = cursor.fetchone()
    global current_user_global
    current_user_temp_list = list(current_user_temp_tuple)
    current_user_temp_list[2] = str(decodeStr(current_user_temp_list[2]))
    current_user_global = current_user_temp_list
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
                                         command=login_create, fg_color='#ffc2d1', text_color='#333')
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
