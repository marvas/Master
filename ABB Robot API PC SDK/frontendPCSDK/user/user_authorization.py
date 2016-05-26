"""
The user authorization module has functions for user authentication on the robot controller.
"""


import os

# Path to the folder with DLL
file_path = os.path.realpath(__file__)
temp = file_path.split('frontendPCSDK')
dll_path = temp[0] + 'ABB_PCSDK_DLL\ABB.Robotics.Controllers.PC.dll'

import clr
clr.AddReferenceToFileAndPath(dll_path)

import ABB.Robotics.Controllers as ctrlrs


def logon_robot_controller_default(controller):
    """
    Log on to a controller after connecting to it with default user.

    Input:
        ABB.Robotics.Controllers.Controller: Controller
    Output:
        Boolean: Indicates if logon is successful
        String: Message with the outcome
    Examples:
        None
    """
    try:
        controller.Logon(ctrlrs.UserInfo.DefaultUser)
        msg = 'Logon successful'
        return True, msg
    except Exception:
        msg = 'Unable to log on:  The operation was not allowed for the given user.'
        return False, msg


def logon_robot_controller_with_username(controller, username, password):
    """
    Log on to a controller after connecting to it with a username and password.

    Input:
        ABB.Robotics.Controllers.Controller: Controller
        String: Username
        String: Password
    Output:
        Boolean: Indicates if logon is successful
        String: Message with the outcome
    Examples:
        None
    """
    try:
        controller.Logon(ctrlrs.UserInfo(username, password))
        msg = 'Logon successful'
        return True, msg
    except Exception:
        msg = 'Unable to log on:  The operation was not allowed for the given user.'
        return False, msg


def logoff_robot_controller(controller):
    """
    Log off the robot controller.

    Input:
        ABB.Robotics.Controllers.Controller: Controller
    Output:
        Boolean: Indicates if logoff is successful
        String: Message with the outcome
    Examples:
        None
    """
    try:
        controller.Logoff()
        msg = 'Logoff successful'
        return True, msg
    except Exception, err:
        return False, err
