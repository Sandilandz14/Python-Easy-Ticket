from tkinter import *

root = Tk()
root.config(bg="red")
root.title("file-handling")
root.geometry("500x300")


def creat_txt():
    text_info = text.get("1.0",END)
    print(text_info)

    txtfile = open("my_weekend_activities.txt", "w")
    txtfile.write(text_info)
    txtfile.close()


def display():
    reader = open("my_weekend_activities.txt","r")
    activities=reader.read()
    text.insert(END,activities)
    reader.close()


def append():
    reader = open("my_weekend_activities.txt","w")
    reader.write(text.get(1.0,END))


def clear():
    reader = open('my_weekend_activities.txt','r+')

    reader.truncate(0)

    text.delete(1.0, END)

def exit():
    root.destroy()

btn1=Button(root, text="My Weekend Activities")
btn1.pack()
btn1.place(x = 170, y = 10)

text = Text(root, width = 40, height = 10)
text.pack()
text.place(x = 90, y = 50)

btn2 = Button(root, text="Create Text File", command=creat_txt)
btn2.pack()
btn2.place(x = 30, y = 230)

btn3 = Button(root, text="Display", command=display)
btn3.pack()
btn3.place(x = 165, y = 230)

btn4 = Button(root, text="Append",command=append)
btn4.pack()
btn4.place(x = 245, y = 230)

btn5 = Button(root, text="Clear",command=clear)
btn5.pack()
btn5.place(x = 325, y = 230)

btn6 = Button(root, text="Exit",command=exit)
btn6.pack()
btn6.place(x = 395, y = 230)
root.mainloop()
