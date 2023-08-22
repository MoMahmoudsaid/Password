from tkinter import *
from distutils.command.config import config
import tkinter
import random
import string
from tkinter.tix import ButtonBox
pro = Tk()
menubar = Menu(pro,tearoff=0)
menubar.add_command(label="Open")
menubar.add_command(label="Save")
menubar.add_command(label="Save As")
menubar.add_command(label="Exit")
menubar.add_cascade(label="File",menu=menubar)
pro.config(menu=menubar)
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.punctuation)
s4 = list(string.digits)
bt1 = tkinter.Button(pro,text="Start")
numpass = input("Please Enter Number of Password : ")
while True:
    try:
        numpass = int(numpass)
        if numpass in range(51,999):
            print("Please Enter number from 10 to 50")
            numpass = input("Please Enter Number of Password Again : ")
        elif numpass in range(0,10):
            print("Please Enter number from 10 to 50")
            numpass = input("Please Enter Number of Password Again : ")
        else:
            break
    except:
        print("Please Enter A Valid Number")
        numpass = input("Please Enter Number of Password Again : ")
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
part1 = round(numpass*(30/100))
part2 = round(numpass*(20/100))
password=[]
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):
    password.append(s2[i])
    password.append(s3[i])
random.shuffle(password)
password="".join(password[0:])
print(password)
File=open("password.txt",'a')
File.writelines(password)
File.writelines("\n")
File.close()
bt1.config(command=print(password))
bt1.pack()
pro.mainloop()