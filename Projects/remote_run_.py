import paramiko
def remote_run(ip = '192.168.43.84',uname='rajkumar',pw='4122',file_with_path='/home/bobby/system_service_api_automation/service_handler.py'):
    data = []
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=uname, password=pw)
    ftp = client.open_sftp()
    ftp.put(file_with_path,'/tmp/demo.py')
    ftp.close()
    stdin,stdout,stderr = client.exec_command('python3 /tmp/demo.py')
    for line in stdout:
        data.append(line)
    client.close()
    return data
info = remote_run()
print(info)
