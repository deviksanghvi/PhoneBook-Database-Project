import file_1
import sqlite3
con=sqlite3.Connection('ContactBook')
cur=con.cursor()
s={1:'Office',2:'Home',3:'Mobile',4:'Office',5:'Personal'}
from Tkinter import *
from tkMessageBox import *
root1=Tk()
root1.title("Phonebook")
root1.geometry("1100x1000")
cur.execute("create table if not exists Phonebook(First_Name varchar(20),Middle_Name varchar(10),Last_Name varchar(20),Company_Name varchar(20),Address varchar(35),City varchar(15),Pin_Code number(6),Website_URL varchar2(35),Date_of_Birth date,Phone_type varchar(10),Phone_Number integer,Email_type varchar(10),Email_id varchar2(45),S_no integer primary key)")
a=PhotoImage(file="image2.gif")
Label(root1,image=a).grid(row=0,column=1)
Label(root1,text="First Name",font='Arial 15').grid(row=1,column=0)
e=Entry(root1)
e.grid(row=1,column=1)
Label(root1,text="Middle Name",font='Arial 15').grid(row=2,column=0)
e1=Entry(root1)
e1.grid(row=2,column=1)
Label(root1,text="Last Name",font='Arial 15').grid(row=3,column=0)
e2=Entry(root1)
e2.grid(row=3,column=1)
Label(root1,text="Company Name",font='Arial 15').grid(row=4,column=0)
e3=Entry(root1)
e3.grid(row=4,column=1)
Label(root1,text="Address",font='Arial 15').grid(row=5,column=0)
e4=Entry(root1)
e4.grid(row=5,column=1)
Label(root1,text="City",font='Arial 15').grid(row=6,column=0)
e5=Entry(root1)
e5.grid(row=6,column=1)
Label(root1,text="Pin Code",font='Arial 15').grid(row=7,column=0)
e6=Entry(root1)
e6.grid(row=7,column=1)
Label(root1,text="Website URL",font='Arial 15').grid(row=8,column=0)
e7=Entry(root1)
e7.grid(row=8,column=1)
Label(root1,text="Date of Birth",font='Arial 15').grid(row=9,column=0)
e8=Entry(root1)
e8.grid(row=9,column=1)
Label(root1,text="Select Phone Type:",font='Arial 15',fg='Blue').grid(row=10,column=0)
v1=IntVar()
v2=IntVar()
Radiobutton(root1,text='Office',variable=v1,value=1,font='Arial 12').grid(row=10,column=1)
Radiobutton(root1,text="Home",variable=v1,value=2,font='Arial 12').grid(row=10,column=2)
Radiobutton(root1,text="Mobile",variable=v1,value=3,font='Arial 12').grid(row=10,column=3)
Label(root1,text="Phone Number:",font='Arial 15').grid(row=11,column=0)
e9=Entry(root1)
e9.grid(row=11,column=1)
Label(root1,text="Select Email Type:",font='Arial 15',fg='Blue').grid(row=12,column=0)
Radiobutton(root1,text='Office',variable=v2,value=4,font='Arial 12').grid(row=12,column=1)
Radiobutton(root1,text="Personal",variable=v2,value=5,font='Arial 12').grid(row=12,column=2)
Label(root1,text="Email id:",font='Arial 15').grid(row=13,column=0)
e10=Entry(root1)
e10.grid(row=13,column=1)
con.commit()
def info():
    cur.execute("Select max(S_no) from Phonebook")
    v=cur.fetchall()
    if e.get()==e1.get()==e2.get() or (e.get()!="" and e1.get()!="" and e.get()==e1.get()) or (e.get()!="" and e2.get()!="" and e.get()==e2.get()) or e9.get()=="" or e.get()==e1.get()==e2.get()=="" or (e1.get()!='' and e2.get()!='' and e1.get()==e2.get()) :
        showerror('Error','ALL Names are not same in any person and Phone number and Name is required')
    else:
        if v[0][0]==None:
                g=1
        else:
            g=v[0][0]
            g=g+1
        p=(e.get(),e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),s.get(v1.get()),e9.get(),s.get(v2.get()),e10.get(),g)
        if e.get()=='' and e1.get()=='' and e2.get()=='' and e3.get()=='' and e4.get()=='' and e5.get()=='' and e6.get()=='' and e7.get()=='' and e8.get()=='' and  e9.get()==''  and e10.get()=='':
            showinfo('Not Saved','No record saved')
        else:
            cur.execute("insert into Phonebook values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",p)
            showinfo('Saved','record successfully saved')
    cur.execute("Select * from Phonebook")
    k=cur.fetchall()
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    con.commit()
def find():
    root2=Tk()
    root2.title("Search")
    root2.geometry("1100x1000")
    Label(root2,text='Searching Phone Book',font='Arial 25',bg='Pink').grid(row=0,column=1)
    Label(root2,text='Enter name',font='Arial 15').grid(row=1,column=0)
    e11=Entry(root2,width=30)
    e11.grid(row=1,column=1)
    cur.execute("select count(S_no) from Phonebook")
    j=cur.fetchall()
    Label(root2,text=j[0][0]).grid(row=1,column=2)
    con.commit()
##    def dev(v=1):
##        lb.delete(0,END)       
##    e11.bind('<Button 1>',dev)
    def devik(dev=1):
        lb.delete(0,END)
        w=("%"+e11.get()+"%")
        cur.execute("select First_Name,Middle_Name,Last_Name from Phonebook where First_Name like ? or Middle_Name like ? or Last_Name like ?",(w,w,w))
        p=cur.fetchall()
        for j in range(len(p)):
            p1=p[j][0]
            p2=p[j][1]
            p3=p[j][2]
            pf=p1+' '+p2+' '+p3
            lb.insert(END,pf)
    e11.bind('<KeyRelease>',devik)
    lb=Listbox(root2,height=30,width=50)
    lb.grid(row=2,column=1)
    def seen(f=1):
        h=lb.curselection()
        df=lb.get(h)
        u=df.split(" ")
        u1=u[0]
        u2=u[1]
        u3=u[2]
        lb.destroy()
        lb_new=Listbox(root2,height=30,width=50,font='Arial 10')
        lb_new.grid(row=2,column=1)
        cur.execute("Select * from Phonebook where First_Name=? and Middle_Name=? and Last_Name=?",(u1,u2,u3))
        ss=cur.fetchall()
        sss=[]
        sss.append('First Name : '+ss[0][0])
        sss.append('Middle Name : '+ss[0][1])
        sss.append('Last Name : '+ss[0][2])
        sss.append('Company : '+ss[0][3])
        sss.append('Address : '+ss[0][4])
        sss.append('City : '+ss[0][5])
        sss.append('Pin Code : '+str(ss[0][6]))
        sss.append('Website URL : '+ss[0][7])
        sss.append('Date of Birth : '+ss[0][8])
        sss.append('Phone Details...')
        sss.append(str(ss[0][9])+' : '+str(ss[0][10]))
        sss.append('Email Addresses...')
        sss.append(str(ss[0][11])+' : '+str(ss[0][12]))
        def remove():
            q=ss[0][13]
            cur.execute("delete from Phonebook where S_no=?",(q,))
            showinfo('Delete',"record deleted")
            con.commit()
            root2.destroy()
        Button(root2,text='Delete',command=remove).grid(row=3,column=2)
        for i in range(len(sss)):
            lb_new.insert(END,sss[i])
        lb_new.itemconfig(9,fg='Red')
        lb_new.itemconfig(11,fg='Red')
    lb.bind("<<ListboxSelect>>",seen)
    cur.execute("Select First_Name,Middle_Name,Last_Name from Phonebook")
    p=cur.fetchall()
    for j in range(len(p)):
        p1=p[j][0]
        p2=p[j][1]
        p3=p[j][2]
        pf=p1+' '+p2+' '+p3
        lb.insert(END,pf)
    def magic():
        root2.destroy()
    Button(root2,text='Close',font='Arial 12',command=magic).grid(row=3,column=1)
    con.commit()  
def fun():
    root1.destroy()
def editor():
    root2=Tk()
    root2.title("Edit")
    root2.geometry("1100x1000")
    Label(root2,text='Enter name',font='Arial 15').grid(row=1,column=0)
    e11=Entry(root2,width=30)
    e11.grid(row=1,column=1)
    def devik(dev=1):
        lb.delete(0,END)
        w=("%"+e11.get()+"%")
        cur.execute("select First_Name,Middle_Name,Last_Name from Phonebook where First_Name like ? or Middle_Name like ? or Last_Name like ?",(w,w,w))
        p=cur.fetchall()
        for j in range(len(p)):
            p1=p[j][0]
            p2=p[j][1]
            p3=p[j][2]
            pf=p1+' '+p2+' '+p3
            lb.insert(END,pf)
    e11.bind('<KeyRelease>',devik)
    lb=Listbox(root2,height=40,width=50)
    lb.grid(row=2,column=1)
    cur.execute("Select First_Name,Middle_Name,Last_Name from Phonebook")
    p=cur.fetchall()
    for j in range(len(p)):
        p1=p[j][0]
        p2=p[j][1]
        p3=p[j][2]
        pf=p1+' '+p2+' '+p3
        lb.insert(END,pf)
    def magic():
        root2.destroy()
    Button(root2,text='Close',font='Arial 12',command=magic).grid(row=3,column=1)
    def seen1(sw=1):
        h=lb.curselection()
        for k in h:
            df=lb.get(k)
        u=df.split(" ")
        u1=u[0]
        u2=u[1]
        u3=u[2]
        root2.destroy()
        root1=Tk()
        root1.title("Contact_Edit")
        cur.execute("Select * from Phonebook where First_Name=? and Middle_Name=? and Last_Name=?",(u1,u2,u3))
        ss=cur.fetchall()
        Label(root1,text="First Name",font='Arial 15').grid(row=1,column=0)
        e=Entry(root1)
        e.grid(row=1,column=1)
        Label(root1,text="Middle Name",font='Arial 15').grid(row=2,column=0)
        e1=Entry(root1)
        e1.grid(row=2,column=1)
        Label(root1,text="Last Name",font='Arial 15').grid(row=3,column=0)
        e2=Entry(root1)
        e2.grid(row=3,column=1)
        Label(root1,text="Company Name",font='Arial 15').grid(row=4,column=0)
        e3=Entry(root1)
        e3.grid(row=4,column=1)
        Label(root1,text="Address",font='Arial 15').grid(row=5,column=0)
        e4=Entry(root1)
        e4.grid(row=5,column=1)
        Label(root1,text="City",font='Arial 15').grid(row=6,column=0)
        e5=Entry(root1)
        e5.grid(row=6,column=1)
        Label(root1,text="Pin Code",font='Arial 15').grid(row=7,column=0)
        e6=Entry(root1)
        e6.grid(row=7,column=1)
        Label(root1,text="Website URL",font='Arial 15').grid(row=8,column=0)
        e7=Entry(root1)
        e7.grid(row=8,column=1)
        Label(root1,text="Date of Birth",font='Arial 15').grid(row=9,column=0)
        e8=Entry(root1)
        e8.grid(row=9,column=1)
        Label(root1,text="Select Phone Type:",font='Arial 15',fg='Blue').grid(row=10,column=0)
        v1=IntVar()
        v2=IntVar()
        Radiobutton(root1,text='Office',variable=v1,value=1,tristatevalue=0,font='Arial 12').grid(row=10,column=1)
        Radiobutton(root1,text="Home",variable=v1,value=2,tristatevalue=0,font='Arial 12').grid(row=10,column=2)
        Radiobutton(root1,text="Mobile",variable=v1,value=3,tristatevalue=0,font='Arial 12').grid(row=10,column=3)
        Label(root1,text="Phone Number:",font='Arial 15').grid(row=11,column=0)
        e9=Entry(root1)
        e9.grid(row=11,column=1)
        Label(root1,text="Select Email Type:",font='Arial 15',fg='Blue').grid(row=12,column=0)
        Radiobutton(root1,text='Office',variable=v2,value=4,tristatevalue=0,font='Arial 12').grid(row=12,column=1)
        Radiobutton(root1,text="Personal",variable=v2,value=5,tristatevalue=0,font='Arial 12').grid(row=12,column=2)
        Label(root1,text="Email id:",font='Arial 15').grid(row=13,column=0)
        e10=Entry(root1)
        e10.grid(row=13,column=1)
        e.insert(0,ss[0][0])
        e1.insert(0,ss[0][1])
        e2.insert(0,ss[0][2])
        e3.insert(0,ss[0][3])
        e4.insert(0,ss[0][4])
        e5.insert(0,ss[0][5])
        e6.insert(0,ss[0][6])
        e7.insert(0,ss[0][7])
        e8.insert(0,ss[0][8])
        e9.insert(0,ss[0][10])
        e10.insert(0,ss[0][12])
        def info():
            c=ss[0][13]
            cur.execute("delete from Phonebook where S_no=?",(c,))
            con.commit()
            cur.execute("Select max(S_no) from Phonebook")
            v=cur.fetchall()
            if v[0][0]==None:
                    g=1
            else:
                g=v[0][0]
                g=g+1
            p=(e.get(),e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),s.get(v1.get()),e9.get(),s.get(v2.get()),e10.get(),g)
            if e.get()=='' and e1.get()=='' and e2.get()=='' and e3.get()=='' and e4.get()=='' and e5.get()=='' and e6.get()=='' and e7.get()=='' and e8.get()=='' and  e9.get()==''  and e10.get()=='':
                showinfo('Not Edited','No record edit')
            else:
                cur.execute("insert into Phonebook values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",p)
                showinfo('Edited','record successfully edited')
            cur.execute("Select * from Phonebook")
            k=cur.fetchall()
            e.delete(0,END)
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
            e7.delete(0,END)
            e8.delete(0,END)
            e9.delete(0,END)
            e10.delete(0,END)
            con.commit()
        def fun():
            root1.destroy()
        Button(root1,text="Save",font='Arial 12',command=info).grid(row=14,column=0)
        Button(root1,text="Close",font='Arial 12',command=fun).grid(row=14,column=2)
        con.commit()
    lb.bind("<<ListboxSelect>>",seen1)
    con.commit()   
Button(root1,text="Save",font='Arial 12',command=info).grid(row=14,column=0)
Button(root1,text="Search",font='Arial 12',command=find).grid(row=14,column=1)
Button(root1,text="Close",font='Arial 12',command=fun).grid(row=14,column=2)
Button(root1,text="Edit",font='Arial 12',command=editor).grid(row=14,column=3)
con.commit()
mainloop()
