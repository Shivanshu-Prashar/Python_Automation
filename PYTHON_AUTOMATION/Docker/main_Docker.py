def docker():
 while True:
  import Docker.install
  import Docker.start
  import Docker.PULL
  import Docker.Cr_Container
  import Docker.DEL
  import Docker.EX
  import pyttsx3
  print('''1. To Install Docker On The Machine
2. To Start Docker Services
3. To pull an image
4. To Create Container
5. To Install HTTPD services inside container
6. To Delete Container
7. EXIT''')
  n=int(input("Choice: "))
  if n==1:
   pyttsx3.speak("Installing docker on the machine")
   Docker.install.install()
   pyttsx3.speak("Successfully Installed ")
  elif n==2:
   pyttsx3.speak("Starting the docker services")
   Docker.start.start()
   pyttsx3.speak("Successfully Started")
  elif n==3:
   Docker.PULL.pull()
   pyttsx3.speak("Successfully Pulled")
  elif n==4:
   pyttsx3.speak("Launching the conatiner")
   Docker.Cr_Container.cont()
   pyttsx3.speak("Container launched successfully")
  elif n==6:
   Docker.DEL.del1()
   pyttsx3.speak("Container Successfully deleted")
  elif n==5:
   Docker.EX.ex()
   pyttsx3.speak("Succesfully Configured")
  elif n==7:
   pyttsx3.speak("EXITING")
   break
