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
    create_account_main()


def create_account_main():
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
                                           command=lambda: createaccount(name_entry.get(), pass_entry.get(),
                                                                         pass_confirm_entry.get()))
    login_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4)

    create_account.mainloop()


def transaction(x, y):
    to_person_input = x
    amount = int(y)
    to_person_selector = "SELECT * from users where userid = {}".format(to_person_input)
    cursor.execute(to_person_selector)
    to_person = list(cursor.fetchone())
    try:
        if amount > current_user_global[3]:
            response = messagebox.askquestion('transaction', 'current balance less than transaction amount')
            if response == 'yes':
                tans_window.destroy()
                transaction_scrren()
    except:

        logined_screen()

    to_person_before_balance = to_person[3]
    to_person_after_balance = to_person_before_balance + amount
    to_person_balance_update = 'update users set balance = {0} where userid = {1} '.format(to_person_after_balance,
                                                                                           to_person_input)
    cursor.execute(to_person_balance_update)
    current_user_balance = current_user_global[3]
    current_user_balance = current_user_balance - amount
    current_user_update = 'update users set balance = {0} where userid = {1} '.format(current_user_balance,
                                                                                      current_user_global[0])
    cursor.execute(current_user_update)
    current_date_time = currenttime()
    current_date = current_date_time[0]
    current_time = current_date_time[1]
    to_trans_log = (
        to_person_input, '{}'.format([current_user_global[0], 'CREDIT', amount, to_person_after_balance]), current_date,
        current_time)
    from_trans_log = (
        current_user_global[0], '{}'.format([to_person_input, 'DEBIT  ', amount, current_user_balance]), current_date,
        current_time)
    insert_1 = 'insert into trans values{}'.format(to_trans_log)
    insert_2 = 'insert into trans values{}'.format(from_trans_log)
    cursor.execute(insert_1)
    cursor.execute(insert_2)
    database.commit()
    current_user_global[3] = current_user_balance
    after_transaction(to_person_input, amount)


def admin_account_main():
    login_window.destroy()
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    global admin_account
    admin_account = customtkinter.CTk()
    admin_account.geometry('800x524')
    admin_account.title('admin Account')

    welcome = customtkinter.CTkLabel(admin_account, text="admin Account", text_font=('Roboto Mono', 28),
                                     text_color='#d7e3fc')
    welcome.pack(pady=40)

    admin_frame = customtkinter.CTkFrame(master=admin_account, width=20, height=250, corner_radius=10)
    admin_frame.pack(ipady=10)

    name_label = customtkinter.CTkLabel(admin_frame, text='name',
                                        text_font=('Roboto Mono', 20))
    name_label.grid(column=1, row=2)
    password_label = customtkinter.CTkLabel(admin_frame, text='password one',
                                            text_font=('Roboto Mono', 20))
    password_label.grid(column=1, row=3, ipadx=50)
    password_confirm_label = customtkinter.CTkLabel(admin_frame, text='password two',
                                                    text_font=('Roboto Mono', 20))
    password_confirm_label.grid(column=1, row=4)

    name_entry = customtkinter.CTkEntry(admin_frame, text_font=('Roboto Mono', 15), width=150, height=35)
    name_entry.grid(column=2, row=2, pady=10, padx=20)

    pass_entry = customtkinter.CTkEntry(admin_frame, text_font=('Roboto Mono', 15), show='*', width=150, height=35)
    pass_entry.grid(column=2, row=3, pady=10)

    pass_confirm_entry = customtkinter.CTkEntry(admin_frame, text_font=('Roboto Mono', 15), show='*', width=150,
                                                height=35)
    pass_confirm_entry.grid(column=2, row=4, pady=10)

    login_button = customtkinter.CTkButton(admin_frame, text='login', text_font=('Roboto Mono', 22),
                                           command=lambda: admin_login(name_entry.get(), pass_entry.get(),
                                                                       pass_confirm_entry.get()))

    login_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4)

    admin_account.mainloop()


def admin_login(x, y, z):
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
            response = messagebox.showinfo('admin login',
                                           'any one of the entered password is incorrect please try again')
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
    admin_account.destroy()
    admin_logined_window = customtkinter.CTk()
    admin_logined_window.geometry('800x524')
    admin_logined_window.title('admin account')

    welcome = customtkinter.CTkLabel(admin_logined_window, text="Admin Login", text_font=('Roboto Mono', 30))
    welcome.pack(pady=40)

    frame = customtkinter.CTkFrame(admin_logined_window, padx=5, pady=5)
    frame.pack()

    trans_button = customtkinter.CTkButton(frame, text='user info', text_font=('Roboto Mono', 22),
                                           command=lambda: user_info_screen())
    trans_button.grid(row=2, column=1, pady=20, ipadx=40)

    spaces = customtkinter.CTkLabel(frame, text=''' ''', text_font=('Roboto Mono', 1))
    spaces.grid(row=2, column=0, padx=1)

    spaces = customtkinter.CTkLabel(frame, text=''' ''', text_font=('Roboto Mono', 1))
    spaces.grid(row=2, column=2, padx=1)

    show_trans_button = customtkinter.CTkButton(frame, text='user transaction', text_font=('Roboto Mono', 22),
                                                command=lambda:
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
    name_label.grid(column=1, row=2, pady=10)

    userid_label = customtkinter.CTkLabel(frame, text='userid: {} '.format(data[0]),
                                          text_font=('Roboto Mono', 20))
    userid_label.grid(column=1, row=3, ipadx=20, pady=10)

    balance_label = customtkinter.CTkLabel(frame, text='balance : {} '.format(data[2]),
                                           text_font=('Roboto Mono', 20))
    balance_label.grid(column=1, row=4, padx=20, pady=10)

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
    label.grid(row=0, column=2, pady=20)

    label = customtkinter.CTkLabel(app,
                                   text='{:<10s}{:>4s}{:>15s}{:>25s}{:>14s}{:>18}'.format('FROM/TO', "CREDIT/DEBIT",
                                                                                          'AMOUNT',
                                                                                          'BALANCE', 'DATE', 'TIME')
                                   , text_font=('Roboto Mono', 16))
    label.grid(row=2, column=2, pady=20, )

    textbox = customtkinter.CTkTextbox(app, text_font=('Roboto Mono', 14))
    textbox.grid(row=4, column=2, ipadx=370, padx=65)

    for i in range(len(all_trans) + 1):
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
            textbox.insert(position,
                           '{:<24s} {:>6s}{:>24s}{:>27s}{:>28s}{:>22}\n'.format(str(from_to), str(info), str(amount),
                                                                                str(balance), str(date),
                                                                                str(time)))
        except:
            pass

    textbox.configure(state="disabled")

    app.mainloop()


def pre_admin_logged_screen():
    data_window.destroy()

def after_transaction(x, y):
    global window_trans
    window_trans = customtkinter.CTkToplevel()
    window_trans.geometry("500x300")
    window_trans.title('Transaction')
    spaces = customtkinter.CTkLabel(window_trans, text=''' ''', text_font=('Roboto Mono', 20))
    spaces.pack()

    welcome = customtkinter.CTkLabel(window_trans, text="Transaction successful", text_font=('Roboto Mono', 24),
                                     text_color='#d7e3fc')
    welcome.pack(anchor=customtkinter.N, pady=20)

    label = customtkinter.CTkLabel(window_trans, text="Amount {0} paid to user {1}".format(y, x),
                                   text_font=('Roboto Mono', 18))
    label.pack()

    login_button = customtkinter.CTkButton(window_trans, text='continue', text_font=('Roboto Mono', 12),
                                           command=pre_login_screen_two)
    login_button.pack(ipadx=10, ipady=4, pady=20)

    window_trans.mainloop()


def transaction_scrren():
    global tans_window
    tans_window = customtkinter.CTk()
    tans_window.geometry('800x524')
    tans_window.title('Transaction')

    welcome = customtkinter.CTkLabel(tans_window, text="TRANSACTION", text_font=('Roboto Mono', 30))
    welcome.pack(pady=30)

    frame = customtkinter.CTkFrame(tans_window, padx=10, pady=5, width=200)
    frame.pack()

    name_label = customtkinter.CTkLabel(frame, text='userid',
                                        text_font=('Roboto Mono', 20))
    name_label.grid(column=1, row=2, pady=20)
    password_label = customtkinter.CTkLabel(frame, text='amount',
                                            text_font=('Roboto Mono', 20))
    password_label.grid(column=1, row=3)

    name_entry = customtkinter.CTkEntry(frame, text_font=('Roboto Mono', 15), width=150, height=35)
    name_entry.grid(column=2, row=2, pady=5, padx=30)

    pass_entry = customtkinter.CTkEntry(frame, text_font=('Roboto Mono', 15), width=150, height=35)
    pass_entry.grid(column=2, row=3, pady=10)

    confirm_button = customtkinter.CTkButton(frame, text='confirm', text_font=('Roboto Mono', 22),
                                             command=lambda: transaction(name_entry.get(), pass_entry.get()))

    confirm_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4, pady=30)
    tans_window.mainloop()


def createaccount(x, y, z):
    name = x
    userid = random.randint(10002, 100000)
    pin = y
    pin2 = z
    if pin != pin2:
        response = messagebox.askquestion('create account', 'the two passwords does not match,try again')
        if response == 'yes':
            create_account.destroy()
            create_account_main()
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

        login_button = customtkinter.CTkButton(frame, text='Login', text_font=('Roboto Mono', 22),
                                               command=pre_login_screen)
        login_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4, pady=10)

        window.mainloop()


def pre_login_screen():
    create_account.destroy()
    login_screen()


def pre_login_screen_two():
    window_trans.destroy()
    tans_window.destroy()



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
        logined_screen()

    else:
        print('entered password is incorrect\n please try again')
        response = messagebox.askquestion('login', 'password is incorrect...try again')
        if response == 'yes':
            login_window.destroy()
            login_screen()
        else:
            sys.exit('user closed')


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
                                                 command=lambda: admin_account_main(), fg_color='#9ceaef', text_color='#333')
    login_button_admin.grid(row=0, column=0, pady=10, padx=20, ipadx=10, ipady=4)

    create_btn = customtkinter.CTkButton(frame_admin, text=' Create new account', text_font=('Roboto Mono', 20),
                                         command=login_create, fg_color='#ffc2d1', text_color='#333')
    create_btn.grid(row=1, column=0, pady=10, padx=20, ipadx=10, ipady=4)

    login_window.mainloop()


def logined_screen():
    logined_window = customtkinter.CTk()
    logined_window.geometry('800x524')
    logined_window.title('Welcome to BANK')
    username = current_user_global[1]

    welcome = customtkinter.CTkLabel(logined_window, text=f"logged in as {username}", text_font=('Roboto Mono', 30))
    welcome.pack(pady=20)

    frame = customtkinter.CTkFrame(logined_window, padx=5, pady=5)
    frame.pack()

    trans_button = customtkinter.CTkButton(frame, text='Transaction', text_font=('Roboto Mono', 22), command=
    lambda: transaction_scrren())  #
    trans_button.grid(row=2, column=1, pady=20, ipadx=32)

    spaces = customtkinter.CTkLabel(frame, text=''' ''', text_font=('Roboto Mono', 1))
    spaces.grid(row=2, column=0, padx=1)

    spaces = customtkinter.CTkLabel(frame, text=''' ''', text_font=('Roboto Mono', 1))
    spaces.grid(row=2, column=2, padx=1)

    deposit_button = customtkinter.CTkButton(frame, text='Deposit', text_font=('Roboto Mono', 22),
                                             command=lambda: deposit_screen())  #
    deposit_button.grid(row=3, column=1, pady=20, ipadx=46)

    withdrawal_button = customtkinter.CTkButton(frame, text='Withdrawal', text_font=('Roboto Mono', 22),
                                                command=lambda: withdraw_screen() ) #
    withdrawal_button.grid(row=4, column=1, pady=20, ipadx=36)

    show_trans_button = customtkinter.CTkButton(frame, text='Show transaction', text_font=('Roboto Mono', 22),
                                                command=pass_)  #
    show_trans_button.grid(row=5, column=1, pady=20)

    exit_button = customtkinter.CTkButton(frame, text='Exit', text_font=('Roboto Mono', 22), command=exit_)  #
    exit_button.grid(row=7, column=1, pady=20, ipadx=48)

    logined_window.mainloop()


def currenttime():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

    d_string = current_time.strftime("20%y-%m-%d")
    t_string = current_time.strftime("%H:%M:%S")
    time = [d_string, t_string]
    return time

def deposit_screen():
    global deposit_window
    deposit_window = customtkinter.CTk()
    deposit_window.geometry('800x524')
    deposit_window.title('Transaction')

    welcome = customtkinter.CTkLabel(deposit_window, text="DEPOSIT", text_font=('Roboto Mono', 30))
    welcome.pack(pady=75)

    frame = customtkinter.CTkFrame(deposit_window, padx=10, pady=5, width=200)
    frame.pack()

    label = customtkinter.CTkLabel(frame, text='amount',
                                        text_font=('Roboto Mono', 20))
    label.grid(column=1, row=2, pady=20)

    entry = customtkinter.CTkEntry(frame, text_font=('Roboto Mono', 15), width=150, height=35)
    entry.grid(column=2, row=2, pady=10,padx = 40)

    confirm_button = customtkinter.CTkButton(frame, text='confirm', text_font=('Roboto Mono', 22),command=lambda: deposit(entry.get()))
    confirm_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4, pady=30)
    deposit_window.mainloop()

def deposit(x):
    dep_amt = int(x)
    current_balance = current_user_global[3]
    current_balance = current_balance + dep_amt
    balance_update = 'update users set balance = {0} where userid = {1} '.format(current_balance,
                                                                                 current_user_global[0])
    cursor.execute(balance_update)
    current_date_time = currenttime()
    current_date = current_date_time[0]
    current_time = current_date_time[1]
    trans_log = (
        current_user_global[0], '{}'.format(['SELF ', 'CREDIT', dep_amt, current_balance]), current_date, current_time)
    insert = 'insert into trans values{}'.format(trans_log)
    cursor.execute(insert)
    database.commit()
    current_user_global[3] = current_balance
    global deposit_window_top
    deposit_window_top = customtkinter.CTkToplevel()
    deposit_window_top.geometry("500x300")
    deposit_window_top.title('Transaction')
    spaces = customtkinter.CTkLabel(deposit_window_top, text=''' ''', text_font=('Roboto Mono', 20))
    spaces.pack()

    welcome = customtkinter.CTkLabel(deposit_window_top, text="Deposit successful", text_font=('Roboto Mono', 24),
                                     text_color='#d7e3fc')
    welcome.pack(anchor=customtkinter.N, pady=20)

    label = customtkinter.CTkLabel(deposit_window_top, text="Amount deposited ={} ".format(x),
                                   text_font=('Roboto Mono', 18))
    label.pack()

    login_button = customtkinter.CTkButton(deposit_window_top, text='continue', text_font=('Roboto Mono', 12),command=after_deposit)

    login_button.pack(ipadx=10, ipady=4, pady=20)

    deposit_window_top.mainloop()


def after_deposit():
    deposit_window.destroy()
    deposit_window_top.destroy()


def withdraw_screen():
    global withdraw_window
    withdraw_window = customtkinter.CTk()
    withdraw_window.geometry('800x524')
    withdraw_window.title('Transaction')

    welcome = customtkinter.CTkLabel(withdraw_window, text="withdraw", text_font=('Roboto Mono', 30))
    welcome.pack(pady=75)

    frame = customtkinter.CTkFrame(withdraw_window, padx=10, pady=5, width=200)
    frame.pack()

    label = customtkinter.CTkLabel(frame, text='amount',
                                   text_font=('Roboto Mono', 20))
    label.grid(column=1, row=2, pady=20)

    entry = customtkinter.CTkEntry(frame, text_font=('Roboto Mono', 15), width=150, height=35)
    entry.grid(column=2, row=2, pady=10, padx=40)

    confirm_button = customtkinter.CTkButton(frame, text='confirm', text_font=('Roboto Mono', 22),
                                             command=lambda: withdraw(entry.get()))
    confirm_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4, pady=30)
    withdraw_window.mainloop()


def withdraw(x):
    with_amt = int(x)
    if with_amt > current_user_global[3]:
        print("please enter a lower value\n than your current balance")
        withdraw()
    current_balance = current_user_global[3]
    current_balance = current_balance - with_amt
    balance_update = 'update users set balance = {0} where userid = {1} '.format(current_balance,
                                                                                 current_user_global[0])
    cursor.execute(balance_update)
    current_date_time = currenttime()
    current_date = current_date_time[0]
    current_time = current_date_time[1]
    trans_log = (
        current_user_global[0], '{}'.format(['SELF ', 'DEBIT ', with_amt, current_balance]), current_date, current_time)
    insert = 'insert into trans values{}'.format(trans_log)
    cursor.execute(insert)
    database.commit()
    current_user_global[3] = current_balance

    global withdraw_window_top
    withdraw_window_top = customtkinter.CTkToplevel()
    withdraw_window_top.geometry("500x300")
    withdraw_window_top.title('Transaction')
    spaces = customtkinter.CTkLabel(withdraw_window_top, text=''' ''', text_font=('Roboto Mono', 20))
    spaces.pack()

    welcome = customtkinter.CTkLabel(withdraw_window_top, text="withdraw successful", text_font=('Roboto Mono', 24),
                                     text_color='#d7e3fc')
    welcome.pack(anchor=customtkinter.N, pady=20)

    label = customtkinter.CTkLabel(withdraw_window_top, text="Amount withdrawed ={} ".format(x),
                                   text_font=('Roboto Mono', 18))
    label.pack()

    login_button = customtkinter.CTkButton(withdraw_window_top, text='continue', text_font=('Roboto Mono', 12),
                                           command=after_withdraw)

    login_button.pack(ipadx=10, ipady=4, pady=20)

    withdraw_window_top.mainloop()


def after_withdraw():
    withdraw_window.destroy()
    withdraw_window_top.destroy()


def exit_():
    sys.exit('user close')


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
