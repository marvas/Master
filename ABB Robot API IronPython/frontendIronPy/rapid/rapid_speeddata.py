"""
Module for reading and setting speeddata. Speeddata is not in RapidDomain in PC SDK as of now (16.02.16).
"""


base_speeddata_list = [5, 10, 20, 30, 40, 50, 60, 80, 100, 150, 200,
                       300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000]


"""
Gets speeddata and returns it as a string.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
Returns:
    String: The result or error
Examples:
    None
"""


def get_speeddata_tostring(rapid_data):
    if rapid_data.RapidType == 'speeddata':
        try:
            speeddata = rapid_data.Value.ToString()
            speeddata = speeddata.translate(None, "[]")
            speeddata_list = speeddata.split(',')
            try:
                # Checks if the data is base speeddata values
                if int(speeddata_list[0]) in base_speeddata_list and int(speeddata_list[1]) == 500 and \
                                int(speeddata_list[2]) == 5000 and int(speeddata_list[3]) == 1000:
                    res = 'Base speeddata: v%d (%s)' % (int(speeddata_list[0]), rapid_data.Value.ToString())
                    return res
                # If not base speed then custom speed.
                else:
                    res = 'Speeddata: %s' % rapid_data.Value.ToString()
                    return res
            # If value is of type float then it will fail on base speed check above.
            # Then the speed must be a custom speed with float.
            except ValueError:
                res = 'Speeddata: %s' % rapid_data.Value.ToString()
                return res
        except Exception, err:
            return err
    else:
        err = 'DataType is '+rapid_data.RapidType+' and not speeddata.'
        return err


"""
Edits the speeddata and writes it to the controller. Only supports base speeddata.
Remember to get mastership before calling this function, and release the mastership right after.

Base speeddata supported:
5, 10, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    String: value
Returns:
    String: result message or error
Examples:
    message = edit_and_write_rapid_data_base(rapid_data,'v100')
    message = edit_and_write_rapid_data_base(rapid_data,'v200')
"""


def edit_and_write_rapid_data_base(rapid_data, value):
    if rapid_data.RapidType == 'speeddata':
        try:
            speeddata = rapid_data.Value
            # Checks if value is string
            if isinstance(value, basestring):
                # Strips value for all leading and trailing whitespaces
                value = value.strip()
                # Checks if the first character is v
                if value[:1].lower() == 'v':
                    value = value.split('v')
                    # Checks if what comes after v is a digit. Checks if the value is in the base list.
                    # Checks if the value list is of length 2 in case the user inserted a longer string, ex 'v100v200'.
                    if value[1].isdigit() and (int(value[1]) in base_speeddata_list) and (len(value) == 2):
                        new_speeddata = '[%d,500,5000,1000]' % int(value[1])
                        speeddata.FillFromString2(new_speeddata)
                        try:
                            rapid_data.Value = speeddata
                            msg = 'Speeddata updated.'
                            return msg
                        except Exception, err:
                            return err
                    else:
                        msg = 'Something wrong with the input format, or the input is not a valid base speed.'
                        return msg
                else:
                    msg = 'Something wrong with the input. Not in format \'v100\''
                    return msg
            else:
                msg = 'Input has to be string. (ex. \'v100\')'
                return msg
        except Exception, err:
            return err
    else:
        msg = 'DataType is ' + rapid_data.RapidType + ' and not speeddata'
        return msg


"""
Edits the speeddata and writes it to the controller.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    ABB.Robotics.Controllers.RapidDomain.RapidData: rapid_data
    Float|Int: vel_tcp
    Float|Int: vel_orient
    Float|Int: vel_lin_extax
    Float|Int: vel_lin_rot_extax
Returns:
    String: result message or error
Examples:
    message = edit_and_write_rapid_data(rapid_data, 100, 500, 5000, 1000)
    message = edit_and_write_rapid_data(rapid_data, 100.5, 500, 5000.37, 1000)
"""


def edit_and_write_rapid_data(rapid_data, vel_tcp, vel_orient, vel_lin_extax, vel_lin_rot_extax):
    if rapid_data.RapidType == 'speeddata':
        try:
            speeddata = rapid_data.Value
            # Checks if all values are either integers or floats.
            if (isinstance(vel_tcp, (int, float)) and isinstance(vel_orient, (int, float)) and
                    isinstance(vel_lin_extax, (int, float)) and isinstance(vel_lin_rot_extax, (int, float))):
                new_speeddata = '[%G,%G,%G,%G]' % (float(vel_tcp), float(vel_orient),
                                                   float(vel_lin_extax), float(vel_lin_rot_extax))
                speeddata.FillFromString2(new_speeddata)
                try:
                    rapid_data.Value = speeddata
                    msg = 'Speeddata updated'
                    return msg
                except Exception, err:
                    return err
            else:
                msg = 'Invalid input in one or more of the arguments'
                return msg
        except Exception, err:
            return err
    else:
        msg = 'DataType is ' + rapid_data.RapidType + ' and not speeddata'
        return msg
