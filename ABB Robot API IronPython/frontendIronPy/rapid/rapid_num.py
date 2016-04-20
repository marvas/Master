"""
Module for handling rapid datatype num. This module makes it possible to edit and write a rapid datatype num,
as well as displaying the value of the num.
"""


import clr
clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')


"""
Gets the value of num and returns it as a string

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    String: The result or error
Examples:
    None
"""


def get_value_tostring(rapid_data):
    if rapid_data.RapidType == 'num':
        try:
            res = 'Value = %s' % rapid_data.Value
            return res
        except Exception, err:
            return err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not num.'
        return err


"""
Gets the value of num and returns it

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Float OR String: Output depends on if it is possible to get the value or not
Examples:
    None
"""


def get_value(rapid_data):
    if rapid_data.RapidType == 'num':
        try:
            return float(rapid_data.Value)
        except Exception, err:
            return err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not num.'
        return err


"""
Edits the num variable to the specified value and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Float|Int: new_value
Returns:
    String: result message or error
Examples:
    message = edit_and_write_rapid_data(rapid_data, 1)
    message = edit_and_write_rapid_data(rapid_data, 20)
"""


def edit_and_write_rapid_data(rapid_data, new_value):
    if rapid_data.RapidType == 'num':
        try:
            rapid_data.Value = ctrlrs.RapidDomain.Num(new_value)
            msg = 'Changed the value'
            return msg
        except Exception, err:
            return err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not num'
        return msg
