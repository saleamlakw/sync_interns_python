import random
import smtplib
from tkinter import *
from tkinter import messagebox
#generate the otp
def generate_otp():
    global otp
    otp=""
    for i in range(6):
        otp+=str(random.randint(0,9))
    send_email()
    print(otp)
#email sending
def send_email():
    global email_id ,otp
    email_id = gmail.get()
    try:
        s=smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("Email_Address" , 'password')
        s.sendmail("Email_Address@gmail.com",email_id,otp)
    except:
        messagebox.showerror("error", "no internet connection")
        print()
def verify():
    global otp,email_id
    if verfication.get()==otp and gmail.get()==email_id  :
        print("welcome")
        screen=Tk()
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.configure(bg="white")
        Label(screen,text="Hello everyone!",bg="#fff",font=('Calibri(body)',50,'bold')).pack(expand=True)
        root.destroy()
        screen.mainloop()
    elif verfication.get()!=otp and gmail.get()!=email_id :
        messagebox.showerror("Invalid","Invalid code and gmail adress")
    elif verfication.get()!=otp and gmail.get()==email_id :
        messagebox.showerror("Invalid", "Invalid code")
    elif verfication.get() == otp and gmail.get()!=email_id :
        messagebox.showerror("Invalid", "Invalid gmail adress")
#Gui
root= Tk()
root.title('login')
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)
img=PhotoImage(file=r"C:\Users\user.DESKTOP-OMQ89VA\Desktop\syncintern\otp\login.png")
Label(root,image=img,bg="white").place(x=50,y=50)
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)
heading=Label(frame,text="Otp verification",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=60,y=5)
def on_enter(e):
    gmail.delete(0,"end")
def on_leave(e):
    name=gmail.get()
    if name=="":
        gmail.insert(0,"Gmail account")
def on_enter2(e):
    verfication.delete(0,"end")
def on_leave2(e):
    name=verfication.get()
    if name=="":
        verfication.insert(0,"verfication code")
gmail = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
gmail.place(x=30,y=80)
gmail.insert(0,"Gmail account")
gmail.bind("<FocusIn>",on_enter)
gmail.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)
Button(frame,width=39,pady=7,text="send otp",bg="#57a1f8",border=0,command=generate_otp).place(x=35,y=134)
verfication = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
verfication.place(x=30,y=177)
verfication.insert(0,"verfication code")
verfication.bind("<FocusIn>",on_enter2)
verfication.bind("<FocusOut>",on_leave2)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=204)
Button(frame,width=39,pady=7,text="Verify",bg="#57a1f8",border=0,command=verify).place(x=35,y=231)
root.mainloop()
