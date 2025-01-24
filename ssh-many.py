import paramiko
from datetime import datetime

def remote_command_on_server(user,command,pvtkey):
    """
    Run a command on multiple machine and get the info
    """
    f = open("machine_ips.txt","r")
    machine_ips = f.readlines()
    f.close()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for ip in machine_ip:
        ip = ip.strip()
        try:
            ssh.connect(ip,username=usser,key_filename=pvt,timeout=5)
            stdin, stdout, stder = ssh.exec_command(command)
            result[ip] = stdout.read().decode()
        except:
            result[ip] = "connection failed"
    return(result)

def save_log(result):
    """
    save command to a log file
    """
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
    filename = f"vm_output_{timestamp}.log"
    f = open(filename,"w")
    for ip,output in result.items():
        f.write(f"\n===={ip}====\n")
        f.write(output)
        f.write("\n")
    f.close()
    printf("Log file created: {filename}")

if __name__ == "__main__":
    user= input("Enter your SSH username:")
    command = input("Enter your remote command to execute")
    pvtkey = input("Enter privateKey file path for SHH:")
    reuslt = remote_command_on_server(user,command,pvtkey)
    save_to_log(result)
