from tkinter import *
from tkinter import messagebox

# Creating the window
root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Username And Password")
root.config(bg="blue")


# Possible Logins
possible_users = {'Devin': 'Fledermaus', 'Paul': 'Walker', 'Skyline': 'GTR', 'Toyota': 'Supra'}  # dictionary of corresponding user name and passwords


# StringVars
the_user = StringVar()
the_pass = StringVar()


# Defining my functions
# Defining the verify button
def verify(main2):
    forget_login_window()
    next_window(main2)
    root.destroy()
    import main2


def calculate():
    login_attempt = the_user.get()
    try:
        if possible_users[login_attempt] == the_pass.get():
            verify(login_attempt)
        else:
            bad_pass.place(x=200, y=250)
    except ValueError as ex:
        bad_pass.place(x=200, y=250)


# Defining the exit button
def button_Exit():
    msg_box = messagebox.askquestion("Terminating Program", "Are you sure you want to close this program?", icon="warning")
    if msg_box == "yes":
        root.destroy()


# Defining the clear button
def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)


# Removing all the login windows items
def forget_login_window():
    lbl1.place_forget()
    lbl2.place_forget()
    lbl3.place_forget()
    bad_pass.place_forget()
    ent1.place_forget()
    ent2.place_forget()
    verbtn.place_forget()
    clrbtn.place_forget()
    extbtn.place_forget()


def next_window(main2):
    root.title(main2)


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
bad_pass = Label(root, text="Incorrect Username or Password", bg="blue")


# Entries
ent1 = Entry(root, width=30, textvariable=the_user)
ent1.place(x=220, y=150)
ent2 = Entry(root, width=30, show='*', textvariable=the_pass)
ent2.place(x=220, y=250)


# Buttons
verbtn = Button(root, text="Login", width=10, bg="green", command=calculate, borderwidth=5)
verbtn.place(x=300, y=350)
clrbtn = Button(root, text="Clear", width=10, bg="yellow", command=clear, borderwidth=5)
clrbtn.place(x=50, y=350)
extbtn = Button(root, text="Exit", width=10, bg="red", command=button_Exit, borderwidth=5)
extbtn.place(x=550, y=350)


# Run Program
root.mainloop()
