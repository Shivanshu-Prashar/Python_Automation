import os
import pyttsx3
def pull():
 pyttsx3.speak("Please enter the ip address")
 IP=input("Enter the IP ADDRESS: ")
 pyttsx3.speak("Please enter the image name")
 name=input("Enter the image name ")
 pyttsx3.speak("Pulling The Image is in progress")
 os.system("ssh -i KEY.pem ec2-user@{} sudo docker pull {}".format(IP,name))
