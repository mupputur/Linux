import subprocess
import os
import sys

def install_NM():
    """
    Discription:- this function will install network_manager service
    """
    try:
        os.system("sudo apt-get install network-manager")
        return True
    except:
        raise Exception("check the internet connection")

def start_NM():
    """
    discription:- it will start the network manager if it is stoped
    """
    try:
        os.system("sudo systemctl start NetworkManager.service")
        print("sucessfully startedd")
        return True
    except:
        raise Exception("it is run time error run once again")

def enable_NM():
    """
    discription:- it will enable the network manager it will help to activate 
                    Enable restarting the network manager when the system reboots
    """
    try:
        os.system("sudo systemctl enable NetworkManager.service")
        print("it is enable")
        return True
    except:
        raise Exception("it is run time error rerun the function ")
def stop_NM():
    """
    Discription:- it will stop the network
    """
    try:
        os.system("sudo systemctl stop network-manager.service")
        print("successfully stoped")
        return True
    except:
        raise Exception("it is runt time error rerun the function")

def disable_NM():
    """
    Discription:- it will disable that meance it stop all the network related how to stop and disable Network Manager without uninstalling it
    """
    try:
        os.system("sudo systemctl disable network-manager.service")
        print("it is disable")
        return True
    except:
        raise Exception("it is run time error run once again")


def restart_NM():
    """
    Discription:- it will restart total network-manager help to start
    """
    try:
        os.system("sudo service network-manager restart")
        print("restart successfully")
        return True
    except:
        raise Exception("it is run time error run once again")

start_NM()
