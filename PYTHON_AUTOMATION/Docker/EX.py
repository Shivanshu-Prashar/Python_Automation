import os
import pyttsx3
def ex():
 pyttsx3.speak("Enter the IP address ")
 IP=input("Enter the IP address ")
 pyttsx3.speak("Enter the name or id of container ")
 name=input("enter name or id:  ")
 pyttsx3.speak("Configuring HTTPD services ")
 os.system("ssh -i KEY.pem ec2-user@{} sudo docker exec {} yum install httpd -y".format(IP,name))
 os.system("ssh -i KEY.pem ec2-user@{} sudo docker exec {} /sbin/httpd".format(IP,name))

