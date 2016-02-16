"""
Module for reading and setting zonedata. Zonedata is not in RapidDomain in PC SDK as of now (16.02.16).
"""


#Base zonedata in format 'pzone_tcp, pzone_ori, pzone_eax, zone_ori, zone_leax, zone_reax'.
#First three points are for tool center point movement and last three point for tool reorientation.
base_zonedata_list = {'z0':     '0.3, 0.3, 0.3, 0.03, 0.3, 0.03',
                      'z1':     '1, 1, 1, 0.1, 1, 0.1',
                      'z5':     '5, 8, 8, 0.8, 8, 0.8',
                      'z10':    '10, 15, 15, 1.5, 15, 1.5',
                      'z15':    '15, 23, 23, 2.3, 23, 2.3',
                      'z20':    '20, 30, 30, 3.0, 30, 3.0',
                      'z30':    '30, 45, 45, 4.5, 45, 4.5',
                      'z40':    '40, 60, 60, 6.0, 60, 6.0',
                      'z50':    '50, 75, 75, 7.5, 75, 7.5',
                      'z60':    '60, 90, 90, 9.0, 90, 9.0',
                      'z80':    '80, 120, 120, 12, 120, 12',
                      'z100':   '100, 150, 150, 15, 150, 15',
                      'z150':   '150, 225, 225, 23, 225, 23',
                      'z200':   '200, 300, 300, 30, 300, 30'}


"""
Gets zonedata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    Boolean: Indicating if zonedata exists
    String: The result or error
Examples:
    None
"""

def get_zonedata_tostring(rapid_data):
    if rapid_data.RapidType == 'zonedata':
        try:
            zonedata = rapid_data.Value.ToString()
            zonedata = zonedata.translate(None, "[]")
            zonedata_list = zonedata.split(',')
            #Checks if the data is base zonedata values
            if :
                res = 'Base zonedata: z%d (%s)' % (int(speeddata_list[0]), rapid_data.Value.ToString())
                return True, res
            else:
                res = 'Zonedata: %s' % rapid_data.Value.ToString()
                return True, res
        except Exception, err:
            return False, err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not zonedata.'
        return False, err

"""
Edits the zonedata and writes it to the controller. Only supports base zonedata.
Remember to get mastership before calling this function, and release the mastership right after.

Base zonedata supported:
0, 1, 5, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: value
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
    rapid_data, message = edit_and_write_rapid_data_zonedata_base(rapid_data,'z0')
    rapid_data, message = edit_and_write_rapid_data_zonedata_base(rapid_data,'z20')
"""

def edit_and_write_rapid_data_zonedata_base(rapid_data, value):
    if rapid_data.RapidType == 'zonedata':
        try:
            zonedata = rapid_data.Value
            if isinstance(value, basestring):
                # Strips value for all leading and trailing whitespaces
                value = value.strip()
                # Checks if the first character is z
                if value[:1].lower() == 'z':
                    value_list = value.split('z')
                    # Checks if what comes after z is a digit. Checks if the value is in the base dictionary.
                    # Checks if the value list is of length 2 in case the user inserted a longer string, ex 'z1v10'.
                    if value_list[1].isdigit() and (value in base_zonedata_list) and (len(value_list) == 2):
                        new_zonedata = '[FALSE,%s]' % base_zonedata_list[value]
                        zonedata.FillFromString2(new_zonedata)
                        try:
                            rapid_data.Value = zonedata
                            msg = 'Zonedata updated.'
                            return rapid_data, msg
                        except Exception, err:
                            return  rapid_data, err
                    else:
                        msg = 'Something wrong with the input format, or the input is not a valid base zone.'
                        return rapid_data, msg
                else:
                    msg = 'Something wrong with the input. Not in format \'z1\''
                    return rapid_data, msg
            else:
                msg = 'Input has to be string. (ex. \'z1\')'
                return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is ' + rapid_data.RapidType + ' and not zonedata'
        return rapid_data, msg


"""
Edits the zonedata and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Boolean: finep
    Float: pzone_tcp
    Float: pzone_ori
    Float: pzone_eax
    Float: zone_ori
    Float: zone_leax
    Float: zone_reax
Returns:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: result message or error
Examples:
    rapid_data, message = edit_and_write_rapid_data_zonedata(rapid_data, False, 1, 1, 1, 0.1, 1, 0.1)
"""

def edit_and_write_rapid_data_zonedata(rapid_data, finep, pzone_tcp, pzone_ori, pzone_eax, zone_ori, zone_leax, zone_reax):
    if rapid_data.RapidType == 'zonedata':
        try:
            zonedata = rapid_data.Value
            #Checks if finep is a boolean, and checks if the rest is a number.
            if ((finep == True or finep == False) and isinstance(pzone_tcp,(int,float)) and
                isinstance(pzone_ori, (int,float)) and isinstance(pzone_eax, (int,float)) and
                isinstance(zone_ori, (int,float)) and isinstance(zone_leax, (int,float)) and
                isinstance(zone_reax, (int,float))):
                if finep == 1: finep = True
                if finep == 0: finep = False
                new_zonedata = '[%s,%G,%G,%G,%G,%G,%G]' % (finep, float(pzone_tcp), float(pzone_ori),
                                                           float(pzone_eax), float(zone_ori), float(zone_leax),
                                                           float(zone_reax))
                zonedata.FillFromString2(new_zonedata)
                try:
                    rapid_data.Value = zonedata
                    msg = 'Zonedata updated.'
                    return rapid_data, msg
                except Exception, err:
                    return rapid_data, err
            else:
                msg = 'Invalid input in one or more of the arguments'
                return rapid_data, msg
        except Exception, err:
            return rapid_data, err
    else:
        msg = 'DataType is ' + rapid_data.RapidType + ' and not zonedata'
        return rapid_data, msg