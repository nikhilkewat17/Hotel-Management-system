from tkinter import*
from PIL import Image,ImageTk


from customer import Cust_wind

from room import Roombooking

from details import Details_room


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
    # ====FirstImage================= #

        img1=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\hotel1.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        labelImg=Label(self.root,image=self.photoimg1,relief=RIDGE)
        labelImg.place(x=0,y=0,width=1550,height=140)
     # ====LogoImage================= #

        img2=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\maxresdefault.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labelImg=Label(self.root,image=self.photoimg2,relief=RIDGE)
        labelImg.place(x=0,y=0,width=230,height=140)
    #=====Title======#
        lb_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",relief=RIDGE)
        lb_title.place(x=0,y=140,width=1550,height=50)

    #=====main frame=====#
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

    #===== menu======#
        lbl_menu=Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

    #=====btn frame=====#
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

    
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.Customer_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.Room_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        
        details_btn=Button(btn_frame,text="DETAILS",command=self.Detail_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        
        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.Logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)


    #=====RIGHT SIDE IMAGE====#
         
        
        img3=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\slide3.jpg")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lBlImg=Label(main_frame,image=self.photoimg3,relief=RIDGE)
        lBlImg.place(x=225,y=0,width=1310,height=590)

    #=====down images====#
         
        
        img4=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\khana.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lBlImg=Label(main_frame,image=self.photoimg4,relief=RIDGE)
        lBlImg.place(x=0,y=225,width=230,height=210)
        
        
        img5=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\myh.jpg")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lBlImg=Label(main_frame,image=self.photoimg5,relief=RIDGE)
        lBlImg.place(x=0,y=420,width=230,height=190)

    def Customer_details(self):
        self.new_wind=Toplevel()
        self.app=Cust_wind(self.new_wind)

    def Room_details(self):
        self.new_wind=Toplevel()
        self.app=Roombooking(self.new_wind)

    def Detail_room(self):
        self.new_wind=Toplevel()
        self.app=Details_room(self.new_wind)

    def Logout(self):
        self.root.destroy()






if __name__ =="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
