password = hash("zahraismylove")


import string
import os
import sys
import random
import time 
import webbrowser
from colorama import Fore

print(Fore.RED + " HI" , os.getlogin())
p = input("please Enter The Password : \n ")

if hash(p) == password :
    print("WELCOME ...")
    time.sleep(1)
    while True :
        print("This App Is a TOOL BOX")
        print(" 1 : Generate a Password \n",
               "2 : Open Somthing \n",
               "3 : Open Calculate \n",
               "4 : Open Some URL \n",
               "5 : Open a Game \n",
               "Enter : Exit \n",
              )
        x = input("")
        if x != "" :
            y = int(x)
        else :
            print("Good Bye Dear ... ", " :) ")
            time.sleep(1)
            break
        if y == 1 :
            z = int(input("please Enter The Length Of The Password : "))
            name = input("please enter your name : ")
            last_name = input("please enter your last name : ")
            phone_number = input("please enter your phone number : ")

            def makepassword(stringLength=z):
                letters = name + last_name + phone_number
                return ''.join(random.choice(letters) for i in range(stringLength))

            print("generated pass is : " ,  makepassword()) 
        elif y == 2 :
            y = input("please Enter The File's Addres : ")
            os.system("%s" % y)
        elif y == 3 :
            os.system("calc.exe")
        elif y == 4 :
            web = input("Please Enter The URL : [GOOGLE.COM]  ")
            if web == "" :
                webbrowser.open("https://www.google.com/")
            else :
                webbrowser.open("%s" %web)
            print("opened :)")
        elif y == 5 :
            os.system("x_o.py")
        else :
            print("  THIS IS NOT DEFINED\n ","TRY AGAIN :) ")
        
else :
    print("The Pass Is Wrong , Try Again")
        

