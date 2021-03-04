import psutil

def check_specific_process_status(process_name):
    try:
        process_status=[]
        for process in psutil.process_iter():
            if process.name()  == process_name:
                process_status.append(process)
                for current_process in process_status:
                    return(current_process.pid, current_process.name(), current_process.status())
    except:
        raise Exception("Process name not valid",process_name)
process_name="chrome"
res=check_specific_process_status(process_name)
print(res)

