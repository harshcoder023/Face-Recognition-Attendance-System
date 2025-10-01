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
from tkinter import filedialog

mydata=[]


class Attendance:
    def __init__(self, root):
        self.root = root
        self.marked_ids = set()  # To keep track of marked IDs in the current session
        self.root.state('zoomed')
        #self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

         # First image  
        img1 = Image.open(r"college_images\smart-attendance.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=800, height=200)

        # Second image
        img2 = Image.open(r"college_images\iStock-182059956_18390_t12.jpg")
        img2 = img2.resize((800, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=800, y=0, width=800, height=200)

         # bg image
        img4 = Image.open(r"C:college_images\rb.jpg")
        img4 = img4.resize((1530, 790), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=790)
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #frame

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=650)

         # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=715 , height=620)

        img_left = Image.open(r"college_images\attendance.jpg")
        img_left = img_left.resize((700, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl1 = Label(Left_frame, image=self.photoimg_left)
        f_lbl1.place(x=4, y=0, width=700, height=130)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white") 
        left_inside_frame.place(x=4,y=135,width=700,height=400)

        #label and entry
        Attendance_Id_label = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 13, "bold"), bg="white")
        Attendance_Id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Attendance_Id_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_id, width=20, font=("times new roman", 13, "bold"))
        Attendance_Id_entry.grid(row=0, column=1, padx=10, sticky=W)

        #roll
        Roll_Id_label = Label(left_inside_frame, text="Roll:", font=("comicsansns", 11, "bold"), bg="white")
        Roll_Id_label.grid(row=0, column=2, padx=4,pady=8, sticky=W)
        Roll_Id_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll, width=22, font=("comicsansns", 11, "bold"))
        Roll_Id_entry.grid(row=0, column=3, pady=8, sticky=W)

        #name
        Name_Id_label = Label(left_inside_frame, text="Name:", font=("comicsansns", 11, "bold"), bg="white")
        Name_Id_label.grid(row=1, column=0)
        Name_Id_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_name, width=22, font=("comicsansns", 11, "bold"))
        Name_Id_entry.grid(row=1, column=1, pady=8)

        #department
        Department_Id_label = Label(left_inside_frame, text="Department:", font=("comicsansns", 11, "bold"), bg="white")
        Department_Id_label.grid(row=1, column=2)
        Department_Id_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep, width=22, font=("comicsansns", 11, "bold"))
        Department_Id_entry.grid(row=1, column=3, pady=8)

        #time
        Time_Id_label = Label(left_inside_frame, text="Time:", font=("comicsansns", 11, "bold"), bg="white")
        Time_Id_label.grid(row=2, column=0)
        Time_Id_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time, width=22, font=("comicsansns", 11, "bold"))
        Time_Id_entry.grid(row=2, column=1, pady=8)

        #date
        Date_Id_label = Label(left_inside_frame, text="Date:", font=("comicsansns", 11, "bold"), bg="white")
        Date_Id_label.grid(row=2, column=2)
        Date_Id_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date, width=22, font=("comicsansns", 11, "bold"))
        Date_Id_entry.grid(row=2, column=3, pady=8)

        #attendance
        atten_label = Label(left_inside_frame, text="Attendance Status:", font=("comocsansns", 11, "bold"), bg="white")
        atten_label.grid(row=3, column=0)
        
        atten_combo = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance, font=("comocsansns", 11, "bold"), state="readonly", width=22)
        atten_combo["values"] = ("Status","Present","Absent")
        atten_combo.current(0)
        atten_combo.grid(row=3, column=1,pady=8)

        # button frame

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=695, height=35 )

          # save, update, delete, reset button

        save_btn = Button(btn_frame, text="Import csv",command=self.importCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        update_btn = Button(btn_frame, text="Export csv",command=self.exportcsv ,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        delete_btn = Button(btn_frame, text="Update", command=self.update_data,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)












        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=715, height=620)

        Table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        Table_frame.place(x=5, y=5, width=700, height=455 )

        #scrollbar

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(Table_frame, columns=("AttendanceID", "Roll", "Name", "Department", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("AttendanceID", text="AttendanceID")
        self.AttendanceReportTable.heading("Roll", text="Roll")
        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Attendance", text="Attendance")
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("AttendanceID", width=100)
        self.AttendanceReportTable.column("Roll", width=100)
        self.AttendanceReportTable.column("Name", width=100)
        self.AttendanceReportTable.column("Department", width=100)
        self.AttendanceReportTable.column("Time", width=100)
        self.AttendanceReportTable.column("Date", width=100)
        self.AttendanceReportTable.column("Attendance", width=100)
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #fetch data

    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )
        with open(fln) as myfile:
            csvreader = csv.reader(myfile,delimiter=",")
            for i in csvreader:
                mydata.append(i)
            self.fetchdata(mydata)

    #export csv
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
            parent=self.root)
            with open(fln,mode="w",newline="")as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

        
    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         row=content['values']
         self.var_atten_id.set(row[0])
         self.var_atten_roll.set(row[1])
         self.var_atten_name.set(row[2])
         self.var_atten_dep.set(row[3])
         self.var_atten_time.set(row[4])
         self.var_atten_date.set(row[5])
         self.var_atten_attendance.set(row[6])

    def reset_data(self):
         self.var_atten_id.set([])
         self.var_atten_roll.set([])
         self.var_atten_name.set([])
         self.var_atten_dep.set([])
         self.var_atten_time.set([])
         self.var_atten_date.set([])
         self.var_atten_attendance.set([])

    def importCsv(self):
        global mydata
        mydata.clear()
        self.csv_file_path = ""  # Store CSV path

        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
            parent=self.root
         )
        if fln:
         self.csv_file_path = fln
        with open(fln) as myfile:
            csvreader = csv.reader(myfile, delimiter=",")
            for i in csvreader:
                mydata.append(i)
            self.fetchdata(mydata)


    def update_data(self):
        print("Update button clicked")

        selected = self.AttendanceReportTable.focus()
        print("Selected item:", selected)  # Debug

        if not selected:
            messagebox.showwarning("No Selection", "Please select a row in the table to update.", parent=self.root)
            return

        content = self.AttendanceReportTable.item(selected)
        current_values = content["values"]
        print("Current row values:", current_values)

        if not current_values:
            messagebox.showwarning("Empty Selection", "Selected row has no data.", parent=self.root)
            return

        updated_row = [
        self.var_atten_id.get(),
        self.var_atten_roll.get(),
        self.var_atten_name.get(),
        self.var_atten_dep.get(),
        self.var_atten_time.get(),
        self.var_atten_date.get(),
        self.var_atten_attendance.get()
    ]

        print("Updated form data:", updated_row)

    # Try to update based on index instead of AttendanceID (simpler + more reliable)
        index = self.AttendanceReportTable.index(selected)
        print("Row index in Treeview/mydata:", index)

        if 0 <= index < len(mydata):
            mydata[index] = updated_row
            self.fetchdata(mydata)
            messagebox.showinfo("Success", "Record updated successfully", parent=self.root)
        else:
         messagebox.showerror("Error", "Could not find the record in the data list.", parent=self.root)

             # Save updated data to the same CSV file (if loaded)
        if hasattr(self, 'csv_file_path') and self.csv_file_path:
            try:
             with open(self.csv_file_path, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(mydata)
                print("CSV file updated successfully")
            except Exception as e:
                print("Failed to save CSV:", e)
                messagebox.showerror("Error", f"Failed to save CSV file:\n{e}", parent=self.root)
















if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()


