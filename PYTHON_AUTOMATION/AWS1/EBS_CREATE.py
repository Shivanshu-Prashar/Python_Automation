import os
def ebs():
 IP =input("Enter the IP ADDRESS OF BASE MACHINE ")
 region=input("enter availability zone ")
 size=input("enter the size ")
 Type=input("enter the volume type ")
 os.system('''ssh -i KEY.pem ec2-user@{} sudo aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'''.format(IP,Type,size,region))
