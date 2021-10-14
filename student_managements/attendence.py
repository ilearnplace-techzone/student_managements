from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



class student:
    def __init__(self,root):
        self.root=root
        self.root.title("student management system")
        self.root.geometry("1530x900+0+0")


        self.stu_id_var=StringVar()
        self.name_var=StringVar()
        self.mobile_no_var=StringVar()
        self.gender_var=StringVar()
        self.address_var=StringVar()
        self.date_var=StringVar()
        self.comingTime_var = StringVar()
        self.GoingTime_var = StringVar()
        self.TimeSpend_var = StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        title=Label(self.root,text="STUDENT MANGEMENT SYSTEM",font=("Times New Roman ",30,"bold"),fg="purple",bg="powder blue",bd=5,relief=RAISED)
        title.pack(side=TOP,fill=X)

        # manage frame
        Manage_frame=Frame(self.root,bd=5,relief=RIDGE,bg="powder blue")
        Manage_frame.place(x=20,y=65,width=550,height=720)

        # Manage title
        M_title=Label(Manage_frame,text="MANAGE STUDENT",font=("Times New Roman ",30,"bold"),fg="purple",bg="powder blue",bd=5,relief=RAISED)
        M_title.grid(row=0,columnspan=2,padx=20,pady=20)


        # label
        lbl_id=Label(Manage_frame,text="stu id.",font=("Times New Roman ",20,"bold"),fg="purple",bg="powder blue")
        lbl_id.grid(row=1,column=0,padx=20,pady=10,sticky=W)

        stu_id_entry=ttk.Entry(Manage_frame,textvariable=self.stu_id_var,font=("times new roman",20,"bold"))
        stu_id_entry.grid(row=1,column=1,padx=20,pady=10,sticky=W)

        lbl_name = Label(Manage_frame, text="Name.", font=("Times New Roman ", 20, "bold"), fg="purple",
                       bg="powder blue")
        lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky=W)

        name_entry = ttk.Entry(Manage_frame,textvariable=self.name_var, font=("times new roman", 20, "bold"))
        name_entry.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        lbl_mobile = Label(Manage_frame, text="Moble No.", font=("Times New Roman ", 20, "bold"), fg="purple",
                       bg="powder blue")
        lbl_mobile.grid(row=3, column=0, padx=20, pady=10, sticky=W)

        mobile_entry = ttk.Entry(Manage_frame,textvariable=self.mobile_no_var,font=("times new roman", 20, "bold"))
        mobile_entry.grid(row=3, column=1, padx=20, pady=10, sticky=W)

        lbl_gender = Label(Manage_frame, text="Gender.", font=("Times New Roman ", 20, "bold"), fg="purple",
                       bg="powder blue")
        lbl_gender.grid(row=4, column=0, padx=20, pady=10, sticky=W)

        combo_gender=ttk.Combobox(Manage_frame,width=18,textvariable=self.gender_var,font=("time new roman",20,"bold"),state="readonly")
        combo_gender["values"]=("Male","Female","other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10,sticky=W)


        lbl_address = Label(Manage_frame, text="Address.", font=("Times New Roman ", 20, "bold"), fg="purple",
                       bg="powder blue")
        lbl_address.grid(row=5, column=0, padx=20, pady=10, sticky=W)

        self.address_text=Text(Manage_frame,width=20,height=2,font=("times new roman",20,"bold"))
        self.address_text.grid(row=5,column=1,padx=20,pady=10,sticky=W)

        lbl_date = Label(Manage_frame, text="Date", font=("Times New Roman ", 20, "bold"), fg="purple",
                            bg="powder blue")
        lbl_date.grid(row=6, column=0, padx=20, pady=10, sticky=W)

        date_entry = ttk.Entry(Manage_frame, textvariable=self.date_var, font=("times new roman", 20, "bold"))
        date_entry.grid(row=6, column=1, padx=20, pady=10, sticky=W)

        lbl_comingTime = Label(Manage_frame, text="comingTime", font=("Times New Roman ", 20, "bold"), fg="purple",
                         bg="powder blue")
        lbl_comingTime.grid(row=7, column=0, padx=20, pady=10, sticky=W)

        comingTime_entry = ttk.Entry(Manage_frame, textvariable=self.comingTime_var, font=("times new roman", 20, "bold"))
        comingTime_entry.grid(row=7, column=1, padx=20, pady=10, sticky=W)

        lbl_GoingTime = Label(Manage_frame, text="GoingTime", font=("Times New Roman ", 20, "bold"), fg="purple",
                         bg="powder blue")
        lbl_GoingTime.grid(row=8, column=0, padx=20, pady=10, sticky=W)

        GoingTime_entry = ttk.Entry(Manage_frame, textvariable=self.GoingTime_var, font=("times new roman", 20, "bold"))
        GoingTime_entry.grid(row=8, column=1, padx=20, pady=10, sticky=W)

        lbl_TimeSpend = Label(Manage_frame, text="Timespend", font=("Times New Roman ", 20, "bold"), fg="purple",
                          bg="powder blue")
        lbl_TimeSpend.grid(row=9, column=0, padx=20, pady=10, sticky=W)

        TimeSpend_entry = ttk.Entry(Manage_frame, textvariable=self.TimeSpend_var, font=("times new roman", 20, "bold"))
        TimeSpend_entry.grid(row=9, column=1, padx=20, pady=10, sticky=W)

        # Buttons Frame
        btn_frame=Frame(self.root,bd=4,relief=RIDGE,bg="powder blue")
        btn_frame.place(x=40,y=718,width=500,height=60)

        add_btn=Button(btn_frame,text="Add",command=self.add_student,width=13,height=2,fg="white",bg="crimson")
        add_btn.grid(row=0,column=1,padx=10,pady=10)

        updet_btn = Button(btn_frame,command=self.update, text="Updet", width=13, height=2, fg="white", bg="crimson")
        updet_btn.grid(row=0, column=2, padx=10, pady=10)

        delete_btn = Button(btn_frame,command=self.delete_data, text="Delete", width=13, height=2, fg="white", bg="crimson")
        delete_btn.grid(row=0, column=3, padx=10, pady=10)

        clear_btn = Button(btn_frame,command=self.clear, text="Clear", width=13, height=2, fg="white", bg="crimson")
        clear_btn.grid(row=0, column=4, padx=10, pady=10)

        # details frame
        Details_frame = Frame(self.root, bd=5, relief=RIDGE, bg="powder blue")
        Details_frame.place(x=600, y=65, width=900, height=718)

        search_lbl=Label(Details_frame,text="search by",font=("times new roman",20,"bold"),fg="red",bg="powder blue")
        search_lbl.grid(row=1,column=0,padx=20,pady=10,sticky=W)

        seqarch_combo=ttk.Combobox(Details_frame,textvariable=self.search_by,width=19,font=("times new roman",15,"bold"),state="readonly")
        seqarch_combo["values"]=("select option","stu_id","name","address")
        seqarch_combo.grid(row=1,column=1,padx=20,pady=10,sticky=W)

        search_entry=ttk.Entry(Details_frame,textvariable=self.search_txt,font=("times new roman",15,"bold"))
        search_entry.grid(row=1,column=2,padx=20,pady=10,sticky=W)

        search_btn = Button(Details_frame,command=self.search_data, text="search", width=13, height=2, fg="white", bg="crimson")
        search_btn.grid(row=1, column=3, padx=10, pady=10)

        showall_btn = Button(Details_frame,command=self.search_data, text="show all", width=13, height=2, fg="white", bg="crimson")
        showall_btn.grid(row=1, column=4, padx=10, pady=10)

        #  Table Frame
        Table_frame = Frame(self.root, bd=5, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=615, y=180, width=870, height=590)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,column=("stu_id","name","mobile no","gender","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("stu_id",text="Stu id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("mobile no", text="Mobile no")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("address", text="Address")
    #    self.student_table.heading("date",text="date")
    #    self.student_table.heading("comingTime", text="comingTime")
    #    self.student_table.heading("GoingTime", text="GoingTime")
     #   self.student_table.heading("TimeSpend", text="TimeSpend")
       # self.student_table.heading("address", text="Address")

        self.student_table["show"]="headings"
        self.student_table.column("stu_id",width=40)
        self.student_table.column("name", width=130)
        self.student_table.column("mobile no", width=80)
        self.student_table.column("gender", width=60)
        self.student_table.column("address", width=150)
     #   self.student_table.column("date", width=50)
      #  self.student_table.column("comingTime", width=50)
       #self.student_table.column("TimeSpend", width=50)
        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()


    def add_student(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky1598",database="school")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into student_Table values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.stu_id_var.get(),
                                                                            self.name_var.get(),
                                                                            self.mobile_no_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.address_text.get("1.0", END),
                                                                            self.date_var.get(),
                                                                            self.comingTime_var.get(),
                                                                            self.GoingTime_var.get(),
                                                                            self.TimeSpend_var.get(),
                                                                        #    self.address_text.get("1.0", END),
                                                                             ))

        conn.commit()
        self.fetch_data()
        conn.close()


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky1598",database="school")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_Table")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def clear(self):
        self.stu_id_var.set("")
        self.name_var.set("")
        self.mobile_no_var.set("")
        self.gender_var.set("")
        self.date_var.set("")
        self.comingTime_var.set("")
        self.GoingTime_var.set("")
        self.TimeSpend_var.set("")
        self.address_text.delete("1.0", END)


    def get_cursor(self,evente=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content["values"]
        self.stu_id_var.set(row[0])
        self.name_var.set(row[1])
        self.mobile_no_var.set(row[2])
        self.gender_var.set(row[3])
        self.date_var.set(row[5])
        self.comingTime_var.set(row[6])
        self.GoingTime_var.set(row[7])
        self.TimeSpend_var.set(row[8])
        self.address_text.delete("1.0", END)
        self.address_text.insert(END,row[4])


    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="vicky1598", database="school")
        my_cursor = conn.cursor()
        my_cursor.execute("update student_Table set name=%s,mobile_no=%s,gender=%s,address=%s,date=%s,comingTime=%s,GoingTime=%s,TimeSpend=%s  where stu_id=%s",(

                                                                                                                 self.name_var.get(),
                                                                                                                 self.mobile_no_var.get(),
                                                                                                                 self.gender_var.get(),
                                                                                                                 self.address_text.get(),
                                                                                                                 self.date_var.get(),
                                                                                                                 self.comingTime_var.get(),
                                                                                                                 self.GoingTime_var.get(),
                                                                                                                 self.TimeSpend_var.get(".0", END),


                                                                                                             #    self.address_text.get("1.0", END),
                                                                                                                 self.stu_id_var.get()
                                                                                                                 ))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
        messagebox.showinfo("update","Record has been updated successfully")


    def delete_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="vicky1598", database="school")
        my_cursor = conn.cursor()
        query="delete from student_Table where stu_id=%s"
        value=(self.stu_id_var.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear()

        messagebox.showinfo("Delete","student has been Deleted successfully")


    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="vicky1598", database="school")
        my_cursor = conn.cursor()
        sql="SELECT * FROM student_Table WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'"
        print(sql)
        my_cursor.execute(sql)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()





        # Time management
       # time_frame = Frame(self.root, bd=5, relief=RIDGE, bg="powder blue")
       # time_frame.place(x=20, y=610, width=1480, height=180)

        # time management title
       # T_title = Label(Manage_frame, text="TIME MANAGE", font=("Times New Roman ", 20, "bold"), fg="purple",
        #                bg="powder blue", bd=5, relief=RAISED)
        #T_title.grid(row=0, columnspan=3, padx=20, pady=20)








root=Tk()
ob=student(root)
root.mainloop()