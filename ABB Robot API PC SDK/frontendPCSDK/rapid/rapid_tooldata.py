"""
Module for handling rapid datatype tooldata. This module makes it possible to edit and write the rapid datatype
tooldata, as well as displaying the different properties of the tooldata.
"""


def get_robhold_tostring(rapid_data):
    """
    Gets Robhold from tooldata and returns it as a string.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: Robhold or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'tooldata':
            res = 'Robhold = %s' % rapid_data.Value.Robhold
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not tooldata.'
            return err
    except Exception, err:
            return err


def get_tframe_tostring(rapid_data):
    """
    Gets Tframe from tooldata and returns it as a string.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: Tframe or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'tooldata':
            res = 'Tframe: [Trans,Rot] = [%s,%s]' % (rapid_data.Value.Tframe.Trans.ToString(),
                                                     rapid_data.Value.Tframe.Rot.ToString())
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not tooldata.'
            return err
    except Exception, err:
            return err


def get_tload_tostring(rapid_data):
    """
    Gets Tload from tooldata and returns it as a string.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: Tload or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'tooldata':
            res = 'Tload: [Mass,Cog,Aom,Ix,Iy,Iz] = [%G,%s,%s,%G,%G,%G]' % \
                  (rapid_data.Value.Tload.Mass, rapid_data.Value.Tload.Cog.ToString(),
                   rapid_data.Value.Tload.Aom.ToString(), rapid_data.Value.Tload.Ix,
                   rapid_data.Value.Tload.Iy, rapid_data.Value.Tload.Iz)
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not tooldata.'
            return err
    except Exception, err:
        return err


def get_tooldata_tostring(rapid_data):
    """
    Gets tooldata and returns it as a string.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: Tooldata or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'tooldata':
            res = 'Tooldata: %s' % rapid_data.Value.ToString()
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not tooldata.'
            return err
    except Exception, err:
        return err


def edit_and_write_rapid_data_property(rapid_data, property, new_value):
    """
    Edits the specified property of the tooldata and writes it to the controller.
    Remember to get mastership before calling this function, and release the mastership right after.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
        String: property (accepted types: robhold, tframe, tload)
        String|Bool: new_value
    Output:
        String: result message or error
    Examples:
        message = edit_and_write_rapid_data_property(rapid_data, 'robhold', True)
        message = edit_and_write_rapid_data_property(rapid_data, 'robhold', False)
        message = edit_and_write_rapid_data_property(rapid_data,'tframe','[0,0,100],[1,0,0,0]')
        message = edit_and_write_rapid_data_property(rapid_data,'tload', '[1,[0,0,1],[1,0,0,0],0,0,0]')
    """
    try:
        if rapid_data.RapidType == 'tooldata':
            tooldata = rapid_data.Value
            tooldata_robhold = rapid_data.Value.Robhold
            tooldata_tframe = rapid_data.Value.Tframe.ToString()
            tooldata_tload = rapid_data.Value.Tload.ToString()
            if property.lower() == 'robhold':
                if new_value == True or new_value == False:
                    if new_value == 1:
                        new_value = True
                    if new_value == 0:
                        new_value = False
                    robhold = "[%s,%s,%s]" % (new_value, tooldata_tframe, tooldata_tload)
                    tooldata.FillFromString2(robhold)
                else:
                    msg = 'Input is not boolean.'
                    return msg
            elif property.lower() == 'tframe':
                # Checks to see if input is string
                if isinstance(new_value, basestring):
                    new_value = new_value.translate(None, "[]")
                    tframe_list = new_value.split(',')
                    if len(tframe_list) == 7:
                        tframe = "[%s,[[%G,%G,%G],[%G,%G,%G,%G]],%s]" % \
                                 (tooldata_robhold, float(tframe_list[0]), float(tframe_list[1]), float(tframe_list[2]),
                                  float(tframe_list[3]), float(tframe_list[4]), float(tframe_list[5]),
                                  float(tframe_list[6]), tooldata_tload)
                        tooldata.FillFromString2(tframe)
                    else:
                        msg = 'Input is not a valid Tframe.'
                        return msg
                else:
                    msg = 'Input is not string.'
                    return msg
            elif property.lower() == 'tload':
                # Checks to see if input is string
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
                    else:
                        msg = 'Input is not a valid Tload.'
                        return msg
                else:
                    msg = 'Input is not string.'
                    return msg
            else:
                msg = 'Property not of type robhold, tframe, tload.'
                return msg
            try:
                rapid_data.Value = tooldata
                msg = '%s updated.' % property.title()
                return msg
            except Exception, err:
                return err
        else:
            msg = 'DataType is ' + rapid_data.RapidType + ' and not tooldata.'
            return msg
    except Exception, err:
        return err


def edit_and_write_rapid_data(rapid_data, robhold, tframe, tload):
    """
    Edits tooldata and writes it to the controller.
    Remember to get mastership before calling this function, and release the mastership right after.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
        Boolean: robhold (ex. True or False)
        String: tframe (ex. '[0,0,100],[0,0,0,1]')
        String: tload (ex. '[1,[0,0,1],[1,0,0,0],0,0,0]')
    Output:
        String: result message or error
    Examples:
        message = edit_and_write_rapid_data(rapid_data, True, '[0,0,100],[1,0,0,0]', '[1,[0,0,1],[1,0,0,0],0,0,0]')
    """
    try:
        if rapid_data.RapidType == 'tooldata':
            tooldata = rapid_data.Value

            # Checks if input is string
            if isinstance(tframe, basestring) and isinstance(tload, basestring):
                tframe = tframe.translate(None, "[]")
                tload = tload.translate(None, "[]")

                tframe_list = tframe.split(',')
                tload_list = tload.split(',')
                if (robhold == True or robhold == False) and (len(tframe_list) == 7) and (len(tload_list) == 11):
                    if robhold == 1:
                        robhold = True
                    if robhold == 0:
                        robhold = False
                    new_tooldata = "[%s,[[%G,%G,%G],[%G,%G,%G,%G]],[%G,[%G,%G,%G],[%G,%G,%G,%G],%G,%G,%G]]" % \
                                   (robhold, float(tframe_list[0]), float(tframe_list[1]), float(tframe_list[2]),
                                    float(tframe_list[3]), float(tframe_list[4]), float(tframe_list[5]),
                                    float(tframe_list[6]), float(tload_list[0]), float(tload_list[1]),
                                    float(tload_list[2]), float(tload_list[3]), float(tload_list[4]),
                                    float(tload_list[5]), float(tload_list[6]), float(tload_list[7]),
                                    float(tload_list[8]), float(tload_list[9]), float(tload_list[10]))
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
        else:
            msg = 'DataType is ' + rapid_data.RapidType + ' and not tooldata.'
            return msg
    except Exception, err:
        return err
