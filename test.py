from tkinter import *


# type each command and make modifications
def createacc_com():
    pass


def logined_screen():
    logined_window = Tk()
    logined_window.geometry('1000x800')
    logined_window.title('Welcome to BANK')

    spaces = Label(logined_window, text="   ", font=('Arial Bold', 40))
    spaces.grid(column=0, row=0)

    welcome = Label(logined_window, text="What do you want to do?", font=('Arial Bold', 50))
    welcome.grid(column=1, row=0, columnspan=4)

    trans_button = Button(logined_window, text='Transaction', font=('Arial Bold', 42), bg='light blue', fg='white',
                          command=createacc_com)  #
    trans_button.grid(row=2, column=1, columnspan=3)
    deposit_button = Button(logined_window, text='Deposit', font=('Arial Bold', 42), bg='light blue', fg='white',
                            command=createacc_com)  #
    deposit_button.grid(row=3, column=1, columnspan=3)
    withdrawal_button = Button(logined_window, text='Withdrawal', font=('Arial Bold', 42), bg='light blue', fg='white',
                               command=createacc_com)  #
    withdrawal_button.grid(row=4, column=1, columnspan=3)
    show_trans_button = Button(logined_window, text='Show transaction', font=('Arial Bold', 42), bg='light blue',
                               fg='white', command=createacc_com)  #
    show_trans_button.grid(row=5, column=1, columnspan=3)
    loan_button = Button(logined_window, text='Loan', font=('Arial Bold', 42), bg='light blue', fg='white',
                         command=createacc_com)  #
    loan_button.grid(row=6, column=1, columnspan=3)
    exit_button = Button(logined_window, text='Exit', font=('Arial Bold', 42), bg='light blue', fg='white',
                         command=createacc_com)  #
    exit_button.grid(row=7, column=1, columnspan=3)

    logined_window.mainloop()
logined_screen()
