
######################################DATA STRU#############################
#------------------------------------------------------------------------------------------------------------------------------#

from tkinter import* 
from tkinter import messagebox
from tkinter import ttk

##from PIL import Image, Im   ageTk
# Simulated database using a list
admin_data = []

root=Tk()
root.title('CRM')
root.geometry("1530x800+0+0")
root.resizable(True,True)
root.configure(background='#1A5276')









#--------------------Signin PAGES ------------------------------------------
def admin_signin():
    global a2,ebb_8,ebb_9
    a2=Frame(a1,bg='#1A5276',height=1000,width=950) 
    a2.place(x=600,y=0)
    a22=Frame(a11,bg='white',height=1000,width=600)
    a22.place(x=0,y=0)

##    img=Image.open('vas2.jpeg')
##    img=img.resize((650,800))
##    img2=ImageTk.PhotoImage(img)
##    imglabel=Label(a22,image=img2,bg="#1A5276")
##    imglabel.image=img2
##    imglabel.place(x=0,y=0)
    
    label=Label(a2,text="A d m i n  S i g n i n",
           font=('century gothic', 35, 'bold'),fg="white",bg='#1A5276')
    label.place(x=170,y=100)


    label=Label(a2,text="Name ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=150,y=318)
    ety1=Entry(a2)
    ety1.place(x=375,y=330,width=220,height=35)

    label=Label(a2,text="Mobile No ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=150,y=408)
    ety2=Entry(a2)
    ety2.place(x=375,y=420,width=220,height=35)
  
    label=Label(a2,text="Password ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=150,y=498)
    ety3=Entry(a2, show="*")
    ety3.place(x=375,y=500,width=220,height=35)
    

    def save():
        if (ety1.get()=="" or ety2.get()=="" or ety3.get()==""  ): 
            messagebox.showerror("Error", "Enter all details")
        else: 
            op = messagebox.askyesno("Save", "Do you really want to save?")
            if op:
                # Simulating database insert operation
                admin_data.append({
                    'name': ety1.get(),
                    'mobile': ety2.get(),
                    'password': ety3.get()
                })
                messagebox.showinfo("Done","Successfully ID Created")
                a2.destroy()
                a22.destroy()

    b6 = Button(a2,text='Register',bg="#EE8309",fg="white",command=save,font=("century gothic", 13, "bold"),
                     height="1",width="15",bd=0,highlightthickness=2,padx=10,pady=5)
    b6.place(x=200, y=600)

    
    def rem():
        a2.destroy()
        a22.destroy()


    b6 = Button(a2,text='Back',bg="white",fg="black",command=rem,font=("century gothic", 13, "bold"),
                     height="1",width="15",bd=0,highlightthickness=2,padx=10,pady=5)
    b6.place(x=450, y=600)


#--------------------------------------------ADMIN PAGES-------------------------------------------------------------------
 
def admin():
    global a1,a11
    a1=Frame(root,bg='#1A5276',height=1000,width=950) #1A5276
    a1.pack(fill=X)
    a11=Frame(root,bg='white',height=1000,width=600)
    a11.place(x=0,y=0)
    
##    img=Image.open('vas2.jpeg')
##    img=img.resize((650,800))  
##    img2=ImageTk.PhotoImage(img)
##    imglabel=Label(a11,image=img2,bg="#1A5276")
##    imglabel.image=img2
##    imglabel.place(x=0,y=0)

    label=Label(a1,text="A d m i n  D a s h b o a r d",
           font=('century gothic', 30, 'bold'),fg="white",bg='#1A5276')
    label.place(x=750,y=60)

    label=Label(a1,text="Login To Access ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=900,y=200)

    label=Label(a1,text="Username ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=800,y=318)
    eb1=Entry(a1,font=('century gothic', 17, 'bold'))
    eb1.place(x=1000,y=330,width=220,height=35)

    label=Label(a1,text="Password ",
           font=('century gothic', 25, 'bold'),fg="white",bg='#1A5276')
    label.place(x=800,y=418)
    eb2=Entry(a1,show="*",font=('century gothic', 17, 'bold'))
    eb2.place(x=1000,y=430,width=220,height=35)

    def admin_details():
        user=eb1.get()
        passs=eb2.get()   
        # Simulating database select operation 
        result = [admin for admin in admin_data if admin['name'] == user and admin['password'] == passs]
        print(result)
        def welcomee():
            
##            a11.destroy()
##            global a3,a33
##            a33=Frame(a1,bg='#1A5276',height=1000,width=325)
##            a33.place(x=0,y=0)
##            a3=Frame(a1,bg='white',height=1000,width=1225) #1A5276
##            a3.place(x=400,y=0)
##
##
##            img=Image.open('imagee.png')
##            img=img.resize((150,150))
##            img2=ImageTk.PhotoImage(img)
##            imglabel=Label(a33,image=img2,bg="#1A5276")
##            imglabel.image=img2
##            imglabel.place(x=110,y=20)
##            b5 = Button(a33,text='Lead',bg="white",fg="black",font=("century gothic", 13, "bold"),
##                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
##            b5.place(x=90, y=230)
##            b5 = Button(a33,text='Students',bg="white",fg="black",font=("century gothic", 13, "bold"),
##                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
##            b5.place(x=90, y=300)
##            b5 = Button(a33,text='Faculty',bg="white",fg="black",font=("century gothic", 13, "bold"),
##                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
##            b5.place(x=90, y=370)
##            b5 = Button(a33,text='Course',bg="white",fg="black",font=("century gothic", 13, "bold"),
##                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
##            b5.place(x=90, y=440)
##            b5 = Button(a33,text='Finance',bg="white",fg="black",font=("century gothic", 13, "bold"),
##                     height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
##            b5.place(x=90, y=510)
##            b5 = Button(a33,text='Placement',bg="white",fg="black",font=("century gothic", 13, "bold"),
##                         height="1",width="17",bd=0,highlightthickness=2,padx=10,pady=5)
##            b5.place(x=90, y=580)
##            b6 = Button(a33,text='Email',bg="#EE8309",fg="white",font=("century gothic", 13, "bold"),
##                             height="1",width="12",bd=0,highlightthickness=2,padx=10,pady=5)
##            b6.place(x=25, y=700)
##
##            def rem():
##                a3.destroy()
##                a33.destroy()
##
            b6 = Button(a33,text='Back',bg="#EE8309",fg="white",command=rem,font=("century gothic", 13, "bold"),
                             height="1",width="12",bd=0,highlightthickness=2,padx=10,pady=5)
            b6.place(x=200, y=700)
        if (eb1.get()=="" or eb2.get()==""):
            messagebox.showerror("Error", "Enter all details")  
        elif(result):
            messagebox.showinfo("open", "Welcome")
            welcomee()

    b5 = Button(a1,text='Login',bg="#26B3E8",fg="white",command=admin_details,font=("century gothic", 13, "bold"),
                     height="1",width="20",bd=0,highlightthickness=2,padx=10,pady=5)
    b5.place(x=900, y=525)

    label=Label(a1,text="Don't Have Account ? ",
           font=('century gothic', 15, 'bold'),fg="white",bg='#1A5276')
    label.place(x=700,y=605)

    b6 = Button(a1,text='Sign In',bg="#EE8309",fg="white",command=admin_signin,font=("century gothic", 13, "bold"),
                     height="1",width="20",bd=0,highlightthickness=2,padx=10,pady=5)
    b6.place(x=1040, y=595)
    def rem():
        a1.destroy()
        a11.destroy()
    b6 = Button(a1,text='Back',bg="white",fg="black",command=rem,font=("century gothic", 13, "bold"),
                     height="1",width="15",bd=0,highlightthickness=2,padx=10,pady=5)
    b6.place(x=1250, y=720)




#--------------------   U S E R   P A G E S ----------------------------------------------
  
##img=Image.open('imagee.png')
##img=img.resize((150,150))
##img2=ImageTk.PhotoImage(img)
##imglabel=Label(root,image=img2,bg="#1A5276")  
##imglabel.image=img2
##imglabel.place(x=560,y=100)


label=Label(root,text="C R M   S O F T W A R E ",
           font=('century gothic', 45, 'bold'),fg="white",
            bg='#1A5276')
label.place(x=350,y=280)

label=Label(root,text="P o w e r e d    B y  I m a g e c o n",
           font=('century gothic',25, 'bold'),fg="white",
            bg='#1A5276')
label.place(x=400,y=370)

btn_next = Button(root, text='GET STARTED',
                  bg="white", fg="#1A5276",
                  command=admin,
                  font=("Times New Roman", 20, "bold"),
       height="2", width="25", bd=2,
                  highlightthickness=5, padx=10, pady=5,
                  highlightbackground="#1CA8D6")
btn_next.place(x=440, y=550)

root.mainloop()






