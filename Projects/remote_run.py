import paramiko
def remote_run():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.43.8', username='rajkumar', password='****')         
    ftp = client.open_sftp()
    ftp.put('/tmp/service_handler','/tmp/service_handler.py')
    ftp.close()
    stdin,stdout,stderr = client.exec_command('python3 /tmp/service_handler.py')
    for line in stdout:
        print(line)
    client.close()
remote_run()
