"""
Module for handling rapid datatype robtarget. This module makes it possible to edit and write the rapid datatype
robtarget, as well as displaying the different properties of the robtarget.
"""


import clr
clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')


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

def get_trans_tostring(rapid_data):
    try:
        res = 'Trans: [X,Y,Z] = [%d,%d,%d]' % (rapid_data.Value.Trans.X,rapid_data.Value.Trans.Y,rapid_data.Value.Trans.Z )
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

def get_rot_tostring(rapid_data):
    try:
        res = 'Rot: [Q1,Q2,Q3,Q4] = [%d,%d,%d,%d]' % (rapid_data.Value.Rot.Q1,rapid_data.Value.Rot.Q2,
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

def get_robconf_tostring(rapid_data):
    try:
        res = 'Robconf: [Cf1,Cf4,Cf6,Cfx] = [%d,%d,%d,%d]' % \
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

def get_extax_tostring(rapid_data):
    try:
        extax = rapid_data.Value.Extax.ToString()
        extax = extax.translate(None, "[]+")
        extax_list = extax.split(',')
        #Loop to format extax.
        for i, eax in list(enumerate(extax_list)):
            if "E" in eax:
                eax = eax.split('E')
                eax = eax[0]+"E%d" % float(eax[1])
                extax_list[i] = eax
            else:
                extax_list[i] = eax
        res = 'Extax: [Eax_a,Eax_b,Eax_c,Eax_d,Eax_e,Eax_f] = [%s,%s,%s,%s,%s,%s]' \
              % (extax_list[0],extax_list[1],extax_list[2],extax_list[3],extax_list[4],extax_list[5])
        return True, res
    except Exception, err:
        return False, err


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
    rapid_data, message = edit_and_write_rapid_data_property(rapid_data,'trans','[100,100,0]')
    rapid_data, message = edit_and_write_rapid_data_property(rapid_data,'rot','[1,0,0,1]')
    rapid_data, message = edit_and_write_rapid_data_property(rapid_data,'robconf','[1,0,1,0]')
    rapid_data, message = edit_and_write_rapid_data_property(rapid_data,'extax','[9E9,9E9,9E9,9E9,9E9,9E9]')
"""

def edit_and_write_rapid_data_property(rapid_data, property, new_value):
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
   rapid_data, message = edit_and_write_rapid_data(rapid_data,'[100,100,0]','[1,0,0,1]','[0,1,0,1]','[9E9,9E9,9E9,9E9,9E9,9E9]')
"""

def edit_and_write_rapid_data(rapid_data, trans, rot, robconf, extax):
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