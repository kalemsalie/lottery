import random
from tkinter import *
from tkinter import simpledialog,messagebox
from datetime import datetime

window = Tk()
window.title("National Lottery")
window.geometry("500x200")

today = datetime.today().strftime('%Y-%m-%d')

def main():
  try:
    age = int(entry2.get())
    if age <18:
      raise ValueError

  except ValueError as e:
    messagebox.showerror("PROHIBITED","You Are Underage, Cannot Play")
    return None

  else:
    if age >=18:
      messagebox.showinfo("Successful","You Are Qualified To Play") 

      file=open("/home/user/Desktop/lotteryinfo.txt","w")
      file.write(
        "player:" + str(entry1.get())
        +"\n"+
        "Age:"+ str(entry2.get())+"\n"+
        "Date:"+ str(today))
      
      file.close()

      window.withdraw()
      import lottery2

 
  

  

label1 = Label(window, text="Welcome To The Lottery")
label2 = Label(window, text="Enter Your Name: ")
label3 = Label(window, text="Enter Your Age: ")
label4 = Label(window, text="no u/18's allowed")

entry1 = Entry(window)
entry1.place(x=150, y=30)
entry2 = Entry(window, width=3)
entry2.place(x=150, y=60)

label1.place(x=175,y=0)
label2.place(x=20, y=30)
label3.place(x=20, y=60)
label4.place(x=200, y=150)

button1 = Button(window, text="Submit", command=main)
exitbtn1 = Button(window, text="Exit", command=exit)

button1.place(x=220, y=100)
exitbtn1.place(x=220, y=175)

def exit():
    sure = messagebox.askyesno(title="Alert",message="Are you sure you want to exit this app?")
    if sure==True:
        window.destroy()
    else:
        return  None





window.mainloop()
