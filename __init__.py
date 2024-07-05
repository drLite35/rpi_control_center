import os
import site
os.system('sudo cp -ru ./rpi '+site.getsitepackages()[0])

import os
import subprocess
cwd = os.getcwd()

# check if the system is Raspberry Pi, if not, raise exception
# Eg. output: Raspberry Pi 5 Model B Rev 1.0
try:
    with open('/sys/firmware/devicetree/base/model', 'r') as file:
        info = file.read()
        if "Raspberry" in info:
            is_rpi = True
        else:
            raise
except Exception:  # file not found
    raise  # change to None if testing on a PC


# check if requirements are met
# req_met = True
# with open(cwd + '/plugins/rpi/req.txt', 'r') as file:
#     req_list = file.read().split("\n")
# installed_modules = os.popen("pip freeze").read()

# for req in req_list:
#     if (req not in installed_modules):
#         req_met = False


# to install req. - called from rpi.py
# def install_req():
#     subprocess.Popen(['pip', 'install', '--break-system-packages', '-r',
#                       cwd + 'libs/rpi/req.txt'])
    # todo: send notif if no internet
