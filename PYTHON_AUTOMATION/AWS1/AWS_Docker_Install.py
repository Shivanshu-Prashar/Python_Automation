import os
def Docker():
 IP=input("BASE MACHINE IP ADDRESS ")
 IP1=input("Enter the ip address ")
 path=input("Enter the path for key ")
 os.system('''ssh -i KEY.pem ec2-user@{} ssh -i {} ec2-user@{} sudo yum install docker -y'''.format(IP,path,IP1))
 os.system('''ssh -i KEY.pem ec2-user@{} ssh -i {} ec2-user@{} sudo systemctl start docker'''.format(IP,path,IP1))
