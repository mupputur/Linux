
"""
import paramiko

class SSHConnect:


    def __init__(self,ip,port,username,password):
        self.ip = ip   #192.168.0.8
        self.port = port  #22
        self.username = username  #rajkumar
        self.password = password  #4122

    def connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, self.port, self.username, self.password )

    def runCommand(self):
        stdin,stdout,stderr = ssh.exec_command(cmd)
        outlines = stdout.readlines()
        resp = ''.join(outlines)
        return resp
        

if __name__ == "__main__":
    
    cmd=input("Enter commands:")
    
    connection = SSHConnect("192.168.0.8", 22, "rajkumar", "4122")
    
    connection.connect()
    connection.runCommand()
    

"""   
    

import paramiko
import sys

import subprocess

def Connect_linux_machine(self):

    #Connect linux machine
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)


    #Enter commands
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    return resp



if __name__ == "__main__":

    ip='192.168.0.8'
    port=22
    username='rajkumar'
    password='4122'
    
    while True:
        cmd = input("Enter Command or Terminal Quit['Q']:")
        if cmd == "Q":
            sys.exit()

        print(Connect_linux_machine(cmd))


        

