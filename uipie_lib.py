# UIPie Library
import os
from piemodules import *
def piestart():
    if masterpwd=="ADMIN":
        print("Please change the configure file 'uilibrc.py'.") 
    print("1.Change A Directory")
    print("2.Link to net with DHCPCD Client")
    print("3.Link to a Wi-Fi Signal")
    print("4.Get the time now")
    print("5.Edit or Open a File")
    print("6.Install a extension of UIPie")
    print("7.Logout of the UIPie user")
    print("8.About UIPie")
    print("9.UIPie Setting and System setting")
    print("\nSelect one,Input the ID.And you can type a UNIX Shell command,too.")
    cmd=input("ID:")
    if cmd=="1":
        dir=input("Input directory:")
        os.chdir(dir)
        piestart()
    elif cmd=="2":
        os.system("dhcpcd")
        piestart()
    elif cmd=="3":
        os.system("sudo wifi-menu")
        piestart()
    elif cmd=="4":
        os.system("date")
        piestart()
    elif cmd=="5":
        editor()
        piestart()
    elif cmd=="6":
        print("Please see the guide of your plugin and operate.")
        print("FAILED")
        piestart()
    elif cmd=="7":
        exit()
    elif cmd=="8":
        print("UIPie is a tool for your CLI Linux UI written by Mr.Arthur(GitHubName:Apsairn)")
        piestart()
    elif cmd=="9":
        setool()
        piestart()
    else:
        os.system(cmd)
        piestart()
