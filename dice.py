from re import L
import tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from unittest import TextTestResult
import random
import time
import customtkinter
# basic imports
# stating strings used
cash = 100
devx = 0
devy = 0

roll1 = 0
roll2 = 0
roll3 = 0
wroll = 0
def create_toplevel(): # open devmenu new window
    global roll1wl
    global roll2wl
    global roll3wl

    def devmon1(): # add 10 cash
        global cash
        cash += 10
        cashla.configure(text=f"Cash: £{cash}")

    def devmon2(): # add 100 cash
        global cash
        cash += 100
        cashla.configure(text=f"Cash: £{cash}")

    def devmon3(): # add 1000 cash
        global cash
        cash += 1000
        cashla.configure(text=f"Cash: £{cash}")

    def devmon4(): # add 10000 cash
        global cash
        cash += 10000
        cashla.configure(text=f"Cash: £{cash}")

    def devmon5(): # add 100000 cash
        global cash
        cash += 100000
        cashla.configure(text=f"Cash: £{cash}")

    def devmon6(): # add 1000000 cash
        global cash
        cash += 1000000
        cashla.configure(text=f"Cash: £{cash}")

    def devmoncom():
        global cash

        cashadd = customCashTextbox.get()
        cash += int(cashadd)
        cashla.configure(text=f"Cash: £{cash}")

    
    devmenu = customtkinter.CTkToplevel() # main build of dev menu
    devmenu.title("Dice - Dev Menu")

    font = Font(family="Uni Sans Heavy")

    label = customtkinter.CTkLabel(devmenu, text="Dev Menu")
    label.grid(row=0, column=0, sticky="ew")

    # add cash set amounts
    cash10 = customtkinter.CTkButton(master=devmenu, text="Cash+10",text_color="green", fg_color="black", border_color="white", hover_color="#313131", corner_radius=8, command=devmon1)
    cash10.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

    cash100 = customtkinter.CTkButton(master=devmenu, text="Cash+100",text_color="green", fg_color="black", border_color="white", hover_color="#313131", corner_radius=8, command=devmon2)
    cash100.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

    cash1000 = customtkinter.CTkButton(master=devmenu, text="Cash+1000",text_color="green", fg_color="black", border_color="white", hover_color="#313131", corner_radius=8, command=devmon3)
    cash1000.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

    cash10000 = customtkinter.CTkButton(master=devmenu, text="Cash+10,000",text_color="green", fg_color="black", border_color="white", hover_color="#313131", corner_radius=8, command=devmon4)
    cash10000.grid(row=4, column=0, padx=20, pady=5, sticky="ew")

    cash100000 = customtkinter.CTkButton(master=devmenu, text="Cash+100,000",text_color="green", fg_color="black", border_color="white", hover_color="#313131", corner_radius=8, command=devmon5)
    cash100000.grid(row=5, column=0, padx=20, pady=5, sticky="ew")

    cash1000000 = customtkinter.CTkButton(master=devmenu, text="Cash+1,000,000",text_color="green", fg_color="black", border_color="white", hover_color="#313131", corner_radius=8, command=devmon6)
    cash1000000.grid(row=6, column=0, padx=20, pady=5, sticky="ew")

    # custom cash amount
    customCashLabel = customtkinter.CTkLabel(master=devmenu, text="Custom Cash Add", text_color="green")
    customCashLabel.grid(row=7, column=0, padx=10, pady=5, sticky="ew")

    customCashTextbox = customtkinter.CTkEntry(master=devmenu)
    customCashTextbox.grid(row=8, column=0, padx=10, sticky="ew")

    cashCustomAdd = customtkinter.CTkButton(master=devmenu, text="Add Cash",text_color="green", fg_color="black", border_color="white", hover_color="#313131", corner_radius=8, command=devmoncom)
    cashCustomAdd.grid(row=9, column=0, padx=10, pady=5, sticky="ew")

    # win or lose indicator 
    roll1lb = customtkinter.CTkLabel(master=devmenu, text="Roll 1: ")
    roll1lb.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    roll2lb = customtkinter.CTkLabel(master=devmenu, text="Roll 2: ")
    roll2lb.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    roll3lb = customtkinter.CTkLabel(master=devmenu, text="Roll 3: ")
    roll3lb.grid(row=3, column=1, padx=10, pady=5, sticky="ew")


    roll1wl = customtkinter.CTkLabel(master=devmenu, text=roll1, text_color="white")
    roll1wl.grid(row=1, column=2, padx=35, pady=5, sticky="ew")

    roll2wl = customtkinter.CTkLabel(master=devmenu, text=roll2, text_color="white")
    roll2wl.grid(row=2, column=2, padx=35, pady=5, sticky="ew")

    roll3wl = customtkinter.CTkLabel(master=devmenu, text=roll3, text_color="white")
    roll3wl.grid(row=3, column=2, padx=35, pady=5, sticky="ew")



def roll(): # rool dice
    global rollnum
    global roll1
    global roll2
    global roll3

    rollnum = random.randint(1, 6) # chose number to role
    #print(rollnum)

    # used to display whats going on 
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



def lessthen3(): # bet that dice role is less then 3 or equal
    global rollnum
    global cash
    global wroll
    global roll1
    global roll2
    global roll3
    global roll1wl
    global roll2wl
    global roll3wl

    if cash < 10:
        return

    roll()

    cash = cash - 10 
    if rollnum <= 3:
        cash += 20
        
        wroll += 1 # track win/lose
        if wroll > 3:
            wroll = 1 

        if wroll == 1:
            roll1 = "Win"

        if wroll == 2:
            roll2 = "Win"

        if wroll == 3:
            roll3 = "Win"
        if wroll > 3:
            wroll = 0 

    else:
        wroll += 1
        if wroll > 3:
            wroll = 1

        if wroll == 1:
            roll1 = "Lose"

        if wroll == 2:
            roll2 = "Lose"

        if wroll == 3:
            roll3 = "Lose"

    cashla.configure(text=f"Cash: £{cash}")

    if roll1 == "Win":
        roll1wl.configure(text=roll1, text_color="green")
    if roll1 == "Lose":
        roll1wl.configure(text=roll1, text_color="red")

    if roll2 == "Win":
        roll2wl.configure(text=roll1, text_color="green")
    if roll2 == "Lose":
        roll2wl.configure(text=roll1, text_color="red")

    if roll3 == "Win":
        roll3wl.configure(text=roll1, text_color="green")
    if roll3 == "Lose":
        roll3wl.configure(text=roll1, text_color="red")

    

def morethen4(): # bet that dice will be more then 4 or equal
    global rollnum
    global cash
    global wroll
    global roll1
    global roll2
    global roll3
    global roll1wl
    global roll2wl
    global roll3wl

    if cash < 10:
        return

    roll()

    cash = cash - 10 
    if rollnum >= 4:
        cash += 20

        wroll += 1
        if wroll > 3:
            wroll = 1

        if wroll == 1:
            roll1 = "Win"

        if wroll == 2:
            roll2 = "Win"

        if wroll == 3:
            roll3 = "Win"

    else:
        wroll += 1
        if wroll > 3:
            wroll = 1 

        if wroll == 1:
            roll1 = "Lose"

        if wroll == 2:
            roll2 = "Lose"

        if wroll == 3:
            roll3 = "Lose"
    
    cashla.configure(text=f"Cash: £{cash}")

    if roll1 == "Win":
        roll1wl.configure(text=roll1, text_color="green")
    if roll1 == "Lose":
        roll1wl.configure(text=roll1, text_color="red")

    if roll2 == "Win":
        roll2wl.configure(text=roll1, text_color="green")
    if roll2 == "Lose":
        roll2wl.configure(text=roll1, text_color="red")

    if roll3 == "Win":
        roll3wl.configure(text=roll1, text_color="green")
    if roll3 == "Lose":
        roll3wl.configure(text=roll1, text_color="red")

        

    

def issix(): # bet that dixe will land on 6
    global rollnum
    global cash
    global wroll
    global roll1
    global roll2
    global roll3
    global roll1wl
    global roll2wl
    global roll3wl

    if cash < 10:
        return

    roll()

    cash = cash - 10 
    if rollnum == 6:
        cash += 40

        wroll += 1
        if wroll > 3:
            wroll = 1 

        if wroll == 1:
            roll1 = "Win"

        if wroll == 2:
            roll2 = "Win"

        if wroll == 3:
            roll3 = "Win"
        

    else:
        wroll += 1
        if wroll > 3:
            wroll = 1 

        if wroll == 1:
            roll1 = "Lose"

        if wroll == 2:
            roll2 = "Lose"

        if wroll == 3:
            roll3 = "Lose"

    cashla.configure(text=f"Cash: £{cash}")

    if roll1 == "Win":
        roll1wl.configure(text=roll1, text_color="green")
    if roll1 == "Lose":
        roll1wl.configure(text=roll1, text_color="red")

    if roll2 == "Win":
        roll2wl.configure(text=roll1, text_color="green")
    if roll2 == "Lose":
        roll2wl.configure(text=roll1, text_color="red")

    if roll3 == "Win":
        roll3wl.configure(text=roll1, text_color="green")
    if roll3 == "Lose":
        roll3wl.configure(text=roll1, text_color="red")
        

    

def x(): # dev menu first click
    global devx
    devx += 1

def y(): # open devmenu on last button click
    global devx 
    global devy

    if devx == 3:
        devx = 0

        print("Opening Dev Menu!")
        create_toplevel()

    else: # if fail devmenu open set x to 0
        devx = 0



    

root = customtkinter.CTk() # deice game body
root.title("Dice")
root.configure(fg_color='#232528')

font = Font(family="Uni Sans Heavy")

cashla = customtkinter.CTkLabel(master=root, text=f"Cash: £{cash}", text_color="green")
cashla.grid(row=0, column=0)

button0 = customtkinter.CTkButton(master=root, text="Roll!", command=roll, corner_radius=12, bg_color="transparent", fg_color="#006399", hover_color="#003857")
button0.grid(row=0, column=1, padx=7, pady=10)

button1 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131", command=x)
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

button9 = customtkinter.CTkButton(master=root, height=60, width=60, text="", corner_radius=4, bg_color="transparent", fg_color="#616161", hover_color="#313131", command=y)
button9.grid(row=3, column=2, padx=4, pady=7)

gamble0 = customtkinter.CTkButton(master=root, height=40, width=60, text="3 Or Below (10)", corner_radius=4, bg_color="transparent", fg_color="#00803a", hover_color="#004720", command=lessthen3)
gamble0.grid(row=4, column=0, padx=4, pady=7)

gamble1 = customtkinter.CTkButton(master=root, height=40, width=60, text="4 Or above (10)", corner_radius=4, bg_color="transparent", fg_color="#00803a", hover_color="#004720", command=morethen4)
gamble1.grid(row=4, column=1, padx=4, pady=7)

gamble2 = customtkinter.CTkButton(master=root, height=40, width=60, text="Is six (3x return)", corner_radius=4, bg_color="transparent", fg_color="#00803a", hover_color="#004720", command=issix)
gamble2.grid(row=4, column=2, padx=4, pady=7)

root.mainloop()


