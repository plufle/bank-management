from model import createAccount,login,generateUser,checkPin,encodeStr,decodeStr,loginScreen
import time

BANK = "Bankist"

# print()
# x = checkValid("kitu",5,5)
# if(x == False):
#     # print("hEY")
# else:
#     print("Boi")

# checkPin(1234)

# login()
# createAccount()
# x = encodeStr("Kishore Is Great")
# print(x)
#
# print(decodeStr("gAAAAABiVZFr01c17-yxY68dNr0MxH2m5JNa2RFIH-5eN1A-qORGCPMyKrr5W8h2x8J4VFTwfdMGNTVoSjvsfzoZzcm6MuVBO4pbyO8v2PprJf1dDRd_vQmikKXDPs6bYNZRfXjWxMbISPjN5EpNimPykNyjmuqzrw=="))

# login()
# x = generateUser()
# print("Boi",x)


# createAccount("Kishore",1234)
print("Welcome to {0}".format(BANK))
time.sleep(1)
print()
print("What Would You Like to Do ?")
time.sleep(1)
print("Login (1)")
print("Sign Up (2)")

ask_login_signup=0

while True:
    try:
        ask_login_signup = int(input("Enter an Option : "))

        if ask_login_signup != 1 and ask_login_signup != 2:
            raise Exception("Invalid Option")

        break
    except:
        print("Please Enter a Valid Option")
        print()

if ask_login_signup ==1 :
    print()
    time.sleep(1)
    login()
    time.sleep(1)
    loginScreen()

else:
    print()
    time.sleep(1)
    createAccount()

#     TO DO
# EMAIL SERVICE
# PERSON TO PERSON TRANSACTION
# FREEZE OPERATIONS IF BALANCE BELOW -10000
