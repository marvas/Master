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
Gets the value of num and returns it as a string

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Result arg1: Boolean indicating if value exists
Result arg2: value or error (String)
"""


def get_value_num_tostring(rapid_data):
    try:
        res = 'Value = %s' % rapid_data.Value
        return True, res
    except Exception, err:
        return False, err


"""
Gets the state of bool and returns it as a string

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Result arg1: Boolean indicating if state exists
Result arg2: state or error (String)
"""


def get_state_bool_tostring(rapid_data):
    try:
        res = 'State = %s' % rapid_data.Value
        return True, res
    except Exception, err:
        return False, err


"""
Gets the trans data from robtarget and returns it as a string.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg1: Boolean indicating if trans exists or not
Return arg2: result of trans or error (String)
"""


def get_trans_robtarget_tostring(rapid_data):
    try:
        res = '(x,y,z) = (%d,%d,%d)' % (rapid_data.Value.Trans.X,rapid_data.Value.Trans.Y,rapid_data.Value.Trans.Z )
        return True, res
    except Exception, err:
        return False, err


"""
Gets the rot data from robtarget and returns it as a string.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg1: Boolean indicating if trans exists or not
Return arg2: result of trans or error (String)
"""


def get_rot_robtarget_tostring(rapid_data):
    try:
        res = '(Q1,Q2,Q3,Q4) = (%d,%d,%d,%d)' % (rapid_data.Value.Rot.Q1,rapid_data.Value.Rot.Q2,
                                                 rapid_data.Value.Rot.Q3,rapid_data.Value.Rot.Q4)
        return True, res
    except Exception, err:
        return False, err


"""
Gets the robconf data from robtarget and returns it as a string.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg1: Boolean indicating if trans exists or not
Return arg2: result of trans or error (String)
"""


def get_robconf_robtarget_tostring(rapid_data):
    try:
        res = '(Cf1,Cf4,Cf6,Cfx) = (%d,%d,%d,%d)' % (rapid_data.Value.Robconf.Cf1,rapid_data.Value.Robconf.Cf4,
                                                     rapid_data.Value.Robconf.Cf6,rapid_data.Value.Robconf.Cfx)
        return True, res
    except Exception, err:
        return False, err


"""
Gets the extax data from robtarget and returns it as a string.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg1: Boolean indicating if trans exists or not
Return arg2: result of trans or error (String)
"""


def get_extax_robtarget_tostring(rapid_data):
    try:
        eax_a = rapid_data.Value.Extax.Eax_a
        eax_b = rapid_data.Value.Extax.Eax_b
        eax_c = rapid_data.Value.Extax.Eax_c
        eax_d = rapid_data.Value.Extax.Eax_d
        eax_e = rapid_data.Value.Extax.Eax_e
        eax_f = rapid_data.Value.Extax.Eax_f
        if eax_a >= 8.9e+09:
            eax_a = '9E9'
        if eax_b >= 8.9e+09:
            eax_b = '9E9'
        if eax_c >= 8.9e+09:
            eax_c = '9E9'
        if eax_d >= 8.9e+09:
            eax_d = '9E9'
        if eax_e >= 8.9e+09:
            eax_e = '9E9'
        if eax_f >= 8.9e+09:
            eax_f = '9E9'
        res = '(Eax_a,Eax_b,Eax_c,Eax_d,Eax_e,Eax_f) = (%s,%s,%s,%s,%s,%s)' \
              % (eax_a,eax_b,eax_c,eax_d,eax_e,eax_f)
        return True, res
    except Exception, err:
        return False, err


"""
Gets Robhold from tooldata and returns it as a string.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg1: Boolean indicating if Robhold exists or not
Return arg2: result of trans or error (String)
"""


def get_robhold_tooldata_tostring(rapid_data):
    try:
        res = 'Robhold = %s' % rapid_data.Value.Robhold.ToString()
        return True, res
    except Exception, err:
        return False, err


"""
Gets Tframe from tooldata and returns it as a string.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg1: Boolean indicating if Tfarme exists or not
Return arg2: result of trans or error (String)
"""


def get_tframe_tooldata_tostring(rapid_data):
    try:
        res = 'Tframe = %s' % rapid_data.Value.Tframe.ToString()
        return True, res
    except Exception, err:
        return False, err


"""
Gets Tload from tooldata and returns it as a string.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg1: Boolean indicating if Tload exists or not
Return arg2: result of trans or error (String)
"""


def get_tload_tooldata_tostring(rapid_data):
    try:
        res = 'Tload = %s' % rapid_data.Value.Tload.ToString()
        return True, res
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



"""
Edits the specified robtarget property and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Argument arg2: property (String), accepted types: trans, rot, robconf, extax
Argument arg3: new_value (String), the new values of the type, ex for trans '100,100,100'
Return arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg2: message or error (String)
"""


def edit_and_write_rapid_data_robtarget_property(rapid_data, property, new_value):
    if rapid_data.RapidType == 'robtarget':
        try:
            robtarget = rapid_data.Value
            robtarget_trans = rapid_data.Value.Trans.ToString()
            robtarget_rot = rapid_data.Value.Rot.ToString()
            robtarget_robconf = rapid_data.Value.Robconf.ToString()
            robtarget_extax = rapid_data.Value.Extax.ToString()
            if property.lower() == 'trans':
                trans_list = new_value.split(',')
                if len(trans_list) == 3:
                    trans = "[[%d,%d,%d],%s,%s,%s]" % \
                          (float(trans_list[0]), float(trans_list[1]), float(trans_list[2]),
                           robtarget_rot, robtarget_robconf, robtarget_extax)
                    robtarget.FillFromString2(trans)
                    try:
                        rapid_data.Value = robtarget
                        msg = 'Trans updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Incorrect format of x,y,z: ex. \'10,50,0\'.'
                    return rapid_data, msg
            elif property.lower() == 'rot':
                rot_list = new_value.split(',')
                if len(rot_list) == 4:
                    rot = "[%s,[%d,%d,%d,%d],%s,%s]" % \
                          (robtarget_trans, float(rot_list[0]),float(rot_list[1]),float(rot_list[2]),float(rot_list[3]),
                           robtarget_robconf, robtarget_extax)
                    robtarget.FillFromString2(rot)
                    try:
                        rapid_data.Value = robtarget
                        msg = 'Rot updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Incorrect format of q1,q2,q3,q4: ex. \'0,0,1,0\'.'
                    return rapid_data, msg
            elif property.lower() == 'robconf':
                conf_data_list = new_value.split(',')
                if len(conf_data_list) == 4:
                    robconf = "[%s,%s,[%d,%d,%d,%d],%s]" % \
                              (robtarget_trans, robtarget_rot,
                               float(conf_data_list[0]),float(conf_data_list[1]),float(conf_data_list[2]),
                               float(conf_data_list[3]),robtarget_extax)
                    robtarget.FillFromString2(robconf)
                    try:
                        rapid_data.Value = robtarget
                        msg = 'Robconf updated.'
                        return  rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Incorrect format of Cf1,Cf4,Cf6,Cfx: ex. \'1,0,1,0\'.'
                    return rapid_data, msg
            elif property.lower() == 'extax':
                extax_list = new_value.split(',')
                if len(extax_list) == 6:
                    extax = "[%s,%s,%s,[%d,%d,%d,%d,%d,%d]]" % \
                            (robtarget_trans, robtarget_rot, robtarget_robconf,
                             float(extax_list[0]),float(extax_list[1]),
                             float(extax_list[2]),float(extax_list[3]),
                             float(extax_list[4]),float(extax_list[5]))
                    robtarget.FillFromString2(extax)
                    try:
                        rapid_data.Value = robtarget
                        msg = 'Extax updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Incorrect format of Eax_a,Eax_b,Eax_c,Eax_d,Eax_e,Eax_f: ex \'9E9,9E9,9E9,9E9,9E9,9E9\'.'
                    return rapid_data, msg
            else:
                msg = 'Property not of type trans, rot, robconf or extax.'
                return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not robtarget'
        return rapid_data, msg


"""
Edits the robtarget and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Argument arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Argument arg2: trans (String), ex. '100,0,100'
Argument arg3: rot (String), ex. '1,0,0,1'
Argument arg4: robconf (String), ex. '0,0,0,1'
Argument arg5: extax (String), ex. '9E9,9E9,9E9,9E9,9E9,9E9'
Return arg1: rapid_data (ABB.Robotics.Controllers.RapidDomain.RapidData)
Return arg2: message or error (String)
"""


def edit_and_write_rapid_data_robtarget(rapid_data, trans, rot, robconf, extax):
    if rapid_data.RapidType == 'robtarget':
        try:
            robtarget = rapid_data.Value

            trans_list = trans.split(',')
            rot_list = rot.split(',')
            robconf_list = robconf.split(',')
            extax_list = extax.split(',')
            if (len(trans_list) == 3) and (len(rot_list) == 4) and (len(robconf_list) == 4) and (len(extax_list) == 6):
                new_robtarget = "[[%d,%d,%d],[%d,%d,%d,%d],[%d,%d,%d,%d],[%d,%d,%d,%d,%d,%d]]" % \
                                (float(trans_list[0]), float(trans_list[1]), float(trans_list[2]),
                                 float(rot_list[0]), float(rot_list[1]), float(rot_list[2]), float(rot_list[3]),
                                 float(robconf_list[0]), float(robconf_list[1]), float(robconf_list[2]),
                                 float(robconf_list[3]), float(extax_list[0]), float(extax_list[1]),
                                 float(extax_list[2]), float(extax_list[3]), float(extax_list[4]), float(extax_list[5]))
                robtarget.FillFromString2(new_robtarget)
                try:
                    rapid_data.Value = robtarget
                    msg = 'Robtarget updated.'
                    return rapid_data, msg
                except Exception, err:
                    return rapid_data, err
            else:
                msg = 'Incorrect format of input data.'
                return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not robtarget'
        return rapid_data, msg


"""
"""
def edit_and_write_rapid_data_tooldata(rapid_data, property, new_value):
    if rapid_data.RapidType == 'tooldata':
        try:
            tooldata = rapid_data.Value
            tooldata_robhold = rapid_data.Value.Robhold.ToString()
            tooldata_tframe = rapid_data.Value.Tframe.ToString()
            tooldata_tload =  rapid_data.Value.Tload.ToString()
            if property.lower() == 'robhold':
                if new_value == True or new_value == False:
                    robhold = "[%i,[%s],[%s]]" % (new_value, tooldata_tframe, tooldata_tload)
                    tooldata.FillFromString2(robhold)
                    try:
                        rapid_data.Value = tooldata
                        msg = 'Robhold updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Input is not boolean.'
                    return rapid_data, msg
            # elif property.lower() == 'tframe':
            #
            # elif property.lower() == 'tload':
            # else:
            #     msg = 'Property not of type robhold, tframe, tload.'
            #     return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not tooldata'
        return rapid_data, msg