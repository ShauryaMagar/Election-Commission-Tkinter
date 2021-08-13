from tkinter import *

import LandingPage
import tkinter.messagebox as tmsg
import mysql.connector as c
conn = c.connect(host="localhost" , user = "root" , passwd="1234",database = 'voter')
mycur= conn.cursor()


def goback(root):
    root.destroy()
    LandingPage.call()

def submitDetails(voterid,dob,name,addr,gender,mobile):
    if voterid.get() == "" or dob.get() == "":
        tmsg.showinfo("Error", "Enter all fields")
    else:

        # find the voter details of voter id, then set values of name, addr using name.set(value)
        q = "select name1,dob,address,gender,num from addvoter where id= %s"
        t = (voterid.get(),)
        mycur.execute(q, t)
        r = mycur.fetchone()

        dob2 = r[1]

        print(dob)
        if (dob.get()== dob2):
            name.set(r[0])
            dob.set(r[1])
            addr.set(r[2])
            gender.set(r[3])
            mobile.set(r[4])
        else:
            tmsg.showinfo("Unscessfull", "Incorrect Details")

def voterdashboard():
    root = Tk()
    root.geometry("800x800")
    root.title("Election Commission")
    background_image = PhotoImage(file="bg.png")
    background_label = Label(root, image = background_image ,bg ="#ffffff")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_frame = Frame(root, height="600", width="300", bg="#ffffff")
    my_frame.pack(pady=160, padx=50)
    Label(my_frame, text="Voter Details", font="comicsansms 19 bold", bg="#ffffff").grid(row=0, column=0, columnspan=2 ,sticky = N)
    voterid = StringVar()
    name = StringVar()
    addr = StringVar()
    dob = StringVar()
    gender = StringVar()
    mobile = IntVar()
    Label(my_frame, text="Enter Voter ID  ", font="comicsansms 10",pady=15, bg="#ffffff").grid(row=1, column=0)
    Entry(my_frame, textvariable=voterid, bg="#ffffff").grid(row=1, column=1)
    Label(my_frame, text="Enter Date of Birth  ", font="comicsansms 10",pady=15, bg="#ffffff").grid(row=2, column=0)
    Entry(my_frame, textvariable=dob, bg="#ffffff").grid(row=2, column=1)
    Button(my_frame, text="Submit", command=lambda: submitDetails(voterid,dob,name,addr,gender,mobile), font="comicsansms 10", bg="#ffffff").grid(row=4,column =1)
    Button(my_frame, text="Back", command=lambda: goback(root), font="comicsansms 10", bg="#ffffff").grid(row=4, column=0)

    Label(my_frame, text=" ", bg='#ffffff').grid(row=6, column=1)
    Label(my_frame, text="Name", font="comicsansms 10", padx=30, pady=5, bg='#ffffff').grid(row=7, column=0)
    Entry(my_frame, textvariable=name, bg='#ffffff').grid(row=7, column=1)
    Label(my_frame, text="Address", font="comicsansms 10", padx=30, pady=5, bg='#ffffff').grid(row=8, column=0)
    Entry(my_frame, textvariable=addr, bg='#ffffff').grid(row=8, column=1)
    Label(my_frame, text="DOB", font="comicsansms 10", padx=30, pady=5, bg='#ffffff').grid(row=9, column=0)
    Entry(my_frame, textvariable=dob, bg='#ffffff').grid(row=9, column=1)
    Label(my_frame, text="Gender", font="comicsansms 10", padx=30, pady=5, bg='#ffffff').grid(row=10, column=0)
    Entry(my_frame, textvariable=gender, bg='#ffffff').grid(row=10, column=1)
    Label(my_frame, text="Mobile", font="comicsansms 10", padx=30, pady=5, bg='#ffffff').grid(row=11, column=0)
    Entry(my_frame, textvariable=mobile, bg='#ffffff').grid(row=11, column=1)
    root.mainloop()


