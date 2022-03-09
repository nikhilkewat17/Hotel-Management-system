from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



from customer import Cust_wind

from room import Roombooking

from details import Details_room
from hotel import HotelManagementSystem

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
## ----Frame---- ###
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

#--Labels--#
    #--------------Username-----------#
        username=Label(frame,text="Username :",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txt_user=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txt_user.place(x=40,y=180,width=270)

    #-----------password----------#

        password=Label(frame,text="Password :",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txt_pass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txt_pass.place(x=40,y=250,width=270)
##----Icon Images--#

        img2=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbl_img2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management\hotel images\lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbl_img3.place(x=650,y=395,width=25,height=25)
##---Login Button----#

        login_button=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login_button.place(x=110,y=300,width=120,height=35)
##---Register Button----#

        reg_button=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        reg_button.place(x=20,y=350,width=160)
##---Forget password  Button----#

        forg_pass=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forg_pass.place(x=20,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    def login(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
             messagebox.showerror("Error","All Field required")
        elif self.txt_user.get()=="nik" and self.txt_pass.get()=="nik358":
            messagebox.showinfo("Success","Welcome Hotel Management system")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="nik358",database="management",port="3306")
            my_cur=conn.cursor()
            my_cur.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txt_user.get(),
                                                                                    self.txt_pass.get()
                                                                                 ))
            row=my_cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    def reset_pass(self):
        if self.combo_security.get()=="Select":
            messagebox.showerror("Error","Select the security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",port="3306")
            my_cur = conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlue=(self.txt_user.get(),self.combo_security.get(),self.txt_security.get())
            my_cur.execute(qury,vlue)
            roe=my_cur.fetchone()
            if roe==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                quey=("update register set password=%s where email=%s")
                val=(self.txt_newpass.get(),self.txt_user.get())
                my_cur.execute(quey,val)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","New passwod set ",parent=self.root2)
                self.root2.destroy()




####----------------------------Forget Password window---------------#####
    def forget_password_window(self):
        if self.txt_user.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="nik358", database="management",port="3306")
            my_cur = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txt_user.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid user")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                L1=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                L1.place(x=0,y=10,relwidth=1)

                # ----------Security Question------#

                security_Q = Label(self.root2, text="Security Question :", font=("times new roman", 15, "bold"),fg="darkgreen", bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security["values"] = ("Select", "Your Birth Place", "Your school name", "Your Nickname")
                self.combo_security.place(x=50, y=110, width=250)
                self.combo_security.current(0)
                # ----------Security Answer-------#

                security_lbl = Label(self.root2, text="Security Answer :", font=("times new roman", 15, "bold"), bg="white",fg="black")
                security_lbl.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2,  font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                #--------New password----------#


                new_password = Label(self.root2, text="New Password :", font=("times new roman", 15, "bold"), bg="white",fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2,  font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass, font=("times new roman", 15),fg="white",bg="green")
                btn.place(x=150,y=290)




####################-------------------------------------------------------Registration form---------------------------------------------------------#####################

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


# ______________________________Variables--------------#

        self.var_fname= StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()



#------Background Wallpaper--#
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")

        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
#----Left Iamge---#
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\back.jpg")

        bg_left=Label(self.root,image=self.bg1)
        bg_left.place(x=50,y=100,width=470, height=550)

#--- main Frame--
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
#--- Label and Entry----

    #---------------------First Name-------------#

        f_name=Label(frame,text="First Name :",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
        f_name.place(x=50,y=100)

        self.text_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.text_fname.place(x=50,y=130,width=250)

    #---------------Last Name---------#

        l_name=Label(frame,text="Last Name :",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

    #---------------------Contact-------------#

        cnt=Label(frame,text="Contact :",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
        cnt.place(x=50,y=170)

        self.txt_cont=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_cont.place(x=50,y=200,width=250)
    #---------------Email---------#

        mail=Label(frame,text="Email :",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
        mail.place(x=370,y=170)

        self.txt_mail=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_mail.place(x=370,y=200,width=250)
    #----------Security Question------#

        security_Q=Label(frame,text="Security Question :",font=("times new roman",15,"bold"),fg="darkgreen",bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security=ttk.Combobox(frame,textvariable=self.var_securityQ ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Birth Place","Your school name","Your Nickname")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)
    #----------Security Answer-------#

        security_lbl=Label(frame,text="Security Answer :",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_lbl.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
    #---------Password------#

        pswd=Label(frame,text="Password :",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
    #---------Confirm password---------

        conf_pswd=Label(frame,text="Confirm Password :",font=("times new roman",15,"bold"),bg="white",fg="black")
        conf_pswd.place(x=370,y=310)

        self.txt_confirm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm.place(x=370,y=340,width=250)

    #-------check-Button---#

        self.var_check=IntVar()

        check_button=Checkbutton(frame,variable=self.var_check,text=" I Agree The Terms & Codition",font=("times new roman",11,"bold"),onvalue=1,offvalue=0)
        check_button.place(x=50,y=380)

###--------Button-------

        button_img=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\register-now-button1.jpg")
        button_img=button_img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(button_img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"))
        b1.place(x=10,y=420,width=200)


        button_img2=Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\loginpng.png")
        button_img2=button_img2.resize((200,50),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(button_img2)
        b1=Button(frame,image=self.photoimage2,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",13,"bold"))
        b1.place(x=330,y=420,width=200)



    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" :
           messagebox.showerror("Error","All Field are required")
        elif self.var_confpass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="nik358",database="management",port="3306")
            my_cur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","already Exist,try another email")
            else:
                my_cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),
                                                                                    self.var_pass.get()
                                                                                  ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Succesfully")


    def return_login(self):
        self.root.destroy()





class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        # ====FirstImage================= #

        img1 = Image.open(
            r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\hotel1.png")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labelImg = Label(self.root, image=self.photoimg1, relief=RIDGE)
        labelImg.place(x=0, y=0, width=1550, height=140)
        # ====LogoImage================= #

        img2 = Image.open(
            r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\maxresdefault.jpg")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelImg = Label(self.root, image=self.photoimg2, relief=RIDGE)
        labelImg.place(x=0, y=0, width=230, height=140)
        # =====Title======#
        lb_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black",
                         fg="gold", relief=RIDGE)
        lb_title.place(x=0, y=140, width=1550, height=50)

        # =====main frame=====#
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ===== menu======#
        lbl_menu = Label(main_frame, text="Menu", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4,
                         relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # =====btn frame=====#
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.Customer_details, width=22,
                          font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.Room_details, width=22,
                          font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", command=self.Detail_room, width=22,
                             font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT",command=self.Logout, width=22, font=("times new roman", 14, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        # =====RIGHT SIDE IMAGE====#

        img3 = Image.open(
            r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lBlImg = Label(main_frame, image=self.photoimg3, relief=RIDGE)
        lBlImg.place(x=225, y=0, width=1310, height=590)

        # =====down images====#

        img4 = Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\khana.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lBlImg = Label(main_frame, image=self.photoimg4, relief=RIDGE)
        lBlImg.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\Hp\AppData\Local\Programs\Python\Python39\Hotel Management System\hotel images\myh.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lBlImg = Label(main_frame, image=self.photoimg5, relief=RIDGE)
        lBlImg.place(x=0, y=420, width=230, height=190)

    def Customer_details(self):
        self.new_wind = Toplevel()
        self.app = Cust_wind(self.new_wind)

    def Room_details(self):
        self.new_wind = Toplevel()
        self.app = Roombooking(self.new_wind)

    def Detail_room(self):
        self.new_wind = Toplevel()
        self.app = Details_room(self.new_wind)
    def Logout(self):
        self.root.destroy()




if __name__=="__main__":
    main()





