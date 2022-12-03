from cryptography.fernet import Fernet
import datetime
import pytz
from datetime import date, timedelta
import main_passwords





key = main_passwords.frenet_key.encode()
fernet = Fernet(key)

def decodeStr(text):
    global fernet, key
    decryptedText = fernet.decrypt(text.encode()).decode()
    return decryptedText

print(decodeStr('gAAAAABjh29m_PRgRCnb3kVe7gps-PyVQbJfNz5UTjDS0Fh6FdffZNf1l-v1B-4SOyv7G36oj94koRKA7D4DB9Eekgww_p8fTA==)'))