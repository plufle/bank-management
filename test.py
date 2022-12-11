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
import tkinter



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
    admin_logined_window.title('admin account')


    welcome = customtkinter.CTkLabel(admin_logined_window, text="Admin Login", text_font=('Roboto Mono', 30))
    welcome.pack(pady=40)

    frame = customtkinter.CTkFrame(admin_logined_window, padx=5, pady=5)
    frame.pack()

    trans_button = customtkinter.CTkButton(frame, text='user info', text_font=('Roboto Mono', 22),command=lambda: user_info_screen())
    trans_button.grid(row=2, column=1, pady=20, ipadx=40)

    spaces = customtkinter.CTkLabel(frame, text=''' ''', text_font=('Roboto Mono', 1))
    spaces.grid(row=2, column=0, padx=1)

    spaces = customtkinter.CTkLabel(frame, text=''' ''', text_font=('Roboto Mono', 1))
    spaces.grid(row=2, column=2, padx=1)

    show_trans_button = customtkinter.CTkButton(frame, text='user transaction', text_font=('Roboto Mono', 22),command=lambda:
                                                trans_userid())
    show_trans_button.grid(row=5, column=1, pady=20)

    exit_button = customtkinter.CTkButton(frame, text='Exit', text_font=('Roboto Mono', 22), command=exit_)  #
    exit_button.grid(row=7, column=1, pady=20, ipadx=48)

    admin_logined_window.mainloop()
    
    
    
    
    
    
    
def user_info_screen():
    global trans_user
    trans_user = customtkinter.CTk()
    trans_user.geometry('800x524')
    trans_user.title('user info')

    welcome = customtkinter.CTkLabel(trans_user, text="User details", text_font=('Roboto Mono', 30))
    welcome.pack(pady=75)

    frame = customtkinter.CTkFrame(trans_user, padx=10, pady=5, width=200)
    frame.pack()

    label = customtkinter.CTkLabel(frame, text='userid',
                                   text_font=('Roboto Mono', 20))
    label.grid(column=1, row=2, pady=20)

    entry = customtkinter.CTkEntry(frame, text_font=('Roboto Mono', 15), width=150, height=35)
    entry.grid(column=2, row=2, pady=10, padx=40)

    confirm_button = customtkinter.CTkButton(frame, text='confirm', text_font=('Roboto Mono', 22),
                                             command=lambda: account_info(entry.get()))
    confirm_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4, pady=30)
    trans_user.mainloop()

    
def account_info(x):
    user = int(x)
    cursor.execute('select userid,name,balance from users where userid  = {} '.format(user))
    data = cursor.fetchone()

    trans_user.destroy()
    global data_window
    data_window = customtkinter.CTk()
    data_window.geometry('800x524')
    data_window.title('user info')
    welcome = customtkinter.CTkLabel(data_window, text="User details", text_font=('Roboto Mono', 30))
    welcome.pack(pady=75)

    frame = customtkinter.CTkFrame(data_window, padx=10, pady=5)
    frame.pack()

    name_label = customtkinter.CTkLabel(frame, text='name : {} '.format(data[1]),
                                        text_font=('Roboto Mono', 20))
    name_label.grid(column=1, row=2,pady=10)

    userid_label = customtkinter.CTkLabel(frame, text='userid: {} '.format(data[0]),
                                        text_font=('Roboto Mono', 20))
    userid_label.grid(column=1, row=3, ipadx=20,pady=10)

    balance_label = customtkinter.CTkLabel(frame, text='balance : {} '.format(data[2]),
                                          text_font=('Roboto Mono', 20))
    balance_label.grid(column=1, row=4,padx = 20,pady=10)

    login_button = customtkinter.CTkButton(frame, text='continue', text_font=('Roboto Mono', 22),
                                           command=pre_admin_logged_screen)
    login_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4, pady=10)
    data_window.mainloop()
    
def trans_userid():
    global trans_user
    trans_user = customtkinter.CTk()
    trans_user.geometry('800x524')
    trans_user.title('user info')

    welcome = customtkinter.CTkLabel(trans_user, text="Transaction of user", text_font=('Roboto Mono', 30))
    welcome.pack(pady=75)

    frame = customtkinter.CTkFrame(trans_user, padx=10, pady=5, width=200)
    frame.pack()

    label = customtkinter.CTkLabel(frame, text='userid',
                                   text_font=('Roboto Mono', 20))
    label.grid(column=1, row=2, pady=20)

    entry = customtkinter.CTkEntry(frame, text_font=('Roboto Mono', 15), width=150, height=35)
    entry.grid(column=2, row=2, pady=10, padx=40)

    confirm_button = customtkinter.CTkButton(frame, text='confirm', text_font=('Roboto Mono', 22),
                                             command=lambda: admin_show_trans(entry.get()))
    confirm_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4, pady=30)
    trans_user.mainloop()

def admin_show_trans(x):
    userid = int(x)
    trans_fetch = 'select alld,date,time from trans where userid = {} order by date(date)desc,time desc'.format(userid)
    cursor.execute(trans_fetch)
    all_trans = cursor.fetchall()
    trans_user.destroy()
    app = customtkinter.CTk()
    app.geometry('1100x524')
    app.title('tansactions')

    label = customtkinter.CTkLabel(app, text='Tranaction of {}'.format(x), text_font=('Roboto Mono', 22))
    label.grid(row=0,column = 2,pady =20)

    label = customtkinter.CTkLabel(app, text='{:<10s}{:>4s}{:>15s}{:>25s}{:>14s}{:>22}'.format('FROM/TO', "CREDIT/DEBIT", 'AMOUNT',
                                                                        'BALANCE', 'DATE', 'TIME')
                                   , text_font=('Roboto Mono', 16))
    label.grid(row=2,column = 2,pady =20,)

    textbox = customtkinter.CTkTextbox(app,text_font=('Roboto Mono', 14))
    textbox.grid(row=4, column=2,ipadx=370,padx = 80)


    for i in range(len(all_trans)+1):
        try:
            user_temp = all_trans[i]
            date = user_temp[1]
            time = user_temp[2]
            other = eval(user_temp[0])
            from_to = other[0]
            info = other[1]
            amount = other[2]
            balance = other[3]

            position = f'{i}.0'
            textbox.insert(position,'{:<24s} {:>6s}{:>24s}{:>27s}{:>28s}{:>22}\n'.format(str(from_to), str(info), str(amount),
                                                                                    str(balance), str(date),
                                                                                    str(time)))
        except:
            pass

    textbox.configure(state="disabled")

    app.mainloop()

def pre_admin_logged_screen():
    data_window.destroy()
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
