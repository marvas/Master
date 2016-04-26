"""
Module for handling rapid datatype wobjdata. This module makes it possible to edit and write the rapid datatype
wobjdata, as well as displaying the different properties of the wobjdata.
"""


import clr
clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')


def get_robhold_tostring(rapid_data):
    """
    Gets Robhold from wobjdata and returns it as a string.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: Robhold or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'wobjdata':
            res = 'Robhold = %s' % rapid_data.Value.Robhold
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not wobjdata.'
            return err
    except Exception, err:
        return err


def get_ufprog_tostring(rapid_data):
    """
    Gets Ufprog from wobjdata and returns it as a string.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: Ufprog or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'wobjdata':
            res = 'Ufprog = %s' % rapid_data.Value.Ufprog
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not wobjdata.'
            return err
    except Exception, err:
        return err


def get_ufmec_tostring(rapid_data):
    """
    Gets Ufmec from wobjdata and returns it as a string.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: Ufmec or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'wobjdata':
            res = 'Ufmec = %s' % rapid_data.Value.Ufmec
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not wobjdata.'
            return err
    except Exception, err:
        return err


def get_uframe_tostring(rapid_data):
    """
    Gets Uframe from wobjdata and returns it as a string.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: Uframe or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'wobjdata':
            res = 'Uframe: [Trans,Rot] = [%s,%s]' % (rapid_data.Value.Uframe.Trans.ToString(),
                                                     rapid_data.Value.Uframe.Rot.ToString())
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not wobjdata.'
            return err
    except Exception, err:
        return err


def get_oframe_tostring(rapid_data):
    """
    Gets Oframe from wobjdata and returns it as a string.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: Oframe or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'wobjdata':
            res = 'Oframe: [Trans,Rot] = [%s,%s]' % (rapid_data.Value.Oframe.Trans.ToString(),
                                                     rapid_data.Value.Oframe.Rot.ToString())
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not wobjdata.'
            return err
    except Exception, err:
        return err


def get_wobjdata_tostring(rapid_data):
    """
    Gets wobjdata and returns it as a string.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Output:
        String: Wobjdata or error
    Examples:
        None
    """
    try:
        if rapid_data.RapidType == 'wobjdata':
            res = 'Wobjdata: %s' % rapid_data.Value.ToString()
            return res
        else:
            err = 'DataType is ' + rapid_data.RapidType + ' and not wobjdata.'
            return err
    except Exception, err:
        return err


def edit_and_write_rapid_data_property(rapid_data, property, new_value):
    """
    Edits the specified property of the wobjdata and writes it to the controller.
    Remember to get mastership before calling this function, and release the mastership right after.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
        String: property (accepted types: robhold, ufprog, ufmec, uframe, oframe)
        String|Bool: new_value
    Output:
        String: result message or error
    Examples:
        message = edit_and_write_rapid_data_property(rapid_data, 'robhold', True)
        message = edit_and_write_rapid_data_property(rapid_data, 'ufprog', False)
        message = edit_and_write_rapid_data_property(rapid_data, 'ufmec', '')
        message = edit_and_write_rapid_data_property(rapid_data,'uframe','[0,0,100],[1,0,0,0]')
        message = edit_and_write_rapid_data_property(rapid_data,'oframe','[0,0,100],[1,0,0,0]')
    """
    try:
        if rapid_data.RapidType == 'wobjdata':
            wobjdata = rapid_data.Value

            wobjdata_robhold = rapid_data.Value.Robhold
            wobjdata_ufprog = rapid_data.Value.Ufprog
            wobjdata_ufmec = rapid_data.Value.Ufmec.ToString()
            wobjdata_uframe = rapid_data.Value.Uframe.ToString()
            wobjdata_oframe = rapid_data.Value.Oframe.ToString()
            if property.lower() == 'robhold':
                if new_value == True or new_value == False:
                    if new_value == 1:
                        new_value = True
                    if new_value == 0:
                        new_value = False
                    robhold = "[%s,%s,%s,%s,%s]" % \
                              (new_value, wobjdata_ufprog, ctrlrs.RapidDomain.String(wobjdata_ufmec),
                               wobjdata_uframe, wobjdata_oframe)
                    wobjdata.FillFromString2(robhold)
                else:
                    msg = 'Input is not boolean.'
                    return msg
            elif property.lower() == 'ufprog':
                if new_value == True or new_value == False:
                    if new_value == 1:
                        new_value = True
                    if new_value == 0:
                        new_value = False
                    ufprog = "[%s,%s,%s,%s,%s]" % \
                             (wobjdata_robhold, new_value, ctrlrs.RapidDomain.String(wobjdata_ufmec),
                              wobjdata_uframe, wobjdata_oframe)
                    wobjdata.FillFromString2(ufprog)
                else:
                    msg = 'Input is not boolean.'
                    return msg
            elif property.lower() == 'ufmec':
                if isinstance(new_value, basestring):
                    ufmec = "[%s,%s,%s,%s,%s]" % \
                            (wobjdata_robhold, wobjdata_ufprog, ctrlrs.RapidDomain.String(new_value),
                             wobjdata_uframe, wobjdata_oframe)
                    wobjdata.FillFromString2(ufmec)
                else:
                    msg = 'Input is not string.'
                    return msg
            elif property.lower() == 'uframe':
                if isinstance(new_value, basestring):
                    new_value = new_value.translate(None, "[]")
                    uframe_list = new_value.split(',')
                    if len(uframe_list) == 7:
                        uframe = "[%s,%s,%s,[[%G,%G,%G],[%G,%G,%G,%G]],%s]" % \
                                 (wobjdata_robhold, wobjdata_ufprog, ctrlrs.RapidDomain.String(wobjdata_ufmec),
                                  float(uframe_list[0]), float(uframe_list[1]), float(uframe_list[2]),
                                  float(uframe_list[3]), float(uframe_list[4]), float(uframe_list[5]),
                                  float(uframe_list[6]), wobjdata_oframe)
                        wobjdata.FillFromString2(uframe)
                    else:
                        msg = 'Input is not a valid Uframe.'
                        return msg
                else:
                    msg = 'Input is not string.'
                    return msg
            elif property.lower() == 'oframe':
                if isinstance(new_value, basestring):
                    new_value = new_value.translate(None, "[]")
                    oframe_list = new_value.split(',')
                    if len(oframe_list) == 7:
                        oframe = "[%s,%s,%s,%s,[[%G,%G,%G],[%G,%G,%G,%G]]]" % \
                                 (wobjdata_robhold, wobjdata_ufprog, ctrlrs.RapidDomain.String(wobjdata_ufmec),
                                  wobjdata_uframe, float(oframe_list[0]), float(oframe_list[1]),
                                  float(oframe_list[2]), float(oframe_list[3]), float(oframe_list[4]),
                                  float(oframe_list[5]), float(oframe_list[6]))
                        wobjdata.FillFromString2(oframe)
                    else:
                        msg = 'Input is not a valid Oframe.'
                        return msg
                else:
                    msg = 'Input is not string.'
                    return msg
            else:
                msg = 'Property not of type robhold, ufprog, ufmec, uframe or oframe.'
                return msg
            try:
                rapid_data.Value = wobjdata
                msg = '%s updated.' % property.title()
                return msg
            except Exception, err:
                return err
        else:
            msg = 'DataType is ' + rapid_data.RapidType + ' and not wobjdata.'
            return msg
    except Exception, err:
        return err


def edit_and_write_rapid_data(rapid_data, robhold, ufprog, ufmec, uframe, oframe):
    """
    Edits the wobjdata and writes it to the controller.
    Remember to get mastership before calling this function, and release the mastership right after.

    Input:
        ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
        Boolean: robhold (ex. True or False)
        Boolean: ufprog (ex. True or False)
        String: ufmec (ex. '')
        String: uframe (ex. '[100,100,100],[1,0,0,0]')
        String: oframe (ex. '[0,0,0],[1,0,0,0]')
    Output:
        String: result message or error
    Examples:
        message = edit_and_write_rapid_data(rapid_data, True, False,'','[100,100,0],[1,0,0,0]','[0,0,0],[1,0,0,0]')
    """
    try:
        if rapid_data.RapidType == 'wobjdata':
            wobjdata = rapid_data.Value

            # Checks if uframe and oframe is of type string.
            if isinstance(uframe, basestring) and isinstance(oframe, basestring):
                uframe = uframe.translate(None, "[]")
                oframe = oframe.translate(None, "[]")

                uframe_list = uframe.split(',')
                oframe_list = oframe.split(',')
                if (robhold == True or robhold == False) and (ufprog == True or ufprog == False)\
                        and (isinstance(ufmec, basestring)) and (len(uframe_list) == 7) and (len(oframe_list) == 7):
                    if robhold == 1:
                        robhold = True
                    if robhold == 0:
                        robhold = False
                    if ufprog == 1:
                        ufprog = True
                    if ufprog == 0:
                        ufprog = False
                    new_wobjdata = "[%s,%s,%s,[[%G,%G,%G],[%G,%G,%G,%G]],[[%G,%G,%G],[%G,%G,%G,%G]]]" % \
                                   (robhold, ufprog, ctrlrs.RapidDomain.String(ufmec), float(uframe_list[0]),
                                    float(uframe_list[1]), float(uframe_list[2]), float(uframe_list[3]),
                                    float(uframe_list[4]), float(uframe_list[5]), float(uframe_list[6]),
                                    float(oframe_list[0]), float(oframe_list[1]), float(oframe_list[2]),
                                    float(oframe_list[3]), float(oframe_list[4]), float(oframe_list[5]),
                                    float(oframe_list[6]))
                    wobjdata.FillFromString2(new_wobjdata)
                    try:
                        rapid_data.Value = wobjdata
                        msg = 'Wobjdata updated.'
                        return msg
                    except Exception, err:
                        return err
                else:
                    msg = 'Incorrect format of input data.'
                    return msg
            else:
                msg = 'Incorrect format of input data.'
                return msg
        else:
            msg = 'DataType is ' + rapid_data.RapidType + ' and not wobjdata.'
            return msg
    except Exception, err:
        return err
