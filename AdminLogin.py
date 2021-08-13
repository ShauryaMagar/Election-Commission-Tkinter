from tkinter import *
import tkinter.messagebox as tmsg
import admindash
import LandingPage


def gotoadmin(usernamvalue, passvalue, root):
    if usernamvalue.get() == "" or passvalue.get() == "":
        tmsg.showinfo("Error", "Enter all fields")
    elif usernamvalue.get() == "admin" or passvalue.get() == "admin":
        print(usernamvalue.get(), passvalue.get())
        root.destroy()
        admindash.admindashboard()
    else:    
        tmsg.showinfo("Error", "Enter valid credentials")

def goback(root):
    root.destroy()
    LandingPage.call()



def adminlog():
    root = Tk()
    root.geometry("800x800")
    root.title("Election Commission")
    background_image = PhotoImage(file="bg.png")
    background_label = Label(root, image = background_image,bg ="#ffffff")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_frame = Frame(root,height = "600", width = "300",bg="#ffffff")
    my_frame.pack(pady=180, padx=50 )
    Label(my_frame, text="Admin Login", font="comicsansms 19 bold", padx=50, pady=30 ,bg="#ffffff").grid(row=0, column=0, columnspan=2, sticky=N)
    Label(my_frame, text="Username", font="comicsansms 19", padx=80, pady=20,bg="#ffffff").grid(row=1, column=0)
    usernamevalue = StringVar()
    passvalue = StringVar()
    Entry(my_frame, textvariable=usernamevalue).grid(row=1, column=1)
    Label(my_frame, text="Password", font="comicsansms 19", padx=80, pady=20,bg="#ffffff").grid(row=2, column=0)
    Entry(my_frame, textvariable=passvalue).grid(row=2, column=1)
    Label(my_frame, text="", font="comicsansms 19", bg="#ffffff").grid(row=3, column=0, columnspan=2)
    Button(my_frame, text="Login", command=lambda: gotoadmin(usernamevalue, passvalue, root), font="comicsansms 15",bg="#ffffff").grid(row=4, column=1)
    Button(my_frame, text="Back", command=lambda: goback(root),font="comicsansms 15",bg="#ffffff").grid(row=4, column=0)
    root.mainloop()

