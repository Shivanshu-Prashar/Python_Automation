import os 
import pyttsx3
def cont():
 pyttsx3.speak("Enter the ip address")
 IP=input("Enter the IP address")
 pyttsx3.speak("enter the name for container")
 name=input("enter the name for container ")
 pyttsx3.speak("Docker Host Port you want to MAP")
 Base_port=input("Docker Host Port you want to MAP ")
 pyttsx3.speak("Container port number which you want to map with Docker Host")
 port=input("Enter Container  port no.  ")
 pyttsx3.speak("enter the image name")
 image=input("image ")
 os.system('''ssh -i KEY.pem ec2-user@{} sudo docker run -itd -p {}:{} --name {} {}'''.format(IP,Base_port,port,name,image))
