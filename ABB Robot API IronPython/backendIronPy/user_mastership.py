"""
The user mastership module is a module for setting mastership on controller.
"""


import clr

clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')


"""
Checks if controller has master access

Argument arg1: controller (ABB.Robotics.Controllers.Controller)
Return arg1: Boolean
Return arg2: Message with the outcome (String)
"""

def is_controller_master(controller):
    try:
        if controller.IsMaster == True:
            msg = 'Has master access'
            return True, msg
        else:
            msg = 'Does not have master access'
            return False, msg
    except Exception, err:
        return False, err


"""
Gets the user access as master on the robot controller. This will make it possible to write and edit RAPID code.

Argument arg1: controller (ABB.Robotics.Controllers.Controller)
Return arg1: Boolean
Return arg2: Message with the outcome (String)
Return arg3: mastership (ABB.Robotics.Controllers.Mastership) or empty string if exception/already exists
"""

def get_master_access_to_controller_rapid(controller):
    # mastership = ''
    try:
        mastership = ctrlrs.Mastership.Request(controller.Rapid)
        msg = 'Got master access to controller'
        return True, msg, mastership
    except Exception, err:
        mastership = ''
        return False, err, mastership


"""
Releases any master access granted on the controller

Argument arg1: mastership (ABB.Robotics.Controllers.Mastership)
Return arg1: Boolean
Return arg2: Message with the outcome (String)
"""

def release_and_dispose_master_access(mastership):
    try:
        mastership.Release()
        mastership.Dispose()
        msg = 'Master access was released.'
        return True, msg
    except Exception, err:
        return False, err