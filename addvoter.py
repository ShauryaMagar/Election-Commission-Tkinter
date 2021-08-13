from tkinter import *
import admindash
import tkinter.messagebox as tmsg
import mysql.connector as c
conn = c.connect(host="localhost" , user = "root" , passwd="1234",database = 'voter')
mycur= conn.cursor()

def gotoadmin(name, dob, addr, gender, mobile,voterid, root):
    q = "insert into addvoter values(%s,%s,%s,%s,%s,%s)" 
    tup=(name,dob,addr,gender,mobile,voterid)
    mycur.execute(q,tup)
    conn.commit()
    tmsg.showinfo("Successful", "Data Inserted")
    root.destroy()
    admindash.admindashboard()

def goback(root):
    root.destroy()
    admindash.admindashboard()

def addv():
    root = Tk()
    root.geometry("800x800")
    root.title("Election Commission")
    background_image = PhotoImage(file="bg.png")
    background_label = Label(root, image = background_image, bg ="#ffffff")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_frame = Frame(root,height = "500", width = "300",bg="#ffffff")
    my_frame.pack(pady=190, padx=50 )
    Label(my_frame, text="Add Voter", font="comicsansms 19 bold" ,padx = 50,bg="#ffffff").grid(row=0, column=0, columnspan=3)
    Label(my_frame, text="Name", font="comicsansms 19", padx=80, pady=5 ,bg="#ffffff").grid(row=1, column=0)
    name = StringVar()
    dob = StringVar()
    addr = StringVar()
    gender = StringVar()
    mobile = IntVar()
    voterid = StringVar()
    Entry(my_frame, textvariable=name ,bg="#ffffff").grid(row=1, column=1)
    Label(my_frame, text="Date of birth", font="comicsansms 15", padx=80, pady=5 ,bg="#ffffff").grid(row=2, column=0)
    Entry(my_frame, textvariable=dob ,bg="#ffffff").grid(row=2, column=1)
    Label(my_frame, text="Address", font="comicsansms 15", padx=80, pady=5 ,bg="#ffffff").grid(row=3, column=0)
    Entry(my_frame, textvariable=addr ,bg="#ffffff").grid(row=3, column=1)
    Label(my_frame, text="Gender", font="comicsansms 15", padx=80, pady=5 ,bg="#ffffff").grid(row=4, column=0)
    Entry(my_frame, textvariable=gender ,bg="#ffffff").grid(row=4, column=1)
    Label(my_frame, text="Mobile number", font="comicsansms 15", padx=80, pady=5 ,bg="#ffffff").grid(row=5, column=0)
    Entry(my_frame, textvariable=mobile ,bg="#ffffff").grid(row=5, column=1)
    Label(my_frame, text="Voter ID", font="comicsansms 15", padx=80, pady=5 ,bg="#ffffff").grid(row=6, column=0)
    Entry(my_frame, textvariable=voterid).grid(row=6, column=1)
    Label(my_frame, text="", bg="#ffffff").grid(row =7)
    Button(my_frame, text="Back", command=lambda: goback(root),font="comicsansms 15",bg="#ffffff").grid(row=8, column=0)

    Button(my_frame, text=" Add ", command=lambda: gotoadmin(name.get(), dob.get(), addr.get(), gender.get(), mobile.get(),voterid.get(), root),
           font="comicsansms 15",bg="#ffffff").grid(row=8, column=1)
    root.mainloop()



