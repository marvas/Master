"""
Module for handling rapid datatype num. This module makes it possible to edit and write a rapid datatype num,
as well as displaying the value of the num.
"""


import clr
clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')


def get_value_tostring(rapid_data):
    """
    Gets the value of num and returns it as a string

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: The result or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'num':
            res = 'Value = %s' % rapid_data.Value
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not num.'
            return err
    except Exception, err:
            return err


def get_value(rapid_data):
    """
    Gets the value of num and returns it

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        Float OR String: Output depends on if it is possible to get the value or not
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'num':
            return float(rapid_data.Value)
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not num.'
            return err
    except Exception, err:
            return err


def edit_and_write_rapid_data(rapid_data, new_value):
    """
    Edits the num variable to the specified value and writes it to the controller.
    Remember to get mastership before calling this function, and release the mastership right after.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
        Float|Int: new_value
    Output:
        String: result message or error
    Examples:
        message = edit_and_write_rapid_data(rapid_data, 1)
        message = edit_and_write_rapid_data(rapid_data, 20)
    """
    try:
        if rapid_data.RapidType == 'num':
            rapid_data.Value = ctrlrs.RapidDomain.Num(new_value)
            msg = 'Changed the value'
            return msg
        else:
            msg = 'DataType is ' + rapid_data.RapidType + ' and not num.'
            return msg
    except Exception, err:
            return err
