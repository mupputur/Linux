import subprocess
import sys
import os
def is_service_active(service): 
    p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    output = output.decode('utf-8')
    if output.strip() == "active":
        return True

def start_service(service_name):
    if not is_service_active():
        subprocess.call(["service", service_name, "start"])
        print("Service {} started successfully.".format(service_name))
    else:
        print("Service {} is alredy running.".format(service_name))

def stop_service(service_name):
    if is_service_active():
        subprocess.call(["service", service_name, "stop"])
        print("Service {} stopped successfully.".format(service_name))
    else:
        print("Service {} is alredy stopped.".format(service_name))

def get_running_services():
    os.system("""service --status-all | grep '\[ + \]'""")
    print("the above list are the active services in your computer")

def install_service(service_to_install):
    if not is_service_acive():
        subprocess.call(["apt-get", "install", service_to_install])
        print("service {} going to install is already existed :".format(service_to_install))
    else:
        print("service {} is already installed".format(service_to_install))

def uninstall_service(service_to_remove):
    if is_service_active():
        subprocess.call(["apt-get", "remove", service_to_remove])
        os.system("apt autoremove")
        print("service {} is totaly removed with meta data ".format(service_to_remove))
    else:
        print("service {} is invalid command".format(service_to_remove))

def all_installed_service():
    os.system("service --status-all")
    print("the list of installed service")

def all_inactive_service():
    os.system("""service --status-all | grep '\[ - \]'""")
    print("the list of non running services")
"""

if __name__ == "__main__":
"""
"""
   args = sys.argv[1:]
   if len(args) != 1:
       print("ERROR: Invalid format: USAGE : python service_handler.py <service_name> ")
       sys.exit(0)
"""
get_running_services()
