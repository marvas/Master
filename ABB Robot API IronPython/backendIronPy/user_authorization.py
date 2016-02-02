"""
The user authorization module has functions for user authentication on the robot controller.
"""


import clr

clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')


"""
Log on to a controller after connecting to it with default user.

Arguments: controller (ABB.Robotics.Controllers.Controller)
Return arg1: logon_success (Boolean)
Return arg2: Message with the outcome (String)
"""


def logon_robot_controller_default(controller):
    logon_success = False
    msg = 'Logon successful'
    try:
        controller.Logon(ctrlrs.UserInfo.DefaultUser)
        logon_success = True
    except Exception:
        msg = 'Unable to logon:  The operation was not allowed for the given user.'
    return logon_success, msg


"""
Log on to a controller after connecting to it with a username and password.

Argument arg1: controller (ABB.Robotics.Controllers.Controller)
Argument arg2: username (String)
Argument arg3: password (String)
Return arg1: logon_success (Boolean)
Return arg2: Message with the outcome (String)
"""


def logon_robot_controller_with_username(controller, username, password):
    logon_success = False
    msg = 'Logon successful'
    try:
        controller.Logon(ctrlrs.UserInfo(username, password))
        logon_success = True
    except Exception:
        msg = 'Unable to log on:  The operation was not allowed for the given user.'
    return logon_success, msg

"""
Log off the robot controller

Argument arg1: controller (ABB.Robotics.Controllers.Controller)
Return arg1: logoff_success (Boolean)
Return arg2: Message with the outcome (String)
"""

def logoff_robot_controller(controller):
    msg = 'Logoff successful'
    logoff_success = False
    try:
        controller.Logoff()
        logoff_success = True
    except Exception:
        msg = 'Unable to log off: User may not be logged in or connection to controller can be lost.'
    return logoff_success, msg