# This script will print current system info
# Shamelessly combined from google and other stackoverflow like sites to form a single function

import platform
import socket
import re
import uuid
import json
import psutil

def get_system_info():
    try:
        info = {}
        info['platform'] = platform.system()
        info['platform-release'] = platform.release()
        info['platform-version'] = platform.version()
        info['architecture'] = platform.machine()
        info['hostname'] = socket.gethostname()
        info['ip-address'] = socket.gethostbyname(socket.gethostname())
        info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor'] = platform.processor()
        info['ram'] = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as error_msg:
        raise Exception(error_msg)

def main():
    try:
        print(get_system_info())
    except Exception as error_msg:
        raise Exception("Error - Something bad happened - {}.".format(error_msg))

# main entry point
if __name__ == "__main__":
    main()
