import tkinter as tk
import AI_ONE_TIME as AI
from tkinter import font as tkFont
from PIL import Image, ImageTk

def destroy_widget(widget):
    widget.destroy()

def show_exception(message):
    global root
    label = tk.Label(root, text=message, font=("Times New Roman", 20), bg="#F0F0F0")
    label.pack(pady=10)
    root.after(3000, destroy_widget, label)

def buttonclicked():
    global print_response, scrollbar
    print_response.pack_forget()
    scrollbar.pack_forget()
    x = tk.Label(root, text="Listening...", font=("Times New Roman", 20, "italic"), fg="#0066CC", bg="#F0F0F0")
    x.pack(pady=20)
    root.update()
    try:
        AI.Run_program()
        x.pack_forget()
        response_text = AI.response if AI.response is not None else "No response received"
        print_response.config(state=tk.NORMAL)
        print_response.delete(1.0, tk.END)
        print_response.insert(tk.END, response_text)
        print_response.config(state=tk.DISABLED)
        print_response.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    except Exception as e:
        x.pack_forget()
        show_exception("Something went wrong, click the button and speak again")
        print(f"Error: {e}")

def buttoncreate(text, x, y, coms):
    button = tk.Button(root, text=text, height=2, width=15, command=coms, bg="#4CAF50", fg="white",
                       font=("Helvetica", 14, "bold"), relief="raised", bd=5)
    button.place(x=x, y=y)

def quiter():
    quit()

def main():
    global root, print_response, scrollbar
    root = tk.Tk()
    root.geometry("700x700")
    root.title("AI Interaction Interface")

    # Load and set the background image
    bg_image_path = r"C:\Users\User\Desktop\last dinner.jpg"  # Use a raw string or escape backslashes
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((1000, 1000), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    # Create a frame to hold the widgets and make the background semi-transparent
    frame = tk.Frame(root, bg="#F0F0F0", bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.8, anchor="n")

    header_font = tkFont.Font(family="Helvetica", size=24, weight="bold")
    header_label = tk.Label(frame, text="Welcome to my voice control AI: Jesus V2", font=header_font, bg="#F0F0F0", fg="#333333", wraplength=500)
    header_label.pack(pady=20)

    buttoncreate("TALK", 150, 500, buttonclicked)
    buttoncreate("QUIT", 350, 500, quiter)

    # Create a frame for the text widget and scrollbar
    text_frame = tk.Frame(root)
    text_frame.place(x=110, y=230, width=500, height=220)  # Ensure it fits within 230 < y < 450

    # Create a Text widget with a scrollbar
    print_response = tk.Text(text_frame, font=("Times New Roman", 20), wrap="word", bg="#F0F0F0", fg="#333333", state=tk.DISABLED)
    scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=print_response.yview)
    print_response.configure(yscrollcommand=scrollbar.set)

    print_response.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    root.mainloop()

if __name__ == '__main__':
    main()
