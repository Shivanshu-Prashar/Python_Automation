import os
def attach():
 IP=input("BASE MACHINE IP ")
 I_ID=input("Enter Instance ID: ")
 V_ID=input("Enter the Volume ID: ")
 os.system('''ssh -i KEY.pem ec2-user@{} sudo aws ec2 attach-volume --volume-id {} --instance-id {}  --device /dev/sdb'''.format(IP,V_ID,I_ID))  
