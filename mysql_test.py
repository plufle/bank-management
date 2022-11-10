import tkinter
from tkinter import messagebox

window=tkinter.Tk()
window.title("Login Form")
window.geometry("1199x600")
window.configure(bg='#111116')

def Login():
    username="BBC"
    password="6969"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in...")
    else:
        messagebox.showinfo(title="Invalid login", message="Invalid login..")


frame=tkinter.Frame(bg='#111116')

#creating widgets
login_label=tkinter.Label(frame, text="MSD LIBRARY", bg='#111116', fg='#FF3399', font=('sans serif','30'))
username_label=tkinter.Label(frame, text="Username", bg='#111116', fg='white', font=('serif','20'))
username_entry=tkinter.Entry(frame)
password_entry=tkinter.Entry(frame, show="*")
password_label=tkinter.Label(frame, text="Password",bg='#111116', fg='white', font=('serif','20'))
login_button=tkinter.Button(frame, text="Login",bg='#FF3399', fg='white', font=('serif','20'))

#Placing wigets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1, column=1,pady=30)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2, pady=30)


frame.pack()
window.mainloop()