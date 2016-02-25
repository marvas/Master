"""
Module for handling rapid datatype bool. This module makes it possible to edit and write a rapid datatype bool,
as well as displaying the value of the bool.
"""


import clr
clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')



"""
Gets the state of bool and returns it as a string

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if state exists
    String: The state or error
Examples:
    None
"""

def get_state_tostring(rapid_data):
    if rapid_data.RapidType == 'bool':
        try:
            res = 'State = %s' % rapid_data.Value
            return True, res
        except Exception, err:
            return False, err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not bool.'
        return False, err


"""
Gets the state of bool and returns it

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    ABB.Robotics.Controllers.RapidDomain.Bool OR String: Output depends on if it is successful or not
Examples:
    None
"""

def get_state(rapid_data):
    if rapid_data.RapidType == 'bool':
        try:
            if rapid_data.Value.ToString().lower() == 'true':
                return True
            elif rapid_data.Value.ToString().lower() == 'false':
                return False
        except Exception, err:
            return err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not bool.'
        return err


"""
Edits the boolean variable to the specified state and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Boolean: new_value
Returns:
    String: result message or error
Example:
    rapid_data, message = edit_and_write_rapid_data(rapid_data, True)
    rapid_data, message = edit_and_write_rapid_data(rapid_data, False)
"""

def edit_and_write_rapid_data(rapid_data, new_value):
    if rapid_data.RapidType == 'bool':
        try:
            rapid_data.Value = ctrlrs.RapidDomain.Bool(new_value)
            msg = 'Changed the value'
            return msg
        except Exception, err:
            return err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not bool'
        return msg