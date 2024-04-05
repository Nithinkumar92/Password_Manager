from tkinter import *
from  tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def mange():
    website=input1.get()
    email=input2.get()
    password=input3.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }

    }

    # messagebox.showinfo(title="conformaiton",message="is it ok")
    input1.delete(0, END)
    input3.delete(0, END)
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message=f"dont leave any field empty.")
    else:
        answer = messagebox.askokcancel(title="details conformation",
                                        message=f"these are the details: \n website:{website}\n email:{email}\n password: {password}\n you want to save?")
        if answer==TRUE:
            try:
                file=open("data.json","r")
                # json.dump(new_data,file,indent=4)
                data_n = json.load(file)

                data_n.update(new_data)

            except FileNotFoundError:
                file = open("data.json", "w")
                json.dump(new_data,file,indent=4)

            else:
                 file=open("data.json","w")

                 json.dump(data_n,file,indent=4)
                 print(type(data_n))


            # file.writelines(f"{website} |{email} | {password}\n")


# ---------------------------- SAVE PASSWORD ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_lett = [random.choice(letters) for i in range(nr_letters)]

password_num= [random.choice(numbers) for i in range(nr_numbers)]

password_sym= [random.choice(symbols) for i in range(nr_symbols)]

password_list=password_lett+password_sym+password_num
random.shuffle(password_list)

password = "".join(password_list)
def generate():
    input3.insert(0,password)
    pyperclip.copy(password)

def retrive():
    website = input1.get()
    try:
        file1=open("data.json","r")
        value=json.load(file1)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="no data file found")
    else:
        if website in value:
            pas=value[website]["password"]
            email=value[website]["email"]
            input3.insert(0,pas)
            messagebox.showinfo(title=website,message=f"email is:{email}\n password is :{pas}")
        else:
            messagebox.showinfo(title="Error", message=f"no values for the given value:{website}")



# print(f"Your password is: {pyperclip.paste()}")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
bg_color="black"
bg_color2="white"

window.title("password manager")
window.config(pady=150,padx=150,bg=bg_color)
canvas=Canvas(width=200,height=200,highlightthickness=0,bg=bg_color)
photo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=1)
# labels
label1=Label(text="website:",fg=bg_color2,bg=bg_color,highlightthickness=0)
label1.grid(row=2,column=0)
label2=Label(text="Email/Username:",fg=bg_color2,bg=bg_color,highlightthickness=0)
label2.grid(row=3,column=0)
label3=Label(text="pasword:",fg=bg_color2,bg=bg_color,highlightthickness=0)
label3.grid(row=4,column=0)
#inputs

input1=Entry(width=21,highlightthickness=0)
input1.grid(row=2,column=1)
input1.focus()
input2=Entry(width=38,highlightthickness=0)
input2.grid(row=3,column=1,columnspan=2)
input2.insert(0,"nithinkumar@gmail.com")
input3=Entry(width=21,highlightthickness=0)
input3.grid(row=4,column=1)
button=Button(text="Generate passward",highlightthickness=0,command=generate,width=14)
button.grid(row=4,column=2)
add=Button(text="add",width=35,highlightthickness=0,command=mange)
add.grid(row=5,column=1,columnspan=2)
search=Button(text="search",width=14,highlightthickness=0,command=retrive)
search.grid(row=2,column=2)
window.mainloop()