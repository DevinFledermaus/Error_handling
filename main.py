from tkinter import *
from tkinter import messagebox

# Creating the window
root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Username And Password")
root.config(bg="blue")


# Defining my functions
# Defining the verify button
# Possible Logins
# dictionary of corresponding user name
def verify():
    possible_users = ["Devin", "Toyota", "Skyline", "Bats"]
    possible_passwords = ["Fleddy", "Supra", "GTR", "Joker"]
    found = False
    for x1 in range(len(possible_users)):
        if ent1.get() == possible_users[x1] and ent2.get() == possible_passwords[x1]:
            found = True
    if found == True:
        messagebox.showinfo("Status", "Access Granted")
        root.destroy()
        import main2
    else:
        messagebox.showinfo("Status", "Access Denied")


# Defining the exit button
def button_Exit():
    msg_box = messagebox.askquestion("Terminating Program", "Are you sure you want to close this program?", icon="warning")
    if msg_box == "yes":
        root.destroy()


# Defining the clear button
def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)


# Labels
lbl1 = Label(root, text="Please Enter Username:", bg="blue")
lbl1['font'] = 'Sans-serif', 13
lbl1.place(x=230, y=100)
lbl2 = Label(root, text="Please Enter Password:", bg="blue")
lbl2['font'] = 'Sans-serif', 13
lbl2.place(x=230, y=200)
lbl3 = Label(root, text="Please enter login details", bg="blue")
lbl3['font'] = 'Sans-serif', 20
lbl3.place(x=190, y=20)


# Entries
ent1 = Entry(root, width=30)
ent1.place(x=220, y=150)
ent2 = Entry(root, width=30, show='*')
ent2.place(x=220, y=250)


# Buttons
verbtn = Button(root, text="Login", width=10, bg="green", command=verify, borderwidth=5)
verbtn.place(x=300, y=350)
clrbtn = Button(root, text="Clear", width=10, bg="yellow", command=clear, borderwidth=5)
clrbtn.place(x=50, y=350)
extbtn = Button(root, text="Exit", width=10, bg="red", command=button_Exit, borderwidth=5)
extbtn.place(x=550, y=350)


# Run Program
root.mainloop()
