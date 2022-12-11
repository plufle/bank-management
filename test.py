import mysql.connector as connector
import random
from cryptography.fernet import Fernet
import datetime
import pytz
from datetime import date, timedelta
import main_passwords
import customtkinter
from tkinter import messagebox
import sys



def admin_account_main():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    global admin_account
    admin_account = customtkinter.CTk()
    admin_account.geometry('800x524')
    admin_account.title('admin Account')

    welcome = customtkinter.CTkLabel(admin_account, text="admin Account", text_font=('Roboto Mono', 28),
                                     text_color='#d7e3fc')
    welcome.pack(pady = 40)

    admin_frame = customtkinter.CTkFrame(master=admin_account, width=20, height=250, corner_radius=10)
    admin_frame.pack(ipady = 10)

    name_label = customtkinter.CTkLabel(admin_frame, text='name',
                                        text_font=('Roboto Mono', 20))
    name_label.grid(column=1, row=2)
    password_label = customtkinter.CTkLabel(admin_frame, text='password one',
                                            text_font=('Roboto Mono', 20))
    password_label.grid(column=1, row=3,ipadx = 50)
    password_confirm_label = customtkinter.CTkLabel(admin_frame, text='password two',
                                                    text_font=('Roboto Mono', 20))
    password_confirm_label.grid(column=1, row=4)

    name_entry = customtkinter.CTkEntry(admin_frame, text_font=('Roboto Mono', 15),width=150, height=35)
    name_entry.grid(column=2, row=2, pady=10,padx = 20)

    pass_entry = customtkinter.CTkEntry(admin_frame, text_font=('Roboto Mono', 15), show='*', width=150, height=35)
    pass_entry.grid(column=2, row=3, pady=10)

    pass_confirm_entry = customtkinter.CTkEntry(admin_frame, text_font=('Roboto Mono', 15), show='*', width=150,
                                                height=35)
    pass_confirm_entry.grid(column=2, row=4, pady=10)

    login_button = customtkinter.CTkButton(admin_frame, text='login', text_font=('Roboto Mono', 22),
                                           command=lambda: admin_login(name_entry.get(),pass_entry.get(),pass_confirm_entry.get()))

    login_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4)

    admin_account.mainloop()

def admin_login(x,y,z):
    userid = x
    password1 = y
    password2 = z
    pin_selector_database = "SELECT * from admin "
    cursor.execute(pin_selector_database)
    current_user_temp_tuple = cursor.fetchone()
    current_user_temp_list = list(current_user_temp_tuple)
    current_user_temp_list[1] = str(decodeStr(current_user_temp_list[1]))
    current_user_temp_list[2] = str(decodeStr(current_user_temp_list[2]))
    current_user_temp_list[0] = str(decodeStr(current_user_temp_list[0]))
    if userid == current_user_temp_list[0]:
        if current_user_temp_list[1] == password1 and current_user_temp_list[2] == password2:
            admin_logined_screen()
        else:
            response = messagebox.showinfo('admin login', 'any one of the entered password is incorrect please try again')
            if response == 'ok':
                admin_account.destroy()
                admin_account_main()

    else:
        print('userid not found\nplease try again')
        response = messagebox.showinfo('admin login',
                                          'userid not found\nplease try again')
        if response == 'ok':
            admin_account.destroy()
            admin_account_main()


def admin_logined_screen():
    admin_logined_window = customtkinter.CTk()
    admin_logined_window.geometry('800x524')
    admin_logined_window.title('Welcome to BANK')


    welcome = customtkinter.CTkLabel(admin_logined_window, text="Admin Login", text_font=('Roboto Mono', 30))
    welcome.pack(pady=40)

    frame = customtkinter.CTkFrame(admin_logined_window, padx=5, pady=5)
    frame.pack()

    trans_button = customtkinter.CTkButton(frame, text='user info', text_font=('Roboto Mono', 22))
    trans_button.grid(row=2, column=1, pady=20, ipadx=40)

    spaces = customtkinter.CTkLabel(frame, text=''' ''', text_font=('Roboto Mono', 1))
    spaces.grid(row=2, column=0, padx=1)

    spaces = customtkinter.CTkLabel(frame, text=''' ''', text_font=('Roboto Mono', 1))
    spaces.grid(row=2, column=2, padx=1)

    show_trans_button = customtkinter.CTkButton(frame, text='user transaction', text_font=('Roboto Mono', 22))
    show_trans_button.grid(row=5, column=1, pady=20)

    exit_button = customtkinter.CTkButton(frame, text='Exit', text_font=('Roboto Mono', 22), command=exit_)  #
    exit_button.grid(row=7, column=1, pady=20, ipadx=48)

    admin_logined_window.mainloop()
    
    
    
    
    
    
    
    
    
    
    
def exit_():
    sys.exit()
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


key = main_passwords.frenet_key.encode()
fernet = Fernet(key)
print(decodeStr('gAAAAABjh29m_PRgRCnb3kVe7gps-PyVQbJfNz5UTjDS0Fh6FdffZNf1l-v1B-4SOyv7G36oj94koRKA7D4DB9Eekgww_p8fTA=='))
cursor = database.cursor()


admin_logined_screen()
