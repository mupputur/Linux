import os, signal

def kill_process(process_name):
    try:
        for line in os.popen("ps ax | grep " + process_name  + " | grep -v grep"):
            fields = line.split()
            pid = fields[0]
            res=os.kill(int(pid), signal.SIGKILL)
        return True
    except:
        raise Exception("error Encountered while running script")

process_name="chrome"
res=kill_process(process_name)
print(res)
