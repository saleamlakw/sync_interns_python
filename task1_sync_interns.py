# import libraries
from tkinter import *
from tkinter.ttk import Combobox
import datetime
import time
from pygame import mixer
from PIL import ImageTk,Image
from threading import Thread
control = 1
def alarm():
    alarm_timer = f"{c_hour.get()}:{c_min.get()}:{c_sec.get()}"
    print(alarm_timer)
    while control:

        time.sleep(1)
        current_time = datetime.datetime.now()
        time_now = current_time.strftime("%H:%M:%S")
        print(time_now)
        day = current_time.strftime("%d:%m:%Y")
        if control==1:
            if (time_now == alarm_timer):
                music()
                break
def music():
    mixer.music.load("mixkit-retro-game-emergency-alarm-1000.wav")
    mixer.music.play()
def activate_alarm():
    t=Thread(target=alarm)
    t.start()
def deactivate():
    mixer.music.stop()
    control=0
mixer.init()
#colors
bg_color= "#ffffff"
frame_color="#566FC6" #blue
col="#000000"
#GUI
clock = Tk()
clock.title("Alarm clock")
clock.geometry("400x200")
clock.configure(bg=bg_color)
frame_line=Frame(clock,height=5,width=450,bg=frame_color)
frame_line.grid(row=0,column=0)
frame_body=Frame(clock,height=300,width=450,bg=bg_color)
frame_body.grid(row=1,column=0)
img=Image.open("icons8-alarm-clock-100.png")
img.resize((180,180))
img=ImageTk.PhotoImage(img)
app_image=Label(frame_body,height=180,image=img,bg=bg_color)
app_image.place(x=10,y=10)
name=Label(frame_body,text="Alarm",height=1,font=('Ivy 18 bold'),bg=bg_color)
name.place(x=150,y=10)
hour=Label(frame_body,text="hour",height=1,font=('Ivy 7 bold'),bg=bg_color,fg=frame_color)
hour.place(x=152,y=40)
c_hour =Combobox(frame_body,width=2,font=("arial 15"))
c_hour["values"]=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24")
c_hour.place(x=155,y=58)
c_hour.current(00)
min=Label(frame_body,text="minute",height=1,font=('Ivy 7 bold'),bg=bg_color,fg=frame_color)
min.place(x=202,y=40)
c_min =Combobox(frame_body,width=2,font=("arial 15"))
c_min["values"]=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
c_min.place(x=205,y=58)
c_min.current(00)
sec=Label(frame_body,text="second",height=1,font=('Ivy 7 bold'),bg=bg_color,fg=frame_color)
sec.place(x=252,y=40)
c_sec =Combobox(frame_body,width=2,font=("arial 15"))
c_sec["values"]=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
c_sec.place(x=255,y=58)
c_sec.current(00)


selected= IntVar()
activate=Radiobutton(frame_body,font="arial 10",value=1,text="Activate",bg=bg_color,command=activate_alarm)
activate.place(x=152,y=95)

deactivate=Radiobutton(frame_body,font="arial 10",value=0,text="deactivate",bg=bg_color,command=deactivate)
deactivate.place(x=230,y=95)
clock.mainloop()




