"""
Module for handling rapid datatype robtarget. This module makes it possible to edit and write the rapid datatype
robtarget, as well as displaying the different properties of the robtarget.
"""

import unicodedata

import requests



"""
Gets the trans data from robtarget and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Trans or error
Examples:
    None
"""

def get_trans_tostring(response_dict):
    if response_dict['dattyp'] == 'robtarget':
        try:
            # Formatting the robtarget to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Robtarget should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Trans: [X,Y,Z] = [%s,%s,%s]' % (value_list[0], value_list[1], value_list[2])
                return res
            else:
                err = 'Something wrong with the robtarget: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not robtarget.'
        return err


"""
Gets the rot data from robtarget and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Rot or error
Examples:
    None
"""

def get_rot_tostring(response_dict):
    if response_dict['dattyp'] == 'robtarget':
        try:
            # Formatting the robtarget to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Robtarget should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Rot: [Q1,Q2,Q3,Q4] = [%s,%s,%s,%s]' % (value_list[3], value_list[4], value_list[5], value_list[6])
                return res
            else:
                err = 'Something wrong with the robtarget: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not robtarget.'
        return err


"""
Gets the robconf data from robtarget and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Robconf or error
Examples:
    None
"""

def get_robconf_tostring(response_dict):
    if response_dict['dattyp'] == 'robtarget':
        try:
            # Formatting the robtarget to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Robtarget should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Robconf: [Cf1,Cf4,Cf6,Cfx] = [%s,%s,%s,%s]' % \
                      (value_list[7], value_list[8], value_list[9], value_list[10])
                return res
            else:
                err = 'Something wrong with the robtarget: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not robtarget.'
        return err


"""
Gets the extax data from robtarget and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Extax or error
Examples:
    None
"""

def get_extax_tostring(response_dict):
    if response_dict['dattyp'] == 'robtarget':
        try:
            # Formatting the robtarget to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Robtarget should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Extax: [Eax_a,Eax_b,Eax_c,Eax_d,Eax_e,Eax_f] = [%s,%s,%s,%s,%s,%s]' % \
                      (value_list[11], value_list[12], value_list[13], value_list[14],
                       value_list[15], value_list[16])
                return res
            else:
                err = 'Something wrong with the robtarget: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not robtarget.'
        return err


"""
Gets robtarget and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Robtarget or error
Examples:
    None
"""

def get_robtarget_tostring(response_dict):
    if response_dict['dattyp'] == 'robtarget':
        try:
            # Formatting the robtarget to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Robtarget should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Robtarget: %s' % response_dict['value']
                return res
            else:
                err = 'Something wrong with the robtarget: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not robtarget.'
        return err


"""
Edit and write the specified robtarget property.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    String: IP address
    Requests.cookies.requestsCookieJar: cookies
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'x')
    String: property (properties: trans, rot, robconf, extax)
    String: new_value (new value, ex '[10,0,0]' for trans)
Returns:
    String: result message or error
Examples:
    message = edit_and_write_rapid_data_property('local', cookies, 'T_ROB1', 'MainModule', 'target', 'trans', '[100,100,0]')
    message = edit_and_write_rapid_data_property('local', cookies, 'T_ROB1', 'MainModule', 'target', 'rot', '[1,0,0,0]')
    message = edit_and_write_rapid_data_property('local', cookies, 'T_ROB1', 'MainModule', 'target', 'robconf', '[0,0,1,0]')
    message = edit_and_write_rapid_data_property('local', cookies, 'T_ROB1', 'MainModule', 'target', 'extax', '[9E9,9E9,9E9,9E9,9E9,9E9]')
"""

def edit_and_write_rapid_data_property(ipaddress, cookies, program, module, variable_name, property, new_value):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) \
        and isinstance(program, basestring) and isinstance(module, basestring) \
        and isinstance(variable_name, basestring) and isinstance(property, basestring) \
        and isinstance(new_value, basestring):
        # Constructs the urls
        if ipaddress.lower() == 'local':
            url_write = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80', program, module, variable_name)
            url_get = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format('localhost:80', program, module, variable_name)
        else:
            url_write = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(), program, module, variable_name)
            url_get = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format(ipaddress.lower(), program, module, variable_name)
        try:
            # Gets the robtarget from controller.
            response = requests.get(url_get, cookies=cookies)
            if response.status_code == 200:
                # Gets the robtarget form response.
                robtarget = response.json()['_embedded']['_state'][0]['value']
                # Formats the robtargets attributes into a list.
                robtarget = unicodedata.normalize('NFKD', robtarget).encode('ascii','ignore')
                robtarget = robtarget.translate(None, "[]")
                robtarget_list = robtarget.split(',')
                new_value = new_value.translate(None, "[]")
                if property.lower() == 'trans':
                    trans_list = new_value.split(',')
                    if len(trans_list) == 3:
                        # Creates the new robtarget.
                        robtarget = '[[%G,%G,%G],[%s,%s,%s,%s],[%s,%s,%s,%s],[%s,%s,%s,%s,%s,%s]]' % \
                        (float(trans_list[0]), float(trans_list[1]), float(trans_list[2]), robtarget_list[3],
                         robtarget_list[4], robtarget_list[5], robtarget_list[6], robtarget_list[7], robtarget_list[8],
                         robtarget_list[9], robtarget_list[10], robtarget_list[11], robtarget_list[12],
                         robtarget_list[13], robtarget_list[14], robtarget_list[15], robtarget_list[16])

                        payload = {'value': robtarget}
                        response = requests.post(url_write, cookies=cookies, data=payload)
                        if response.status_code == 204:
                            msg = 'Robtarget trans updated.'
                            return msg
                        else:
                            err = 'Error updating robtarget: ' + str(response.status_code)
                            return err
                    else:
                        err = 'Incorrect format of trans. Ex \'[10,0,100]\''
                        return err
                elif property.lower() == 'rot':
                    rot_list = new_value.split(',')
                    if len(rot_list) == 4:
                        # Creates the new robtarget.
                        robtarget = '[[%s,%s,%s],[%G,%G,%G,%G],[%s,%s,%s,%s],[%s,%s,%s,%s,%s,%s]]' % \
                        (robtarget_list[0], robtarget_list[1], robtarget_list[2], float(rot_list[0]),
                         float(rot_list[1]), float(rot_list[2]), float(rot_list[3]), robtarget_list[7],
                         robtarget_list[8], robtarget_list[9], robtarget_list[10], robtarget_list[11],
                         robtarget_list[12], robtarget_list[13], robtarget_list[14], robtarget_list[15],
                         robtarget_list[16])

                        payload = {'value': robtarget}
                        response = requests.post(url_write, cookies=cookies, data=payload)
                        if response.status_code == 204:
                            msg = 'Robtarget rot updated.'
                            return msg
                        else:
                            err = 'Error updating robtarget: ' + str(response.status_code)
                            return err
                    else:
                        err = 'Incorrect format of rot. Ex \'[1,0,0,0]\''
                        return err
                elif property.lower() == 'robconf':
                    robconf_list = new_value.split(',')
                    if len(robconf_list) == 4:
                        # Creates the new robtarget.
                        robtarget = '[[%s,%s,%s],[%s,%s,%s,%s],[%d,%d,%d,%d],[%s,%s,%s,%s,%s,%s]]' % \
                        (robtarget_list[0], robtarget_list[1], robtarget_list[2], robtarget_list[3], robtarget_list[4],
                         robtarget_list[5], robtarget_list[6], int(robconf_list[0]), int(robconf_list[1]),
                         int(robconf_list[2]), int(robconf_list[3]), robtarget_list[11], robtarget_list[12],
                         robtarget_list[13], robtarget_list[14], robtarget_list[15], robtarget_list[16])

                        payload = {'value': robtarget}
                        response = requests.post(url_write, cookies=cookies, data=payload)
                        if response.status_code == 204:
                            msg = 'Robtarget robconf updated.'
                            return msg
                        else:
                            err = 'Error updating robtarget: ' + str(response.status_code)
                            return err
                    else:
                        err = 'Incorrect format of robconf. Ex \'[0,0,0,0]\''
                        return err
                elif property.lower() == 'extax':
                    extax_list = new_value.split(',')
                    if len(extax_list) == 6:
                        # Creates the new robtarget.
                        robtarget = '[[%s,%s,%s],[%s,%s,%s,%s],[%s,%s,%s,%s],[%G,%G,%G,%G,%G,%G]]' % \
                        (robtarget_list[0], robtarget_list[1], robtarget_list[2],robtarget_list[3], robtarget_list[4],
                         robtarget_list[5], robtarget_list[6], robtarget_list[7], robtarget_list[8],
                         robtarget_list[9], robtarget_list[10], float(extax_list[0]), float(extax_list[1]),
                         float(extax_list[2]), float(extax_list[3]), float(extax_list[4]), float(extax_list[5]))

                        payload = {'value': robtarget}
                        response = requests.post(url_write, cookies=cookies, data=payload)
                        if response.status_code == 204:
                            msg = 'Robtarget extax updated.'
                            return msg
                        else:
                            err = 'Error updating robtarget: ' + str(response.status_code)
                            return err
                    else:
                        err = 'Incorrect format of extax. Ex \'[9E9,9E9,9E9,9E9,9E9,9E9]\''
                        return err
                else:
                    msg = 'Property not of type trans, rot, robconf or extax.'
                    return msg
            else:
                err = 'Error getting robtarget from controller: ' + str(response.status_code)
                return err
        except Exception, err:
            return err
    else:
        err = 'Something wrong with arguments.'
        return err


"""
Edit and write the robtarget.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    String: IP address
    Requests.cookies.requestsCookieJar: cookies
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'x')
    String: trans (ex '[100,0,0]')
    String: rot (ex '[1,0,0,0]')
    String: robconf (ex '[0,1,0,0]')
    String: extax (ex '[9E9,9E9,9E9,9E9,9E9,9E9]')
Returns:
    String: result message or error
Examples:
   message = edit_and_write_rapid_data('local', cookies,'T_ROB1', 'MainModule', 'target', '[100,100,0]','[1,0,0,0]',
                                                                            '[0,0,0,1]','[9E9,9E9,9E9,9E9,9E9,9E9]')
"""

def edit_and_write_rapid_data(ipaddress, cookies, program, module, variable_name, trans, rot, robconf, extax):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) \
        and isinstance(program, basestring) and isinstance(module, basestring) \
        and isinstance(variable_name, basestring) and isinstance(trans, basestring) \
        and isinstance(rot, basestring) and isinstance(robconf, basestring) \
        and isinstance(extax, basestring):
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80', program, module, variable_name)
        else:
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(), program, module, variable_name)
        try:
            trans = trans.translate(None, "[]")
            rot = rot.translate(None, "[]")
            robconf = robconf.translate(None, "[]")
            extax = extax.translate(None, "[]")

            trans_list = trans.split(',')
            rot_list = rot.split(',')
            robconf_list = robconf.split(',')
            extax_list = extax.split(',')
            if len(trans_list) == 3 and len(rot_list) == 4 and len(robconf_list) == 4 and len(extax_list) == 6:
                robtarget = '[[%G,%G,%G],[%G,%G,%G,%G],[%d,%d,%d,%d],[%G,%G,%G,%G,%G,%G]]' % \
                            (float(trans_list[0]), float(trans_list[1]), float(trans_list[2]),
                             float(rot_list[0]), float(rot_list[1]), float(rot_list[2]), float(rot_list[3]),
                             int(robconf_list[0]), int(robconf_list[1]), int(robconf_list[2]),
                             int(robconf_list[3]), float(extax_list[0]), float(extax_list[1]),
                             float(extax_list[2]), float(extax_list[3]), float(extax_list[4]),
                             float(extax_list[5]))
                payload = {'value': robtarget}
                response = requests.post(url, cookies=cookies, data=payload)
                if response.status_code == 204:
                    msg = 'Robtarget updated.'
                    return msg
                else:
                    err = 'Error updating robtarget: ' + str(response.status_code)
                    return err
            else:
                err = 'Incorrect format of input data.'
                return err
        except Exception, err:
            return err
    else:
        err = 'Something wrong with arguments.'
        return err