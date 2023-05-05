from tkinter import *
# GUI
root = Tk()
root.resizable(False, False)
root.title("Chatbot")
BG_GRAY = "#ABB2B9"
BG_COLOR = "#ffffff"
TEXT_COLOR = "black"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
# Send function
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
    user = e.get().lower()
    if (user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")
    elif (user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")
    elif (user == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! and you")
    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")
    elif (user == "thanks" or user == "thank you" or user == "now its my time"):
        txt.insert(END, "\n" + "Bot -> My pleasure !")
    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
        txt.insert(
            END, "\n" + "Bot -> Why don't scientists trust atoms?\n         Because they make up everything!")
    elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
        txt.insert(END, "\n" + "Bot -> Have a nice day!")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")
    e.delete(0, END)
lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,command=send).grid(row=2, column=1)
root.mainloop()
