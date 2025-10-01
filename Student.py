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












class student:
    
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        #self.root.geometry("1530x790+0+0")
        self.root.title("student")

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_search_by = StringVar()
        self.var_search_text = StringVar()

        



         # First image
        img1 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second image
        img2 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\student-portal_1.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third image
        img3 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\AdobeStock_303989091.jpeg")
        img3 = img3.resize((550, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=1000, y=0, width=550, height=130)

         # bg image
        img4 = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\rb.jpg")
        img4 = img4.resize((1530, 790), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=790)
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #frame

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=650)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=715 , height=620)

        img_left = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\work.jpg")
        img_left = img_left.resize((700, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl1 = Label(Left_frame, image=self.photoimg_left)
        f_lbl1.place(x=4, y=0, width=700, height=130)

        #course details

        current_course_frame = LabelFrame(Left_frame , bd=2, bg="white", relief=RIDGE, text="CURRENT COURSE INFORMATION", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=700, height=150)

        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)
        # course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)
        # year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)
        # semester
        sem_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10, sticky=W)
        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly", width=20)
        sem_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10,sticky=W)

        # class student information

        class_student_frame = LabelFrame(Left_frame , bd=2, bg="white", relief=RIDGE, text="CLASS STUDENT INFORMATION", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=290, width=700, height=300)

        # student id
        
        studentId_label = Label(class_student_frame, text="StudentID:", font=("times new roman", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        studentId_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, sticky=W)

        # student name

        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)
        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, sticky=W)

        # class division

        class_div_label = Label(class_student_frame, text="Class Divison:", font=("times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10,pady=5, sticky=W)
        

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div, font=("times new roman", 12, "bold"), state="readonly", width=18)
        div_combo["values"] = ("A", "B", "C", "D")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10,pady=5,sticky=W)

        # roll no

        roll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10,pady=5, sticky=W)
        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, sticky=W) 

        #gender

        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10,pady=5, sticky=W)
        
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Male", "Female", "Other", "Prefer not to say")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10,pady=5,sticky=W)

        # dob

        dob_label = Label(class_student_frame, text="D.O.B:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10,pady=5, sticky=W)
        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, sticky=W)

        # email

        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10,pady=5, sticky=W)
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, sticky=W)

        # phone no

        phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10,pady=5, sticky=W)
        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, sticky=W)

        # address
         
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10,pady=5, sticky=W)
        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, sticky=W)

        # teacher name

        teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10,pady=5, sticky=W)
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, sticky=W)
        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = Radiobutton(class_student_frame,variable=self.var_radio1, text="Take Photo Sample", value="yes")
        radiobtn1.grid(row=5, column=0)
        
        radiobtn2 = Radiobutton(class_student_frame,variable=self.var_radio1, text="No Photo Sample",  value="no")
        radiobtn2.grid(row=5, column=1)

        # button frame

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=2, y=200, width=690, height=40)

          # save, update, delete, reset button

        save_btn = Button(btn_frame, text="Save",command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data ,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame2 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=2, y=235, width=690, height=40)

         # photo sample button

        take_photo_btn = Button(btn_frame2, text="Take Photo Sample",command=self.generate_dataset, width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)
        update_photo_btn = Button(btn_frame2, text="Update Photo Sample",command=self.update_photo, width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)





  

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=715, height=620)

        img_right = Image.open(r"C:\Users\bhard\Desktop\face recoginition system\college_images\rite.jpg")
        img_right = img_right.resize((700, 130), Image.LANCZOS) 
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl1 = Label(Right_frame, image=self.photoimg_right)
        f_lbl1.place(x=4, y=0, width=700, height=130)
        # search system
        search_frame = LabelFrame(Right_frame , bd=2, bg="white", relief=RIDGE, text="SEARCH SYSTEM", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=700, height=70)
        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search_by,font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search_text, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, sticky=W)
        search_btn = Button(search_frame, text="Search",command=self.search_data, width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3,padx=4)
        showAll_btn = Button(search_frame, text="Show All",command=self.load_data_from_db, width=12, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)
        # table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=700, height=350)

        # scroll bar

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div","roll","gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course") 
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DoB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100) 
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1) 
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
                try:
                    conn=mysql.connector.connect(host="localhost", username="root", password="workbench@1234", database="face_recog_system")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        
                
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()

                                                                                                         )) 
                    conn.commit()
                    self.fetch_data()
                    

                    conn.close()
                    messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
                    self.reset_data()
                except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def fetch_data(self,event=""):
        conn=mysql.connector.connect(host="localhost", username="root", password="workbench@001", database="face_recog_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
       
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # update function
    def update_data(self):
        if self.var_dep.get()=="" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if update > 0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="workbench@1234", database="face_recog_system")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s, course=%s, year=%s, semester=%s, name=%s, divison=%s, roll=%s,gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo_sample=%s where student_id=%s",(
                                                                                                            
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_std_id.get()
                                                                                                            ))

                else:
                    if not update:
                        return
                conn.commit()
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                
                self.fetch_data()
                self.reset_data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="workbench@1234", database="face_recog_system")
                    my_cursor=conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


        # generate data set or take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            

            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="workbench@001",
                database="face_recog_system"
            )
            my_cursor = conn.cursor()

            # Update student data
            my_cursor.execute("""
                UPDATE student SET Dep=%s, course=%s, year=%s, semester=%s, name=%s, divison=%s, roll=%s,
                gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photo_sample=%s 
                WHERE student_id=%s
            """, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                "Yes",
                self.var_std_id.get()
            ))
            conn.commit()
            conn.close()

            # Prepare face classifier
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y + h, x:x + w]
                return None

            # Get the student ID
            student_id = self.var_std_id.get()

            # Create data directory if it doesn't exist
            if not os.path.exists("data"):
                os.makedirs("data")

            # Get next available image ID
            def get_start_img_id(student_id):
                files = glob.glob(f"data/user.{student_id}.*.jpg")
                if files:
                    ids = [int(os.path.splitext(f)[0].split('.')[-1]) for f in files]
                    return max(ids) + 1
                else:
                    return 1

            img_id = get_start_img_id(student_id)

            # Start webcam
            cap = cv2.VideoCapture(0)

            while True:
                ret, my_frame = cap.read()
                if not ret:
                    break

                face = face_cropped(my_frame)
                if face is not None:
                    face = cv2.resize(face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)

                    cv2.putText(face, str(img_id), (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                    img_id += 1

                if cv2.waitKey(1) == 13 or img_id > 100:
                    break

            cap.release()
            cv2.destroyAllWindows()

            messagebox.showinfo("Result", "Generating data sets completed!!!", parent=self.root)
            self.fetch_data()

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def update_photo(self):
        try:
            if self.var_std_id.get() == "":
                messagebox.showerror("Error", "Please enter the Student ID first", parent=self.root)
                return

            student_id = self.var_std_id.get()

        # Delete old photos for this student
            for file in glob.glob(f"data/user.{student_id}.*.jpg"):
             os.remove(file)

        # Define face classifier
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        # Define face crop function
            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y + h, x:x + w]
                return None

        # Ensure 'data' directory exists
            if not os.path.exists("data"):
                os.makedirs("data")

            img_id = 1  # Start fresh
            cap = cv2.VideoCapture(0)  # ✅ Corrected

            

            while True:
                ret, my_frame = cap.read()
                if not ret:
                    break

                face = face_cropped(my_frame)
                if face is not None:
                    face = cv2.resize(face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)
                    img_id += 1

                if cv2.waitKey(1) == 13 or img_id > 100:  # Enter key or 5 photos
                 break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Success", f"Photo update completed for ID {student_id}", parent=self.root)
            self.fetch_data()

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    def load_data_from_db(self, event=""):
        

        conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="workbench@001",
        database="face_recog_system"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data = my_cursor.fetchall()
        conn.close()

        
        if data:
            self.mydata = data  # ✅ Needed for searching
           
            self.update_table(data)
        else:
            print(">> No data fetched")

    def update_table(self, data):
        self.student_table.delete(*self.student_table.get_children())
        for row in data:
            self.student_table.insert("", "end", values=row)



    def search_data(self):
        

        search_by = self.var_search_by.get().strip().lower()
        search_text = self.var_search_text.get().strip()

        

        if search_by == "select":
            messagebox.showerror("Error", "Please select a search criteria", parent=self.root)
            
            return

        if not search_text:
            messagebox.showerror("Error", "Please enter search text", parent=self.root)
            
            return

        column_map = {
        "roll no": 7,
        "phone no": 11
        }

        column_index = column_map.get(search_by)
        

        if column_index is None:
            messagebox.showerror("Error", f"Unsupported search criteria: {search_by}", parent=self.root)
            return

        if not hasattr(self, 'mydata') or not self.mydata:
            messagebox.showerror("Error", "No data loaded from database. Click 'Show All' first.", parent=self.root)
            
            return

    # Filter data
        filtered_data = []
        for i, row in enumerate(self.mydata):
            try:
                value = str(row[column_index]).strip().lower()
                
                if value == search_text.lower():
                    
                    filtered_data.append(row)
            except IndexError:
                
                continue

        

        if filtered_data:
            self.update_table(filtered_data)
        else:
            messagebox.showinfo("No Results", "No matching data found", parent=self.root)
            self.update_table([])








if __name__ == "__main__":
    root = Tk()
    root.state('zoomed')
    obj = student(root)
    root.mainloop()
    

