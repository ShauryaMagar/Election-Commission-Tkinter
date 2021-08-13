from tkinter import *
import admindash
import tkinter.messagebox as tmsg
import mysql.connector as c
conn = c.connect(host="localhost" , user = "root" , passwd="12345",database = 'voter')
mycur= conn.cursor()


def findvoter(voterid, name, addr, dob, gender, mobile):
    print(voterid.get())
    # find the voter details of voter id, then set values of name, addr using name.set(value)
    q = "select name1,dob,address,gender,num from addvoter where id= %s"
    t=(voterid.get(),)
    mycur.execute(q,t)
    r= mycur.fetchone()
    
    print(mobile)
    name.set(r[0])
    dob.set(r[1])
    addr.set(r[2])
    gender.set(r[3])
    mobile.set(r[4])



def goback(root):
    root.destroy()
    admindash.admindashboard()

def updateVoter(voterid, name, addr, dob, gender, mobile):
    print(name)
    # send an update request from here to mysql
    q = "update addvoter set name1=%s,dob=%s,address=%s,gender=%s,num=%s where id = %s" 
    tup=(name.get(),dob.get(),addr.get(),gender.get(),mobile.get(),voterid.get(),)
    mycur.execute(q,tup)
    conn.commit()
    tmsg.showinfo("Successful", "The Voter's data has been Updated")



def updatev():
    root = Tk()
    root.geometry("800x800")
    root.title("Election Commission")
    background_image = PhotoImage(file="bg.png")
    background_label = Label(root, image = background_image ,bg ="#ffffff")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_frame = Frame(root, height="600", width="300", bg="#ffffff")
    my_frame.pack(pady=185, padx=50)
    Label(my_frame, text="Update Voter", font="comicsansms 19 bold", padx=50, bg='#ffffff').grid(row=0, column=0, columnspan=3)
    Label(my_frame, text="Enter voter id", font="comicsansms 15", padx=30, pady=5, bg='#ffffff').grid(row=1, column=0)
    voterid = StringVar()
    name = StringVar()
    addr = StringVar()
    dob = StringVar()
    gender = StringVar()
    mobile = IntVar()
    Entry(my_frame, textvariable=voterid, bg='#ffffff').grid(row=1, column=1)
    Button(my_frame, text="Find voter", font="comicsansms 12", command=lambda: findvoter(voterid, name, addr, dob, gender, mobile), bg='#ffffff').grid(row=1, column=2)
    Label(my_frame, text="Name", font="comicsansms 15", padx=30, pady=5, bg='#ffffff').grid(row=2, column=0)
    Entry(my_frame, textvariable=name, bg='#ffffff').grid(row=2, column=1)
    Label(my_frame, text="Address", font="comicsansms 15", padx=30, pady=5 , bg='#ffffff').grid(row=3, column=0)
    Entry(my_frame, textvariable=addr , bg='#ffffff').grid(row=3, column=1)
    Label(my_frame, text="DOB", font="comicsansms 15", padx=30, pady=5 , bg='#ffffff').grid(row=4, column=0)
    Entry(my_frame, textvariable=dob, bg='#ffffff').grid(row=4, column=1)
    Label(my_frame, text="Gender", font="comicsansms 15", padx=30, pady=5, bg='#ffffff').grid(row=5, column=0)
    Entry(my_frame, textvariable=gender, bg='#ffffff').grid(row=5, column=1)
    Label(my_frame, text="Mobile", font="comicsansms 15", padx=30, pady=5, bg='#ffffff').grid(row=6, column=0)
    Entry(my_frame, textvariable=mobile, bg='#ffffff').grid(row=6, column=1)
    Label(my_frame, text="    ", bg='#ffffff').grid(row=7)
    Button(my_frame, text="Go back", font="comicsansms 12",command=lambda: goback(root), bg='#ffffff').grid(row=8, column=0)
    Label(my_frame, text="    ", bg='#ffffff').grid(row=8, column=1)
    Button(my_frame, text="Update voter", font="comicsansms 12",command=lambda: updateVoter(voterid, name, addr, dob, gender, mobile), bg='#ffffff').grid(row=8, column=2)
    root.mainloop()

