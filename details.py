from os import close
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Details_room():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System Room Page")
        self.root.geometry("1295x550+230+220")


# =====Title======#
        lb_title = Label(self.root, text="Room Booking  Details", font=("times new roman", 18, "bold"), bg="black",fg="gold", relief=RIDGE)
        lb_title.place(x=0, y=0, width=1295, height=50)

 # ====LogoImage================= #

        img2 = Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\maxresdefault.jpg")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelImg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        labelImg.place(x=5, y=2, width=100, height=40)

# ====LabelFrame====#
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add ",font=("times new roman", 12, "bold"), padx=2, pady=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

 # floor
        lbl_floor=Label(labelframeleft,text=" Floor:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)

# Room no.
        lbl_floor=Label(labelframeleft,text=" Room No:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=20,font=("arial",13,"bold"))
        enty_floor.grid(row=1,column=1,sticky=W)

# Room Type
        lbl_floor=Label(labelframeleft,text=" Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("arial",13,"bold"))
        enty_floor.grid(row=2,column=1,sticky=W)

# ----Room Botton Frame---#
        Btn_Frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        Btn_Frame.place(x=0, y=200, width=412, height=40)

        btn_add = Button(Btn_Frame, text="Add",command=self.add,font=("arial", 12, "bold"), bg="black",fg="gold", width=9)
        btn_add.grid(row=0, column=0, padx=1)

        btn_upd = Button(Btn_Frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black",fg="gold", width=9)
        btn_upd.grid(row=0, column=1, padx=1)

        btn_dele = Button(Btn_Frame, text="Delete", command=self.Delete,font=("arial", 12, "bold"), bg="black",fg="gold", width=9)
        btn_dele.grid(row=0, column=2, padx=1)

        btn_reset = Button(Btn_Frame, text="Reset",command=self.reset, font=("arial", 12, "bold"), bg="black",fg="gold", width=9)
        btn_reset.grid(row=0, column=3, padx=1)

#==== Search Room Table Frame====#
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2,pady=2)
        table_frame.place(x=600,y=55,width=600,height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.room_details_table = ttk.Treeview(table_frame, column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_details_table.xview)
        scroll_y.config(command=self.room_details_table.yview)


        self.room_details_table.heading("floor", text="Floor")
        self.room_details_table.heading("roomno", text="Room No")
        self.room_details_table.heading("roomType", text="Roon Type")

        self.room_details_table["show"] = "headings"

        self.room_details_table.column("floor", width=100)
        self.room_details_table.column("roomno", width=100)
        self.room_details_table.column("roomType", width=100)


        self.room_details_table.pack(fill=BOTH, expand=1)
        self.room_details_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

#### ADD Room data

    def add(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror("Error", "Required All Feild", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",
                                               port="3306")
                curs = conn.cursor()
                curs.execute("insert into details values(%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_roomNo.get(),
                    self.var_RoomType.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "New Room Added succefully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"some thing went to wrong:{str(es)}", parent=self.root)
## Fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",
                                           port="3306")
        curs = conn.cursor()
        curs.execute(" select * from details ")
        rows = curs.fetchall()
        if len(rows) != 0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()
#get cursor
    def get_cuersor(self,event=""):
        cur_row=self.room_details_table.focus()
        content=self.room_details_table.item(cur_row)
        row=content["values"]
        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])
##### Update Room
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Eroor", "please enter Floor no.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",
                                           port="3306")
            curs = conn.cursor()
            curs.execute(
                "update details set Floor=%s,RoomType=%s where RoomNo=%s ",
                (

                    self.var_floor.get(),
                    self.var_RoomType.get(),
                    self.var_roomNo.get()

                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", " New Room is update successfully ! ", parent=self.root)
## Delete room
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want you delete this room details? ",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="nik358",database="management",port="3306" )
            curs=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            curs.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
####### reset room
    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")





if __name__ =="__main__":
    root=Tk()
    obj=Details_room(root)
    root.mainloop()