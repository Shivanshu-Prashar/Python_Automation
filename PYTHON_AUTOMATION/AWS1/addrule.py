import os
import pyttsx3
def ingress():
 while True:
  print(''' 1. Ingress/Inbound rule
            2. Egress/Outbound rule
            3. Exit ''')
  pyttsx3.speak("Enter one for inbound rule and 2 for outbound rule")
  n=int(input("enter choice: "))
  if n==1:
   pyttsx3.speak("Enter the IP ADDRESS of base machine")
   IP=input("ENTER THE IP ADDRESS OF BASE MACHINE ")
   pyttsx3.speak("Enter the Security Group name")
   name=input("Security Group Name: ")
   pyttsx3.speak("Enter the Security Group ID ")
   GP_ID=input("Group ID: ")
   pyttsx3.speak("Enter the Port number you want to allow")
   Port=input("Port: ")
   os.system('''ssh -i KEY.pem ec2-user@{} sudo aws ec2 authorize-security-group-ingress --group-name {} --group-id {} --protocol  tcp --port {} --cidr 0.0.0.0/0'''.format(IP,name,GP_ID,Port))
   pyttsx3.speak("Rule Added Succesfully ")
  elif n==2:
   pyttsx3.speak("Enter the IP ADDRESS of base machine")
   IP=input("ENTER THE IP ADDRESS OF BASE MACHINE ")
   pyttsx3.speak("Enter the Security Group name ")
   name=input("Security Group Name ")
   pyttsx3.speak("Enter the Security Group ID ")
   GP_ID=input("SECURITY GROUP ID ") 
   pyttsx3.speak("Enter the Port number you want to allow")
   Port=input("Port ")
   os.system('''ssh -i KEY.pem ec2-user@{} sudo aws ec2 authorize-security-group-egress --group-name {} --group-id {} --protocol tcp --port {} --cidr 0.0.0.0/0'''.format(IP,name,GP_ID,Port))
   pyttsx3.speak("Rule Added Succesfully ")
  elif n==3:
   break
   

