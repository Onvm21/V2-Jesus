import tkinter as tk

root = tk.Tk()
root.geometry("700x700")

def destroy_widget(widget):
    widget.destroy()
def exception():
    label = tk.Label(root, text="Smth went wrong, click the button and speak again", font=("Times New Roman", 20))
    label.pack()
    root.after(3000, destroy_widget,label)

def buttonclicked():
    try:
        import AI_ONE_TIME as AI
        AI.Run_program()# i think it just blocks out the rest of the tkinter stuff from working here cuz i imported ai one time.

        print_response = tk.Label(root, text=AI.response, font=("Times New Roman", 20))
        print_response.pack
        #print(print_response)
        #print("hi")
    except:
        exception()




def buttoncreate(text,x,y,coms):
    button = tk.Button(root, text = text,height= 5, width=10, command = coms)
    button.pack()
    button.place(x=x, y=y)

def quiter():
    quit()


buttoncreate("TALK", 200, 500, buttonclicked)
buttoncreate("QUIT",400,500, quiter)
root.update()
root.mainloop()


