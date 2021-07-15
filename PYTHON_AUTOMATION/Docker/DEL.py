import os 
import pyttsx3
def del1():
    pyttsx3.speak("Enter The IP address")
    IP=input("Enter the IP address ")
    pyttsx3.speak("Enter the name or id of container ")
    name=input("Enter name or id ")
    pyttsx3.speak("Deleting the container")
    os.system("ssh -i KEY.pem ec2-user@{} sudo docker rm -f {}".format(IP,name))
