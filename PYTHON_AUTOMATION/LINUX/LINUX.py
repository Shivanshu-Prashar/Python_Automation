import os
import pyttsx3
import LINUX.DIR
def linux():
        while True:
            print('''                  1.  To Create Directory
                  2.  To create file
                  3.  To set permissions on file
                  4.  To delete directory/file
                  5.  To set ACL 
                  6.  To Create Group
                  7.  To change File Group ownership
                  8.  To add/change user Primary group
                  9.  To Delete User
                  10. To Install any package
                  11. To download rpm repo from internet
                  12. To remove any package
                  13. To Start Any Service
                  14. Exit''')
            x=int(input("enter The Choice: "))
            if x==1:
             LINUX.DIR.cr()
            elif x==2:
                pyttsx3.speak("enter The IP Address Of Machine")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("enter name for file")
                name=input("enter name for file ")
                pyttsx3.speak("Enter The Path where You want to create the file ")
                path=input("enter path [/root/ ] ")
                os.system("ssh -i KEY.pem ec2-user@{} sudo touch {}{}".format(IP,path,name))
                pyttsx3.speak("Successfully created")
            elif x==3:
                print("""4 --> read
2 --> write
1 --> execute""")
                pyttsx3.speak("enter The IP Address Of Machine")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("Permission for file owner")
                owner=input("Permissions for user(4,2,1) ")
                pyttsx3.speak("Permission for file group")
                group=input("Permissions for group ")
                pyttsx3.speak("Permission for others")
                other=input("Permissions for others ")
                pyttsx3.speak("Enter the file name with absolute Path")
                path=input("enter  filename with path ")
                os.system("ssh -i KEY.pem ec2-user@{} sudo chmod {}{}{} {}".format(IP,owner,group,other,path))
                pyttsx3.speak("Successfully Changed")
            elif x==4:
                pyttsx3.speak("enter The IP Address Of Machine")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("Enter the file name with absolute Path")
                name=input("Enter file name with proper path ")
                os.system("ssh -i KEY.pem ec2-user@{} sudo rm -rf {}".format(IP,name))
                pyttsx3.speak("Successfully removed")
            elif x==5:
                pyttsx3.speak("enter The IP Address Of Machine")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("Enter the username")
                user=input("Enter The Username: ")
                pyttsx3.speak("Enter the permissions ")
                per=input("Permission for user: ")
                pyttsx3.speak("Enter the file name with absolute Path")
                file=input("Enter the file name with absolute Path: ")
                os.system("ssh -i KEY.pem ec2-user@{} sudo setfacl -m u:{}:{} {}".format(IP,user,per,file))
                pyttsx3.speak("Successfully changed")
            elif x==6:
                pyttsx3.speak("enter The IP Address Of Machine")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("Enter the  group name")
                name=input("Group Name: ")
                os.system("ssh -i KEY.pem ec2-user@{} sudo groupadd {}".format(IP,name))
                pyttsx3.speak("Successfully created")
            elif x==7:
                pyttsx3.speak("enter The IP Address Of Machine")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("Enter the new group name for file")
                name=input("New Group Name ")
                pyttsx3.speak("Enter the file name with absolute Path")
                filename=input("Enter The File Name with absolute path ")
                os.system("ssh -i KEY.pem ec2-user@{} sudo chgrp {} {}".format(IP,name,filename))
                pyttsx3.speak("Successfully changed")
            elif x==8:
                pyttsx3.speak("enter The IP Address Of Machine")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("Enter the Primary group name for user ")
                name=input("Primary Group Name ")
                pyttsx3.speak("Enter the username ")
                user=input("Enter Username ")
                os.system("ssh -i KEY.pem ec2-user@{} sudo usermod -g {} {}".format(IP,name,user))
                pyttsx3.speak("Successfully changed")
            elif x==9:
                pyttsx3.speak("enter The IP Address Of Machine ")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("Enter the name of user to delete ")
                user=input("Enter name of user to delete ")
                os.system("ssh -i KEY.pem ec2-user@{} sudo userdel -r {}".format(IP,user))
                pyttsx3.speak("Successfully deleted")
            elif x==10:
                pyttsx3.speak("enter The IP Address Of Machine")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("Enter the package name to install ")
                pack=input("package name ")
                os.system("ssh -i KEY.pem ec2-user@{} yum install {} -y".format(IP,pack))
                pyttsx3.speak("Successfully installed")
            elif x==11:
                pyttsx3.speak("enter The IP Address Of Machine")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("Enter the URL ")
                url=input("enter the url ")
                os.system("ssh -i KEY.pem ec2-user@{} sudo wget {}".format(IP,url))
                pyttsx3.speak("Successfully downloaded")
            elif x==12:
                pyttsx3.speak("enter The IP Address Of Machine")
                IP=input("enter The IP Address Of Machine ")
                pyttsx3.speak("Enter the package name to remove")
                remove=input("Enter the package name ")
                os.system("ssh -i KEY.pem ec2-user@{} sudo yum remove {} -y".format(IP,remove))
                pyttsx3.speak("Successfully removed")
            elif x==13:
               pyttsx3.speak("enter The IP Address Of Machine")
               IP=input("enter The IP Address Of Machine ")
               pyttsx3.speak("Enter the service name to be started")
               service=input("Enter the Service Name ")
               os.system("ssh -i KEY.pem ec2-user@{} sudo systemctl start {}".format(IP,service)) 
               pyttsx3.speak("Successfully started")
            elif x==14:
             pyttsx3.speak("Moving To Main Menu ")
             break
