import subprocess
import sys
import os

def install_firewall():
    resp = os.system("sudo apt-get install ufw")
    if resp == 0:
        return True
    else:
        return False

def enable_firewall():
    """
    """
    try:
        message_expected  = "Firewall is active and enabled on system startup"
        repe = subprocess.Popen(["sudo", "ufw", "enable"],stdout = subprocess.PIPE)
        (output,err) = repe.communicate()
        output = output.decode('utf-8')
        if message_expected in output:
            return (True, output)
        else:
            return (False, output)
    except:
        raise Exception("it is a run time error please run again")

def enable_filrewall(enable=True):
    try:
        if enable:
            message_expected  = "Firewall is active and enabled on system startup"
            command = "enable"
        else:
            message_expected = ""
            command = "disable"
        repe = subprocess.Popen(["sudo", "ufw", command],stdout = subprocess.PIPE)
        (output,err) = repe.communicate()
        output = output.decode('utf-8')
        if message_expected in output:
            return (True, output)
        else:
            return (False, output)
    except:
        raise Exception("it is a run time error please run again")

def disable_firewall():
    try:
        repe = subprocess.Popen(["sudo", "ufw", "disable"],stdout = subprocess.PIPE)
        (output,err) = repe.communicate()
        output = output.decode('utf-8')
        return output
    except:
        raise Exception("it is a run time error please run again")

def status_firewall():
    try:
        repe = subprocess.Popen(["sudo", "ufw", "status"],stdout = subprocess.PIPE)
        (output,err) = repe.communicate()
        output = output.decode('utf-8')
        return output
    except:
        raise Exception("it is a run time error please run again")

def reset_firewall():
    try:
        subprocess.call(["sudo", "ufw", "reset"])
        #print(""" "ufw" just know it was reset that means it's change to default settings""")
        return True
    except:
        raise Exception("it is a run time error please run again")

def allow_connection_firewall(connections):
    """
    Discription:-
                befor going to use this function you must aware of it in linux we can individually allow different ports 
    Prams:- 
    
                the type of the args <string> recommended arguments"ssh","22/tcp","2222/tcp" here 22 and 2222 are the different connection ports
                with that there are some web server those are "www"or"80/tcp", "ftp"or"21/tcp" 
    return:-
                it will print the connection is successful
    
    """
    try:
        subprocess.call(["sudo", "ufw", "allow", connections])
        return True
    except: 
        raise Exception("it is a run time error please run again")

def deny_connection_firewall(connections):
    """
    Discription:-
                befor going to use this function you must aware of it in linux we can individually deny different ports 
    Prams:- 
    
                the type of the args <string> recommended arguments"ssh","22/tcp","2222/tcp" here 22 and 2222 are the different connection ports
                with that there are some web server those are "www"or"80/tcp", "ftp"or"21/tcp" 
    return:-
                it will print the connection is deny successful
    
    """
    try:
        subprocess.call(["sudo", "ufw", "deny", connections])
        return True
    except:
        raise Exception("it is a run time error please run again")

def deleteing_rules_firewall(connections):
    """
    Discription:-
                befor going to use this function you must aware of it in linux we can individually delete the allow ports rules 
    Prams:- 
    
                the type of the args <string> recommended arguments"ssh","22/tcp","2222/tcp" here 22 and 2222 are the different connection ports
                with that there are some web server those are "www"or"80/tcp", "ftp"or"21/tcp" 
    return:-
                it will print the rules are deleted succesful
    
    """
    try:
        subprocess.call(["sudo", "ufw", "allow", "delete", conections])
        print("the message form ufw service just delete the rules of the {}".format(conections))
        return True
    except:
        raise Exception("it is a run time error please run again")


if __name__ == "__main__":
    resp = enable_firewall()
    print("---->", resp)
    """
    if resp:
        print("Fire wall installed succcess")
    else:
        print("Fail to install filrewall")
    """
