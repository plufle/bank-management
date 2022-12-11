from tkinter import messagebox
import mysql.connector as connector
import customtkinter
def deposit_screen(x):
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

    login_button = customtkinter.CTkButton(deposit_window_top, text='continue', text_font=('Roboto Mono', 12))

    login_button.pack(ipadx=10, ipady=4, pady=20)

    deposit_window_top.mainloop()



deposit_screen(10)