import paramiko
import logging
def reinstall_pypackage(ip = '192.168.43.84',uname = 'rajkumar',pw='4122',command = 'sudo dmesg'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=uname, password=pw)
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.write(pw,'\n')
    logging.warning('password was not reading ')
    stdin.flush()
    data = stdout.read().split()
    for line in data:
        print(line)
    ssh.close()
    """
    doc type:- this is for how to enter the parameter you have to follow the patron first you need to enter the 
                "ip" address of the remote system next 
                "user name" of the remote system and
                "password " for the remote system
                final parrameter "command" you have to follow the sysntax:- "sudo apt-get install -y <package name>"
    """
reinstall_pypackage()