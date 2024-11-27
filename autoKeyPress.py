import json
import os
import sys
from pynput.keyboard import Key, Controller
from time import sleep

#----- Functions -----
def readConfig(settingsFile):
    if os.path.isfile(settingsFile):
        with open(settingsFile) as json_file:
            data = json.load(json_file)
    else:
        data = {
            "keyPress": "A",
            "timer": 200
        }
        # Serializing json
        json_object = json.dumps(data, indent=4)
 
        # Writing to config.json
        with open(settingsFile, "w") as outfile:
            outfile.write(json_object)
    return data
#----- End Functions -----
keyboard = Controller()

# Get the current working
# directory (CWD)

try:
    this_file = __file__
except NameError:
    this_file = sys.argv[0]
this_file = os.path.abspath(this_file)
if getattr(sys, 'frozen', False):
    cwd = os.path.dirname(sys.executable)
else:
    cwd = os.path.dirname(this_file)

print("Current working directory:", cwd)

#Read Config File
settingsFile = os.path.join(cwd, "appconfig.json")
config = readConfig(settingsFile)
keyPress = config["keyPress"]
timer = config["timer"]

print("Ready, wait 5 Seconds to start")
sleep(5)
while True:
    # Press and release space
    keyboard.press(keyPress)
    keyboard.release(keyPress)

    sleep(timer)