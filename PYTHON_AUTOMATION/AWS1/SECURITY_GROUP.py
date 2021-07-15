import os
import pyttsx3
def sg():
  pyttsx3.speak("Enter the IP Address of Base machine")
  IP=input("ENTER THE IP ADDRESS OF BASE MACHINE ")
  pyttsx3.speak("Please enter Name For Security Group")
  name_SG=input("Please enter Name For Security Group: ")
  pyttsx3.speak("Any description for Security Group")
  desc=input("DESCRIPTION : ")
  os.system("ssh -i KEY.pem ec2-user@{} sudo aws ec2 create-security-group --group-name {} --description {}".format(IP,name_SG,desc))
