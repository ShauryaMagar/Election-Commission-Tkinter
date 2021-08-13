from tkinter import *
import admindash
import tkinter.messagebox as tmsg
import mysql.connector as c
conn = c.connect(host="localhost" , user = "root" , passwd="1234",database = 'voter')
mycur= conn.cursor()

def deleteVoter(voterid):
    if voterid == "":
        print("Values required")
    else:
        
    # find voter id from mysql and delete the voter
        q=" delete from addvoter where id= %s "
        tup1=(voterid,)
        mycur.execute(q,tup1)
        conn.commit()
        print(voterid)
        tmsg.showinfo("Successful", "The Voter's data has been Deleted")

def goback(root):
    root.destroy()
    admindash.admindashboard()

def deletev():
    root = Tk()
    root.geometry("800x800")
    root.title("Election Commission")
    background_image = PhotoImage(file="bg.png")
    background_label = Label(root, image = background_image,bg ="#ffffff")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_frame = Frame(root, height="600", width="300", bg="#ffffff")
    my_frame.pack(pady=200, padx=50)
    Label(my_frame, text="Delete Voter", font="comicsansms 19 bold", padx=50, pady=30, bg='#ffffff').grid(row=0, column=0, columnspan=2)
    voterid = StringVar()
    Label(my_frame, text="Enter voter id", font="comicsansms 15", padx=30, pady=5, bg='#ffffff').grid(row=1, column=0)
    Entry(my_frame, textvariable=voterid, bg='#ffffff').grid(row=1, column=1)
    Label(my_frame, text="    ", bg='#ffffff').grid(row=2, column=1)
    Button(my_frame, text="Go back", font="comicsansms 12",command=lambda: goback(root), bg='#ffffff').grid(row=3, column=0)
    Label(my_frame, text="    ", bg='#ffffff').grid(row=3, column=1)
    Button(my_frame, text="Delete voter", font="comicsansms 12", command=lambda: deleteVoter(voterid.get()), bg='#ffffff').grid(row=3, column=2)
    root.mainloop()

