import tkinter as tk
import AI_ONE_TIME as AI

global root, print_response


def destroy_widget(widget):
    widget.destroy()


def exception():
    global root
    label = tk.Label(root, text="Smth went wrong, click the button and speak again", font=("Times New Roman", 20))
    label.pack()
    root.after(3000, destroy_widget, label)


def buttonclicked():
    global print_response
    print_response.destroy()
    x = tk.Label(root, text="listening...", font=("Times New Roman", 20))
    x.pack()
    x.place(x=50, y=50)
    root.update()
    try:
        AI.Run_program()
        x.destroy()
        print_response = tk.Label(root, text=AI.response, font=("Times New Roman", 20), wraplength=600, justify="center")
        print_response.pack()
        print_response.place(x=50, y=50)
        # root.update()

    except exception():
        exception()


def buttoncreate(text,x,y,coms):
    button = tk.Button(root, text = text,height= 5, width=10, command = coms)
    button.pack()
    button.place(x=x, y=y)


def quiter():
    quit()


def main():
    global root, print_response
    root = tk.Tk()
    root.geometry("700x700")
    buttoncreate("TALK",  200, 500, buttonclicked)
    buttoncreate("QUIT", 400, 500, quiter)
    print_response = tk.Label()
    root.update()
    root.mainloop()


if __name__ == '__main__':
    main()
