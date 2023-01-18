from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]


    random.shuffle(password_list)

    generated_password = ""
    for char in password_list:
        generated_password += char
    if len(input_password.get()) == 0:    
        input_password.insert(END,f"{generated_password}")  
        pyperclip.copy(generated_password)
    else :
        input_password.delete(0,END)
        input_password.insert(END,f"{generated_password}")
        pyperclip.copy(generated_password)

# print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {website: {
        "email": email,
        "password":password
    }}

    if len(website) == 0 or len(password) == 0: 
        messagebox.showinfo(title="OOPS",message="Please don't leave any fields empty")
        # messagebox.showinfo(title="Password Manager",message="Kya bhai kaisa hai tu?")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nAre you sure you want to save it?")
        if is_ok:
            try:
                with open("password.json",mode="r") as password_file:
                    # password_file.write(f"Website: {website} \nEmail/Username: {email} \nPassword: {password}\n\n")
                    data  = json.load(password_file) #IT WILL READ THE DATA
            except FileNotFoundError:     
                with open("password.json",mode="w") as password_file:
                    json.dump(new_data,password_file,indent=4)   
            else:        
                data.update(new_data) #IT WILL UPDATE THE DATA
                with open("password.json",mode="w") as password_file:
                    json.dump(data,password_file,indent=4)
            finally:
                input_website.delete(0,END)    
                input_password.delete(0,END)    

        else:
            input_website.delete(0,END)    
            input_password.delete(0,END)
            input_website.focus()

def find_password():
    website = input_website.get()
    try:
        with open("password.json") as password_file:
            data = json.load(password_file)
    except FileNotFoundError:    
        messagebox.showinfo(title="Error",message="No Data File Found.You need to first Add the Data.")
    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
                messagebox.showinfo(title="Error",message=f"No details for {website} exists.")   


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50,pady=50,bg="black")

canvas = Canvas(height=200,width=200,bg="black",highlightthickness=0)
lock = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock)
canvas.grid(column=1,row=0)

website_label = Label(text="Website :",bg="black",fg="#EB6746",font=("san sarif",11,"bold"))
website_label.grid(column=0,row=1)


input_website = Entry(width=30,font=("san sarif",12))
input_website.grid(column=1,row=1,pady=10,padx=7)
input_website.focus()

search_btn = Button(width=16,text="Search",bg="black",fg="#EB6746",font=("san sarif",9,"bold"),command=find_password)
search_btn.grid(column=2,row=1)

email_username_label = Label(text="Email/Username :",bg="black",fg="#EB6746",font=("san sarif",11,"bold"))
email_username_label.grid(column=0,row=2)

input_email = Entry(width=45,font=("san sarif",12))
input_email.insert(END,"jitbherwani92@gmail.com")
input_email.grid(column=1,columnspan=2,row=2,pady=10)

password = Label(text="Password :",bg="black",fg="#EB6746",font=("san sarif",11,"bold"))
password.grid(column=0,row=3)

input_password = Entry(width=30,font=("san sarif",12))
input_password.grid(column=1,row=3,pady=10,padx=7)

generate_password_btn = Button(text="Generate Password",bg="black",fg="#EB6746",font=("san sarif",9,"bold"),command=generate_password)
generate_password_btn.grid(column=2,row=3)

add_btn = Button(width=51,text="Add",bg="black",fg="#EB6746",font=("san sarif",10,"bold"),command=save)
add_btn.grid(column=1,columnspan=2,row=4,pady=10)


window.mainloop()

