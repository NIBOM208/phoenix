password = hash("phoenix")


import string
import os
import sys
import random
import time 
import webbrowser
from requests import get

ip = get('https://api.ipify.org').text

print('''
\033[1;34m
                       ..:::::::::..
                  ..:::aad8888888baa:::..
              .::::d:?88888888888?::8b::::.
             .:::d8888:?88888888??a888888b:::.
          .:::d8888888a8888888aa8888888888b:::.
         ::::dP::::::::88888888888::::::::Yb::::
        ::::dP:::::::::Y888888888P:::::::::Yb::::
       ::::d8:::::::::::Y8888888P:::::::::::8b::::
      .::::88::::::::::::Y88888P::::::::::::88::::.
      :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
      :::::::Y88888888888P::|::Y88888888888P:::::::
      ::::::::::::::::888:::|:::888::::::::::::::::
      `:::::::::::::::8888888888888b::::::::::::::'
       :::::::::::::::88888888888888::::::::::::::
        :::::::::::::d88888888888888:::::::::::::
         ::::::::::::88::88::88:::88::::::::::::
          `::::::::::88::88::88:::88::::::::::'
            `::::::::88::88::P::::88::::::::'
              `::::::88::88:::::::88::::::'
                 ``:::::::::::::::::::''
                      ``:::::::::''

\033[1;m
\033[1;32m
      github : https://github.com/nibom208
\033[1;34m
your public ip addres
=====================\033[1;34m
''')
print(ip , "\n")
print("\033[1;34m " "HI" , os.getlogin())

print(" ")
p = input("please Enter The Password : \n ")

if hash(p) == password :
    print("WELCOME ...")
    time.sleep(1)
    while True :
        print('''
            \033[1;32m
                    {1} Open HACKER TOOLS
                    ==============================
                    {2} Generate a Strong Password 
                    ==============================
                    {3} Open a File
                    ==============================
                    {4} Open Calculate
                    ==============================
                    {5} Open a Site
                    ==============================
                    {6} Open a Passlist Maker
                    ==============================
                    {7} Open a Game 
                    ==============================
                    {99}exit
            \033[1;m
            ''')
        y = input("$ROOT===>  ")
        if y == "" :
            print(""" 
            \033[1;31m 
    please try again ...\n you should enter a number ...
            """)
        if int(y) == 1 :
            os.system("clrar")
            os.system("clear")
            os.system("clear")

            print('''
            \033[1;32m
                    {1} nmap-jilrot
                    ======================
                    {2} payload
                    ======================
                    {3} ddos attack
                    ======================
                    {4} web tools
                    ======================
                    {5} termux os
                    ======================
                    {6} password tools
                    ======================
                    {7} cracking
                    ======================
                    {8} evil codes
                    ======================
                    {99}exit
            \033[1;m
            ''')

            print ("  ")

            x = input("$ROOT===>  ")

            if x == 1:
                os.system("python2 modules/nmap/nmap.py")
            if x == 2:
                os.system("python2 modules/payload/payload.py")
            if x == 3:
                os.system("python2 modules/ddos/ddos.py")
            if x == 4:
                os.system("python2 modules/webtools/webtools.py")
            if x == 5:
                os.system("python2 modules/os/os.py")
            if x == 6:
                os.system("python2 modules/password/password.py")
            if x == 7:
                os.system("python2 modules/crack/crack.py")
            if x == 8:
                os.system("python2 modules/evilcode/evilcode.py")
            if x == 99 :
                break
        
        if int(y) == 2 :
            z = int(input("please Enter The Length Of The Password : "))
            name = input("please enter your name : ")
            last_name = input("please enter your last name : ")
            phone_number = input("please enter your phone number : ")

            def makepassword(stringLength=z):
                letters = name + last_name + phone_number
                return ''.join(random.choice(letters) for i in range(stringLength))

            print("generated pass is : " ,  makepassword()) 
        elif int(y) == 3 :
            y = input("please Enter The File's Addres : ")
            os.system("%s" % y)
        elif int(y) == 4 :
            os.system("calc.exe")
        elif int(y) == 5 :
            web = input("Please Enter The URL : [GOOGLE.COM]  ")
            if web == "" :
                webbrowser.open("https://www.google.com/")
            else :
                webbrowser.open("%s" %web)
            print("opened :)")
        if int(y) == 6 :
            os.system("python3 cupp/cupp.py -i")
        elif int(y) == 7 :
            os.system("python3 x_o.py")

        if int(y) == 99 :
            print(" Good Bye Dear ... ", " :) ")
            break
        
else :
    print("The Pass Is Wrong , Try Again")
        

