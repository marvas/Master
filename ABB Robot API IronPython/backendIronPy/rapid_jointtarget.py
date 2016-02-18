"""
Module for handling rapid datatype jointtarget. This module makes it possible to edit and write the rapid datatype
jointtarget, as well as displaying the different properties of the jointtarget.
"""



"""
Gets RobAx from jointtarget and returns it as a string

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if RobAx exists or not
    String: RobAx or error
Examples:
    None
"""

def get_robax_tostring(rapid_data):
    if rapid_data.RapidType == 'jointtarget':
        try:
            res = 'RobAx: [Rax_1,Rax_2,Rax_3,Rax_4,Rax_5,Rax_6] = %s' % rapid_data.Value.RobAx.ToString()
            return True, res
        except Exception, err:
            return False, err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not jointtarget.'
        return False, err


"""
Gets ExtAx from jointtarget and returns it as a string

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if ExtAx exists or not
    String: ExtAx or error
Examples:
    None
"""

def get_extax_tostring(rapid_data):
    if rapid_data.RapidType == 'jointtarget':
        try:
            extax = rapid_data.Value.ExtAx.ToString()
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
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not jointtarget.'
        return False, err


"""
Gets jointtarget and returns it as a string

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if jointtarget exists or not
    String: Jointtarget or error
Examples:
    None
"""

def get_jointtarget_tostring(rapid_data):
    if rapid_data.RapidType == 'jointtarget':
        try:
            res = 'Jointtarget: %s' % rapid_data.Value.ToString()
            return True, res
        except Exception, err:
            return False, err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not jointtarget.'
        return False, err


"""
Edits the specified property of the jointtarget and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: property (accepted types: robax, extax)
    String: new_value
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
    rapid_data, message = edit_and_write_rapid_data_property(rapid_data, 'robax', '[0,0,0,0,0,0]')
    rapid_data, message = edit_and_write_rapid_data_property(rapid_data, 'extax', '[9E9,9E9,9E9,9E9,9E9,9E9]')
"""

def edit_and_write_rapid_data_property(rapid_data, property, new_value):
    if rapid_data.RapidType == 'jointtarget':
        try:
            jointtarget = rapid_data.Value

            jointtarget_robax = rapid_data.Value.RobAx.ToString()
            jointtarget_extax = rapid_data.Value.ExtAx.ToString()

            #Checks if input is string
            if isinstance(new_value, basestring):
                new_value = new_value.translate(None,"[]")
                if property.lower() == 'robax':
                    robax_list = new_value.split(',')
                    if len(robax_list) == 6:
                        robax = "[[%G,%G,%G,%G,%G,%G],%s]" % \
                                (float(robax_list[0]), float(robax_list[1]), float(robax_list[2]),
                                 float(robax_list[3]), float(robax_list[4]), float(robax_list[5]),
                                 jointtarget_extax)
                        jointtarget.FillFromString2(robax)
                        try:
                            rapid_data.Value = jointtarget
                            msg = 'Robax updated.'
                            return rapid_data, msg
                        except Exception, err:
                            return rapid_data, err
                    else:
                        msg = 'Incorrect format of input data.'
                        return rapid_data, msg
                elif property.lower() == 'extax':
                    extax_list = new_value.split(',')
                    if len(extax_list) == 6:
                        extax = "[%s,[%G,%G,%G,%G,%G,%G]]" % \
                                (jointtarget_robax, float(extax_list[0]), float(extax_list[1]), float(extax_list[2]),
                                 float(extax_list[3]), float(extax_list[4]), float(extax_list[5]))
                        jointtarget.FillFromString2(extax)
                        try:
                            rapid_data.Value = jointtarget
                            msg = 'Extax updated.'
                            return rapid_data, msg
                        except Exception, err:
                            return rapid_data, err
                    else:
                        msg = 'Incorrect format of input.'
                        return rapid_data, msg
                else:
                    msg = 'Incorrect format of input data.'
                    return rapid_data, msg
            else:
                msg = 'Input is not string.'
                return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not jointtarget'
        return rapid_data, msg


"""
Edits the whole jointtarget and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: robax (ex. '[0,0,0,0,0,0]')
    String: extax (ex. '[9E9,9E9,9E9,9E9,9E9,9E9]')
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
    rapid_data, message = edit_and_write_rapid_data(rapid_data, '[0,0,0,0,0,0]', '[9E9,9E9,9E9,9E9,9E9,9E9]')
"""

def edit_and_write_rapid_data(rapid_data, robax, extax):
    if rapid_data.RapidType == 'jointtarget':
        try:
            jointtarget = rapid_data.Value
            #Checks if input is string
            if isinstance(robax, basestring) and isinstance(extax, basestring):
                robax = robax.translate(None, "[]")
                extax = extax.translate(None, "[]")

                robax_list = robax.split(',')
                extax_list = extax.split(',')
                if (len(robax_list) == 6) and (len(extax_list) == 6):
                    new_jointtarget = "[[%G,%G,%G,%G,%G,%G],[%G,%G,%G,%G,%G,%G]]" % \
                                   (float(robax_list[0]), float(robax_list[1]), float(robax_list[2]),
                                    float(robax_list[3]), float(robax_list[4]), float(robax_list[5]),
                                    float(extax_list[0]), float(extax_list[1]), float(extax_list[2]),
                                    float(extax_list[3]), float(extax_list[4]), float(extax_list[5]))
                    jointtarget.FillFromString2(new_jointtarget)
                    try:
                        rapid_data.Value = jointtarget
                        msg = 'Jointtarget updated.'
                        return rapid_data, msg
                    except Exception, err:
                        return rapid_data, err
                else:
                    msg = 'Incorrect format of input data.'
                    return rapid_data, msg
            else:
                msg = 'Input is not string.'
                return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not jointtarget'
        return rapid_data, msg