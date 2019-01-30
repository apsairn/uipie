# Install PieModules in here
# Module:Editor
import os
from uipierc import *
def editor():
    print("If you want to continue,Please input your UIPie Master Password.")
    pwd2=input("Master Password:")
    if pwd2==masterpwd:
        print("1.A New Document")
        print("2.Old Documents")
        doctype=input("ID:")
        if doctype=="1":
            os.system("nano")
        if doctype=="2":
            direc=input("Directory:")
            os.system(("nano",direc))
        else:
            exit()
def setool():
    print("It is developing.")
    exit()
