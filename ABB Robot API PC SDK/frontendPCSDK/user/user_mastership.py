"""
The user mastership module is a module for setting mastership on controller.
"""


import os

# Path to the folder with DLL
file_path = os.path.realpath(__file__)
temp = file_path.split('frontendPCSDK')
dll_path = temp[0] + 'ABB_PCSDK_DLL\ABB.Robotics.Controllers.PC.dll'

import clr
clr.AddReferenceToFileAndPath(dll_path)

import ABB.Robotics.Controllers as ctrlrs


def is_controller_master(controller):
    """
    Checks if controller is holding mastership

    Input:
        ABB.Robotics.Controllers.Controller: Controller
    Output:
        Boolean: Indicates if master or not
    Examples:
        None
    """
    try:
        return bool(controller.IsMaster)
    except Exception:
        return False


def get_master_access_to_controller_rapid(controller):
    """
    Gets the user access as master on the robot controller. This will make it possible to edit and write RAPID code.
    Remember to call this method before editing and writing data to controller.

    Input:
        ABB.Robotics.Controllers.Controller: Controller
    Output:
        Boolean: Indicates if mastership was successful
        String: Message with the outcome
        ABB.Robotics.Controllers.Mastership OR None: Mastership is returned if successful, None if something went wrong
    Examples:
        None
    """
    try:
        mastership = ctrlrs.Mastership.Request(controller.Rapid)
        msg = 'Got master access to controller'
        return True, msg, mastership
    except Exception, err:
        return False, err, None


def release_and_dispose_master_access(mastership):
    """
    Releases any master access granted on the controller.
    Remember to call this method after editing and writing data to controller.

    Input:
        ABB.Robotics.Controllers.Mastership: Mastership
    Output:
        Boolean: Indicates if mastership was released and disposed
        String: Message with the outcome
    Examples:
        None
    """
    try:
        mastership.Release()
        mastership.Dispose()
        msg = 'Master access was released.'
        return True, msg
    except Exception, err:
        return False, err
