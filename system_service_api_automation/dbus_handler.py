import subprocess
import os
import sys

def message_the_application(message):
    """
    Description:- by using the concept of the dbus we are using the one to one communication by passing a message in the terminal this code help u to                   do the thing easy
    argument:- the argument type <string> like for fire fox pass the argument of firefox
                                               for chrome pass the argument of google-chrome
    
    return:- no
    """
    try:
        repe = subprocess.Popen([message],stdout = subprocess.PIPE)
        (output,err) = repe.communicate()
        output = output.decode('utf-8')
        return output
    except:
        raise Exception("run time error")


def message_the_app_tostop(passing):
    """
    Description:- by using the concept of the dbus we are using the one ot one communication by passing a message in the terminal to stop the running                   application
    argumentt:- the argument type<string> like for firefox pass the argument of firefox
                                                for chrome pass the argument of google-chrome
    
    return:- output

    """
    try:
        repe = subprocess.Popen(["pkill", passing],stdout = subprocess.PIPE)
        (output,err) = repe.communicate()
        output = output.decode('utf-8')
        return output
    except:
        raise Exception("run time error")

message_the_application("google-chrome")


args = sys.argv[1:]
if not len(args) == 1:
    print("invalid input")
    sys.exit(0)
res = args[0]
