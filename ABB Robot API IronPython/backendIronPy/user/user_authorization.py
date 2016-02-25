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
    try:
        controller.Logon(ctrlrs.UserInfo.DefaultUser)
        msg = 'Logon successful'
        return True, msg
    except Exception:
        msg = 'Unable to log on:  The operation was not allowed for the given user.'
        return False, msg


"""
Log on to a controller after connecting to it with a username and password.

Args:
    ABB.Robotics.Controllers.Controller: Controller
    String: Username
    String: Password
Returns:
    Boolean: Indicates if logon is successful
    String: Message with the outcome
Examples:
    None
"""

def logon_robot_controller_with_username(controller, username, password):
    try:
        controller.Logon(ctrlrs.UserInfo(username, password))
        msg = 'Logon successful'
        return True, msg
    except Exception:
        msg = 'Unable to log on:  The operation was not allowed for the given user.'
        return False, msg


"""
Log off the robot controller and dispose of the controller.

Args:
    ABB.Robotics.Controllers.Controller: Controller
Returns:
    Boolean: Indicates if logoff is successful
    String: Message with the outcome
Examples:
    None
"""

def logoff_robot_controller(controller):
    try:
        controller.Logoff()
        controller.Dispose()
        msg = 'Logoff successful'
        return True, msg
    except Exception, err:
        return False, err