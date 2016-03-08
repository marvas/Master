"""
Module for handling rapid datatype tooldata. This module makes it possible to edit and write the rapid datatype
tooldata, as well as displaying the different properties of the tooldata.
"""



"""
Gets Robhold from tooldata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    String: Robhold or error
Examples:
    None
"""

def get_robhold_tostring(rapid_data):
    if rapid_data.RapidType == 'tooldata':
        try:
            res = 'Robhold = %s' % rapid_data.Value.Robhold.ToString()
            return res
        except Exception, err:
            return err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not tooldata.'
        return err


"""
Gets Tframe from tooldata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    String: Tframe or error
Examples:
    None
"""

def get_tframe_tostring(rapid_data):
    if rapid_data.RapidType == 'tooldata':
        try:
            res = 'Tframe: [Trans,Rot] = [%s,%s]' % (rapid_data.Value.Tframe.Trans.ToString(),
                                                     rapid_data.Value.Tframe.Rot.ToString())
            return res
        except Exception, err:
            return err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not tooldata.'
        return err


"""
Gets Tload from tooldata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    String: Tload or error
Examples:
    None
"""

def get_tload_tostring(rapid_data):
    if rapid_data.RapidType == 'tooldata':
        try:
            res = 'Tload: [Mass,Cog,Aom,Ix,Iy,Iz] = [%G,%s,%s,%G,%G,%G]' % \
                  (rapid_data.Value.Tload.Mass, rapid_data.Value.Tload.Cog.ToString(),
                   rapid_data.Value.Tload.Aom.ToString(),rapid_data.Value.Tload.Ix,
                   rapid_data.Value.Tload.Iy, rapid_data.Value.Tload.Iz)
            return res
        except Exception, err:
            return err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not tooldata.'
        return err


"""
Gets tooldata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    String: Tooldata or error
Examples:
    None
"""

def get_tooldata_tostring(rapid_data):
    if rapid_data.RapidType == 'tooldata':
        try:
            res = 'Tooldata: %s' % rapid_data.Value.ToString()
            return res
        except Exception, err:
            return err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not tooldata.'
        return err


"""
Edits the specified property of the tooldata and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: property (accepted types: robhold, tframe, tload)
    String|Bool: new_value
Returns:
    String: result message or error
Examples:
    message = edit_and_write_rapid_data_property(rapid_data, 'robhold', True)
    message = edit_and_write_rapid_data_property(rapid_data, 'robhold', False)
    message = edit_and_write_rapid_data_property(rapid_data,'tframe','[0,0,100],[1,0,0,0]')
    message = edit_and_write_rapid_data_property(rapid_data,'tload', '[1,[0,0,1],[1,0,0,0],0,0,0]')
"""

def edit_and_write_rapid_data_property(rapid_data, property, new_value):
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
                        return msg
                    except Exception, err:
                        return err
                else:
                    msg = 'Input is not boolean.'
                    return msg
            elif property.lower() == 'tframe':
                #Checks to see if input is string
                if isinstance(new_value, basestring):
                    new_value = new_value.translate(None, "[]")
                    tframe_list = new_value.split(',')
                    if len(tframe_list) == 7:
                        tframe = "[%s,[[%G,%G,%G],[%G,%G,%G,%G]],%s]" % \
                                 (tooldata_robhold, float(tframe_list[0]), float(tframe_list[1]), float(tframe_list[2]),
                                  float(tframe_list[3]), float(tframe_list[4]), float(tframe_list[5]),float(tframe_list[6]),
                                  tooldata_tload)
                        tooldata.FillFromString2(tframe)
                        try:
                            rapid_data.Value = tooldata
                            msg = 'Tframe updated.'
                            return msg
                        except Exception, err:
                            return err
                    else:
                        msg = 'Input is not a valid Tframe.'
                        return msg
                else:
                    msg = 'Input is not string.'
                    return msg
            elif property.lower() == 'tload':
                #Checks to see if input is string
                if isinstance(new_value, basestring):
                    new_value = new_value.translate(None, "[]")
                    tload_list = new_value.split(',')
                    if len(tload_list) == 11:
                        tload = "[%s,%s,[%G,[%G,%G,%G],[%G,%G,%G,%G],%G,%G,%G]]" % \
                                (tooldata_robhold, tooldata_tframe, float(tload_list[0]), float(tload_list[1]),
                                 float(tload_list[2]), float(tload_list[3]), float(tload_list[4]), float(tload_list[5]),
                                 float(tload_list[6]), float(tload_list[7]), float(tload_list[8]), float(tload_list[9]),
                                 float(tload_list[10]))
                        tooldata.FillFromString2(tload)
                        try:
                            rapid_data.Value = tooldata
                            msg = 'Tload updated.'
                            return msg
                        except Exception, err:
                            return err
                    else:
                        msg = 'Input is not a valid Tload.'
                        return msg
                else:
                    msg = 'Input is not string.'
                    return msg
            else:
                msg = 'Property not of type robhold, tframe, tload.'
                return msg
        except Exception, err:
            return err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not tooldata.'
        return msg


"""
Edits tooldata and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Boolean: robhold (ex. True or False)
    String: tframe (ex. '[0,0,100],[0,0,0,1]')
    String: tload (ex. '[1,[0,0,1],[1,0,0,0],0,0,0]')
Returns:
    String: result message or error
Examples:
    message = edit_and_write_rapid_data(rapid_data, True, '[0,0,100],[1,0,0,0]', '[1,[0,0,1],[1,0,0,0],0,0,0]')
"""

def edit_and_write_rapid_data(rapid_data, robhold, tframe, tload):
    if rapid_data.RapidType == 'tooldata':
        try:
            tooldata = rapid_data.Value

            #Checks if input is string
            if isinstance(tframe, basestring) and isinstance(tload, basestring):
                tframe = tframe.translate(None, "[]")
                tload = tload.translate(None, "[]")

                tframe_list = tframe.split(',')
                tload_list = tload.split(',')
                if (robhold == True or robhold == False) and (len(tframe_list) == 7) and (len(tload_list) == 11):
                    if robhold == 1: robhold = True
                    if robhold == 0: robhold = False
                    new_tooldata = "[%s,[[%G,%G,%G],[%G,%G,%G,%G]],[%G,[%G,%G,%G],[%G,%G,%G,%G],%G,%G,%G]]" % \
                                   (robhold, float(tframe_list[0]), float(tframe_list[1]), float(tframe_list[2]),
                                    float(tframe_list[3]), float(tframe_list[4]), float(tframe_list[5]),
                                    float(tframe_list[6]), float(tload_list[0]), float(tload_list[1]), float(tload_list[2]),
                                    float(tload_list[3]), float(tload_list[4]), float(tload_list[5]), float(tload_list[6]),
                                    float(tload_list[7]), float(tload_list[8]), float(tload_list[9]), float(tload_list[10]))
                    tooldata.FillFromString2(new_tooldata)
                    try:
                        rapid_data.Value = tooldata
                        msg = 'Tooldata updated.'
                        return msg
                    except Exception, err:
                        return err
                else:
                    msg = 'Incorrect format of input data.'
                    return msg
            else:
                msg = 'Input is not string.'
                return msg
        except Exception, err:
            return err
    else:
        msg = 'DataType is '+rapid_data.RapidType+' and not tooldata'
        return msg