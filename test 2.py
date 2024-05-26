import tkinter as tk


class Message(tk.Frame):
    def __init__(self, parent, name, text):
        super().__init__(parent, width=250)
        self.lblName = tk.Label(self, text=name, font=('Arial', '10'))
        self.lblName.grid(row=0, column=0)
        self.lblText = tk.Message(self, text=text, font=('Arial', '14'))
        self.lblText.grid(row=1, column=1)


class MessageFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Add a canvas in that frame
        self.canvas = tk.Canvas(self, bg="yellow")
        self.canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsb.set)

        # Create a frame to contain the buttons
        self.frame_buttons = tk.Frame(self.canvas, bg="blue")
        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor='nw')

        self.messages = []
        self.msgItems = []

    def add_message(self, sender, text):
        self.messages.append({'name': sender, 'text': text})
        self.refresh_msg_list()

    def refresh_msg_list(self):
        if self.msgItems:
            for item in self.msgItems:
                item.destroy()
            self.msgItems = []

        for idx, msg in enumerate(self.messages):
            newItem = Message(self.frame_buttons, msg['name'], msg['text'])
            # newItem = tk.Button(self.frame_buttons, text=task['task'])
            newItem.grid(row=idx, column=0, sticky='news', pady=10)
            self.msgItems.append(newItem)

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        self.frame_buttons.update_idletasks()

        # Resize the canvas frame to fit 5 messages
        first5rows_height = max([task.winfo_height() for task in self.msgItems]) * 5
        item_width = max([task.winfo_width() for task in self.msgItems])
        ##frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
        ##                    height=first5rows_height)
        self.config(height=first5rows_height, width=item_width + self.vsb.winfo_width())

        # Set the canvas scrolling region
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


def add_new_item():
    pass


def add_first_item():
    msg.add_message('SenderName', 'How are you?')
    msg.add_message('SenderName', 'How are you?')
    msg.add_message('SenderName', 'How are you?')
    msg.add_message('SenderName', 'How are you?')
    msg.add_message('SenderName', 'How are you?')


root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root, bg="gray")
frame_main.grid(sticky='news')

# Create a frame for the canvas with non-zero row&column weights
msg = MessageFrame(frame_main)
msg.grid(row=2, column=0, pady=(5, 0), sticky='nw')
msg.grid_rowconfigure(0, weight=1)
msg.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
msg.grid_propagate(False)

root.after_idle(add_first_item)

root.after(2000, add_new_item)

root.mainloop()