"""

"""


import clr

clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')



"""
Gets a Rapid object that reference a Rapid data instance on the robot controller.

Argument arg1: controller (ABB.Robotics.Controllers.Controller)
Argument arg2: program (String), typically "T_ROB1"
Argument arg3: module (String), name of the module, ex "MainModule"
Argument arg4: variable_name (String), name of the variable to get, ex "target_10"
Return arg1: Boolean, if able to get the data or not.
Return arg2: If success, the object || If fail, error string
"""


def get_rapid_data(controller, program, module, variable_name):
    try:
        rapid_data = controller.Rapid.GetRapidData(program, module, variable_name)
        return True, rapid_data
    except Exception, err:
        return False, err


"""
Edits the boolean variable to the specified state and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Argument arg2: new_value (Boolean)
Return arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg2: message or error (String)
"""


def edit_and_write_rapid_data_bool(rapid_data, new_value):
    if rapid_data.RapidType == 'bool':
        try:
            rapid_data.Value = ctrlrs.RapidDomain.Bool(new_value)
            msg = 'Changed the value'
            return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not bool'
        return rapid_data, msg


"""
Edits the num variable to the specified value and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Argument arg2: new_value (number)
Return arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg2: message or error (String)
"""


def edit_and_write_rapid_data_num(rapid_data, new_value):
    if rapid_data.RapidType == 'num':
        try:
            rapid_data.Value = ctrlrs.RapidDomain.Num(new_value)
            msg = 'Changed the value'
            return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not num'
        return rapid_data, msg
