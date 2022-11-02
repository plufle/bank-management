import mysql.connector as connector
import random
from cryptography.fernet import Fernet
import datetime
import pytz
from datetime import date, timedelta
import main_passwords

transactionPage = 1


def login():
    userid = int(input("enter your userid :"))
    password = input("enter your password: ")

    pin_selector_database = "SELECT * from users where userid = {}".format(userid)
    cursor.execute(pin_selector_database)
    current_user_temp_tuple = cursor.fetchone()
    current_user_temp_list = list(current_user_temp_tuple)
    current_user_temp_list[2] = str(decodeStr(current_user_temp_list[2]))
    if current_user_temp_list[2] == password:
        print('successfully logined to the account')
    else:
        print('entered password is incorrect\n please try again')
        login()
    return current_user_temp_list


def createaccount():
    name = input("enter your name      : ")
    userid = random.randint(10002, 100000)
    pin = input("enter you password    :  ")
    pin2 = input("confirm your password : ")
    if pin != pin2:
        print("pin dose not match\nplease try again")
        createaccount()
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


def loginscreen():
    global current_user_global
    while True:
        print('*' * 20)
        print('LOGINED AS {}'.format(current_user_global[1]))
        print("Please Select an Option Below : ")
        print("Transaction      (1)")
        print("Deposit          (2)")
        print("Withdrawal       (3)")
        print("show transaction (4)")
        print("Loan             (5)")
        print("Exit             (6)")
        option = int(input("chose an option : "))
        if option == 1:
            transaction()
        elif option == 2:
            deposit()
        elif option == 3:
            withdraw()
        elif option == 4:
            showtransaction()
        elif option == 5:
            loan()
        elif option == 6:
            break
        else:
            print("please choose a valid option \n kindly try again")


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
    pass


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

print("___________WELCOME TO THE BANK__________")
print("What Would You Like to Do ?")
print("1)Login")
print("2)Create Account")
ask_login_signup = int(input("Enter an Option : "))

if ask_login_signup == 1:
    current_user_global = login()
    loan_check_login()
else:
    createaccount()
    current_user_global = login()


database.close()
#TODO : loan repayment
#TODO : admin account
#TODO :add exit option on show transaction
