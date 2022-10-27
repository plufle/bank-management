'''import mysql.connector as con

try:
    a = con.connect(host='localhost', database='test', user='root', password='Sarvesh@2005')

    print('connected')
except:
    print('not connected')

cursor = a.cursor()
cursor.execute("SELECT * FROM shop ORDER BY article")

b = cursor.fetchall()

for c in b:
    print(c)'''