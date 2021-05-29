from tkinter import *
from tkinter import messagebox
import json
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)


    print(f"Your password is: {password}")

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:
                    {
                        "email": email,
                        "password": password
                    }}

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Oops", message="dont leave any field empty")
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
        except:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


def search():

    website = website_entry.get()

    try:
        with open("passwords.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("passwords.json", "w") as file:
            messagebox.showerror(title="Search", message="File not yet created")
    else:

        try:
            messagebox.showinfo(title="Search", message=f'Website: {website}\n'
                                                        f'Email Id: {data[website]["email"]}\n'
                                                        f'Password: {data[website]["password"]}')
        except KeyError:
            messagebox.showerror(title="Search", message="Website does not exist")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
window.minsize(width=442, height=262)
logo = PhotoImage(file="password_logo.gif")
canvas = Canvas()
canvas.create_image(221, 131, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "shubhammishra10@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

gen_btn = Button(text="Generate Password", command=generate_password)
gen_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=add)
add_btn.grid(row=4, column=1, columnspan=2)

search_btn = Button(text="Search", command=search)
search_btn.grid(row=1, column=2)


window.mainloop()