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

class Help:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        #self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1540, height=45)

        # First image
        img1 = Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img1 = img1.resize((1540,720), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=45, width=1540, height=780)

        dev_label = Label(f_lbl1, text="Email: bhardwajharsh129@gmail.com", font=("times new roman", 20, "bold"), bg="white")
        dev_label.place(x=540,y=260)


if __name__ ==  "__main__":
 root = Tk()
 root.state('zoomed')
 obj = Help(root)
 root.mainloop()