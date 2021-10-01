from tkinter import *
from PIL import ImageTk,Image , ImageFont, ImageDraw
from tkinter import ttk
import datetime
import smtplib
import pyttsx3
import speech_recognition as sr
import os
import wikipedia as wikipedia
import webbrowser
import random
import requests
import time
import voice
from tkinter import messagebox
from itertools import count, cycle
import tkinter as tk



root = Tk()
#defining title
root.title("G16 VOICE ASSISTANT")


# create label
myLabel1= Label(root , text = "Welcome to G16 Voice Assistant !", font =("",14,'bold'))
myLabel1.pack()

#define image
bg = ImageTk.PhotoImage(file="narendra.jpg")
#creating a canvas
my_canvas = Canvas(root,width=800,height=500)
my_canvas.pack(fill="both",expand=True)
#set image in canvas
my_canvas.create_image(0,0,image=bg,anchor="nw")


def resizer(e):
    global  bg1,resized_bg , new_bg
    #Open the image
    bg1=Image.open("narendra.jpg")
    #Resize the image
    resized_bg = bg1.resize((e.width , e.height), Image.ANTIALIAS)
    #Define the image
    new_bg = ImageTk.PhotoImage(resized_bg)
    #Add it back to canvas
    my_canvas.create_image(0, 0, image=new_bg, anchor="nw")


def open1():

    splash_root1 = Tk()

    # Adjust size
    splash_root1.geometry("250x50")
    splash_root1.title("Processing.......")

    my_progress1 = ttk.Progressbar(splash_root1, orient=HORIZONTAL, length=200, mode='determinate')
    my_progress1.pack(pady=20)
    my_progress1.start(5)

    def main1():
        # destory splash window
        splash_root1.destroy()
        root = Tk()


        class Window(Frame):
            def __init__(self, master=None):

                super().__init__(master)
                self.master = master
                self.pack()
                master.title("G16 voice assistant")

                A = Label(master, text="Here to help you!(Say goodbye  to stop or close the window)")
                A.pack(side="top")


                Button(master, text="Tap to start!", width=100, relief="groove", command=self.Processo_r).pack(
                    side="bottom")

            def Processo_r(self):
                voice.Mainclass()

        # instance of the class
        app = Window(root)
        root.geometry("700x300")
        # Runs the application until we close
        #root.mainloop()
    splash_root1.after(3000, main1)

    # Execute tkinter
    mainloop()


def open():
    splash_root = Tk()

    # Adjust size
    splash_root.geometry("250x50")
    splash_root.title("Processing....")

    my_progress = ttk.Progressbar(splash_root, orient=HORIZONTAL, length=200, mode='determinate')
    my_progress.pack(pady=20)

    my_progress.start(5)

    # main window function
    def main():

        # destory splash window
        splash_root.destroy()

        # Execute tkinter
        root = Tk()

        # Adjust size
        root.geometry("400x400")
        root.title("G16 voice assistant")

        my_label = Label(root , text= "Choose Your language :-",font=18)
        my_label.pack()



        #creating radiobutton
        i = IntVar()

        r1 = Radiobutton(root,text="English", value=0,variable = i)
        #r2 = Radiobutton(root,text="Hindi", value=1, variable=i)
        r1.pack()
        #r2.pack()

        my_button = Button(root , text="Next" ,command =open1)
        my_button.pack()
        my_button.place(x=300,y=300,width=40,height=35)

    # Set Interval
    splash_root.after(3000, main)

    # Execute tkinter
    mainloop()

def login():
    def ok():
        uname = e1.get()
        password = e2.get()

        if (uname == "" and password == ""):
            messagebox.showinfo(",Blank not allowed")

        elif (uname == "Admin" and password == "123"):
            messagebox.showinfo("", "Login success")

        else:
            messagebox.showinfo("", "Incorrect username and password")

    root = Tk()
    root.title("Login")
    root.geometry("400x300")
    global e1
    global e2

    Label(root, text="Username").place(x=10, y=10)
    Label(root, text="Password").place(x=10, y=40)

    e1 = Entry(root)
    e1.place(x=140, y=10)

    e2 = Entry(root)
    e2.place(x=140, y=48)
    e2.config(show="*")

    Button(root, text="Login", command=ok, height=3, width=13).place(x=10, y=188)
    root.mainloop()


myButton1 = Button(root ,text = "Start", command=open)
myButton1.pack()
myButton1.place(x=700,y=720,width=40,height=35)

button_quit=Button(root, text="Exit", command = root.quit)
button_quit.pack()
button_quit.place(x=850,y=720,width=40,height=35)

root.bind('<Configure>', resizer)
root.mainloop()