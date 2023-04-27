from tkinter import*
from tkinter import messagebox
import pyshorteners
def url_shortner():
    try:
        URL=url.get()
        result=pyshorteners.Shortener().tinyurl.short(URL)
        url_entry.insert(END,result)
    except:
        messagebox.showerror("error","NO intrnet connection")
root=Tk()
root.title("Url Shortner")
root.geometry("800x300")
heading=Label(root,text="URL Shortner",font=("Georgia 25 bold"),fg="purple").pack(pady=10)
frame=Frame(root)
Label(frame,text="Paste URL here",font=("Georgia 15 bold")).pack(side="left")
url=Entry(frame,width=40,font=("Georgia 15 bold"))
url.pack()
frame.pack(pady=10)
Button(root,text="Generate Link",font=("Georgia 15 bold"),command=url_shortner).pack(pady=10)
frame2=Frame(root)
Label(frame2,text="Copy URL",font=("Georgia 15 bold")).pack(side="left")
url_entry=Entry(frame2,width=25,font=("Georgia 15 bold"),fg="blue")
url_entry.pack()
frame2.pack(pady=10)
root.mainloop()
