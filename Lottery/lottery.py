import random
from tkinter import *

def main():
  print("Click")
  window2 = Tk()
  window2.title("National Lottery")
  window2.geometry("500x500")
  
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

  lbl1.place(x=134, y=50)

  
  
  
  
  
  
  
  
  
  window2.mainloop()

window = Tk()
window.title("National Lottery")
window.geometry("500x200")

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
button1.place(x=220, y=100)




userNumbers = []
#we want the user to input 6 numbers
for i in range(0,6):

    number = int(input("Please enter a number between 1 and 49:"))
    while (number in userNumbers or number<1 or number>49): #make sure user is not entering a same number or numb out of range. use while loop
        print("invalid number, try again")
        number = int(input("Please enter a number between 1 and 49:")) # put this into while loop

#if number is valid it will be appended to list of users.
    userNumbers.append(number)

#---------------------------------------------------------------------


lot_num = [] #intialize empty list

for i in range (0,6): #used a for loop that repeats 6 times, to generate r random numbers.
  number = random.randint(1,49)

  while number in lot_num:
    number= random.randint(1,49)
#make sure these numbers are unique, using a while loop this checks if the number is already in the list,
#if it is,then we need to create a new random number, do it again until we find a unique number


  lot_num.append(number) #once we have a new number, we append it to our list.

#sort list in ascending order.
lot_num.sort()

#-----------------------------------------
#Display list

#display user selection.
print("These are your chosen lottery numbers:")
print(userNumbers)

print(">>>Todays lottery numbers are:")
print(lot_num)

#--------------------------------------------------------------
#now we are comapring both lists to see if we have won anything
#count hw many of the numbers appear in both lists

#we use a counter, and initialize it to zero

counter= 0
#for each number from the userNUmbers, if the number is in the lottery list, the counter will increment by 1.
for number in userNumbers:
    if number in lot_num:
        counter +=1

print("You guessed:" + str(counter) + " number(s) correctly") #convert counter to string

window.mainloop()
