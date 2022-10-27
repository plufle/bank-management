import mysql.connector
import random
from cryptography.fernet import Fernet
import time

connection = False
user = 0
key = "ardUzMIZoH2GkWy3anKAs2YFTFyLHrcqub3WHazfdUY=".encode()
# print(key)
# # print(key)
fernet = Fernet(key)

try:
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='kishore@123',
        port='3306',
    )
    # database.autocommit(True)
except:
    print("Couldn't Connect to The Database")
    exit(0)
else:
    connection = True
# else:
#     print("Hey")
#     connection = True

cursor = database.cursor()
cursor.execute("use bank")

def login():
    global user
    while True:
        try:
            username = str(input("Enter The User ID : "))
            password = int(input("Enter The Pin : "))

            if (checkPin(password) == False):
                print("Please Enter a 4 digit Pin")
                exit(0)

            data = 0
            try:
                makeCurrent(username)
                data = eval(decodeStr(user))
                # print(data)
            except :
                print("User Doesn't Exist")
                print()

            if data["pin"] != password:
                time.sleep(1)
                # print()
                print("Pin Doesn't Match\nPlease Try Again")
                print()
            else:
                time.sleep(1)
                print()
                print("--------------------------------------")
                print("Welcome Back, {0}".format(data["name"]))
                print("--------------------------------------")
                break

            # print(user)
        except:
            print("Something Went Wrong")
            time.sleep(1)
            print("Please Try again")

def loginScreen():
    global user
    while True:
        print()
        print("Please Select an Option Below{0}".format(calcStats()))
        print("Loan (1)")
        print("Deposit (2)")
        print("Withdrawal (3)")
        print("Exit (4)")
        data = eval(decodeStr(user))
        try:
            ask_option = int(input("Enter an Option : "))
            if (ask_option not in [1, 2, 3, 4]):
                raise Exception("Invalid Option")
            else:
                if ask_option == 1:
                    loan(data)
                elif ask_option == 2:
                    deposit(data)
                elif ask_option == 3:
                    withdrawal(data)
                else:
                    break

        except:
            print("Invalid Option\nPlease Try Again")

def loan(data):
    global user
    time.sleep(1)
    print()
    print("--------------------------------------")
    print("Loan Request")
    print("--------------------------------------")
    print()
    try:
        # while True:
            loan_amt = int(input("Please Enter The Amount to be Requested : "))
            if loan_amt < 50000:
                print("Amount Too Low\nPlease Enter an Amount above rs50000")
            else:
                print("Processing Loan")
                cnt = 0
                for i in data["movements"]:
                    if ((loan_amt * 5)/100 <= i):
                        cnt = cnt +1

                if(cnt > 0):
                    time.sleep(3)
                    print("Loan Approved")
                    data["movements"].append(loan_amt)
                    saveDetails(data)
                else:
                    time.sleep(3)
                    print("Loan Declined\nCredit Too Low")
                # user = encodeStr(str(data))
                # break
    except:
        print("Invalid Amount")


def deposit(data):
    global user
    time.sleep(1)
    print()
    print("--------------------------------------")
    print("Money Deposit")
    print("--------------------------------------")
    print()
    try:
        # while True:
            depo_amt = int(input("Please Enter The Amount to be Deposited : "))
            if depo_amt < 1000:
                print("Amount Too Low\nPlease Enter an Amount above rs1000")
            else:
                print("Processing Deposit")
                time.sleep(3)
                print("rs{0} Successfully Deposited".format(depo_amt))
                data["movements"].append(depo_amt)
                saveDetails(data)
                # user = encodeStr(str(data))
                # break
    except:
        print("Invalid Amount")

def withdrawal(data):
    global user
    time.sleep(1)
    print()
    print("--------------------------------------")
    print("Money Withdrawal")
    print("--------------------------------------")
    print()
    try:
        # while True:
            with_amt = int(input("Please Enter The Amount to be Withdrawed : "))
            if with_amt < 1000:
                print("Amount Too Low\nPlease Enter an Amount above rs1000")
            else:
                print("Processing Deposit")
                time.sleep(3)
                print("rs{0} Successfully Withdrawed".format(with_amt))
                withStr = int("-{0}".format(with_amt))
                data["movements"].append(withStr)
                saveDetails(data)
                # user = encodeStr(str(data))
                # break
    except:
        print("Invalid Amount")


# def checkValid(username,pass1,pass2):
#     global user
#     if pass1 != pass2:
#         return False
#     cursor.execute("select * from accounts where user = '{0}'".format(username))
#     try:
#         temp = list(cursor.fetchall()[0])
#         if temp:
#             # print(temp)
#             user = temp[0]
#             # print(user)
#     except:
#         print("User Doesn't Exist")

def checkPin(x):
    if(len(str(x)) != 4):
        return False

def makeCurrent(username):
    global user
    cursor.execute("select * from accounts where user = '{0}'".format(username))
    try:
        temp = list(cursor.fetchall()[0])
        if temp:
            # print(temp)
            user = temp[0]
            temp = eval(decodeStr(user))
            # print("Welcome",temp["name"])
            # print("Current User",user)
    except:
        raise Exception("User Doesn't Exist")
        # print("User Doesn't Exist")

def createAccount():
    global user
    while True:
        try:
            print("An User ID will Be Generated Automatically")
            time.sleep(1)
            name = str(input("Enter Your Name : "))
            age = int(input("Please Enter Your Age : "))

            if (age < 18):
                time.sleep(1)
                print("Underage Account Please Try Again")
                print()

            else:
                pin1 = int(input("Enter a Pin : "))
                pin2 = int(input("Confirm Pin : "))
                if (pin1 != pin2):
                    print("Pin Doesn't Match The Confirm Pin\nPlease Try Again")
                else:
                    if (checkPin(pin1) == False):
                        print("Please Enter a 4 digit Pin")
                    else:
                        username = generateUser()
                        time.sleep(1)
                        print("Your User ID is {0}".format(username))
                        time.sleep(1)
                        print("Please Remember This User ID as this will be used to Login into The Bank")

                        insertObj = {}

                        insertObj["name"] = name
                        insertObj["pin"] = pin2
                        insertObj["age"] = age
                        insertObj["movements"] = []

                        insertStr = "insert into accounts values('{0}','{1}')".format(encodeStr(str(insertObj)),
                                                                                      username)
                        # print(insertStr)
                        # print(type(insertStr))

                        cursor.execute(insertStr)
                        database.commit()
                        time.sleep(1)
                        print("Account Created Successfully")
                        time.sleep(1)
                        print("--------------------------------------")
                        print("Welcome to Bank")
                        print("--------------------------------------")
                        makeCurrent(username)
                        break
                        # print(user)
        except:
            print("Something Went Wrong")

def calcStats():
    global user
    data = eval(decodeStr(user))

#     CALC BALANCE
    balTotal = 0
    for i in data["movements"]:
        balTotal = balTotal + i

# TOTAL DEPOSITS AND TOTAL WITHDRAWAL

    depTotal = 0
    withTotal = 0
    for i in data["movements"]:
        if(i > 0):
            depTotal = depTotal + i
        elif (i < 0):
            withTotal = withTotal + i

    finalStr = "\t\t\t\tTotal Balance : {0}\t\tTotal Deposits : {1}\t\tTotal Withdrawal : {2}".format(balTotal,depTotal,withTotal)

    return finalStr



def generateUser():
    while(True):
        x = random.randint(100000, 999999)
        # x = random.randint(0, 1)
        # print(x)
        cursor.execute("select * from accounts where user = '{0}'".format(x))
        try:
            temp = list(cursor.fetchall()[0])
            if temp:
                # print("User Exists Already")
                continue
                # print(connection)
        except:
            return x
            break

def saveDetails(data):
    global user
    saveStr = encodeStr(str(data))
    cursor.execute("update accounts set acc = '{0}' where acc = '{1}'".format(saveStr,user))
    database.commit()
    user = saveStr
    # print(user)

def encodeStr(text):
    global fernet,key
    encryptedText = fernet.encrypt(text.encode()).decode()
    return encryptedText
    # print(encryptedText)
    # print(cipher_text)
    # decryptedText = fernet.decrypt(encryptedText.encode())
    # print(decryptedText.decode())

def decodeStr(text):
    global fernet, key
    # encryptedText = fernet.encrypt(text.encode()).decode()
    # print(encryptedText)
    # print(encryptedText)
    # print(cipher_text)
    decryptedText = fernet.decrypt(text.encode()).decode()
    return decryptedText