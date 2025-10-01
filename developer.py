from tkinter import *
from tkinter import ttk
# from typing_extensions import Self   # Not needed in this context
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import glob
import time

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        #self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1540, height=45)

        # First image
        img1 = Image.open(r"college_images\dev.jpg")
        img1 = img1.resize((1540,720), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=45, width=1540, height=780)

        main_frame = Frame( f_lbl1, bd=2, bg="white")
        main_frame.place(x=1050, y=28, width=500, height=500)

        img_2 = Image.open(r"college_images\harsh.webp")
        img_2 = img_2.resize((200,200), Image.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)
        f_lbl2 = Label(main_frame, image=self.photoimg_2)
        f_lbl2.place(x=300, y=0, width=200, height=200)

        dev_label = Label(main_frame, text="Developer: HARSH", font=("times new roman", 15, "bold"), bg="white")
        dev_label.place(x=0,y=35)

        dev_labe2 = Label(main_frame, text="Role: Full-stack Development", font=("times new roman", 15, "bold"), bg="white")
        dev_labe2.place(x=0,y=70)

        dev_labe3 = Label(main_frame, text="Skills: Python, Tkinter, MySQL", font=("times new roman", 15, "bold"), bg="white")
        dev_labe3.place(x=0,y=105)

        img3 = Image.open(r"college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img3 = img3.resize((500,400), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(main_frame, image=self.photoimg3)
        f_lbl3.place(x=0, y=200, width=500, height=400)









if __name__ ==  "__main__":
 root = Tk()
 root.state('zoomed')
 obj = Developer(root)
 root.mainloop()