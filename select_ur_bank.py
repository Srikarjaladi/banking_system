from tkinter import *
import sqlite3
  
top = Tk()  
top.title('Select your bank') 
top.geometry("400x250")

bank=StringVar()

def database():
    bank=Selectyourbank.get()
    conn=sqlite3.connect('Bank.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS bank (Select your bank TEXT)')
    cursor.execute('INSERT INTO bank (select your bank) VALUES(?)',(selectyourbank))
    conn.commit()
menubutton = Menubutton(top, text = "Select your bank", relief = FLAT)  
  
menubutton.grid()  
  
menubutton.menu = Menu(menubutton)  
  
menubutton["menu"]=menubutton.menu  
  
menubutton.menu.add_checkbutton(label = "AXIS BANK", variable=IntVar(),command=database)  
  
menubutton.menu.add_checkbutton(label = "ICICI BANK", variable = IntVar(),command=database)

menubutton.menu.add_checkbutton(label = "YES BANK", variable = IntVar(),command=database)

menubutton.menu.add_checkbutton(label = "STATE BANK OF INDIA", variable = IntVar(),command=database)

menubutton.menu.add_checkbutton(label = "HDFC BANK", variable = IntVar(),command=database)

menubutton.menu.add_checkbutton(label = "ANDHRA BANK", variable = IntVar(),command=database)
  
menubutton.pack()  
  
top.mainloop()  
