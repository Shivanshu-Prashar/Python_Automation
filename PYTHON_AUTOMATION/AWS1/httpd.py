import os
def service():
 IP=input("ENTER THE IP ADDRESS OF BASE MACHINE ")
 IP1=input("Enter the ip address ")
 path=input("Enter the path for key ")
 os.system('''ssh -i KEY.pem ec2-user@{} sudo ssh -i {} ec2-user@{} sudo yum install httpd -y'''.format(IP,path,IP1))
 os.system('''ssh -i KEY.pem ec2-user@{} sudo ssh -i {} ec2-user@{} sudo systemctl start httpd'''.format(IP,path,IP1))
