
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



