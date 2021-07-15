import os
import pyttsx3
def cr():
 pyttsx3.speak("enter The IP Address Of Machine")
 IP=input("enter The IP Address Of Machine ")
 pyttsx3.speak("Enter the Name for Directory")
 name=input("enter name for dir ")
 pyttsx3.speak("Enter The Path where you want to create the directory ") 
 path=input("enter path  ")
 os.system("ssh -i KEY.pem ec2-user@{} sudo mkdir {}{}".format(IP,path,name))
 pyttsx3.speak("Successfully created")
