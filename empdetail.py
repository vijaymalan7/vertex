from tkinter import *
from tkinter import messagebox
from datetime import datetime
import time
from tkinter import PhotoImage

import sqlite3

try:
    conobj=sqlite3.connect(database='employee.sqlite')
    curobj=conobj.cursor()
    curobj.execute("create table emp(id integer primary key autoincrement,name text,dpt text,mob text,adrs text,date text,cl integer,sl integer,bl integer)")
    conobj.commit()
    print('Table created')
except:
    print("something went wrong,or table is already exsist!")
conobj.close()


win=Tk()
win.title("Employee Detail")
win.state('zoomed')
win.configure(bg='powder blue')
win.resizable(width=False,height=False)
##########
img_path="vertex_logo.png"
img=PhotoImage(file=img_path)
##########
img_path1="img_bg1.png"
img1=PhotoImage(file=img_path1)

lbl_vetext=Label(win,image=img,bg='powder blue')
lbl_vetext.place(relx=0,rely=0)

lbl=Label(win,text='Welcome to vertex Group',font=('Arial',45,'bold','underline'),bg='powder blue')
lbl.pack()

lbl_time=Label(win,text=f'{datetime.now().date()}',font=('Arial',15,'bold','underline'),bg='powder blue')
lbl_time.place(relx=.9,rely=.1)

def newempscreen():
    frm=Frame(win)
    frm.configure(bg='#1a2e1f')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    lbl_bg=Label(frm,image=img1,bg='#1a2e1f')
    lbl_bg.place(relx=.12,rely=0)

    lbl_wel=Label(frm,text='Enter the details of the Employee to save in Database!',font=("arial",20,'bold','underline'),bg='#1a2e1f',fg='white')
    lbl_wel.pack()
    def back():
        frm.destroy
        mainscreen()

    def newempdb():
        empID=e_ID.get()
        name=e_name.get()
        mob=e_Mob.get()
        adrs=e_Adr.get()
        date=time.ctime()
        dpt=e_DPT.get()
        cl=7
        sl=7
        bl=7
        if len(name)==0 or len(mob)==0 or len(dpt)==0:
            messagebox.showerror('Empty Field','Empty fields are not allowed')
        else:
            conobj=sqlite3.connect(database='employee.sqlite')
            curobj=conobj.cursor()  
            curobj.execute("insert into emp(id,name,dpt,mob,adrs,date,cl,sl,bl) values(?,?,?,?,?,?,?,?,?)",(empID,name,dpt,mob,adrs,date,cl,sl,bl))
            conobj.commit()
            conobj.close()
        
        conobj=sqlite3.connect(database='employee.sqlite')
        curobj=conobj.cursor()
        curobj.execute("select max(id) from emp")
        tup=curobj.fetchone()
        conobj.close()
        messagebox.showinfo('record updated',f"Record updated with Employee ID:{tup[0]}")

    def reset():
        e_ID.delete(0,"end")
        e_Adr.delete(0,'end')
        e_DPT.delete(0,'end')
        e_Mob.delete(0,'end')
        e_name.delete(0,'end')


    lbl_ID=Label(frm,text='Emp ID:',font=('Arial',20,'bold',),bg='powder blue')
    lbl_ID.place(relx=.15,rely=.1)

    e_ID=Entry(frm,font=('Arial',20,'bold',),bg='powder blue')
    e_ID.place(relx=.3,rely=.1)
    e_ID.focus()

    lbl_name=Label(frm,text='Emp Name:',font=('Arial',20,'bold',),bg='powder blue')
    lbl_name.place(relx=.15,rely=.2)

    e_name=Entry(frm,font=('Arial',20,'bold',),bg='powder blue')
    e_name.place(relx=.3,rely=.2)
    # e_name.focus()

    lbl_DPT=Label(frm,text='Emp Dpt:',font=('Arial',20,'bold',),bg='powder blue')
    lbl_DPT.place(relx=.15,rely=.3)

    e_DPT=Entry(frm,font=('Arial',20,'bold',),bg='powder blue')
    e_DPT.place(relx=.3,rely=.3)

    lbl_Mob=Label(frm,text='Mob No:',font=('Arial',20,'bold',),bg='powder blue')
    lbl_Mob.place(relx=.15,rely=.4)

    e_Mob=Entry(frm,font=('Arial',20,'bold',),bg='powder blue')
    e_Mob.place(relx=.3,rely=.4)
    

    lbl_Adr=Label(frm,text='Address:',font=('Arial',20,'bold',),bg='powder blue')
    lbl_Adr.place(relx=.15,rely=.5)

    e_Adr=Entry(frm,font=('Arial',20,'bold',),bg='powder blue')
    e_Adr.place(relx=.3,rely=.5)

    btn_submit=Button(frm,text='Submit',command=newempdb,font=('Arial',20,'bold'))
    btn_submit.place(relx=.25,rely=.6)

    btn_reset=Button(frm,text='Reset',command=reset,font=('Arial',20,'bold'))
    btn_reset.place(relx=.4,rely=.6)

    btn_back=Button(frm,text='Back',command=back,font=('Arial',20,'bold'))
    btn_back.place(relx=0,rely=0)

def delempscreen():
    frm=Frame(win)
    frm.configure(bg='#1a2e1f')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    ####
    lbl_bg=Label(frm,image=img1,bg='#1a2e1f')
    lbl_bg.place(relx=.12,rely=0)

    lbl_wel=Label(frm,text='Enter the Emp ID to delete the Employee',font=("arial",20,'bold'),bg='#1a2e1f',fg='white')
    lbl_wel.pack()

    def back():
        frm.destroy
        mainscreen()

    def reset():
        lbl_e1.delete(0,'end')
   
    def deldb():
        ID1=int(lbl_e1.get())
        try:
            conobj=sqlite3.connect(database='employee.sqlite')
            curobj=conobj.cursor()
            curobj.execute("delete from emp where id=?",(ID1,))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('info',f'Employee succesfully deleted with Emp ID:{ID1}')
        except Exception as e:
            messagebox.showerror('error',f'something went wrong!{e}')

    #######
    btn_back=Button(frm,text='Back',command=back,font=('Arial',20,'bold'))
    btn_back.place(relx=0,rely=0)
    
    lbl_1=Label(frm,text='Enter Emp ID:',font=('Arial',20,'bold'),bg='powder blue')
    lbl_1.place(relx=.2,rely=.2)

    lbl_e1=Entry(frm,text='Enter Emp ID:',font=('Arial',20,'bold'))
    lbl_e1.place(relx=.4,rely=.2)
    lbl_e1.focus()

    btn_del=Button(frm,text='Delete',command=deldb,font=('Arial',20,'bold'),bg='red',fg='white')
    btn_del.place(relx=.4,rely=.3)

    btn_reset=Button(frm,text='Reset',command=reset,font=('Arial',20,'bold'))
    btn_reset.place(relx=.5,rely=.3)

def GCL():
    frm=Frame(win,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='#1c5e5e')
    frm.place(relx=.7,rely=.4,relheight=.2,relwidth=.27)

    lbl_s=Label(frm,text='Are you sure to grant Permision!',font=('Arial',15,'bold'),bg='#1c5e5e')
    lbl_s.place(relx=.05,rely=.1)

    lbl_s2=Label(frm,text='for',font=('Arial',15,'bold'),bg='#1c5e5e')
    lbl_s2.place(relx=.2,rely=.3)
    
    lbl_s3=Label(frm,text='Casual Leave',font=('Arial',15,'bold'),bg='#1c5e5e',fg='#dce2e6')
    lbl_s3.place(relx=.3,rely=.3)
    def yes():
        try:
            conobj=sqlite3.connect(database='employee.sqlite')
            curobj=conobj.cursor()
            curobj.execute("update emp set cl=cl-1 where id=?",(eid,))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('info',f'Employee succesfully Granted for leave')
            leavedb()
        except Exception as e:
            messagebox.showerror('error',f'something went wrong!{e}')

    def no():
        leavesc()

    btn_y=Button(frm,text='Yes',command=yes,font=('Arial',12,'bold'))
    btn_y.place(relx=.3,rely=.6)

    btn_y=Button(frm,text='No',command=no,font=('Arial',12,'bold'))
    btn_y.place(relx=.6,rely=.6)

def GSL():
    frm=Frame(win,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='#1c5e5e')
    frm.place(relx=.7,rely=.4,relheight=.2,relwidth=.27)

    lbl_s=Label(frm,text='Are you sure to grant Permision!',font=('Arial',15,'bold'),bg='#1c5e5e')
    lbl_s.place(relx=.05,rely=.1)
    lbl_s=Label(frm,text='for',font=('Arial',15,'bold'),bg='#1c5e5e')
    lbl_s.place(relx=.2,rely=.3)

    lbl_s3=Label(frm,text='Sick Leave',font=('Arial',15,'bold'),bg='#1c5e5e',fg='#dce2e6')
    lbl_s3.place(relx=.3,rely=.3)

    def yes():
        try:
            conobj=sqlite3.connect(database='employee.sqlite')
            curobj=conobj.cursor()
            curobj.execute("update emp set sl=sl-1 where id=?",(eid,))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('info',f'Employee succesfully Granted for leave')
            leavedb()
        except Exception as e:
            messagebox.showerror('error',f'something went wrong!{e}')

    def no():
        leavesc()

    btn_y=Button(frm,text='Yes',command=yes,font=('Arial',12,'bold'))
    btn_y.place(relx=.3,rely=.6)

    btn_y=Button(frm,text='No',command=no,font=('Arial',12,'bold'))
    btn_y.place(relx=.6,rely=.6)

def GBL():
    frm=Frame(win,highlightbackground='black',highlightthickness=2)
    frm.configure(bg='#1c5e5e')
    frm.place(relx=.7,rely=.4,relheight=.2,relwidth=.27)

    lbl_s=Label(frm,text='Are you sure to grant Permision!',font=('Arial',15,'bold'),bg='#1c5e5e')
    lbl_s.place(relx=.05,rely=.1)

    lbl_s=Label(frm,text='for',font=('Arial',15,'bold'),bg='#1c5e5e')
    lbl_s.place(relx=.2,rely=.3)

    lbl_s3=Label(frm,text='Basic Leave',font=('Arial',15,'bold'),bg='#1c5e5e',fg='#dce2e6')
    lbl_s3.place(relx=.3,rely=.3)
    

    def yes():
        try:
            conobj=sqlite3.connect(database='employee.sqlite')
            curobj=conobj.cursor()
            curobj.execute("update emp set bl=bl-1 where id=?",(eid,))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('info',f'Employee succesfully Granted for leave')
            leavedb()
        except Exception as e:
            messagebox.showerror('error',f'something went wrong!{e}')

    def no():
        leavesc()

    btn_y=Button(frm,text='Yes',command=yes,font=('Arial',12,'bold'))
    btn_y.place(relx=.3,rely=.6)

    btn_y=Button(frm,text='No',command=no,font=('Arial',12,'bold'))
    btn_y.place(relx=.6,rely=.6)


def leavesc():
    frm=Frame(win)
    frm.configure(bg='#1a2e1f')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    lbl_bg=Label(frm,image=img1,bg='#1a2e1f')
    lbl_bg.place(relx=.12,rely=0)

    lbl_wel=Label(frm,text='This screen is to check the details of leaves of Employee.',font=("arial",20,'bold'),bg='#1a2e1f',fg='white')
    lbl_wel.pack()


    def back():
        frm.destroy
        mainscreen()
    ######
    global leavedb
    def leavedb():
        global eid
        eid=e_1.get()

        def clear():
            frm.destroy()
            leavesc()

        try:
            conobj=sqlite3.connect(database='employee.sqlite')
            curobj=conobj.cursor()
            curobj.execute("select *from emp where id=?",(eid,))
            tup=curobj.fetchone()
            conobj.close()

            lbl_n=Label(frm,text=f'Employee name:\t\t{tup[1]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_n.place(relx=.25,rely=.2)

            lbl_cl=Label(frm,text=f'Casual Leave:\t\t{tup[6]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_cl.place(relx=.25,rely=.3)

            lbl_sl=Label(frm,text=f'Sick Leave:\t\t{tup[7]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_sl.place(relx=.25,rely=.4)

            lbl_bl=Label(frm,text=f'Basic Leave:\t\t{tup[8]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_bl.place(relx=.25,rely=.5)

            btn_clear=Button(frm,text='Clear Details',command=clear,font=('Arial',15,'bold'))
            btn_clear.place(relx=.35,rely=.7)

            btn_ok1=Button(frm,text='Grant CL',command=GCL,font=('Arial',15,'bold'))
            btn_ok1.place(relx=.6,rely=.3)

            btn_ok2=Button(frm,text='Grant SL',command=GSL,font=('Arial',15,'bold'))
            btn_ok2.place(relx=.6,rely=.4)

            btn_ok3=Button(frm,text='Grant BL',command=GBL,font=('Arial',15,'bold'))
            btn_ok3.place(relx=.6,rely=.5)
        except:
            messagebox.showerror('error','Empty Fied or invalid Emp ID')
            clear()


    lbl_1=Label(frm,text="Enter Emp ID:",font=('Arial',20,'bold'),bg='powder blue')
    lbl_1.place(relx=.25,rely=.1)
    
    e_1=Entry(frm,font=('Arial',20,'bold'),bg='powder blue',width='10')
    e_1.place(relx=.42,rely=.1)
    e_1.focus()

    btn_back=Button(frm,text='Back',command=back,font=('Arial',20,'bold'))
    btn_back.place(relx=0,rely=0)

    btn_ok=Button(frm,text='OK',command=leavedb,font=('Arial',15,'bold'))
    btn_ok.place(relx=.5,rely=.1)


def mainscreen():
    frm=Frame(win)
    frm.configure(bg='#1a2e1f')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    lbl_bg=Label(frm,image=img1,bg='#1a2e1f')
    lbl_bg.place(relx=.12,rely=0)

    def empdetail():
        frm.destroy()
        empdetailscreen()

    def newemp():
        frm.destroy()
        newempscreen()

    def delemp():
        frm.destroy()
        delempscreen()

    def logout():
        frm.destroy()
        login()

    def lscreen():
        frm.destroy()
        leavesc()

    btn_empid=Button(frm,text='Emp Detail',command=empdetail,font=('Arial',20,'bold'),bg='powder blue')
    btn_empid.place(relx=.2,rely=.2)
    

    btn_newemp=Button(frm,text='New Emp',command=newemp,font=('Arial',20,'bold'),bg='powder blue')
    btn_newemp.place(relx=.6,rely=.2)
    

    btn_empdel=Button(frm,text='Delete Employee',command=delemp,font=('Arial',20,'bold'),bg='powder blue')
    btn_empdel.place(relx=.2,rely=.4)

    btn4=Button(frm,text="Leave's Detail",command=lscreen,font=('Arial',20,'bold'),bg='powder blue')
    btn4.place(relx=.6,rely=.4)

    btn_back=Button(frm,text='Logout',command=logout,font=('Arial',20,'bold'),bg='#f76060',fg='white')
    btn_back.place(relx=.915,rely=0)
    
def empdetailscreen():
    frm=Frame(win)
    frm.configure(bg='#1a2e1f')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    lbl_bg=Label(frm,image=img1,bg='#1a2e1f')
    lbl_bg.place(relx=.12,rely=0)

    def back():
        frm.destroy
        mainscreen()
        
    def vDetail():
        empid=e_ID.get()

        def clear():
            frm.destroy()
            empdetailscreen()
   
        try:
            conobj=sqlite3.connect(database='employee.sqlite')
            curobj=conobj.cursor()
            curobj.execute("select *from emp where id=?",(empid,))
            tup=curobj.fetchone()
            conobj.close()

            lbl_id=Label(frm,text=f'Emp ID:\t\t{tup[0]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_id.place(relx=.1,rely=.15)

            lbl_name=Label(frm,text=f'Emp Name:\t{tup[1]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_name.place(relx=.1,rely=.25)

            lbl_dpt=Label(frm,text=f'Emp Dpt:\t{tup[2]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_dpt.place(relx=.1,rely=.35)

            lbl_date=Label(frm,text=f'Mob No:\t\t{tup[3]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_date.place(relx=.1,rely=.45)

            lbl_date=Label(frm,text=f'Address:\t\t{tup[4]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_date.place(relx=.1,rely=.55)

            lbl_date=Label(frm,text=f'Date of joining:\t{tup[5]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_date.place(relx=.1,rely=.65)
            ###########
            lbl_cl=Label(frm,text=f'Casual Leave:\t\t{tup[6]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_cl.place(relx=.6,rely=.15)

            lbl_sl=Label(frm,text=f'Sick Leave:\t\t{tup[7]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_sl.place(relx=.6,rely=.25)

            lbl_bl=Label(frm,text=f'Basic Leave:\t\t{tup[8]}',font=('Arial',20,'bold',),bg='#1a2e1f',fg='white')
            lbl_bl.place(relx=.6,rely=.35)

            btn_clear=Button(frm,text='Clear Details',command=clear,font=('Arial',15,'bold'))
            btn_clear.place(relx=.4,rely=.8)
        except:
            messagebox.showerror('error','Empty Fied or invalid Emp ID')
            clear()

        # btn_back=Button(frm,text='Back',command=mainscreen,font=('Arial',20,'bold'),bg='yellow')
        # btn_back.place(relx=.9,rely=.3)


    ###########
    lbl_ID=Label(frm,text="Enter Emp ID:",font=('Arial',20,'bold'),bg='powder blue')
    lbl_ID.place(relx=.2,rely=.03)

    e_ID=Entry(frm ,font=('Arial',20,'bold'),bg='powder blue',width=10)
    e_ID.place(relx=.35,rely=.03)
    e_ID.focus()

    btn_viewDetail=Button(frm,text='View Details',command=vDetail,font=('Arial',15,'bold'),bg='powder blue')
    btn_viewDetail.place(relx=.52,rely=.03)

    btn_back=Button(frm,text='Back',command=back,font=('Arial',20,'bold'))
    btn_back.place(relx=0,rely=0)
    


def login():
    frm=Frame(win)
    frm.configure(bg='#1a2e1f')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    lbl_bg=Label(frm,image=img1,bg='#1a2e1f')
    lbl_bg.place(relx=.12,rely=0)

    def newpage():
        username=e_admin.get()
        userpass=e_pass.get()
        if username=='admin' or userpass=='admin':
            frm.destroy()
            mainscreen()
        else:
            messagebox.showerror("error",'wrong ID or Password')

    def reset():
        e_admin.delete(0,'end')
        e_pass.delete(0,'end')
        e_admin.focus()

    lbl_admin=Label(frm,text='User name:',font=('Arial',20,'bold'),bg='powder blue')
    lbl_admin.place(relx=.25,rely=.2)

    e_admin=Entry(frm,font=('Arial',20,'bold',),bg='powder blue')
    e_admin.place(relx=.4,rely=.2)
    e_admin.focus()

    lbl_pass=Label(frm,text='Password:',font=('Arial',20,'bold',),bg='powder blue')
    lbl_pass.place(relx=.25,rely=.3)

    e_pass=Entry(frm,font=('Arial',20,'bold'),bg='powder blue',show='*')
    e_pass.place(relx=.4,rely=.3)

    btn_login=Button(frm,text='Login',command=newpage,font=('Arial',20,'bold'),bg='green',fg='white')
    btn_login.place(relx=.4,rely=.4)

    btn_reset=Button(frm,text='Reset',command=reset,font=('Arial',20,'bold'),bg='powder blue')
    btn_reset.place(relx=.5,rely=.4)



login()
win.mainloop()
