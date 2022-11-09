# modules
from tkinter import *
from cryptography.fernet import Fernet
import mysql.connector as connector
import main_passwords
import random
import datetime
import pytz
from datetime import date, timedelta

# functions
def loan():
    print()
    print("--------------------------------------")
    print("             Loan                     ")
    print("--------------------------------------")
    print()
    while True:
        print("Please Select an Option Below : ")
        print("Request Loan    (1)")
        print("Loan details    (2)")
        print("Loan repayment  (3)")
        print("Exit            (4)")
        option = int(input("enter a option : "))
        if option == 1:
            requestloan()
        elif option == 2:
            loandetails()
        elif option == 3:
            loanrepayment()
        elif option == 4:
            break
        else:
            print("please enter a valid option")


def requestloan():
    global current_user_global
    loan_amt = int(input("Please Enter The Amount to be Requested : "))
    if loan_amt < 1000:
        print("Amount Too Low\nPlease Enter an Amount above rs50000")
    else:
        if current_user_global[3] > (loan_amt / 10):
            time = int(input('enter the period of loan in years(eg: 1 or 2) : '))
            rate = 7.5
            simple_interest = (loan_amt * time * rate) / 100
            total_payment = loan_amt + simple_interest
            month = time * 12
            interst_per_month = total_payment // month
            interest_dates = loan_dates(time)
            loan_date_list = currenttime()
            loan_date = loan_date_list[0]
            time = loan_date_list[1]
            total_paid = 0
            status = 'ongoing'
            insert = (
            current_user_global[0], loan_amt, total_payment, loan_date, interst_per_month, '{}'.format(interest_dates),
            total_paid, status)
            insert_statement = "insert into loan values{}".format(insert)
            cursor.execute(insert_statement)
            current_balance = current_user_global[3] + loan_amt
            balance_update = 'update users set balance = {0} where userid = {1} '.format(current_balance,
                                                                                         current_user_global[0])
            cursor.execute(balance_update)
            current_user_global[3] = current_balance
            trans_log = (
                current_user_global[0], '{}'.format(['LOAN', 'CREDIT', loan_amt, current_balance]),
                loan_date, time)
            trans_log_statement = "insert into trans values{}".format(trans_log)
            cursor.execute(trans_log_statement)
            database.commit()


        else:
            print("Loan Declined\nCredit Too Low")

    return current_user_global


def loan_dates(x):
    month = x * 12
    date_interest = []
    days = 30
    for i in range(0, month):
        days_after = (date.today() + timedelta(days)).isoformat()
        days = days + 30
        date_interest.append(days_after)

    return date_interest


def loan_check():
    global current_user_global
    cursor.execute('select * from loan where userid = {}'.format(current_user_global[0]))
    loan_details = cursor.fetchone()
    if loan_details == None:
        return True
    else:
        return False

def loan_check_login():
    global current_user_global
    cursor.execute('select * from loan where userid = {}'.format(current_user_global[0]))
    loan_details = cursor.fetchone()
    if loan_details == None:
        loginscreen()
    else:
        total_amount = loan_details[2]
        total_amount_paid = loan_details[6]
        interest_date = eval(loan_details[5])
        next_payment = interest_date[0]
        current_date_list = currenttime()
        current_date = current_date_list[0]
        interest_per_month = loan_details[4]
        if total_amount >= total_amount_paid:
            if current_date < next_payment:
                print("Your next loan payment due is on {0} for a payment of {1}".format(next_payment,interest_per_month))
                loginscreen()
            else:
                print("Pay your loan due to continue using the bank")
                loanrepayment()
        else:
            loginscreen()

def loandetails():
    while True:
        if loan_check():
            print('______________________________' * 3)
            print('You dont have any ongoing loans\n if you want one try appyling for it')
            print('______________________________' * 3)
            break
        else:
            global current_user_global
            cursor.execute('select * from loan where userid = {}'.format(current_user_global[0]))
            loan_details = list(cursor.fetchone())
            loan_amt = loan_details[1]
            total_amount = loan_details[2]
            loan_date = loan_details[3]
            interest_per_month = loan_details[4]
            interest_date = eval(loan_details[5])
            next_payment = interest_date[0]
            total_amount_paid = loan_details[6]
            if loan_details[7] == 'ongoing':
                staus = 'Loan amount not fully paid'
            else:
                staus = 'Loan amount fully paid'
            print('______________________________' * 3)
            print('                                       loan details')
            print('______________________________' * 3)
            print("Loan amount received            : ", loan_amt)
            print("Total amount including interest : ", total_amount)
            print("Starting date of loan           : ", loan_date)
            print("Interest per month              : ", interest_per_month)
            print("Next payment date               : ", next_payment)
            print("Total amount paid               : ", total_amount_paid)
            print()
            print(staus)
            print('______________________________' * 3)
            break


def loanrepayment():
    global current_user_global
    while True:
        print('______________________________' * 3)
        print('                               loan repayment ')
        print('______________________________' * 3)
        if loan_check():
            print("No ongoing loans found\nif needed try applying one")
        else:
            cursor.execute('select * from loan where userid = {}'.format(current_user_global[0]))
            loan_details = list(cursor.fetchone())




def showtransaction():
    global current_user_global
    current_userid = current_user_global[0]
    trans_fetch = 'select alld,date,time from trans where userid = {} order by date(date)desc,time desc'.format(
        current_userid)
    cursor.execute(trans_fetch)
    while True:
        all_trans = cursor.fetchall()
        if all_trans is None:
            break
        else:
            show_trans = int(input("press 1 to show transaction : "))
            if show_trans == 1:
                print('{:<10s}{:>4s}{:>15s}{:>25s}{:>14s}{:>22}'.format('FROM/TO', "CREDIT/DEBIT", 'AMOUNT',
                                                                        'CURRENT BALANCE', 'DATE', 'TIME'))
                transactionPage = 1
                while True:
                    if (len(all_trans) >= transactionPage * 10):
                        for i in range((transactionPage - 1) * 10, transactionPage * 10):
                            data = all_trans[i]
                            a = eval(data[0])
                            print('{:<10s}{:>4s}{:>20s}{:>22s}{:>22s}{:>22}'.format(str(a[0]), str(a[1]), str(a[2]),
                                                                                    str(a[3]), str(data[1]),
                                                                                    str(data[2])))
                            # print(all_trans[i])
                        askTransactionPageContinue = str(
                            input("Do you want to get Page {0} of Transactions? (y/n) : ".format(transactionPage + 1)))
                        if (askTransactionPageContinue == "y"):
                            transactionPage = transactionPage + 1
                            continue
                        else:
                            break
                    else:
                        finaLoopNum = (transactionPage * 10) - len(all_trans)
                        if (finaLoopNum != 0):
                            for i in range((transactionPage - 1) * 10,
                                           ((transactionPage - 1) * 10) + (10 - finaLoopNum)):
                                data = all_trans[i]
                                a = eval(data[0])
                                print('{:<10s}{:>4s}{:>20s}{:>22s}{:>22s}{:>22}'.format(str(a[0]), str(a[1]), str(a[2]),
                                                                                        str(a[3]), str(data[1]),
                                                                                        str(data[2])))
                            break
                        else:
                            print("No Transactions Left")
                            break
                break


def deposit():
    global current_user_global
    print()
    print("--------------------------------------")
    print("Money Deposit")
    print("--------------------------------------")
    print()
    dep_amt = int(input("enter the amount to be deposited : "))
    if dep_amt < 100:
        print("please enter a higher value")
        deposit()
    current_balance = current_user_global[3]
    current_balance = current_balance + dep_amt
    balance_update = 'update users set balance = {0} where userid = {1} '.format(current_balance,
                                                                                 current_user_global[0])
    cursor.execute(balance_update)
    current_date_time = currenttime()
    current_date = current_date_time[0]
    current_time = current_date_time[1]
    trans_log = (
        current_user_global[0], '{}'.format(['self', 'CREDIT', dep_amt, current_balance]), current_date, current_time)
    insert = 'insert into trans values{}'.format(trans_log)
    cursor.execute(insert)
    database.commit()
    current_user_global[3] = current_balance
    return current_user_global


def withdraw():
    global current_user_global
    print()
    print("--------------------------------------")
    print("Money Withdraw")
    print("--------------------------------------")
    print()
    with_amt = int(input("enter the amount to be withdraw : "))
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
        current_user_global[0], '{}'.format(['self', 'DEBIT ', with_amt, current_balance]), current_date, current_time)
    insert = 'insert into trans values{}'.format(trans_log)
    cursor.execute(insert)
    database.commit()
    current_user_global[3] = current_balance
    return current_user_global


def transaction():
    global current_user_global
    to_person_input = input('enter the person to whom you wish to send money : ')
    amount = int(input("enter the amount you want to send to '{}' :".format(to_person_input)))
    to_person_selector = "SELECT * from users where userid = {}".format(to_person_input)
    cursor.execute(to_person_selector)
    to_person = list(cursor.fetchone())
    try:
        if amount > current_user_global[3]:
            print(
                "The amount you wish to send is greater than\n your current balance\n so try deposting the money to proceed")
    except:
        loginscreen()
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
        current_user_global[0], '{}'.format([to_person_input, 'DEBIT ', amount, current_user_balance]), current_date,
        current_time)
    insert_1 = 'insert into trans values{}'.format(to_trans_log)
    insert_2 = 'insert into trans values{}'.format(from_trans_log)
    cursor.execute(insert_1)
    cursor.execute(insert_2)
    database.commit()
    current_user_global[3] = current_user_balance
    return current_user_global


def currenttime():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

    d_string = current_time.strftime("20%y-%m-%d")
    t_string = current_time.strftime("%H:%M:%S")
    time = [d_string, t_string]
    return time


def login():
    global current_user_global
    userid = int(userid_e.get())
    password = pass_e_login.get()

    pin_selector_database = "SELECT * from users where userid = {}".format(userid)
    cursor.execute(pin_selector_database)
    current_user_temp_tuple = cursor.fetchone()
    if current_user_temp_tuple == None:
        print('account not found\nplease try again')
        login_window.destroy()
        login_screen()
    else:
        current_user_temp_list = list(current_user_temp_tuple)
        current_user_temp_list[2] = str(decodeStr(current_user_temp_list[2]))
        current_user_global = current_user_temp_list
        if current_user_temp_list[2] == password:
            print('successfully logined to the account')
            login_window.destroy()
            logined_screen()
        else:
            print('entered password is incorrect\n please try again')
            login_window.destroy()
            login_screen()



def createaccount():
    name = name_e.get()
    userid = random.randint(10002, 100000)
    pin = pass_e.get()
    pin2 = pass_chk_e.get()
    if pin != pin2:
        print("pin dose not match\nplease try again")
        Create_Account.destroy()
        create_screen()
    else:
        balance = 0
        pin_encoded = str(encodeStr(pin))
        print(type(pin_encoded))
        insertstr = "insert into users values('{0}','{1}','{2}','{3}')".format(userid, name, pin_encoded, balance)
        cursor.execute(insertstr)
        database.commit()
        print("account sucessfully created :-")
        print("name    = {}".format(name))
        print("userid  = {}".format(userid))
        print("pin     = {}".format(pin))
        print("balance = 0")
        Create_Account.destroy()


def logined_screen():
    logined_window = Tk()
    logined_window.geometry('1000x800')
    logined_window.title('Welcome to BANK')

    spaces = Label(logined_window, text="   ", font=('Arial Bold', 40))
    spaces.grid(column=0, row=0)

    welcome = Label(logined_window, text="What do you want to do?", font=('Arial Bold', 50))
    welcome.grid(column=1, row=0, columnspan=4)

    trans_button = Button(logined_window, text='Transaction', font=('Arial Bold', 42), bg='light blue', fg='white',
                          command=transaction)  #
    trans_button.grid(row=2, column=1, columnspan=3)
    deposit_button = Button(logined_window, text='Deposit', font=('Arial Bold', 42), bg='light blue', fg='white',
                            command=deposit)  #
    deposit_button.grid(row=3, column=1, columnspan=3)
    withdrawal_button = Button(logined_window, text='Withdrawal', font=('Arial Bold', 42), bg='light blue', fg='white',
                               command=withdraw)  #
    withdrawal_button.grid(row=4, column=1, columnspan=3)
    show_trans_button = Button(logined_window, text='Show transaction', font=('Arial Bold', 42), bg='light blue',
                               fg='white', command=showtransaction)  #
    show_trans_button.grid(row=5, column=1, columnspan=3)
    loan_button = Button(logined_window, text='Loan', font=('Arial Bold', 42), bg='light blue', fg='white',
                         command=login)  #
    loan_button.grid(row=6, column=1, columnspan=3)
    exit_button = Button(logined_window, text='Exit', font=('Arial Bold', 42), bg='light blue', fg='white',
                         command=login_admin)  #
    exit_button.grid(row=7, column=1, columnspan=3)
    logined_window.mainloop()

def login_admin():
    pass


def encodeStr(text):
    global fernet, key
    encryptedText = fernet.encrypt(text.encode()).decode()
    return encryptedText


def decodeStr(text):
    global fernet, key
    decryptedText = fernet.decrypt(text.encode()).decode()
    return decryptedText


def login_screen():
    global userid_e,pass_e_login,login_window
    login_window = Tk()
    login_window.geometry('1000x800')
    login_window.title('Login')

    welcome = Label(login_window, text="                     Welcome to Online Bank                     ",
                    font=('Arial Bold', 40))
    welcome.grid(column=0, row=0, columnspan=6)

    spaces = Label(login_window, text="           ", font=('Arial Bold', 40))
    spaces.grid(column=0, row=1)

    welcome = Label(login_window, text="   Login   ", font=('Arial Bold', 40))
    welcome.grid(column=1, row=1, columnspan=2)

    spaces = Label(login_window, text="             ", font=('Arial Bold', 40))
    spaces.grid(column=0, row=1)

    userid_label = Label(login_window, text="   User ID   ", font=('Arial Bold', 30))
    userid_label.grid(column=1, row=3)

    userid_e = Entry(login_window, borderwidth=10, font=('Arial Bold', 20))
    userid_e.grid(column=2, row=3)

    spaces = Label(login_window, text="             ", font=('Arial Bold', 40))
    spaces.grid(column=0, row=4)

    pass_label = Label(login_window, text="Password   ", font=('Arial Bold', 30))
    pass_label.grid(column=1, row=4)

    pass_e_login = Entry(login_window, borderwidth=10, font=('Arial Bold', 20))
    pass_e_login.grid(column=2, row=4)

    spaces = Label(login_window, text="             ", font=('Arial Bold', 40))
    spaces.grid(column=0, row=5)
    spaces = Label(login_window, text="             ", font=('Arial Bold', 40))
    spaces.grid(column=1, row=5)

    login_button = Button(login_window, text='Login', font=('Arial Bold', 24), bg='light blue', fg='white',
                          command=login)
    login_button.grid(row=5, column=1, columnspan=2)

    spaces = Label(login_window, text="             ", font=('Arial Bold', 40))
    spaces.grid(column=0, row=6)

    frame_admin = LabelFrame(login_window, text='Administrator', font=('Arial Bold', 20))
    frame_admin.grid(column=1, row=6)

    login_button_admin = Button(frame_admin, text='Login', font=('Arial Bold', 24), bg='#FF7F50', fg='white',
                                command=login_admin)
    login_button_admin.grid(row=0, column=0, )

    frame_new = LabelFrame(login_window, text='New Account', font=('Arial Bold', 20), padx=5, pady=5)
    frame_new.grid(column=2, row=6, columnspan=2)

    create_btn = Button(frame_new, text='Create new account', font=('Arial Bold', 24), bg='#00008B', fg='white', padx=7,
                        pady=3, command=create_screen)
    create_btn.grid(row=5, column=0)

    login_window.mainloop()


def create_screen():
    global name_e,pass_e,pass_chk_e,Create_Account
    Create_Account = Tk()
    Create_Account.geometry('1000x800')
    Create_Account.title('Create Account')

    welcome = Label(Create_Account, text="                     Create Account                    ",
                    font=('Arial Bold', 40))
    welcome.grid(column=1, row=0, columnspan=4)

    spaces = Label(Create_Account, text="   ", font=('Arial Bold', 40))
    spaces.grid(column=0, row=1)
    welcome = Label(Create_Account, text="                 Name:", font=('Arial Bold', 40))
    welcome.grid(column=1, row=1)
    name_e = Entry(Create_Account, borderwidth=10, font=('Arial Bold', 30))
    name_e.grid(column=3, row=1)

    spaces = Label(Create_Account, text="    ", font=('Arial Bold', 40))
    spaces.grid(column=0, row=2)
    welcome = Label(Create_Account, text="          Password:", font=('Arial Bold', 40))
    welcome.grid(column=1, row=2)
    pass_e = Entry(Create_Account, borderwidth=10, font=('Arial Bold', 30))
    pass_e.grid(column=3, row=2)

    spaces = Label(Create_Account, text="   ", font=('Arial Bold', 40))
    spaces.grid(column=0, row=3)
    welcome = Label(Create_Account, text="Check Password:", font=('Arial Bold', 40))
    welcome.grid(column=1, row=3)
    pass_chk_e = Entry(Create_Account, borderwidth=10, font=('Arial Bold', 30))
    pass_chk_e.grid(column=3, row=3)

    login_button = Button(Create_Account, text='Create Account', font=('Arial Bold', 24), bg='light blue', fg='white',
                          padx=10, pady=5, command=createaccount)
    login_button.grid(row=4, column=1, columnspan=3)

    Create_Account.mainloop()

# main

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

