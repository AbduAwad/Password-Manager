import tkinter
from tkinter import * #only imports all classes
from tkinter import messagebox #not a class
import math
import random

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#FFFFFF"
BLACK = "#000000"
FONT_NAME = "arial"

#---------------------------------- PASSWROD GENERATOR ---------------------------------#

def password_generate():
  
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
  
  password_list = []

  password_letters = [random.choice(letters) for i in range(0, random.randint(8, 10))]
  password_symbols = [random.choice(symbols) for i in range(0, random.randint(2, 4))]
  password_numbers = [random.choice(numbers) for i in range(0, random.randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers
  random.shuffle(password_list)

  password = "".join(password_list) #converts password list into one strin
  password_entry.insert(0, password)
  
#--------------------------------- Save Password ---------------------------------------#
#Saves website, username and password into a file called data.txt
def add_button():

 
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()

  if len(website) == 0 or len(email) == 0 or len(password) == 0:
    messagebox.showinfo(title="Entry Error",message="Ensure no entries are empty...")
  else:
    #Message box:
    ok = messagebox.askokcancel(title=website, message=f"Your details: \nEmail: {email}\nPassword: {password}")
  
    if ok:  
      with open("data.txt", mode="a") as file: #Adds to old text a = append
        file.write(f"Website: {website} | Account info - Email: {email}, Pass: {password}\n")
    
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
  
#------------------------------------- UI SETUP ----------------------------------------#
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50,pady=50, bg = WHITE) #Adds window space outside image

#Background with logo image
canvas = tkinter.Canvas(width=200,height=200, bg = WHITE, highlightthickness=0) #highlightthickness sets canvas border
logo = tkinter.PhotoImage(file="logo.png")# Reads image file
canvas.create_image(100, 100,image=logo)
canvas.grid(row=0, column =1)

website_label = Label(text="Website:", fg=BLACK, bg=WHITE, font=(FONT_NAME, 12, "normal"))
website_label.grid(column=0, row=2)

user_label = Label(text="Email/Username:", fg=BLACK, bg=WHITE, font=(FONT_NAME, 12, "normal"))
user_label.grid(column=0, row=3)

pass_label = Label(text="Password:", fg=BLACK, bg=WHITE, font=(FONT_NAME, 12, "normal"))
pass_label.grid(column=0, row=4)

#Entries
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=2, column = 1, columnspan = 2)
website_entry.focus() #Will start cursor on this entry

email_entry = tkinter.Entry(width=35)
email_entry.grid(row=3, column = 1, columnspan = 2)

password_entry = tkinter.Entry(width=17)
password_entry.grid(column=1, row=4)

#Buttons
passwrod_button = Button(text="Generate Password", command=password_generate)
passwrod_button.grid(row=4, column=2)

add_button = Button(text="Add", width = 33, command=add_button)
add_button.grid(row=5, column = 1, columnspan = 2)


window.mainloop() #Loops through and checks if something happenend every miliseconds
#*Can't use loops other than this intkinter GUI's