from tkinter import *  
  
top = Tk()  
  
top.geometry("400x250")  
  
menubutton = Menubutton(top, text = "Select your country", relief = FLAT)  
  
menubutton.grid()  
  
menubutton.menu = Menu(menubutton)  
  
menubutton["menu"]=menubutton.menu  
  
menubutton.menu.add_checkbutton(label = "INDIA", variable=IntVar())  
  
menubutton.menu.add_checkbutton(label = "USA", variable = IntVar())

menubutton.menu.add_checkbutton(label = "UK", variable = IntVar())

menubutton.menu.add_checkbutton(label = "CANADA", variable = IntVar())

menubutton.menu.add_checkbutton(label = "AUSTRALIA", variable = IntVar())

menubutton.menu.add_checkbutton(label = "CANADA", variable = IntVar())

menubutton.menu.add_checkbutton(label = "RUSSIA", variable = IntVar())

menubutton.menu.add_checkbutton(label = "JAPAN", variable = IntVar())

menubutton.menu.add_checkbutton(label = "EUROPE", variable = IntVar())
  
menubutton.pack()  
  
top.mainloop()  
