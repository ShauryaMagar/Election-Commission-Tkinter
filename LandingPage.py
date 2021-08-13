from tkinter import *

import voter
import AdminLogin
def voterfunc(root):
    root.destroy()
    voter.voterdashboard()

def admin(root):
    root.destroy()
    AdminLogin.adminlog()


def call():
    root = Tk()
    root.geometry("800x800")
    root.title("Election Commission")
    background_image = PhotoImage(file="bg.png")
    background_label = Label(root, image = background_image,bg ="#ffffff")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_frame = Frame(root,height = "600", width = "300",bg="#ffffff")
    my_frame.pack(pady=175, padx=50 )
    Label(my_frame, text="Election Commission", font="comicsansms 19 bold", padx="10",pady="10",bg = "#ffffff").grid(row=0, column=0, columnspan=2, sticky=N)
    Label(my_frame, text="", font="comicsansms 19",bg="#ffffff").grid(row=1, column=0, columnspan=2)
    Label(my_frame, text="Voter Details", font="comicsansms 19",bg="#ffffff").grid(row=2, column=0, columnspan = 2)
    Button(my_frame, text="Go", command=lambda: voterfunc(root), font="comicsansms 15",padx="10",pady="10",bg="#ffffff").grid(row=3, column=0 , columnspan = 2)
    Label(my_frame, text="", font="comicsansms 19",bg="#ffffff").grid(row=4, column=0, columnspan=2)
    Label(my_frame, text="Admin Login", font="comicsansms 19",bg="#ffffff").grid(row=5, column=0,columnspan = 2)
    Button(my_frame, text="Go", command=lambda: admin(root), font="comicsansms 15",padx="10",pady="10",bg="#ffffff").grid(row=6, column=0, columnspan = 2)
    root.mainloop()

