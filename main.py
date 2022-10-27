import mysql.connector as connector
import random
#functions
def login(userid,pin):
    pin_selector_database = "SELECT * from acc where userid = {}".format(userid)
    try:
       cursor.execute(pin_selector_database)
       b = cursor.fetchall()
       cursor.execute("select * from acc where userid = '{0}'".format(userid))
       current_user_local = cursor.fetchall()
       if current_user_local[0][2] == pin:
           print("successfully logined")
       else:
           print("Pin Doesn't Match\nPlease Try Again")
    except:
          print("account not found_")
    return current_user_local





def create_account():
    name = input("enter your name :")
    userid = random.randint(1003,10000)
    pin = int(input("enter you pin (4 digit password) :  "))
    pin2 = int(input("confirm pin :"))
    if pin != pin2:
        print("pin dose not match\nplease try again")
        create_account()
    else:
        balance = 0
        insertStr = "insert into acc values('{0}','{1}','{2}','{3}')".format(name,userid,pin,balance)
        print("account sucessfully created :-")
        print("name    = {}".format(name))
        print("userid  = {}".format((userid)))
        print("pin     = {}".format((pin)))
        print("balance = 0")
        cursor.execute(insertStr)
        database.commit()

#**********************************************************************************
# **********************************************************************************
# **********************************************************************************
# **********************************************************************************
# **********************************************************************************
try:
    database = connector.connect(host='localhost', database='bank', user='root', password='Sarvesh@2005')

    print('successfully connected to database')
except:
    print('database not connected')

cursor = database.cursor()
cursor.execute("use bank")

print("___________WELCOME TO THE BANK__________")
print("What Would You Like to Do ?")
print("1)Login")
print("2)Create Account")
ask_login_signup = int(input("Enter an Option : "))
#try:
if ask_login_signup == 1:
     userid= int(input("enter :"))
     pin = int(input("enter: "))
     current_user_global = login(userid,pin)
     print(current_user_global)
else:
     create_account()
#except:
    #print("Choose An Valid Option")





