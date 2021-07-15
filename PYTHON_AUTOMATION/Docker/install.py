def install():
 import os
 import pyttsx3
 pyttsx3.speak("Enter The IP Address")
 IP=input("Enter The IP Address ")
 os.system("""ssh -i KEY.pem ec2-user@{} sudo yum install docker -y """.format(IP))
