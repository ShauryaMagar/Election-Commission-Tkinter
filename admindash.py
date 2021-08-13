from tkinter import *
import addvoter
import updatevoter
import deletevoter
import LandingPage

def addvoterfunc(root):
    root.destroy()
    addvoter.addv()


def updatevoterfunc(root):
    root.destroy()
    updatevoter.updatev()


def deletevoterfunc(root):
    root.destroy()
    deletevoter.deletev()

def goback(root):
    root.destroy()
    LandingPage.call()

def admindashboard():
    root = Tk()
    root.geometry("800x800")

    background_image = PhotoImage(file="bg.png")
    background_label = Label(root, image = background_image ,bg ="#ffffff")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_frame = Frame(root, height="600", width="300", bg="#ffffff")
    my_frame.pack(pady=135, padx=50)
    Label(my_frame, text="Welcome", font="comicsansms 20 bold", pady=25,bg="#ffffff").pack(fill=X)
    Button(my_frame, text="Add voter", command=lambda: addvoterfunc(root), font="comicsansms 15",bg="#ffffff").pack()
    Label(my_frame, text="", pady=15 ,bg="#ffffff").pack()
    Button(my_frame, text="Update voter", command=lambda: updatevoterfunc(root), font="comicsansms 15",bg="#ffffff").pack()
    Label(my_frame, text="", pady=15 ,bg="#ffffff").pack()
    Button(my_frame, text="Delete voter", command=lambda: deletevoterfunc(root), font="comicsansms 15",bg="#ffffff").pack()
    Label(my_frame, text="", pady=15 ,bg="#ffffff").pack()
    Button(my_frame, text="Go back", command=lambda: goback(root), font="comicsansms 15",bg="#ffffff").pack()
    root.mainloop()

