#!/usr/bin/python3
import subprocess
import os
import sys

print("Welcome to All-rounder Hacking suit! made by DedSec")
print("To use this Program select any Options,Please remember use commands in 1 line with no spaces")
print("Feel Free to modify it by me giving some credit under GNU license\n\n")
#VARIABLES Settings
dnsx = "1)Dnsenum"
forex = "2)Foremost"
searchx = "3)Searchsploit"
netx = "4)Netdiscover"
update="5)Install or update"
exit = "6)Exit\n"


while True: #loop Settings
    print("Please choose your Options:\n")
    print(dnsx)
    print(forex)
    print(searchx)
    print(netx)
    print(update)
    print(exit)

    s1 = input('Whats your Selction?:') # input commands for connecting to main tools in Linux.


    # From here the Tools are connected and commands are piped to the main Tool.
    if s1 == 1:
        dns = raw_input("Input Dnsenum Commands directly,Eg -h:")
        subprocess.call(["dnsenum",(dns)])

    if s1 == 2:
        fore=raw_input("Input Foremost Commands Directly,Eg -h:")
        subprocess.call(["foremost",(fore)])

    if s1 == 3:
        search=raw_input("Input Searchsploit Commands Directly,Eg -h:")
        subprocess.call(["searchsploit",(search)])

    if s1 == 4:
        net=raw_input("Input NetDiscover Commands Directly,Eg -h:")
        subprocess.call(["netdiscover",(net)])

    if s1 == 5:
            up=raw_input("Do you want to 1:Update or 2:Install?:")
    if up == '1' or 'update':
        subprocess.call(["sudo","apt-get","update"])

    if up == '2' or 'install':
        subprocess.call(["sudo","apt-get", "install","foremost"])
        subprocess.call(["sudo","apt-get","install","dnsenum"])
        subprocess.call(["sudo","apt-get","install","Searchsploit"])
        subprocess.call(["sudo","apt-get","install","netdiscover\n\n"])

    if s1 == 6:
        sys.exit

    if s1 == 0 :
        print("Select again! something went wrong!")
        
#THIS IS FINAL VERSION feel free to Add more software support for other Kali tools
