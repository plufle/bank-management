from tkinter import messagebox
import mysql.connector as connector
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
create_account = customtkinter.CTk()
create_account.geometry('800x524')
create_account.title('Create Account')
spaces = customtkinter.CTkLabel(create_account, text=''' ''', text_font=('Roboto Mono', 20))
spaces.pack()
welcome = customtkinter.CTkLabel(create_account, text="Create Account", text_font=('Roboto Mono', 28),
                                 text_color='#d7e3fc')
welcome.pack(anchor=customtkinter.N)

create_frame = customtkinter.CTkFrame(master=create_account, width=20, height=250, corner_radius=10)
create_frame.pack(ipady=5, ipadx=10, expand=True)


spaces = customtkinter.CTkLabel(create_frame, text=''' ''', text_font=('Roboto Mono', 5))
spaces.grid(row=1, column=3)
spaces = customtkinter.CTkLabel(create_frame, text=''' ''', text_font=('Roboto Mono', 5))
spaces.grid(row=3, column=2)
spaces = customtkinter.CTkLabel(create_frame, text=''' ''', text_font=('Roboto Mono', 5))
spaces.grid(row=5, column=2)

name_label = customtkinter.CTkLabel(create_frame, text='                 name                 ', text_font=('Roboto Mono', 20))
name_label.grid(column=1, row=2)
password_label = customtkinter.CTkLabel(create_frame, text='                 password             ', text_font=('Roboto Mono', 20))
password_label.grid(column=1, row=3)
password_confirm_label = customtkinter.CTkLabel(create_frame, text='                 password confirm ', text_font=('Roboto Mono', 20))
password_confirm_label.grid(column=1, row=4)

name_entry = customtkinter.CTkEntry(create_frame, text_font=('Roboto Mono', 15), width=150, height=35)
name_entry.grid(column=2, row=2,pady = 10)

pass_entry = customtkinter.CTkEntry(create_frame, text_font=('Roboto Mono', 15), show='*', width=150, height=35)
pass_entry.grid(column=2, row=3,pady = 10)

pass_confirm_entry = customtkinter.CTkEntry(create_frame, text_font=('Roboto Mono', 15), show='*', width=150, height=35)
pass_confirm_entry.grid(column=2, row=4,pady = 10)

login_button = customtkinter.CTkButton(create_frame, text='create account', text_font=('Roboto Mono', 22))
login_button.grid(row=5, column=1,columnspan = 10, ipadx=10, ipady=4)

create_account.mainloop()
