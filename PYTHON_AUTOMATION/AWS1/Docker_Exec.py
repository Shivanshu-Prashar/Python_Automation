import os
def ex():
 IP=input("BASE MACHINE IP ADDRESS ")
 IP1=input("Enter the ip address of target instance ")
 path=input("Enter the path for key ")
 expose=input("Enter the BASE MACHINE  Port NO. To MAP ")
 os.system('''ssh -i KEY.pem ec2-user@{} sudo ssh -i {} ec2-user@{}  sudo docker run -itd -p {}:80  --name myos centos'''.format(IP,path,IP1,expose))
 os.system(''' ssh -i KEY.pem ec2-user@{} sudo ssh -i {} ec2-user@{} sudo docker exec myos /usr/sbin/httpd'''.format(IP,path,IP1))    
