from re import L
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import random
import time
import customtkinter

cash = 100

def roll():
    global rollnum

    rollnum = random.randint(1, 6)
    print(rollnum)

    if rollnum == 1:
        button1.configure(bg_color="transparent", fg_color="transparent")
        button2.configure(bg_color="transparent", fg_color="transparent")
        button3.configure(bg_color="transparent", fg_color="transparent")
        button4.configure(bg_color="transparent", fg_color="transparent")
        #button5.configure(bg_color="transparent", fg_color="transparent")
        button6.configure(bg_color="transparent", fg_color="transparent")
        button7.configure(bg_color="transparent", fg_color="transparent")
        button8.configure(bg_color="transparent", fg_color="transparent")
        button9.configure(bg_color="transparent", fg_color="transparent")

        button5.configure(bg_color="transparent", fg_color="#616161")

    if rollnum == 2:
        #button1.configure(bg_color="transparent", fg_color="transparent")
        button2.configure(bg_color="transparent", fg_color="transparent")
        button3.configure(bg_color="transparent", fg_color="transparent")
        button4.configure(bg_color="transparent", fg_color="transparent")
        button5.configure(bg_color="transparent", fg_color="transparent")
        button6.configure(bg_color="transparent", fg_color="transparent")
        button7.configure(bg_color="transparent", fg_color="transparent")
        button8.configure(bg_color="transparent", fg_color="transparent")
        #button9.configure(bg_color="transparent", fg_color="transparent")

        button1.configure(bg_color="transparent", fg_color="#616161")
        button9.configure(bg_color="transparent", fg_color="#616161")

    if rollnum == 3:
        #button1.configure(bg_color="transparent", fg_color="transparent")
        button2.configure(bg_color="transparent", fg_color="transparent")
        button3.configure(bg_color="transparent", fg_color="transparent")
        button4.configure(bg_color="transparent", fg_color="transparent")
        #button5.configure(bg_color="transparent", fg_color="transparent")
        button6.configure(bg_color="transparent", fg_color="transparent")
        button7.configure(bg_color="transparent", fg_color="transparent")
        button8.configure(bg_color="transparent", fg_color="transparent")
        #button9.configure(bg_color="transparent", fg_color="transparent")

        button1.configure(bg_color="transparent", fg_color="#616161")
        button5.configure(bg_color="transparent", fg_color="#616161")
        button9.configure(bg_color="transparent", fg_color="#616161")

    if rollnum == 4:
        #button1.configure(bg_color="transparent", fg_color="transparent")
        button2.configure(bg_color="transparent", fg_color="transparent")
        #button3.configure(bg_color="transparent", fg_color="transparent")
        button4.configure(bg_color="transparent", fg_color="transparent")
        button5.configure(bg_color="transparent", fg_color="transparent")
        button6.configure(bg_color="transparent", fg_color="transparent")
        #button7.configure(bg_color="transparent", fg_color="transparent")
        button8.configure(bg_color="transparent", fg_color="transparent")
        #button9.configure(bg_color="transparent", fg_color="transparent")

        button1.configure(bg_color="transparent", fg_color="#616161")
        button3.configure(bg_color="transparent", fg_color="#616161")
        button7.configure(bg_color="transparent", fg_color="#616161")
        button9.configure(bg_color="transparent", fg_color="#616161")

    if rollnum == 5:
        #button1.configure(bg_color="transparent", fg_color="transparent")
        button2.configure(bg_color="transparent", fg_color="transparent")
        #button3.configure(bg_color="transparent", fg_color="transparent")
        button4.configure(bg_color="transparent", fg_color="transparent")
        #button5.configure(bg_color="transparent", fg_color="transparent")
        button6.configure(bg_color="transparent", fg_color="transparent")
        #button7.configure(bg_color="transparent", fg_color="transparent")
        button8.configure(bg_color="transparent", fg_color="transparent")
        #button9.configure(bg_color="transparent", fg_color="transparent")

        button1.configure(bg_color="transparent", fg_color="#616161")
        button3.configure(bg_color="transparent", fg_color="#616161")
        button5.configure(bg_color="transparent", fg_color="#616161")
        button7.configure(bg_color="transparent", fg_color="#616161")
        button9.configure(bg_color="transparent", fg_color="#616161")

    if rollnum == 6:
        #button1.configure(bg_color="transparent", fg_color="transparent")
        button2.configure(bg_color="transparent", fg_color="transparent")
        #button3.configure(bg_color="transparent", fg_color="transparent")
        #button4.configure(bg_color="transparent", fg_color="transparent")
        button5.configure(bg_color="transparent", fg_color="transparent")
        #button6.configure(bg_color="transparent", fg_color="transparent")
        #button7.configure(bg_color="transparent", fg_color="transparent")
        button8.configure(bg_color="transparent", fg_color="transparent")
        #button9.configure(bg_color="transparent", fg_color="transparent")

        button1.configure(bg_color="transparent", fg_color="#616161")
        button3.configure(bg_color="transparent", fg_color="#616161")
        button4.configure(bg_color="transparent", fg_color="#616161")
        button6.configure(bg_color="transparent", fg_color="#616161")
        button7.configure(bg_color="transparent", fg_color="#616161")
        button9.configure(bg_color="transparent", fg_color="#616161")



def lessthen3():
    global rollnum
    global cash

    if cash < 10:
        return

    roll()

    cash = cash - 10 
    if rollnum <= 3:
        cash += 20
    cashla.configure(text=f"Cash: £{cash}")

def morethen4():
    global rollnum
    global cash

    if cash < 10:
        return

    roll()

    cash = cash - 10 
    if rollnum >= 4:
        cash += 20
    cashla.configure(text=f"Cash: £{cash}")

def issix():
    global rollnum
    global cash

    if cash < 10:
        return

    roll()

    cash = cash - 10 
    if rollnum == 6:
        cash += 30
    cashla.configure(text=f"Cash: £{cash}")

    

root = customtkinter.CTk()
root.title("Dice")
root.configure(fg_color='#232528')

font = Font(family="Uni Sans Heavy")

cashla = customtkinter.CTkLabel(master=root, text=f"Cash: £{cash}", text_color="green")
cashla.grid(row=0, column=0)

button0 = customtkinter.CTkButton(master=root, text="Roll!", command=roll, corner_radius=12, bg_color="transparent", fg_color="#006399", hover_color="#003857")
button0.grid(row=0, column=1, padx=7, pady=10)

button1 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131")
button1.grid(row=1, column=0, padx=4, pady=7)

button2 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131")
button2.grid(row=1, column=1, padx=4, pady=7)

button3 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131")
button3.grid(row=1, column=2, padx=4, pady=7)

button4 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131")
button4.grid(row=2, column=0, padx=4, pady=7)

button5 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131")
button5.grid(row=2, column=1, padx=4, pady=7)

button6 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131")
button6.grid(row=2, column=2, padx=4, pady=7)

button7 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131")
button7.grid(row=3, column=0, padx=4, pady=7)

button8 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131")
button8.grid(row=3, column=1, padx=4, pady=7)

button9 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131")
button9.grid(row=3, column=2, padx=4, pady=7)

gamble0 = customtkinter.CTkButton(master=root, height=40, width=60, text="3 Or Below (10)", corner_radius=4, bg_color="transparent", fg_color="#00803a", hover_color="#004720", command=lessthen3)
gamble0.grid(row=4, column=0, padx=4, pady=7)

gamble1 = customtkinter.CTkButton(master=root, height=40, width=60, text="4 Or above (10)", corner_radius=4, bg_color="transparent", fg_color="#00803a", hover_color="#004720", command=morethen4)
gamble1.grid(row=4, column=1, padx=4, pady=7)

gamble2 = customtkinter.CTkButton(master=root, height=40, width=60, text="Is six (3x return)", corner_radius=4, bg_color="transparent", fg_color="#00803a", hover_color="#004720", command=issix)
gamble2.grid(row=4, column=2, padx=4, pady=7)

root.mainloop()


