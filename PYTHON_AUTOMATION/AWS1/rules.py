import os
def ingress():
 while True:
  print(''' 1. Ingress/Inbound rule
            2. Egress/Outbound rule
            3. Exit ''')
  n=int(input("enter choice: "))
  if n==1:
   name=input("Name")
   GP_ID=input("ID")
   Port=input("Port")
   os.system('''aws ec2 authorize-security-group-ingress --group-name {} --group-id {} --protocol  tcp --port {} --cidr 0.0.0.0/0'''.format(name,GP_ID,Port))
  elif n==2:
   name=input("Name")
   GP_ID=input("ID")
   Port=input("Port")
   os.system('''aws ec2 authorize-security-group-egress --group-name {} --group-id {} --protocol   tcp --port {} --cidr 0.0.0.0/0'''.format(name,GP_ID,Port))
  elif n==3:
   break

