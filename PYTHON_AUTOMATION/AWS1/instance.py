import os
import pyttsx3
def launch():
  IP=input("ENTER THE IP ADDRESS OF BASE MACHINE ")
  name=input("Enter Key To Attach with Instance: ")
  SG=input("Security Group for instance: ")
  image_id=input("Image ID: ")
  type=input("Instance Type: ")
  os.system('''ssh -i KEY.pem ec2-user@{} sudo aws ec2 run-instances --image-id {} --instance-type {} --key-name {}   --security-group-ids {}'''.format(IP,image_id,type,name,SG))
