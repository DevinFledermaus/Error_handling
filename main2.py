from tkinter import *
from tkinter import messagebox

# Creating the window
root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Exception Handling")
root.config(bg="blue")


# Defining Functions
# Defining the Check Button
def check():
    try:
        # For when requirements are met
        if float(ent1.get()) >= 3000:
            messagebox.showinfo("Status Feedback", "Congratulations, You qualify for the Malaysia trip.")
        # For when requirements are not met
        else:
            messagebox.showinfo("Status Feedback", "Sorry, Please deposit more funds for this excursion.")
        # For when inputs are invalid
    except ValueError as x:
        ent1.config(state="normal")
        ent1.delete(0, END)

        messagebox.showerror("ERROR", "Please enter your amount(digits).")


# Defining the Clear Button
def clearing():
    ent1.delete(0, END)


# Defining the Exit Button
def button_Exit():
    msg_box = messagebox.askquestion("Terminating Program", "Are you sure you want to close this program?", icon="warning")
    if msg_box == "yes":
        root.destroy()


# Label
lbl1 = Label(root, text="Please enter amount in your account", bg="blue")
lbl1['font'] = "Sans-serif", 20
lbl1.place(x=100, y=50)


# Entry
ent1 = Entry(root, width=40)
ent1.place(x=180, y=120)


# Button
btn = Button(root, text="Check Qualification", bg="green", borderwidth=5, command=check)
btn.place(x=260, y=180)
extbtn = Button(root, text="Exit", bg="red", borderwidth=5, command=button_Exit)
extbtn.place(x=130, y=300)
clrbtn = Button(root, text="Clear", bg="yellow", borderwidth=5, command=clearing)
clrbtn.place(x=480, y=300)


# Run Program
root.mainloop()
