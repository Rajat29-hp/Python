from paramiko.client import SSHClient
from paramiko.client import AutoAddPolicy
import sys

def sshserverone(server_name,server_user,server_pass,server_cmd):
  client = SSHClient()
  client.set_missing_host_key_policy(AutoAddPolicy)
  client.connect(server_name,username=server_user,password=server_pass)
  stdin,stdout,stderr = client.exec_command(server_cmd)
  print(stdout.read().decode())
  print(stdin.read().decode())
  client.close()

sshserverone(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
