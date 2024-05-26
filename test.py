
# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a function
def myClick():
   greet= "Hello " + name.get()
   label=Label(win, text=greet, font=('Arial', 12))
   label.pack(pady=10)

# Create an entry widget
name=Entry(win, width=50, font=('Arial 24'))
name.pack(padx=10, pady=10)

# Create a button
button=Button(win, text="Submit", command=myClick)
button.pack(pady=10)

win.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
from tkinter import ttk
import tkinter as tk


# from tkinter.ttk import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def button_clicked(self):
        self.label.config(text="greet", font=('Arial', 100), fg="#000000")
        self.label.pack(padx=10, pady=10)
        self.label.place(relx=0.26, rely=0.03)
        print("Button clicked!")
        print("lable text", self.label.cget("text"))

    def create_widgets(self):
        #self.label = tk.Label(self)
        self.label = tk.Label(root, text="Hello, World!", font=("Arial", 24))
        self.label.pack(pady=20)
        self.button = tk.Button(self)
        self.button["text"] = "Click me"
        self.button["command"] = self.button_clicked
        # self.button.place(relx=0.26, rely=0.03)
        #self.label.config(text="greet", font=('Arial', 100), fg="#000000")
        #self.label.pack(padx=20, pady=20)
        self.button.pack()


root = tk.Tk()
root.geometry("700x350")
app = Application(master=root)
# Create a label widget with the desired text

root.update()
app.mainloop()

'''
import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.geometry("500x350")


def button():
    print("test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

button1 = customtkinter.CTkButton(master=frame, text="Talk", command=button)
button1.pack(pady=12, padx=10)


root.mainloop()
'''


