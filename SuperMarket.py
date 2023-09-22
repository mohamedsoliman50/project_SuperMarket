from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import messagebox
import webbrowser 
import os 
import sys
shop = Tk()
shop.geometry("800x450+280+50")
shop.resizable(False,False)
shop.title("SuperMarket")
shop.iconbitmap("C:\\Users\\HP\\Downloads\\project shop\\logo.ico")
title = Label(shop,text ="Super Market System",fg ="gold",bg ="black",font =("tajawal",18,"bold"))
title.pack(fill = X)
u1 ="https://www.facebook.com/mohamedmohamedsab3?mibextid=ZbWKwL"
u2 ="https://instagram.com/mohamedmohamedsab3?utm_source=qr&igshid=MzNlNGNkZWQ4Mg%3D%3D "
u3 = "https://www.linkedin.com/in/mohamed-soliman-649061256/"
u4 = "https://github.com/mohamedsoliman50"

def open1():
    webbrowser.open_new(u1)
def open2():
    webbrowser.open_new(u2)
def open3():
    webbrowser.open_new(u3)
def open4():
    webbrowser.open_new(u4)
def about():
    messagebox.showinfo("About","A supermarket that was established in 1995 and contains products")
def log():
    user = En1.get()
    passw = En2.get()
    if user =="admin" and passw =="5400" :
        messagebox.showinfo("Welcome","تم تسجيل الدخول بنجاح")
        
    else :
        messagebox.showinfo("Error","sorry,incorrect information username or password !!")

F1 = Frame(shop,width = 230 ,height =450,bg="#0B2F3A" )
F1.place(x=570,y=35)
image0= Image.open("C:\\Users\\HP\\Downloads\\project shop\\LIDL.png")
photo0 = ImageTk.PhotoImage(image0)
imo0 =tk.Label(shop,image=photo0)
imo0.place(x=650,y=76,width=50,height=50)

Title1 = Label(F1,text ="SuperMarket",bg ="#0B2F3A",fg="white",font = ("tajawal",14,"bold"))
Title1.place(x=42,y=11)

Title2 = Label(F1,text ="وسائل الاتصال بنا",bg ="#0B2F3A",fg="white",font = ("tajawal",14,"bold"))
Title2.place(x=57,y=92)

B1 = Button(F1,text ="Facebook",width = 26,fg ="black",bg ="#DBA901",font =("tajawal",14,"bold"),command=open1)
B1.place(x=1,y=125)

B2 = Button(F1,text ="Instagram",width = 26,fg ="black",bg ="#DBA901",font =("tajawal",14,"bold"),command=open2)
B2.place(x=1,y=170)

B3 = Button(F1,text ="About",width = 26,fg ="black",bg ="#DBA901",font =("tajawal",14,"bold"),command=about)
B3.place(x=1,y=217)

B4 = Button(F1,text ="Linkedin",width = 26,fg ="black",bg ="#DBA901",font =("tajawal",14,"bold"),command=open3)
B4.place(x=1,y=263)

B5 = Button(F1,text ="GitHub",width = 26,fg ="black",bg ="#DBA901",font =("tajawal",14,"bold"),command=open4)
B5.place(x=1,y=310)

B6 = Button(F1,text ="اغلاق البرنامج",width = 26,fg ="black",bg ="#DBA901",font =("tajawal",14,"bold"),command=quit)
B6.place(x=1,y=355)

image = Image.open("C:\\Users\\HP\\OneDrive\\سطح المكتب\\shop.ico")
photo = ImageTk.PhotoImage(image)
imo =tk.Label(shop,image=photo)
imo.place(x=125,y=120,width=270,height=220)

F2 = Frame(shop,width =570 ,height =135 ,bg ="#0B2F3A")
F2.place(x=0 ,y =335)
image1= Image.open("C:\\Users\\HP\\Downloads\\project shop\\login.png")
photo1 = ImageTk.PhotoImage(image1)
imo1 =tk.Label(shop,image=photo1)
imo1.place(x=450,y=340,width=100,height=100)
L1 = Label(F2,text ="اسم المستخدم",fg="gold",bg="#0B2F3A",font=("tajawal",14))
L1.place(x=350,y=23)
L2 = Label(F2,text ="كلمه المرور",fg="gold",bg="#0B2F3A",font=("tajawal",14))
L2.place(x=355,y=58)

En1 =Entry(F2,font =("tajawal",14),justify= "center")
En1.place(x=117,y=25)
En2 =Entry(F2,font =("tajawal",14),justify="center",show="*")
En2.place(x=117,y=62)

B = Button(F2,text = "تسجيل الدخول ",bg="#DBA901",font = ("tajawal",12),width=10,height=3,command=log)
B.place(x=10,y=20)


shop.mainloop()
