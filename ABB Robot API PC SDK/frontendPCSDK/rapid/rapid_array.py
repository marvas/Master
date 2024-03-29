"""
Module handling one dimensional arrays in RAPID. This module only supports editing and writing rapid type num.
"""


import os

# Path to the folder with DLL
file_path = os.path.realpath(__file__)
temp = file_path.split('frontendPCSDK')
dll_path = temp[0] + 'ABB_PCSDK_DLL\ABB.Robotics.Controllers.PC.dll'

import clr
clr.AddReferenceToFileAndPath(dll_path)

import ABB.Robotics.Controllers as ctrlrs


def get_length(rapid_data):
    """
    Gets the length of array and returns it. Only shows the length of first dimension.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        Int|String: Output depends on if it is possible to get the length or not
    Examples:
        None
    """
    try:
        if rapid_data.IsArray:
            return int(rapid_data.Value.Length)
        else:
            err = 'The input is not an array.'
            return err
    except Exception, err:
            return err


def get_dimensions(rapid_data):
    """
    Gets the dimension of array and returns it.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        Int|String: Output depends on if it is possible to get the dimension or not
    Examples:
        None
    """
    try:
        if rapid_data.IsArray:
            return int(rapid_data.Value.Rank)
        else:
            err = 'The input is not an array.'
            return err
    except Exception, err:
            return err


def edit_and_write_rapid_data_num_index(rapid_data, index, value):
    """
    Inserts a value into num array with index and writes it to the controller.
    Remember to get mastership before calling this function, and release the mastership right after.
    Index starts from 0.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
        Integer: Index, array index
        Float|Int: Value
    Output:
        String: result message or error
    Examples:
        message = edit_and_write_rapid_data_num_index(rapid_data, 0, 100)
    """
    try:
        if rapid_data.RapidType == 'num' and rapid_data.IsArray:
            if index < rapid_data.Value.Length and index >= 0 and isinstance(index, int):
                if isinstance(value, (int, float)):
                    rapid_data.WriteItem(ctrlrs.RapidDomain.Num(value), index)
                    msg = 'Array updated.'
                    return msg
                else:
                    msg = 'Value is not a number.'
                    return msg
            else:
                msg = 'Index is not valid.'
                return msg
        else:
            msg = 'Datatype is not array of num.'
            return msg
    except Exception, err:
            return err


def edit_and_write_rapid_data_num(rapid_data, values):
    """
    Inserts a list of values into num array and writes it to the controller.
    Remember to get mastership before calling this function, and release the mastership right after.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
        List: values, ex([100,1,2])
    Output:
        String: result message or error
    Examples:
        If RAPID array is of length 3:
        message = edit_and_write_rapid_data_num(rapid_data, []) Formats array to default.
        message = edit_and_write_rapid_data_num(rapid_data, [100,1,50])
        message = edit_and_write_rapid_data_num(rapid_data, [100,1.1,50])
        message = edit_and_write_rapid_data_num(rapid_data, [100])
        If RAPID array is of length 3 this is not possible:
        message = edit_and_write_rapid_data_num(rapid_data, [100,1,50,100])
    """
    try:
        if rapid_data.RapidType == 'num' and rapid_data.IsArray:
            num_array = rapid_data.Value
            # Checks if values are a list.
            if isinstance(values, list):
                # Returns if values are larger than the RAPID list.
                if len(values) > rapid_data.Value.Length:
                    msg = 'Input list is larger than RAPID list.'
                    return msg
                # Checks if all values in input values are of type int or float.
                for value in values:
                    if isinstance(value, (int, float)) == False:
                        msg = 'Something wrong in list.'
                        return msg
                # If size of values are smaller than RAPID list, then fill the list
                # with zeroes until they are the same size.
                if len(values) < rapid_data.Value.Length:
                    diff = rapid_data.Value.Length - len(values)
                    for _ in range(0, diff):
                        values.append(0)
                    new_array = str(values)
                else:
                    new_array = str(values)
                num_array.FillFromString(new_array)
                msg = 'Array updated.'
                return msg
            else:
                msg = 'Values is not a list.'
                return msg

        else:
            msg = 'Datatype is not array of num.'
            return msg
    except Exception, err:
        return err
