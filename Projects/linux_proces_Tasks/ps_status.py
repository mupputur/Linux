
import psutil

def check_process_status(process_name):
    try:
        process_status=[proc for proc in psutil.process_iter() if proc.name() == process_name]
        for current_process in process_status:
           return("Process id is %s, name is %s, staus is %s"%(current_process.pid, current_process.name(), current_process.status()))
    except:
        raise Exception("Process name not valid", process_name)
name=input("enter a process name:")
a=check_process_status(name)
print(a)

