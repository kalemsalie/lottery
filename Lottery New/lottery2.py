import random
from tkinter import *
from tkinter import simpledialog,messagebox

window2 = Tk()
window2.title("National Lottery")
window2.geometry("500x500")
mynumbers = set()

lot_num = set()

def randomnums():
    lot_num = set()

    for i in range (0,6):
        number = random.randint(1,49)

        while number in lot_num:
            number= random.randint(1,49)
        lot_num.add(number)


    lbl2.config(text=str("The Lottery Numbers: "+str(lot_num))) 

    counter= 0

    for number in mynumbers:
        if number in lot_num:
            counter +=1
        lbl4.config(text=str("You guessed:" + str(counter) + " number(s) correctly."))

    if counter == 6:

        messagebox.showinfo("Thanks For Playing","Congratulations! You have won R10 000!!!")

        file=open('/home/user/Desktop/lotteryinfo.txt','a')
        file.write("\n"+"Amount won: You have won R 10 000")
        file.close()

    elif counter ==5:

        messagebox.showinfo("Thanks For Playing","Congrtaulations! You have won R 8,584.00")

        file=open('/home/user/Desktop/lotteryinfo.txt','a')
        file.write("\n"+"Amount won: You have won R 8,584.00")
        file.close()

    elif counter ==4:

        messagebox.showinfo("Thanks For Playing","Congrtaulations! You have won R 2,384.00")

        file=open('/home/user/Desktop/lotteryinfo.txt','a')
        file.write("\n"+"Amount won: You have won R 2,384.00")
        file.close()

    elif counter ==3:

        messagebox.showinfo("Thanks For Playing","Amount won:R 100.50")

        file=open('/home/user/Desktop/lotteryinfo.txt','a')
        file.write("\n"+"Amount won: You have won R100.50")
        file.close()

    elif counter ==2:

        messagebox.showinfo("Thanks For Playing","You have won R 20")
        file=open('/home/user/Desktop/lottery.txt','a')
        file.write("\n"+"Amount won:You have won R20.")
        file.close()

    elif counter <=1:
        messagebox.showinfo("Thanks For Playing","You have not won anything.")
        file=open('/home/user/Desktop/lotteryinfo.txt','a')
        file.write("\n"+"Amount won: You have not won anything.")

        file.close()

        lbl4.config(text=str("You guessed:" + str(counter) + " number(s) correctly!"))
    

    





mynumbers = set()
def mylist():
    
    try:
        num1 = int(n1.get())
        mynumbers.add(num1)

        num2 = int(n2.get())
        mynumbers.add(num2)

        num3 = int(n3.get())
        mynumbers.add(num3)

        num4 = int(n4.get())
        mynumbers.add(num4)

        num5 = int(n5.get())
        mynumbers.add(num5)

        num6 = int(n6.get())
        mynumbers.add(num6)

    except ValueError:



        messagebox.showerror("Error","Please Use Numbers Only")

    for i in mynumbers:
       if i >49:
          messagebox.showerror("Error","Number Greater Than 49 Are Not Allowed")

    

n1 = Entry(window2, width=3)
n2 = Entry(window2, width=3)
n3 = Entry(window2, width=3)
n4 = Entry(window2, width=3)
n5 = Entry(window2, width=3)
n6 = Entry(window2, width=3)

n1.place(x=110, y=20)
n2.place(x=160, y=20)
n3.place(x=210, y=20)
n4.place(x=260, y=20)
n5.place(x=310, y=20)
n6.place(x=360, y=20)

lbl1 = Label(window2, text="Enter 6 Numbers Between 1 and 49")
lbl2 = Label(window2)
lbl3 = Label(window2)
lbl4 = Label(window2)

lbl1.place(x=134, y=50)
lbl2.place(x=90, y=150)
lbl3.place(x=90, y=190)
lbl4.place(x=90, y=230)


btn1 = Button(window2, text="Play", command=randomnums)
exitbtn = Button(window2, text="Exit", command=exit)

btn1.place(x=225, y=80)
exitbtn.place(x=225, y=450)

def exit():
    sure = messagebox.askyesno(title="Alert",message="Are you sure you want to exit this app?")
    if sure==True:
        window.destroy()
    else:
        return  None


window2.mainloop()


