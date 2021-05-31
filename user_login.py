from tkinter import *

root = Tk()

username = str(input()) #that's the given username
password = str(input()) #that's the given password

#username entry
username_entry = Entry(root)
username_entry.pack()

#password entry
password_entry = Entry(root, show='*')
password_entry.pack()

def trylogin(): #this method is called when the button is pressed
    #to get what's written inside the entries, I use get()
    #check if both username and password in the entries are same of the given ones
    if username == username_entry.get() and password == password_entry.get():
        print("Correct")
    else:
        print("Wrong")

#when you press this button, trylogin is called
button = Button(root, text="check", command = trylogin) 
button.pack()

#App starter
root.mainloop()
