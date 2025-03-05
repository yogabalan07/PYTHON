from tkinter import*
from tkinter import messagebox
from tkinter import ttk

admin_data=[]

root=Tk()
root.title("YB software")
root.geometry("1750x700")
root.resizable(True,True)
root.configure(bg="#1CA8D6")





def login():
    global a2
    a2=Frame(a1,bg='#1A5276',height=1000,width=950)
    a2.pack(fill=X)

    
    label3=Label(a1,text="SIGN IN",
            font=("century gothic",25,"bold"),fg="white",bg="#1A5276")
    label3.place(x=500,y=170)
    
    label4=Label(a1,text="Name or User name:",
            font=("century gothic",25,"bold"),fg="white",bg="#1A5276")
    label4.place(x=300,y=240)

    label4=Label(a1,text="Password:",
            font=("century gothic",25,"bold"),fg="white",bg="#1A5276")
    label4.place(x=475,y=340)

    label5=Label(a1,text="Re-Password:",
            font=("century gothic",25,"bold"),fg="white",bg="#1A5276")
    label5.place(x=425,y=440)
    
    
    name=Entry(a2,font=("century gothic",15,"bold"))
    name.place(x=630,y=250,width=220,height=30)

    passwrd=Entry(a2,show='.',font=("century gothic",15,"bold"))
    passwrd.place(x=640,y=345,width=220,height=30)

    repass=Entry(a2,show='.',font=("century gothic",15,"bold"))
    repass.place(x=640,y=450,width=220,height=30)

    reg=Button(a2,text='REGISTER',font=("century gothic",20,"bold"),fg="#1A5276",bg="white")
    reg.place(x=550,y=550)






###-----------------login function call start-------------------###


def admin():
    global a1
    a1=Frame(root,bg='#1A5276',height=1000,width=950)
    a1.pack(fill=X)

    label=Label(root,text="YB SOFTWARES",
            font=("century gothic",50,"bold"),fg="white",bg="#1A5276")
    label.place(x=350,y=70)


    label=Label(a1,text="LOGIN PAGE",font=('Helvetica',35,'bold italic'),fg="#1A5276",bg='white')
    label.place(x=400,y=200)


    

    label2=Label(a1,text="Username:",font=('Helvetica',25,'bold italic'),fg="#1A5276",bg='white')
    label2.place(x=350,y=340)    
    
    
    eb1=Entry(a1,font=("century gothic",15,"bold"))
    eb1.place(x=550,y=350,width=220,height=30)

    label3=Label(a1,text="Password:",font=('Helvetica',25,'bold'),fg="#1A5276",bg='white')
    label3.place(x=350,y=440) 
        
   

    eb2=Entry(a1,show=".",font=("century gothic",15,"bold"))
    eb2.place(x=550,y=450,width=220,height=30)

    def admin_details():
        user=eb1.get()
        passs=eb2.get()
        tesult=[admin for admin in admin_data if admin['name']==user and admin['password']]
        print(result)

        def rem():
            a1.destory()

    lgbtn=Button(a1,text='LOGIN',font=("century gothic",20,"bold"),fg="#1A5276",bg="white")
    lgbtn.place(x=500,y=550)
    lgbtn=Button(a1,text='SIGNUP',font=("century gothic",20,"bold"),fg="#1A5276",bg="white",command=login)
    lgbtn.place(x=650,y=550)


    
###-----------------login function call end-------------------###

#sign up

label=Label(root,text="YB SOFTWARE",
            font=("century gothic",50,"bold"),fg="white",bg="#1A5276")
label.place(x=500,y=258)

label=Label(root,text="POWERED BY YB",
            font=("century gothic",10,"bold"),fg="black",)
label.place(x=800,y=350)
btn=Button(root,text="""  LET's START  """,font=("Helvetica",20,"bold italic"),
           bg="white",fg="#1CA8D6",command=admin)
btn.place(x=750,y=400)





root.mainloop()
