from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import re

class Train:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        #self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # First image
        img1 = Image.open(r"college_images\facialrecognition.png")
        img1 = img1.resize((1530,250), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=47, width=1530, height=250)

        img2 = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        img2 = img2.resize((1530,660), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=0, y=300, width=1530, height=550)


        # train button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="blue", fg="white")
        b1_1.place(x=0, y=300, width=1530, height=60)
   


    def extract_id(self, filename):
        try:
            parts = filename.split('.')
            return int(parts[1])  # e.g., user.1.23.jpg → ID = 1
        except (IndexError, ValueError):
            return None



    def train_classifier(self):
        data_dir = "data"
        trained_images_file = "trained_images.txt"

        trained_images = set()
        if os.path.exists(trained_images_file):
            with open(trained_images_file, "r") as f:
                trained_images = set(f.read().splitlines())

        all_files = [file for file in os.listdir(data_dir) if file.lower().endswith((".jpg", ".jpeg", ".png"))]
        new_files = [file for file in all_files if file not in trained_images]

        

        if not new_files:
            messagebox.showinfo("Info", "No new images to train.", parent=self.root)
            return

        faces, ids = [], []
    
        for filename in new_files:
            image_path = os.path.join(data_dir, filename)
            try:
                img = Image.open(image_path).convert('L')
                image_np = np.array(img, 'uint8')
                id = self.extract_id(filename)
                if id is None:
                    continue
                faces.append(image_np)
                ids.append(int(float(id)))  # id is already an int
                
                cv2.imshow("Training", image_np)
                cv2.waitKey(1)
            except Exception as e:
                print(f">> Error with {filename}:", e)


        ids = np.array(ids)

        try:
                clf = cv2.face.LBPHFaceRecognizer_create()
                if os.path.exists("classifier.xml"):
                    clf.read("classifier.xml")
                    clf.update(faces, ids)
                else:
                    clf.train(faces, ids)
                clf.write("classifier.xml")
                

                with open(trained_images_file, "a") as f:
                    for file in new_files:
                        f.write(file + "\n")

                messagebox.showinfo("Result", f"Training completed on {len(new_files)} new images!", parent=self.root)
        except Exception as e:
                messagebox.showerror("Error", f"Training failed: {e}", parent=self.root)

        cv2.destroyAllWindows()
    

if __name__ == "__main__":
    root = Tk()
    root.state('zoomed')
    obj = Train(root)
    root.mainloop()
    