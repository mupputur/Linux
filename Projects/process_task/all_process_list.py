import psutil
def all_process_list():
    try:
        process_data={}
        for proc in psutil.process_iter():
            processName = proc.name()
            processID = proc.pid
            process_data[processName]=processID
        return process_data
    except:
        raise Exception (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess)
data = all_process_list()
print(data)
