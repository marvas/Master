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

Args:
    ABB.Robotics.Controllers.Controller: Controller
Returns:
    Boolean: Indicates if logon is successful
    String: Message with the outcome
Examples:
    None
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

Args:
    ABB.Robotics.Controllers.Controller: Controller
    String: Username
    String: Password
Returns
    Boolean: Indicates if logon is successful
    String: Message with the outcome
Examples:
    None
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
Log off the robot controller and dispose of the controller.

Args:
    ABB.Robotics.Controllers.Controller: Controller
Returns:
    Boolean: Indicates if logoff is successful
    String: Message with the outcome
"""

def logoff_robot_controller(controller):
    try:
        controller.Logoff()
        controller.Dispose()
        msg = 'Logoff successful'
        return True, msg
    except Exception, err:
        return False, err