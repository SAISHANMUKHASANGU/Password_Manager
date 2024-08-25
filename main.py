from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    global password_entry
    password_entry.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(6,9)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    li=[]
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    li=password_letters+password_numbers+password_symbols

    random.shuffle(li)

    password="".join(li)
    password_entry.insert(END,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(password)==0 or len(website)==0 or len(email)==0:
        messagebox.showinfo(title=website,message="Don't leave any fields empty")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"these are the entered details:\n Email:{email}\n Password:{password}")

        if is_ok:
            with open(file="Stored_Passwords.txt",mode="a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=200)
image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)


website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2 )
email_entry.insert(END,"SSS@gmail.com")

password_entry=Entry(width=25)
password_entry.grid(row=3,column=1)

generate_button=Button(text="Generate",command=generate)
generate_button.grid(row=3,column=2)

add_button=Button(text="ADD",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()