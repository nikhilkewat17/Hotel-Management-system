from os import close
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Roombooking():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System Room Page")
        self.root.geometry("1295x550+230+220")

        #=== Variables===#
        self.var_contact=StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # =====Title======#
        lb_title = Label(self.root, text="Room Booking  Details", font=("times new roman", 18, "bold"), bg="black",fg="gold", relief=RIDGE)
        lb_title.place(x=0, y=0, width=1295, height=50)

        # ====LogoImage================= #

        img9 = Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\maxresdefault.jpg")
        img9 = img9.resize((100, 40), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        labelImg = Label(self.root, image=self.photoimg9, bd=0, relief=RIDGE)
        labelImg.place(x=5, y=2, width=100, height=40)

        # ====LabelFrame====#
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details",font=("times new roman", 12, "bold"), padx=2, pady=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        #====Room Labels And Entry====#
        # customer contact
        cus_contact=Label(labelframeleft,text="Customer Contact :",font=("arial",12,"bold"),padx=2,pady=6)
        cus_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("arial",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)

    #---Fetch Data Button---
        Fetch_button = Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",9, "bold"), bg="black",fg="gold", width=8)
        Fetch_button.place(x=350,y=4)

    #---check in date
        check_in_date=Label(labelframeleft,text="Check in Date :",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        enty_check_in_date=ttk.Entry(labelframeleft,width=28,textvariable=self.var_checkin,font=("arial",13,"bold"))
        enty_check_in_date.grid(row=1,column=1)

    #---check out date
        mother_name=Label(labelframeleft,text="Check Out Date :",font=("arial",12,"bold"),padx=2,pady=6)
        mother_name.grid(row=2,column=0,sticky=W)
        enty_m_name=ttk.Entry(labelframeleft,width=28,textvariable=self.var_checkout,font=("arial",13,"bold"))
        enty_m_name.grid(row=2,column=1)

    #---room type combobox
        room_type=Label(labelframeleft,text=" Room Type :",font=("arial",12,"bold"),padx=2,pady=6)
        room_type.grid(row=3,column=0,sticky=W)

        conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management", port="3306")
        curs = conn.cursor()
        curs.execute(" select RoomType from details ")
        ide = curs.fetchall()

        comb_room=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=26,textvariable=self.var_roomtype,state="readonly")
        comb_room["value"]=ide
        comb_room.current(0)
        comb_room.grid(row=3,column=1)

    #---Available Room
        available_room=Label(labelframeleft,text="Available Rooms :",font=("arial",12,"bold"),padx=2,pady=6)
        available_room.grid(row=4,column=0,sticky=W)
        #enty_avaiable_room=ttk.Entry(labelframeleft,width=28,textvariable=self.var_roomavailable,font=("arial",13,"bold"))
        #enty_avaiable_room.grid(row=4,column=1)

        conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",port="3306")
        curs = conn.cursor()
        curs.execute(" select RoomNo from details ")
        rows = curs.fetchall()

        comb_RoomNo = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=26, textvariable=self.var_roomavailable,state="readonly")
        comb_RoomNo["value"] =rows
        comb_RoomNo.current(0)
        comb_RoomNo.grid(row=4, column=1)

    # ---Meal
        room_meal = Label(labelframeleft, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=6)
        room_meal.grid(row=5, column=0, sticky=W)
        ent_room_meal = ttk.Entry(labelframeleft,textvariable=self.var_meal,font=("arial", 12, "bold"), width=28)
        ent_room_meal.grid(row=5, column=1)

    # ---No. of days
        room_no_days = Label(labelframeleft, text="No. of Days :", font=("arial", 12, "bold"), padx=2, pady=6)
        room_no_days.grid(row=6, column=0, sticky=W)
        enty_no_days = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, width=28, font=("arial", 13, "bold"))
        enty_no_days.grid(row=6, column=1)

    # ---Paid Tax
        room_tax = Label(labelframeleft, text="Paid Tax :", font=("arial", 12, "bold"), padx=2, pady=6)
        room_tax.grid(row=7, column=0, sticky=W)
        enty_room_tax = ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=28, font=("arial", 13, "bold"))
        enty_room_tax.grid(row=7, column=1)

    # ---Sub Total
        room_sub_total = Label(labelframeleft, text="Sub Total:", font=("arial", 12, "bold"), padx=2, pady=6)
        room_sub_total.grid(row=8, column=0, sticky=W)
        ent_sub_total = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal,font=("arial", 12, "bold"), width=28)
        ent_sub_total.grid(row=8, column=1)

    # ---Total Cost
        Total_cost = Label(labelframeleft, text="Total Cost :", font=("arial", 12, "bold"), padx=2, pady=6)
        Total_cost.grid(row=9, column=0, sticky=W)
        enty_cost = ttk.Entry(labelframeleft, textvariable=self.var_total,width=28, font=("arial", 13, "bold"))
        enty_cost.grid(row=9, column=1)

    # ---Bill Button---
        bill_button = Button(labelframeleft, text="Bill", command=self.total,font=("arial", 10, "bold"), bg="black", fg="gold",width=12)
        bill_button.grid(row=10,column=1,sticky=W,padx=1)

# ----Room Botton Frame---#
        Btn_Frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        Btn_Frame.place(x=0, y=400, width=412, height=40)

        btn_add = Button(Btn_Frame, text="Add", command=self.R_add_data,font=("arial", 12, "bold"), bg="black",fg="gold", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        btn_upd = Button(Btn_Frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black",fg="gold", width=9)
        btn_upd.grid(row=0, column=1, padx=1)

        btn_dele = Button(Btn_Frame, text="Delete", command=self.mDelete, font=("arial", 12, "bold"), bg="black",fg="gold", width=9)
        btn_dele.grid(row=0, column=2, padx=1)

        btn_reset = Button(Btn_Frame, text="Reset",command=self.reset, font=("arial", 12, "bold"), bg="black",fg="gold", width=9)
        btn_reset.grid(row=0, column=3, padx=1)

#===Right side images
        img3=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\bed.jpg")
        img3=img3.resize((530,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img3)
        labelImg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        labelImg.place(x=760,y=55,width=530,height=220)

#==== Search Room Table Frame====#
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),padx=2,pady=2)
        table_frame.place(x=435,y=280,width=860,height=260)

        lbl_search=Label(table_frame,font=("arial",12,"bold"),text="Search By :",bg="red",fg="white")
        lbl_search.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        comb_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        comb_search["value"]=("Contact","Room")
        comb_search.current(0)
        comb_search.grid(row=0,column=1,padx=2)

        self.search_txt=StringVar()

        enty_search=ttk.Entry(table_frame,textvariable=self.search_txt,width=24,font=("arial",13,"bold"))
        enty_search.grid(row=0,column=2,padx=2)

        btn_search=Button(table_frame,text="Search",command=self.Room_search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_search.grid(row=0,column=3,padx=2)

        btn_show=Button(table_frame,text="Show All",command=self.R_fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_show.grid(row=0,column=4,padx=2)

# ----show table details---#
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_details_table = ttk.Treeview(details_table, column=("Contact", "check in Date", "check out Date", "Room Type", "Available Room", "Meal", "No of Days"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_details_table.xview)
        scroll_y.config(command=self.room_details_table.yview)

        self.room_details_table.heading("Contact", text="Contact")
        self.room_details_table.heading("check in Date", text="Check in Date")
        self.room_details_table.heading("check out Date", text="Check out Date")
        self.room_details_table.heading("Room Type", text="Room Type")
        self.room_details_table.heading("Available Room", text="Available Room No.")
        self.room_details_table.heading("Meal", text="Meal")
        self.room_details_table.heading("No of Days", text="No of Days")

        self.room_details_table["show"] = "headings"

        self.room_details_table.column("Contact", width=100)
        self.room_details_table.column("check in Date", width=100)
        self.room_details_table.column("Room Type", width=100)
        self.room_details_table.column("check out Date", width=100)
        self.room_details_table.column("Available Room", width=100)
        self.room_details_table.column("Meal", width=100)
        self.room_details_table.column("No of Days", width=100)

        self.room_details_table.pack(fill=BOTH, expand=1)

        self.room_details_table.bind("<ButtonRelease-1>", self.get_cuersor)

        self.R_fetch_data()
#### ADD Room data
    def R_add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","Required All Feild",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="nik358",database="management",port="3306" )
                curs=conn.cursor()
                curs.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                   self.var_contact.get(),
                                                                                   self.var_checkin.get(),
                                                                                   self.var_checkout.get(),
                                                                                   self.var_roomtype.get(),
                                                                                   self.var_roomavailable.get(),
                                                                                   self.var_meal.get(),
                                                                                   self.var_noofdays.get()
                                                                               ))
                conn.commit()
                self.R_fetch_data()
                conn.close()


                messagebox.showinfo("Success","Room data is added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went to wrong:{str(es)}",parent=self.root)
####### Room Fetch data
    def R_fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",
                                           port="3306")
        curs = conn.cursor()
        curs.execute(" select * from room ")
        rows = curs.fetchall()
        if len(rows) != 0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()
###### Get cursor room
    def get_cuersor(self,event=""):
        cur_row=self.room_details_table.focus()
        content=self.room_details_table.item(cur_row)
        row=content["values"]
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
##### Update Room
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Eroor", "please enter Contact no.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",
                                           port="3306")
            curs = conn.cursor()
            curs.execute(
                "update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s ",
                (

                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get()
                ))

            conn.commit()
            self.R_fetch_data()
            conn.close()
            messagebox.showinfo("Success", " Room Information is update successfully ! ", parent=self.root)
## Delete room
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want you delete this room ? ",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="nik358",database="management",port="3306" )
            curs=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            curs.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.R_fetch_data()
        conn.close()
####### reset room
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")

 ####=== Fetch All Data=====####
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact no.",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",port="3306")
            curs = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            curs.execute(query,value)
            row=curs.fetchone()

            if row==None:
                messagebox.showerror("Error","This number is not valid",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataFrame,text="Name :",font=("arial",10,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("arial",10,"bold"))
                lbl.place(x=90,y=0)

                #####Gender fetch Data

                conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",port="3306")
                curs = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                curs.execute(query, value)
                row = curs.fetchone()

                lblName=Label(showDataFrame,text="Gender :",font=("arial",10,"bold"))
                lblName.place(x=0,y=30)

                lbl=Label(showDataFrame,text=row,font=("arial",10,"bold"))
                lbl.place(x=90,y=30)

                ############ Email fetch data ######
                conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",port="3306")
                curs = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                curs.execute(query, value)
                row = curs.fetchone()

                lblName=Label(showDataFrame,text="Email :",font=("arial",10,"bold"))
                lblName.place(x=0,y=60)

                lbl=Label(showDataFrame,text=row,font=("arial",10,"bold"))
                lbl.place(x=90,y=60)

                ##### Natinolity fetch data

                conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",port="3306")
                curs = conn.cursor()
                query = ("select nat from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                curs.execute(query, value)
                row = curs.fetchone()

                lblName=Label(showDataFrame,text="Nationality :",font=("arial",10,"bold"))
                lblName.place(x=0,y=90)

                lbl=Label(showDataFrame,text=row,font=("arial",10,"bold"))
                lbl.place(x=90,y=90)

                ############ Address fetch data ######
                conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",port="3306")
                curs = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                curs.execute(query, value)
                row = curs.fetchone()

                lblName=Label(showDataFrame,text="Address :",font=("arial",10,"bold"))
                lblName.place(x=0,y=120)

                lbl=Label(showDataFrame,text=row,font=("arial",10,"bold"))
                lbl.place(x=90,y=120)
#### search room system ######
    def Room_search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management")
        curs = conn.cursor()

        curs.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = curs.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate = datetime.strptime(outdate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outdate-indate).days)

        if (self.var_meal.get()=="Breakfast" or self.var_roomtype.get()=="Laxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Dinner" or self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" or self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)








if __name__ =="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()