from tkinter import messagebox
import mysql.connector as connector
import customtkinter
def transaction_scrren():
    global tans_window
    tans_window = customtkinter.CTk()
    tans_window.geometry('800x524')
    tans_window.title('Transaction')

    welcome = customtkinter.CTkLabel(tans_window, text="TRANSACTION", text_font=('Roboto Mono', 30))
    welcome.pack(pady=30)

    frame = customtkinter.CTkFrame(tans_window, padx=10, pady=5, width=200)
    frame.pack()

    name_label = customtkinter.CTkLabel(frame, text='userid',
                                        text_font=('Roboto Mono', 20))
    name_label.grid(column=1, row=2, pady=20)
    password_label = customtkinter.CTkLabel(frame, text='amount',
                                            text_font=('Roboto Mono', 20))
    password_label.grid(column=1, row=3)

    name_entry = customtkinter.CTkEntry(frame, text_font=('Roboto Mono', 15), width=150, height=35)
    name_entry.grid(column=2, row=2, pady=5, padx=30)

    pass_entry = customtkinter.CTkEntry(frame, text_font=('Roboto Mono', 15), width=150, height=35)
    pass_entry.grid(column=2, row=3, pady=10)

    confirm_button = customtkinter.CTkButton(frame, text='confirm', text_font=('Roboto Mono', 22)
                                             )

    confirm_button.grid(row=5, column=1, columnspan=10, ipadx=10, ipady=4, pady=30)
    tans_window.mainloop()



transaction_scrren()