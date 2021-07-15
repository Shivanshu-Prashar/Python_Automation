import os
import LINUX
import AWS1.AWS
import Docker.main_Docker
import LINUX.LINUX
import pyttsx3
while(True):
    print(".....................Select One Technology: .......................")
    pyttsx3.speak(" Select One Technology ")
    print('''\t\t\t1. Linux
\t\t\t2. AWS
\t\t\t3. Docker
\t\t\t4. Exit''')
    X=int(input("Enter Your Choice: "))
    if X==1:
      pyttsx3.speak("You Have Chossen option one linux ")
      LINUX.LINUX.linux()

    if X==2:
       pyttsx3.speak("You Have Chossen option two AWS")
       AWS1.AWS.aws()
    
    if X==3:
        pyttsx3.speak("You Have Chossen option three docker")
        Docker.main_Docker.docker()


    if X==4:
        pyttsx3.speak("Bye Bye")
        break
























        
