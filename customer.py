from os import close
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_wind():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System Customer Deatails")
        self.root.geometry("1295x550+230+220")

    #####====Variables=====#

        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x)) 

        self.cust_name=StringVar()
        self.cust_mother=StringVar()
        self.cust_gender=StringVar()
        self.cust_post=StringVar()
        self.cust_mobile=StringVar()
        self.cust_email=StringVar()
        self.cust_nat=StringVar()
        self.cust_address=StringVar()
        self.cust_id_prof=StringVar()
        self.cust_id_nom=StringVar()


        
    #=====Title======#
        lb_title=Label(self.root,text="Add Customer Details",font=("times new roman",18,"bold"),bg="black",fg="gold",relief=RIDGE)
        lb_title.place(x=0,y=0,width=1295,height=50)
        
    # ====LogoImage================= #

        img2=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\maxresdefault.jpg")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labelImg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        labelImg.place(x=5,y=2,width=100,height=40)

    #====LabelFrame====#
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2,pady=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
    #====Labels And Entry====#
        #----ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

        #---name
        lbl_name=Label(labelframeleft,text="Customer Name :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_name.grid(row=1,column=0,sticky=W)
        enty_name=ttk.Entry(labelframeleft,textvariable=self.cust_name,width=29,font=("arial",13,"bold"))
        enty_name.grid(row=1,column=1)

        #---mother name
        mother_name=Label(labelframeleft,text="Mother  Name :",font=("arial",12,"bold"),padx=2,pady=6)
        mother_name.grid(row=2,column=0,sticky=W)
        enty_m_name=ttk.Entry(labelframeleft,textvariable=self.cust_mother,width=29,font=("arial",13,"bold"))
        enty_m_name.grid(row=2,column=1)

        #---gender combobox
        gend=Label(labelframeleft,text=" Gender :",font=("arial",12,"bold"),padx=2,pady=6)
        gend.grid(row=3,column=0,sticky=W)

        comb_gend=ttk.Combobox(labelframeleft,textvariable=self.cust_gender,font=("arial",12,"bold"),width=27,state="readonly")
        comb_gend["value"]=("Male","Feamle","Other")
        comb_gend.current(0)
        comb_gend.grid(row=3,column=1)

        #---postcode
        postcode=Label(labelframeleft,text="PostCode :",font=("arial",12,"bold"),padx=2,pady=6)
        postcode.grid(row=4,column=0,sticky=W)
        enty_postcode=ttk.Entry(labelframeleft,textvariable=self.cust_post,width=29,font=("arial",13,"bold"))
        enty_postcode.grid(row=4,column=1)

        
        #---natinality
        nat=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        nat.grid(row=5,column=0,sticky=W)

        
        comb_nat=ttk.Combobox(labelframeleft,textvariable=self.cust_nat,font=("arial",12,"bold"),width=27,state="readonly")
        comb_nat["value"]=("Indian","USA","British","Other")
        comb_nat.current(0)
        comb_nat.grid(row=5,column=1)

        #---Email
        cust_email=Label(labelframeleft,text="Email :",font=("arial",12,"bold"),padx=2,pady=6)
        cust_email.grid(row=6,column=0,sticky=W)
        enty_email=ttk.Entry(labelframeleft,textvariable=self.cust_email,width=29,font=("arial",13,"bold"))
        enty_email.grid(row=6,column=1)

        
        #---mobile num
        lbl_cust_no=Label(labelframeleft,text="Mobile Number :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_no.grid(row=7,column=0,sticky=W)
        enty_number=ttk.Entry(labelframeleft,textvariable=self.cust_mobile,width=29,font=("arial",13,"bold"))
        enty_number.grid(row=7,column=1)

         
        #---id proof type
        lbl_cust_email=Label(labelframeleft,text="ID Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_email.grid(row=8,column=0,sticky=W)

        comb_id=ttk.Combobox(labelframeleft,textvariable=self.cust_id_prof,font=("arial",12,"bold"),width=27,state="readonly")
        comb_id["value"]=("Adhar Number","Pan Number","Passport","other")
        comb_id.current(0)
        comb_id.grid(row=8,column=1)

        #---id number
        id_no=Label(labelframeleft,text="ID Number :",font=("arial",12,"bold"),padx=2,pady=6)
        id_no.grid(row=9,column=0,sticky=W)
        enty_id=ttk.Entry(labelframeleft,textvariable=self.cust_id_nom,width=29,font=("arial",13,"bold"))
        enty_id.grid(row=9,column=1)

        #---address
        addr=Label(labelframeleft,text="Address :",font=("arial",12,"bold"),padx=2,pady=6)
        addr.grid(row=10,column=0,sticky=W)
        enty_addr=ttk.Entry(labelframeleft,textvariable=self.cust_address,width=29,font=("arial",13,"bold"))
        enty_addr.grid(row=10,column=1)

       #----Botton Frame---#
        Btn_Frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        Btn_Frame.place(x=0,y=400,width=412,height=40)

        btn_add=Button(Btn_Frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_add.grid(row=0,column=0,padx=1)
       
        btn_upd=Button(Btn_Frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_upd.grid(row=0,column=1,padx=1)

        btn_dele=Button(Btn_Frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_dele.grid(row=0,column=2,padx=1)

        btn_reset=Button(Btn_Frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_reset.grid(row=0,column=3,padx=1)

        #====Table Frame====#
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),padx=2,pady=2)
        table_frame.place(x=435,y=50,width=860,height=490)

        lbl_search=Label(table_frame,font=("arial",12,"bold"),text="Search By :",bg="red",fg="white")
        lbl_search.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        comb_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        comb_search["value"]=("Mobile","Ref","Adhar","Other")
        comb_search.current(0)
        comb_search.grid(row=0,column=1,padx=2)

        self.search_txt=StringVar()

        enty_search=ttk.Entry(table_frame,textvariable=self.search_txt,width=24,font=("arial",13,"bold"))
        enty_search.grid(row=0,column=2,padx=2)

        btn_search=Button(table_frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_search.grid(row=0,column=3,padx=2)

        btn_show=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btn_show.grid(row=0,column=4,padx=2)

        #----show table details---#
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table,orient=VERTICAL)

        self.show_details_table=ttk.Treeview(details_table,column=("ref","name","mother","Gender","Post","Nat","Email","Mobile","Id Proof","Id Number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.show_details_table.xview)
        scroll_y.config(command=self.show_details_table.yview)

        self.show_details_table.heading("ref",text="Refer No")
        self.show_details_table.heading("name",text="Name")
        self.show_details_table.heading("mother",text="Mother Name")
        self.show_details_table.heading("Gender",text="Gender")
        self.show_details_table.heading("Post",text="Post Code")
        self.show_details_table.heading("Nat",text="Nationality")
        self.show_details_table.heading("Email",text="Email")
        self.show_details_table.heading("Mobile",text="Mobile no.")
        self.show_details_table.heading("Id Proof",text="Id Proof")
        self.show_details_table.heading("Id Number",text="Id Number")
        self.show_details_table.heading("Address",text="Address")

        self.show_details_table["show"]="headings"

        self.show_details_table.column("ref",width=100)
        self.show_details_table.column("name",width=100)
        self.show_details_table.column("mother",width=100)
        self.show_details_table.column("Gender",width=100)
        self.show_details_table.column("Post",width=100)
        self.show_details_table.column("Nat",width=100)
        self.show_details_table.column("Email",width=100)
        self.show_details_table.column("Mobile",width=100)
        self.show_details_table.column("Id Proof",width=100)
        self.show_details_table.column("Id Number",width=100)
        self.show_details_table.column("Address",width=100)

        self.show_details_table.pack(fill=BOTH,expand=1)
        self.show_details_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()


    def add_data(self):
        if self.cust_mobile.get()=="" or self.cust_mother.get()=="":
            messagebox.showerror("Error","Required All Feild",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="nik358",database="management",port="3306" )
                curs=conn.cursor()
                curs.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                             self.var_ref.get(),
                                                             self.cust_name.get(),
                                                             self.cust_mother.get(),
                                                             self.cust_gender.get(),
                                                             self.cust_post.get(),
                                                             self.cust_nat.get(),
                                                             self.cust_email.get(),
                                                             self.cust_mobile.get(),
                                                             self.cust_id_prof.get(),
                                                             self.cust_id_nom.get(),
                                                             self.cust_address.get()
                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close() 


                messagebox.showinfo("Success","customer data is added",parent=self.root) 
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went to wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="nik358",database="management",port="3306" )
        curs=conn.cursor()
        curs.execute( " select * from customer " )
        rows=curs.fetchall()
        if len(rows)!=0:
            self.show_details_table.delete(*self.show_details_table.get_children())
            for i in rows:
                self.show_details_table.insert("",END,values=i)
            conn.commit()   
        conn.close()                                       
    def get_cuersor(self,event=""):
        cur_row=self.show_details_table.focus()
        content=self.show_details_table.item(cur_row)
        row=content["values"]



        self.var_ref.set(row[0]),
        self.cust_name.set(row[1]),
        self.cust_mother.set(row[2]),
        self.cust_gender.set(row[3]),
        self.cust_post.set(row[4]),
        self.cust_nat.set(row[5]),
        self.cust_email.set(row[6]),
        self.cust_mobile.set(row[7]),
        self.cust_id_prof.set(row[8]),
        self.cust_id_nom.set(row[9]),
        self.cust_address.set(row[10])

    def update(self):
        if self.cust_mobile.get()=="":
            messagebox.showerror("Eroor","please enter mobile no.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="nik358",database="management",port="3306" )
            curs=conn.cursor()
            curs.execute( "update customer set Name=%s,mother=%s,gender=%s,post=%s,nat=%s,email=%s,mobile=%s,id_proof=%s,id_number=%s,address=%s where Ref=%s ",(
                                                                                                                                                                                                                    
                                                                                                                                                     self.cust_name.get(),
                                                                                                                                                     self.cust_mother.get(),
                                                                                                                                                     self.cust_gender.get(),
                                                                                                                                                     self.cust_post.get(),
                                                                                                                                                     self.cust_nat.get(),
                                                                                                                                                     self.cust_email.get(),
                                                                                                                                                     self.cust_mobile.get(),
                                                                                                                                                     self.cust_id_prof.get(),
                                                                                                                                                     self.cust_id_nom.get(),
                                                                                                                                                     self.cust_address.get(),   
                                                                                                                                                     self.var_ref.get() 
                                                                                                                                                  ))     
                                  

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Information is update successfully ! ",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want you delete this customer ? ",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="nik358",database="management",port="3306" )
            curs=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            curs.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
        #self.var_ref.set(""),
        self.cust_name.set(""),
        self.cust_mother.set(""),
        #self.cust_gender.set(""),
        self.cust_post.set(""),
        #self.cust_nat.set(""),
        self.cust_email.set(""),
        self.cust_mobile.set(""),
        #self.cust_id_prof.set(""),
        self.cust_id_nom.set(""),
        self.cust_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="nik358",database="management",port="3306" )
        curs=conn.cursor()

        curs.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=curs.fetchall()
        if len (rows)!=0:
            self.show_details_table.delete(*self.show_details_table.get_children())
            for i in rows:
                self.show_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()    

if __name__ =="__main__":
    root=Tk()
    obj=Cust_wind(root)
    root.mainloop()