import os
import pyttsx3
def key():
 pyttsx3.speak("Enter the IP Address of Base machine")
 IP=input("Enter The IP Address of Base Machine ")
 pyttsx3.speak("Enter the name for key")
 name=input("enter the name for key: ")
 #path=input('''enter the path where you want to save the key locally:e.g /root  ''')
 pyttsx3.speak("Enter the name with which you want to store key locally")
 local=input("enter the name for key file locally  ")
 os.system("""ssh -i KEY.pem ec2-user@{} "sudo aws ec2 create-key-pair --key-name {} --output text>/home/ec2-user/{}" """.format(IP,name,local))

