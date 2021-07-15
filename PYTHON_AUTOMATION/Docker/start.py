def start():
 import os
 import pyttsx3
 pyttsx3.speak("enter the ip address of machine ")
 IP=input("Enter the IP Address ")
 os.system("""ssh -i KEY.pem ec2-user@{} sudo systemctl start docker """.format(IP))
