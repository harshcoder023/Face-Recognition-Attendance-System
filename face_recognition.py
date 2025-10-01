from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime
from time import strftime
import mysql.connector
import cv2
import os
import numpy as np
import csv
# Clear all contents of the attendance CSV
import os
from datetime import datetime



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.marked_ids = set()  # To keep track of marked IDs in the current session
        self.root.state('zoomed')
        #self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

         # First image

        img1 = Image.open(r"college_images\face_detector1.jpg")
        img1 = img1.resize((650,700), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=45, width=650, height=700)

        # Second image

        img2 = Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img2 = img2.resize((950,700), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=650, y=45, width=950, height=700)

        # face recognition button
        b1_1 = Button(f_lbl2, text="FACE DETECTOR",command=self.face_recognition,  cursor="hand2", font=("times new roman", 15, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=370, y=620, width=200, height=40)

  



    def mark_attendance(self, id, roll, name, department,attendance_status):
        if id in self.marked_ids:
            return  # Already marked for this session, skip

        self.marked_ids.add(id)  # Mark this ID so we don't do it again

        now = datetime.now()
        date_string = now.strftime("%Y-%m-%d")
        time_string = now.strftime("%H:%M:%S")

        filename = f"attendance_{date_string}.csv"

        # Check if this person is already marked today (in the file)
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row and row[0] == str(id):
                        return  # Already marked today
        except FileNotFoundError:
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([id, name, roll, department, date_string, time_string,attendance_status]) # File doesn't exist yet — first attendance today
                return

        # Append the attendance record
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id, name, roll, department, date_string, time_string,attendance_status])




    def face_recognition(self):
             def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                coord = []

                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                    id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                    confidence = int((100 * (1 - predict / 300)))

                    conn = mysql.connector.connect(host="localhost", username="root", password="workbench@1234", database="face_recog_system")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select Name from student where Student_id=" + str(id))
                    n = my_cursor.fetchone()
                    n = "+".join(n)

                    my_cursor.execute("select Roll from student where Student_id=" + str(id))
                    r = my_cursor.fetchone()
                    r = "+".join(r)

                    my_cursor.execute("select Dep from student where Student_id=" + str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d)

                    if confidence > 77:
                        cv2.putText(img, f"ID:{id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Dep:{d}", (x, y -5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_attendance(id, r, n, d,"present")
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)  
                    coord.append((x, y, w, h))
                return coord
             def recognize(img, clf, faceCascade):
                coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
                return img
             faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
             clf = cv2.face.LBPHFaceRecognizer_create()
             clf.read("classifier.xml")
             video_cap = cv2.VideoCapture(0)
             while True:
                ret, img = video_cap.read()
                if not ret:
                 break
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome To Face Recognition", img)

                if cv2.waitKey(1) == 13 or cv2.getWindowProperty("Welcome To Face Recognition", cv2.WND_PROP_VISIBLE) < 1:  # 13 is the Enter Key
                    break
             video_cap.release()
             cv2.destroyAllWindows()
            
        
          

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()