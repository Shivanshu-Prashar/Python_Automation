import os
import pyttsx3
def aws():
    import AWS1.addrule
    import AWS1.instance
    import AWS1.httpd
    import AWS1.AWS_Docker_Install
    import AWS1.EBS_CREATE
    import AWS1.EBS_ATTACH
    import AWS1.CREATE_KEY
    import AWS1.SECURITY_GROUP
    import AWS1.Docker_Exec
    import pyttsx3
    
    while True:
        pyttsx3.speak("SELECT WHAT YOU WANT TO DO")
        print('''SELECT WHAT YOU WANT TO DO
                 1.  Create AWS key-pair
                 2.  Create AWS Security-Group
                 3.  To edit rules to Security-Group
                 4.  To Launch AWS Instance
                 5.  To Install and Start HTTPD Services on AWS linux Machine 
                 6.  To Install And Start Docker Services on AWS Linux Machine
                 7.  To Install And Start HTTPD services inside docker container
                 9.  To Create An EBS Volume
                 10. To Attach EBS to Instance)
                 11. Exit ''')
        x=int(input("Enter Your Choice: "))
        if x==1:
         AWS1.CREATE_KEY.key()
         pyttsx3.speak("KEY CREATED SUCCESSFULLY")
        elif x==2:
         AWS1.SECURITY_GROUP.sg()
         pyttsx3.speak("SECURITY GROUP  CREATED SUCCESSFULLY")
        elif x==3:
          AWS1.addrule.ingress()
        elif x==4:
            AWS1.instance.launch()
            print("LAUNCHED")
        elif x==9:
          AWS1.EBS_CREATE.ebs()
          print("CREATED")
        elif x==10:
            AWS1.EBS_ATTACH.attach()
            print("VOLUME ATTACHED SUCCESSFULLY")
        elif x==5:
          AWS1.httpd.service()
          print("DONE!!")
        elif x==6:
          AWS1.AWS_Docker_Install.Docker()
          print("DONE!!")
        elif x==7:
          AWS1.Docker_Exec.ex()
        elif x==11:
            pyttsx3.speak("Moving to Main Menu")
            break

