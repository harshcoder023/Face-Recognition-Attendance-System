from tkinter import *
from tkinter import ttk
# from typing_extensions import Self   # Not needed in this context
from PIL import Image, ImageTk
from Student import student
from tkinter import Toplevel,Label
from tkinter import messagebox
import mysql.connector
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help_desk import Help
import tkinter
from datetime import datetime
from time import strftime





            

        

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        #self.root.geometry("1530x790+0+0")
       

        self.root.title("Face Recognition System")

        # Live Date and Time Label
        

        

        


        # First image
        img1 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\BestFacialRecognition.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second image
        img2 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\facialrecognition.png")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third image
        img3 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\images.jpg")
        img3 = img3.resize((550, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=550, height=130)

        # fourth image
        img4 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\rb.jpg")
        img4 = img4.resize((1530, 790), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=790)
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        self.time_label = Label(bg_img, font=("times new roman", 14, "bold"), bg="white", fg="black")
        self.time_label.place(x=1200, y=50)  # Adjust x/y based on your layout
        self.update_time()


        


        # student button
        img5 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\gettyimages-1022573162.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoimg5,command= self.student_detail, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="STUDENT DETAILS",command=self.student_detail, cursor="hand2" ,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)
        

        # face detector button

        img6 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\face_detector1.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimg6, command=self.face_data,cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="FACE DETECTOR",command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        # attendance button

        img7 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\report.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7,command=self.attendance_data, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="ATTENDANCE",command=self.attendance_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # help desk button

        img8 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\help-desk-customer-care-team-icon-blue-square-button-isolated-reflected-abstract-illustration-89657179.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimg8,command=self.help_data, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="HELP DESK", cursor="hand2",command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # train data button

        img9 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\Train.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoimg9,command=self.train_data, cursor="hand2")
        b1.place(x=200, y=400, width=220, height=220)
        b1_1 = Button(bg_img, text="TRAIN DATA",command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=600, width=220, height=40)

        # photos button

        img10 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\harsh.png")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoimg10,command=self.open_img , cursor="hand2")
        b1.place(x=500, y=400, width=220, height=220)
        b1_1 = Button(bg_img, text="PHOTOS",command=self.open_img , cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=600, width=220, height=40)

        # developer button
        
        img11 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\Team-Management-Software-Development.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img, image=self.photoimg11,command=self.developer_data, cursor="hand2")
        b1.place(x=800, y=400, width=220, height=220)
        b1_1 = Button(bg_img, text="DEVELOPER", cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=600, width=220, height=40)

        # exit button
        
        img12 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\Exit.jpg")
        img12 = img12.resize((220, 220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b1 = Button(bg_img, image=self.photoimg12,command=self.iExit, cursor="hand2")
        b1.place(x=1100, y=400, width=220, height=220)
        b1_1 = Button(bg_img, text="EXIT", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=600, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        
    def update_time(self):
            now = datetime.now()
            time_string = now.strftime("%H:%M:%S %p")
            date_string = now.strftime("%Y-%m-%d")
            self.time_label.config(text=f"Date: {date_string}   Time: {time_string}")
            self.time_label.after(1000, self.update_time)

    


    def student_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

          


         

                    

      



if __name__ ==  "__main__":
    root = Tk()
    root.state('zoomed')
    obj = Face_Recognition_System(root)
    root.mainloop()
