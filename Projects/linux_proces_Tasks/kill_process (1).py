
import os, signal

def process():

    # Ask user for the name of process 
    name = input("Enter process Name: ")
    try:

        # iterating through each instance of the proess 
        for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
            fields = line.split()

            # extracting Process ID from the output 
            pid = fields[0]

            # terminating process  
            os.kill(int(pid), signal.SIGKILL)
        print("Process Successfully terminated")

    except:
        print("Error Encountered while running script")

process()
"""
import os, signal
name=input("enter a process name:")

def check_kill_process():
    for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
        print(line)
        fields = line.split()
        pid = fields[0]
        a=os.kill(int(pid), signal.SIGKILL)
    return a 
#name=input("enter a process name:")
x=check_kill_process()
print(x)
"""
