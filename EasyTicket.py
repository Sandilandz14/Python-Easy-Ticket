#OOP Task // Easy Ticket

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Easy Ticket")
root.geometry("500x800")

#Creating variables
variables=["Soccer","Movie","Theater"]
sctcket= 40
mvietcket= 75
thtretkt= 100


label1 = Label(root, text="Enter Your Cell Number")
label1.pack()
label1.place(x = 30, y = 200)

cellno=Entry(root, textvariable="")
cellno.pack()
cellno.place(x = 250, y = 200)

label2=Label(root, text="Select Category")
label2.pack()
label2.place(x = 30, y = 300)

cat = ttk.Combobox(root, value=variables)
cat.pack()
cat.place(x = 250, y = 300)
cat.config(width=20)

label3=Label(root, text="Number Of Tickets")
label3.pack()
label3.place(x = 30, y = 400)

nrtickets= Spinbox(root, from_=0, to=20, state="readonly")
nrtickets.pack()
nrtickets.place(x = 250, y = 400)

ans1=Label(root)
ans1.pack()
ans1.place(x = 60, y = 600)


class clsTicketSales:


    def __init__(self, cellno, nrtickets,tprice):
        self.cellno=cellno
        self.nrtickets=nrtickets
        self.tprice=tprice
        return


def calc():

    tcketsale= clsTicketSales(cellno.get(),float(nrtickets.get()), cat.get())

    if cat.get() == "Soccer":
        scprice = sctcket * int(nrtickets.get()) + (14/100)
        ans1.config(text = "Price:" + str(scprice) + "\n" + "tickets:" + str(nrtickets.get()) + "\n" + "numbers:" + str(cellno.get()))
    if cat.get() == "Movie":
        mvprice = sctcket * int(nrtickets.get()) + (14/100)
        ans1.config(text = "Price:" + str(mvprice) + "\n" + "tickets:" + str(nrtickets.get()) + "\n" + "numbers:" + str(cellno.get()))
    if cat.get() == "Theater":
        thtrprice = sctcket * int(nrtickets.get()) + (14/100)
        ans1.config(text = "Price:" + str(thtrprice) + "\n" + "tickets:" + str(nrtickets.get()) + "\n" + "numbers:" + str(cellno.get()))



calbtn= Button(root, text="Calculate", command=calc)
calbtn.pack()
calbtn.place(x = 30, y = 500)

root.mainloop()
