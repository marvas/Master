"""

"""


import clr
clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')



"""
Gets a Rapid object that reference a Rapid data instance on the robot controller.

Args:
    ABB.Robotics.Controllers.Controller: Controller
    String: Program (name of the program, typically "T_ROB1")
    String: Module (name of the module, ex "MainModule")
    String: Name of the variable to get (ex "target_10")
Returns:
    Boolean: Indicates if able to get the data or not
    ABB.Robotics.Controllers.RapidDomain.RapidData OR String: Rapid data object if successful and error string if not
Examples:
    bool, rapid_data = rapid_datatypes.get_rapid_data(controller,'T_ROB1','MainModule','p20')
"""

def get_rapid_data(controller, program, module, variable_name):
    try:
        rapid_data = controller.Rapid.GetRapidData(program, module, variable_name)
        return True, rapid_data
    except Exception, err:
        return False, err


"""
Gets the value of num and returns it as a string

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if value exists
    String: The result or error
Examples:
    None
"""

def get_value_num_tostring(rapid_data):
    try:
        res = 'Value = %s' % rapid_data.Value
        return True, res
    except Exception, err:
        return False, err


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

def get_state_bool_tostring(rapid_data):
    try:
        res = 'State = %s' % rapid_data.Value
        return True, res
    except Exception, err:
        return False, err


"""
Gets the trans data from robtarget and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if trans exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_trans_robtarget_tostring(rapid_data):
    try:
        res = 'Trans: (X,Y,Z) = (%d,%d,%d)' % (rapid_data.Value.Trans.X,rapid_data.Value.Trans.Y,rapid_data.Value.Trans.Z )
        return True, res
    except Exception, err:
        return False, err


"""
Gets the rot data from robtarget and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if trans exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_rot_robtarget_tostring(rapid_data):
    try:
        res = 'Rot: (Q1,Q2,Q3,Q4) = (%d,%d,%d,%d)' % (rapid_data.Value.Rot.Q1,rapid_data.Value.Rot.Q2,
                                                 rapid_data.Value.Rot.Q3,rapid_data.Value.Rot.Q4)
        return True, res
    except Exception, err:
        return False, err


"""
Gets the robconf data from robtarget and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if trans exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_robconf_robtarget_tostring(rapid_data):
    try:
        res = 'Robconf: (Cf1,Cf4,Cf6,Cfx) = (%d,%d,%d,%d)' % \
              (rapid_data.Value.Robconf.Cf1,rapid_data.Value.Robconf.Cf4,
                rapid_data.Value.Robconf.Cf6,rapid_data.Value.Robconf.Cfx)
        return True, res
    except Exception, err:
        return False, err


"""
Gets the extax data from robtarget and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if trans exists or not
    String: The result of trans or error
Examples:
    None
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
        res = 'Extax: (Eax_a,Eax_b,Eax_c,Eax_d,Eax_e,Eax_f) = (%s,%s,%s,%s,%s,%s)' \
              % (eax_a,eax_b,eax_c,eax_d,eax_e,eax_f)
        return True, res
    except Exception, err:
        return False, err


"""
Gets Robhold from tooldata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if Robhold exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_robhold_tooldata_tostring(rapid_data):
    try:
        res = 'Robhold = %s' % rapid_data.Value.Robhold.ToString()
        return True, res
    except Exception, err:
        return False, err


"""
Gets Tframe from tooldata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if Tframe exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_tframe_tooldata_tostring(rapid_data):
    try:
        res = 'Tframe: (Trans,Rot) = (%s,%s)' % (rapid_data.Value.Tframe.Trans.ToString(),
                                                 rapid_data.Value.Tframe.Rot.ToString())
        return True, res
    except Exception, err:
        return False, err


"""
Gets Tload from tooldata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if Tload exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_tload_tooldata_tostring(rapid_data):
    try:
        res = 'Tload: (Mass,Cog,Aom,Ix,Iy,Iz) = %d,%s,%s,%d,%d,%d' % \
              (rapid_data.Value.Tload.Mass, rapid_data.Value.Tload.Cog.ToString(),
               rapid_data.Value.Tload.Aom.ToString(),rapid_data.Value.Tload.Ix,
               rapid_data.Value.Tload.Iy, rapid_data.Value.Tload.Iz)
        return True, res
    except Exception, err:
        return False, err


"""
Gets Robhold from wobjdata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if Robhold exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_robhold_wobjdata_tostring(rapid_data):
    try:
        res = 'Robhold = %s' % rapid_data.Value.Robhold.ToString()
        return True, res
    except Exception, err:
        return False, err


"""
Gets Ufprog from wobjdata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if Ufprog exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_ufprog_wobjdata_tostring(rapid_data):
    try:
        res = 'Ufprog = %s' % rapid_data.Value.Ufprog.ToString()
        return True, res
    except Exception, err:
        return False, err


"""
Gets Ufmec from wobjdata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if Ufmec exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_ufmec_wobjdata_tostring(rapid_data):
    try:
        res = 'Ufmec = %s' % rapid_data.Value.Ufmec
        return True, res
    except Exception, err:
        return False, err


"""
Gets Uframe from wobjdata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if Uframe exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_uframe_wobjdata_tostring(rapid_data):
    try:
        res = 'Uframe: (Trans,Rot) = (%s,%s)' % (rapid_data.Value.Uframe.Trans.ToString(),
                                                 rapid_data.Value.Uframe.Rot.ToString())
        return True, res
    except Exception, err:
        return False, err


"""
Gets Oframe from wobjdata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if Oframe exists or not
    String: The result of trans or error
Examples:
    None
"""

def get_oframe_wobjdata_tostring(rapid_data):
    try:
        res = 'Oframe: (Trans,Rot) = (%s,%s)' % (rapid_data.Value.Oframe.Trans.ToString(),
                                                 rapid_data.Value.Oframe.Rot.ToString())
        return True, res
    except Exception, err:
        return False, err


"""
Edits the boolean variable to the specified state and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Boolean: new_value
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Example:
    rapid_data, message = edit_and_write_rapid_data_bool(rapid_data, True)
    rapid_data, message = edit_and_write_rapid_data_bool(rapid_data, False)
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

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Number: new_value
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
    rapid_data, message = edit_and_write_rapid_data_num(rapid_data, 1)
    rapid_data, message = edit_and_write_rapid_data_num(rapid_data, 20)
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

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: property (accepted types: trans, rot, robconf, extax)
    String: new_value
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
    rapid_data, message = edit_and_write_rapid_data_robtarget_property(rapid_data,'trans','[100,100,0]')
    rapid_data, message = edit_and_write_rapid_data_robtarget_property(rapid_data,'rot','[1,0,0,1]')
    rapid_data, message = edit_and_write_rapid_data_robtarget_property(rapid_data,'robconf','[1,0,1,0]')
    rapid_data, message = edit_and_write_rapid_data_robtarget_property(rapid_data,'extax','[9E9,9E9,9E9,9E9,9E9,9E9]')
"""

def edit_and_write_rapid_data_robtarget_property(rapid_data, property, new_value):
    if rapid_data.RapidType == 'robtarget':
        try:
            robtarget = rapid_data.Value
            robtarget_trans = rapid_data.Value.Trans.ToString()
            robtarget_rot = rapid_data.Value.Rot.ToString()
            robtarget_robconf = rapid_data.Value.Robconf.ToString()
            robtarget_extax = rapid_data.Value.Extax.ToString()

            new_value = new_value.translate(None, "[]")
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

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: trans
    String: rot
    String: robconf
    String: extax
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
   rapid_data, message = edit_and_write_rapid_data_robtarget(rapid_data,'[100,100,0]','[1,0,0,1]','[0,1,0,1]','[9E9,9E9,9E9,9E9,9E9,9E9]')
"""

def edit_and_write_rapid_data_robtarget(rapid_data, trans, rot, robconf, extax):
    if rapid_data.RapidType == 'robtarget':
        try:
            robtarget = rapid_data.Value

            trans = trans.translate(None, "[]")
            rot = rot.translate(None, "[]")
            robconf = robconf.translate(None, "[]")
            extax = extax.translate(None, "[]")

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
Edits the specified property of the tooldata and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: property (accepted types: robhold, tframe, tload)
    String: new_value
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
    rapid_data, message = edit_and_write_rapid_data_tooldata_property(rapid_data, 'robhold', True)
    rapid_data, message = edit_and_write_rapid_data_tooldata_property(rapid_data, 'robhold', False)
    rapid_data, message = edit_and_write_rapid_data_tooldata_property(rapid_data,'tframe','[0,0,100],[1,0,0,0]')
    rapid_data, message = edit_and_write_rapid_data_tooldata_property(rapid_data,'tload', '[1,[0,0,1],[1,0,0,0],0,0,0]')
"""

def edit_and_write_rapid_data_tooldata_property(rapid_data, property, new_value):
    if rapid_data.RapidType == 'tooldata':
        try:
            tooldata = rapid_data.Value
            tooldata_robhold = rapid_data.Value.Robhold.ToString()
            tooldata_tframe = rapid_data.Value.Tframe.ToString()
            tooldata_tload =  rapid_data.Value.Tload.ToString()
            if property.lower() == 'robhold':
                if new_value == True or new_value == False:
                    if new_value == 1: new_value = True
                    if new_value == 0: new_value = False
                    robhold = "[%s,%s,%s]" % (new_value, tooldata_tframe, tooldata_tload)
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
            elif property.lower() == 'tframe':
                new_value = new_value.translate(None, "[]")
                tframe_list = new_value.split(',')
                if len(tframe_list) == 7:
                    tframe = "[%s,[[%d,%d,%d],[%d,%d,%d,%d]],%s]" % \
                             (tooldata_robhold, float(tframe_list[0]), float(tframe_list[1]), float(tframe_list[2]),
                              float(tframe_list[3]), float(tframe_list[4]), float(tframe_list[5]),float(tframe_list[6]),
                              tooldata_tload)
                    tooldata.FillFromString2(tframe)
                    try:
                        rapid_data.Value = tooldata
                        msg = 'Tframe updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Input is not a valid Tframe.'
                    return rapid_data, msg
            elif property.lower() == 'tload':
                new_value = new_value.translate(None, "[]")
                tload_list = new_value.split(',')
                if len(tload_list) == 11:
                    tload = "[%s,%s,[%d,[%d,%d,%d],[%d,%d,%d,%d],%d,%d,%d]]" % \
                            (tooldata_robhold, tooldata_tframe, float(tload_list[0]), float(tload_list[1]),
                             float(tload_list[2]), float(tload_list[3]), float(tload_list[4]), float(tload_list[5]),
                             float(tload_list[6]), float(tload_list[7]), float(tload_list[8]), float(tload_list[9]),
                             float(tload_list[10]))
                    tooldata.FillFromString2(tload)
                    try:
                        rapid_data.Value = tooldata
                        msg = 'Tload updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Input is not a valid Tload.'
                    return rapid_data, msg
            else:
                msg = 'Property not of type robhold, tframe, tload.'
                return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not tooldata.'
        return rapid_data, msg


"""
Edits tooldata and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Boolean: robhold (ex. True or False)
    String: tframe (ex. '[0,0,100],[0,0,0,1]')
    String: tload (ex. '[1,[0,0,1],[1,0,0,0],0,0,0]')
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
    rapid_data, message = edit_and_write_rapid_data_tooldata(rapid_data, True, '[0,0,100],[1,0,0,0]', '[1,[0,0,1],[1,0,0,0],0,0,0]')
"""

def edit_and_write_rapid_data_tooldata(rapid_data, robhold, tframe, tload):
    if rapid_data.RapidType == 'tooldata':
        try:
            tooldata = rapid_data.Value

            tframe = tframe.translate(None, "[]")
            tload = tload.translate(None, "[]")

            tframe_list = tframe.split(',')
            tload_list = tload.split(',')
            if (robhold == True or robhold == False) and (len(tframe_list) == 7) and (len(tload_list) == 11):
                if robhold == 1: robhold = True
                if robhold == 0: robhold = False
                new_tooldata = "[%s,[[%d,%d,%d],[%d,%d,%d,%d]],[%d,[%d,%d,%d],[%d,%d,%d,%d],%d,%d,%d]]" % \
                               (robhold, float(tframe_list[0]), float(tframe_list[1]), float(tframe_list[2]),
                                float(tframe_list[3]), float(tframe_list[4]), float(tframe_list[5]),
                                float(tframe_list[6]), float(tload_list[0]), float(tload_list[1]), float(tload_list[2]),
                                float(tload_list[3]), float(tload_list[4]), float(tload_list[5]), float(tload_list[6]),
                                float(tload_list[7]), float(tload_list[8]), float(tload_list[9]), float(tload_list[10]))
                tooldata.FillFromString2(new_tooldata)
                try:
                    rapid_data.Value = tooldata
                    msg = 'Tooldata updated.'
                    return rapid_data, msg
                except Exception, err:
                    return rapid_data, err
            else:
                msg = 'Incorrect format of input data.'
                return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not tooldata'
        return rapid_data, msg


"""
Edits the specified property of the wobjdata and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: property (accepted types: robhold, ufprog, ufmec, uframe, oframe)
    String: new_value
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
    rapid_data, message = edit_and_write_rapid_data_tooldata_property(rapid_data, 'robhold', True)
    rapid_data, message = edit_and_write_rapid_data_tooldata_property(rapid_data, 'ufprog', False)
    rapid_data, message = edit_and_write_rapid_data_tooldata_property(rapid_data, 'ufmec', '')
    rapid_data, message = edit_and_write_rapid_data_tooldata_property(rapid_data,'uframe','[0,0,100],[1,0,0,0]')
    rapid_data, message = edit_and_write_rapid_data_tooldata_property(rapid_data,'oframe','[0,0,100],[1,0,0,0]')
"""

def edit_and_write_rapid_data_wobjdata_property(rapid_data, property, new_value):
    if rapid_data.RapidType == 'wobjdata':
        try:
            wobjdata = rapid_data.Value

            wobjdata_robhold = rapid_data.Value.Robhold.ToString()
            wobjdata_ufprog = rapid_data.Value.Ufprog.ToString()
            wobjdata_ufmec = rapid_data.Value.Ufmec.ToString()
            wobjdata_uframe = rapid_data.Value.Uframe.ToString()
            wobjdata_oframe = rapid_data.Value.Oframe.ToSTring()
            if property.lower() == 'robhold':
                if new_value == True or new_value == False:
                    if new_value == 1: new_value = True
                    if new_value == 0: new_value = False
                    robhold = "[%s,%s,%s,%s,%s]" % \
                              (new_value, wobjdata_ufprog, wobjdata_ufmec, wobjdata_uframe, wobjdata_oframe)
                    wobjdata.FillFromString2(robhold)
                    try:
                        rapid_data.Value = wobjdata
                        msg = 'Robhold updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Input is not boolean.'
                    return rapid_data, msg
            elif property.lower() == 'ufprog':
                if new_value == True or new_value == False:
                    if new_value == 1: new_value = True
                    if new_value == 0: new_value = False
                    ufprog = "[%s,%s,%s,%s,%s]" % \
                             (wobjdata_robhold, new_value, wobjdata_ufmec, wobjdata_uframe, wobjdata_oframe)
                    wobjdata.FillFromString2(ufprog)
                    try:
                        rapid_data.Value = wobjdata
                        msg = 'Ufprog updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Input is not boolean.'
                    return rapid_data, msg
            elif property.lower() == 'ufmec':
                if isinstance(new_value, basestring):
                    ufmec = "[%s,%s,%s,%s,%s]" % \
                            (wobjdata_robhold, wobjdata_ufprog, new_value, wobjdata_uframe, wobjdata_oframe)
                    wobjdata.FillFromString2(ufmec)
                    try:
                        rapid_data.Value = wobjdata
                        msg = 'Ufmec updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Input is not string.'
                    return rapid_data, msg
            elif property.lower() == 'uframe':
                new_value = new_value.translate(None, "[]")
                uframe_list = new_value.split(',')
                if len(uframe_list) == 7:
                    uframe = "[%s,%s,%s,[[%d,%d,%d],[%d,%d,%d,%d]],%s]" % \
                             (wobjdata_robhold, wobjdata_ufprog, wobjdata_ufmec,
                              float(uframe_list[0]), float(uframe_list[1]), float(uframe_list[2]),
                              float(uframe_list[3]), float(uframe_list[4]), float(uframe_list[5]),
                              float(uframe_list[6]), wobjdata_oframe)
                    wobjdata.FillFromString2(uframe)
                    try:
                        rapid_data.Value = wobjdata
                        msg = 'Uframe updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Input is not a valid Uframe.'
                    return rapid_data, msg
            elif property.lower() == 'oframe':
                new_value = new_value.translate(None, "[]")
                oframe_list = new_value.split(',')
                if len(oframe_list) == 7:
                    oframe = "[%s,%s,%s,%s,[[%d,%d,%d],[%d,%d,%d,%d]]]" % \
                            (wobjdata_robhold, wobjdata_ufprog, wobjdata_ufmec, wobjdata_uframe,
                             float(oframe_list[0]), float(oframe_list[1]), float(oframe_list[2]),
                             float(oframe_list[3]), float(oframe_list[4]), float(oframe_list[5]),
                             float(oframe_list[6]))
                    wobjdata.FillFromString2(oframe)
                    try:
                        rapid_data.Value = wobjdata
                        msg = 'Oframe updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Input is not a valid Oframe.'
                    return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not wobjdata'
        return rapid_data, msg


"""
Edits a wobjdata and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Boolean: robhold (ex. True or False)
    Boolean: ufprog (ex. True or False)
    String: ufmec (ex. '')
    String: uframe (ex. '[100,100,100],[1,0,0,0]')
    String: oframe (ex. '[0,0,0],[1,0,0,0]')
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
    rapid_data, message = edit_and_write_rapid_data_wobjdata(rapid_data, True, False,'','[100,100,0],[1,0,0,0]','[0,0,0],[1,0,0,0]')
"""

def edit_and_write_rapid_data_wobjdata(rapid_data, robhold, ufprog, ufmec, uframe, oframe):
    if rapid_data.RapidType == 'wobjdata':
        try:
            wobjdata = rapid_data.Value

            uframe = uframe.translate(None, "[]")
            oframe = oframe.translate(None, "[]")

            uframe_list = uframe.split(',')
            oframe_list = oframe.split(',')
            if (robhold == True or robhold == False) and (ufprog == True or ufprog == False)\
                    and (isinstance(ufprog, basestring)) and (len(uframe_list) == 7) and (len(oframe_list) == 7):
                if robhold == 1: robhold = True
                if robhold == 0: robhold = False
                if ufprog == 1: ufprog = True
                if ufprog == 0: ufprog = False
                new_wobjdata = "[%s,%s,%s,[[%d,%d,%d],[%d,%d,%d,%d]],[[%d,%d,%d],[%d,%d,%d,%d]]]" % \
                               (robhold, ufprog, ufmec, float(uframe_list[0]), float(uframe_list[1]), float(uframe_list[2]),
                                float(uframe_list[3]), float(uframe_list[4]), float(uframe_list[5]), float(uframe_list[6]),
                                float(oframe_list[0]), float(oframe_list[1]), float(oframe_list[2]), float(oframe_list[3]),
                                float(oframe_list[4]), float(oframe_list[5]), float(oframe_list[6]))
                wobjdata.FillFromString2(new_wobjdata)
                try:
                    rapid_data.Value = wobjdata
                    msg = 'Wobjdata updated.'
                    return rapid_data, msg
                except Exception, err:
                    return rapid_data, err
            else:
                msg = 'Incorrect format of input data.'
                return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not wobjdata'
        return rapid_data, msg


# """
# """
#
# def