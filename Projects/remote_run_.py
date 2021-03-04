import paramiko
def remote_run(ip = '192.168.43.84',uname='rajkumar',pw='4122',file_with_path='/tmp/service_handler.py'):
    data = []
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=uname, password=pw)
    ftp = client.open_sftp()
    ftp.put(file_with_path,'/tmp/service_handler.py')
    ftp.close()
    stdin,stdout,stderr = client.exec_command('python3 /tmp/service_handler.py')
    for line in stdout:
        data.append(line)
    client.close()
    return data
info = remote_run()
print(info)
