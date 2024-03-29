"""
Module for handling rapid datatype bool. This module makes it possible to edit and write a rapid datatype bool,
as well as displaying the value of the bool.
"""


import os

# Path to the folder with DLL
file_path = os.path.realpath(__file__)
temp = file_path.split('frontendPCSDK')
dll_path = temp[0] + 'ABB_PCSDK_DLL\ABB.Robotics.Controllers.PC.dll'

import clr
clr.AddReferenceToFileAndPath(dll_path)

import ABB.Robotics.Controllers as ctrlrs


def get_state_tostring(rapid_data):
    """
    Gets the state of bool and returns it as a string

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: The state or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'bool':
            res = 'State = %s' % rapid_data.Value
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not bool.'
            return err
    except Exception, err:
            return err


def get_state(rapid_data):
    """
    Gets the state of bool and returns it

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        Boolean OR String: Output depends on if it is successful or not
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'bool':
            if rapid_data.Value.ToString().lower() == 'true':
                return True
            elif rapid_data.Value.ToString().lower() == 'false':
                return False
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not bool.'
            return err
    except Exception, err:
            return err


def edit_and_write_rapid_data(rapid_data, new_value):
    """
    Edits the boolean variable to the specified state and writes it to the controller.
    Remember to get mastership before calling this function, and release the mastership right after.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
        Boolean: new_value
    Output:
        String: result message or error
    Example:
        message = edit_and_write_rapid_data(rapid_data, True)
        message = edit_and_write_rapid_data(rapid_data, False)
    """
    try:
        if rapid_data.RapidType == 'bool':
            rapid_data.Value = ctrlrs.RapidDomain.Bool(new_value)
            msg = 'Changed the value'
            return msg
        else:
            msg = 'DataType is ' + rapid_data.RapidType + ' and not bool.'
            return msg
    except Exception, err:
            return err
