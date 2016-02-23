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

Args:
    ABB.Robotics.Controllers.Controller: Controller
Returns:
    Boolean: Indicates if master or not
Examples:
    None
"""

def is_controller_master(controller):
    try:
        if controller.IsMaster == True:
            return True
        else:
            return False
    except Exception, err:
        return False


"""
Gets the user access as master on the robot controller. This will make it possible to edit and write RAPID code.
Remember to call this method before editing and writing data to controller.

Args:
    ABB.Robotics.Controllers.Controller: Controller
Returns:
    Boolean: Indicates if mastership was successful
    String: Message with the outcome
    ABB.Robotics.Controllers.Mastership OR 0: Mastership is returned if accomplished, 0 if something went wrong
Examples:
    None
"""

def get_master_access_to_controller_rapid(controller):
    try:
        mastership = ctrlrs.Mastership.Request(controller.Rapid)
        msg = 'Got master access to controller'
        return True, msg, mastership
    except Exception, err:
        mastership = 0
        return False, err, mastership


"""
Releases any master access granted on the controller.
Remember to call this method after editing and writing data to controller.

Args:
    ABB.Robotics.Controllers.Mastership: Mastership
Returns:
    Boolean: Indicates if mastership was released and disposed
    String: Message with the outcome
Examples:
    None
"""

def release_and_dispose_master_access(mastership):
    try:
        mastership.Release()
        mastership.Dispose()
        msg = 'Master access was released.'
        return True, msg
    except Exception, err:
        return False, err