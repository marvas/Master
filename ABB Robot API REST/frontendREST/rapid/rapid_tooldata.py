"""
Module for handling rapid datatype tooldata. This module makes it possible to edit and write the rapid datatype
tooldata, as well as displaying the different properties of the tooldata.
"""


import unicodedata

import requests


"""
Gets Robhold from tooldata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Robhold or error
Examples:
    None
"""

def get_robhold_tostring(response_dict):
    if response_dict['dattyp'] == 'tooldata':
        try:
            # Formatting the tooldata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Tooldata should consist of 19 numbers.
            if len(value_list) == 19:
                res = 'Robhold: = %s' % (value_list[0])
                return res
            else:
                err = 'Something wrong with tooldata: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not tooldata.'
        return err


"""
Gets Tframe from tooldata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Tframe or error
Examples:
    None
"""

def get_tframe_tostring(response_dict):
    if response_dict['dattyp'] == 'tooldata':
        try:
            # Formatting the tooldata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Tooldata should consist of 19 numbers.
            if len(value_list) == 19:
                res = 'Tframe: [Trans,Rot] = [[%s,%s,%s],[%s,%s,%s,%s]]' % (value_list[1], value_list[2], value_list[3],
                                                                            value_list[4], value_list[5], value_list[6],
                                                                            value_list[7])
                return res
            else:
                err = 'Something wrong with tooldata: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not tooldata.'
        return err


"""
Gets Tload from tooldata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Tload or error
Examples:
    None
"""

def get_tload_tostring(response_dict):
    if response_dict['dattyp'] == 'tooldata':
        try:
            # Formatting the tooldata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Tooldata should consist of 19 numbers.
            if len(value_list) == 19:
                res = 'Tload: [Mass,Cog,Aom,Ix,Iy,Iz] = [%s,[%s,%s,%s],[%s,%s,%s,%s],%s,%s,%s]' % (value_list[8],
                                                                value_list[9], value_list[10], value_list[11],
                                                                value_list[12], value_list[13], value_list[14],
                                                                value_list[15],value_list[16],value_list[17],
                                                                value_list[18])
                return res
            else:
                err = 'Something wrong with tooldata: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not tooldata.'
        return err


"""
Gets tooldata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Tooldata or error
Examples:
    None
"""

def get_tooldata_tostring(response_dict):
    if response_dict['dattyp'] == 'tooldata':
        try:
            # Formatting tooldata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Tooldata should consist of 19 numbers.
            if len(value_list) == 19:
                res = 'Tooldata: %s' % response_dict['value']
                return res
            else:
                err = 'Something wrong with tooldata: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not tooldata.'
        return err


"""
Edits and writes the specified property of the tooldata to controller.
Remember to overwrite the old cookie with the new returned cookie from this function.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'tool')
    String: property (properties: robhold, tframe, tload)
    String|Bool: new_value
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                            'tool', 'robhold', True)
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                            'tool', 'robhold', False)
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'tool', 'tframe','[0,0,100],[1,0,0,0]')
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                        'tool', 'tload', '[1,[0,0,1],[1,0,0,0],0,0,0]')
"""

def edit_and_write_rapid_data_property(ipaddress, cookies, digest_auth, program, module, variable_name, property, new_value):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) \
        and isinstance(program, basestring) and isinstance(module, basestring) \
        and isinstance(variable_name, basestring) and isinstance(property, basestring)\
        and isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        # Constructs the urls
        if ipaddress.lower() == 'local':
            url_write = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80', program, module, variable_name)
            url_get = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format('localhost:80', program, module, variable_name)
        else:
            url_write = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(), program, module, variable_name)
            url_get = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format(ipaddress.lower(), program, module, variable_name)
        try:
            # Gets tooldata from controller.
            response = requests.get(url_get, cookies=cookies)
            # If response includes a new cookie to use, set the new cookie.
            if len(response.cookies) > 0:
                cookies = response.cookies
            # If the user has timed out, need to authenticate again.
            if response.status_code == 401:
                response = requests.get(url_get, auth=digest_auth, cookies=cookies)
                if response.status_code == 200:
                    cookies = response.cookies
            if response.status_code == 200:
                # Gets the tooldata from response.
                tooldata = response.json()['_embedded']['_state'][0]['value']
                # Formats the tooldata attributes into a list.
                tooldata = unicodedata.normalize('NFKD', tooldata).encode('ascii','ignore')
                tooldata = tooldata.translate(None, "[]")
                tooldata_list = tooldata.split(',')
                if property.lower() == 'robhold':
                    if new_value == True or new_value == False:
                        if new_value == 1: new_value = True
                        if new_value == 0: new_value = False
                        # Creates the new tooldata.
                        new_tooldata = '[%s,[[%s,%s,%s],[%s,%s,%s,%s]],[%s,[%s,%s,%s],[%s,%s,%s,%s],%s,%s,%s]]' % (
                            new_value, tooldata_list[1],tooldata_list[2],tooldata_list[3],tooldata_list[4],
                            tooldata_list[5],tooldata_list[6],tooldata_list[7],tooldata_list[8],tooldata_list[9],
                            tooldata_list[10],tooldata_list[11],tooldata_list[12],tooldata_list[13],tooldata_list[14],
                            tooldata_list[15],tooldata_list[16],tooldata_list[17],tooldata_list[18]
                        )

                        payload = {'value': new_tooldata}
                    else:
                        msg = 'Input is not boolean.'
                        return msg, cookies
                elif property.lower() == 'tframe':
                    if isinstance(new_value, basestring):
                        new_value = new_value.translate(None, "[]")
                        tframe_list = new_value.split(',')
                        if len(tframe_list) == 7:
                            new_tooldata = '[%s,[[%G,%G,%G],[%G,%G,%G,%G]],[%s,[%s,%s,%s],[%s,%s,%s,%s],%s,%s,%s]]' % (
                                tooldata_list[0], float(tframe_list[0]), float(tframe_list[1]), float(tframe_list[2]),
                                float(tframe_list[3]), float(tframe_list[4]), float(tframe_list[5]), float(tframe_list[6]),
                                tooldata_list[8], tooldata_list[9], tooldata_list[10], tooldata_list[11], tooldata_list[12],
                                tooldata_list[13], tooldata_list[14], tooldata_list[15], tooldata_list[16],
                                tooldata_list[17], tooldata_list[18]
                            )

                            payload = {'value': new_tooldata}
                        else:
                            msg = 'Input is not a valid Tframe.'
                            return msg, cookies
                    else:
                        msg = 'Input is not string.'
                        return msg, cookies
                elif property.lower() == 'tload':
                    if isinstance(new_value, basestring):
                        new_value = new_value.translate(None, "[]")
                        tload_list = new_value.split(',')
                        if len(tload_list) == 11:
                            new_tooldata = '[%s,[[%s,%s,%s],[%s,%s,%s,%s]],[%G,[%G,%G,%G],[%G,%G,%G,%G],%G,%G,%G]]' % (
                                tooldata_list[0], tooldata_list[1], tooldata_list[2], tooldata_list[3], tooldata_list[4],
                                tooldata_list[5], tooldata_list[6], tooldata_list[7], float(tload_list[0]),
                                float(tload_list[1]), float(tload_list[2]), float(tload_list[3]), float(tload_list[4]),
                                float(tload_list[5]), float(tload_list[6]), float(tload_list[7]), float(tload_list[8]),
                                float(tload_list[9]), float(tload_list[10])
                            )

                            payload = {'value': new_tooldata}
                        else:
                            msg = 'Input is not a valid tload.'
                            return msg, cookies
                    else:
                        msg = 'Input is not string.'
                        return msg, cookies
                else:
                    msg = 'Property not of type robhold, tframe, tload.'
                    return msg, cookies
                response = requests.post(url_write, cookies=cookies, data=payload)
                # If response includes a new cookie to use, set the new cookie.
                if len(response.cookies) > 0:
                    cookies = response.cookies
                # If the user has timed out, need to authenticate again.
                if response.status_code == 401:
                    response = requests.post(url_write, auth=digest_auth, cookies=cookies, data=payload)
                    if response.status_code == 204:
                        cookies = response.cookies
                if response.status_code == 204:
                    msg = 'Tooldata %s updated.' % property
                    return msg, cookies
                else:
                    err = 'Error updating tooldata: ' + str(response.status_code)
                    return err, cookies
            else:
                err = 'Error getting tooldata from controller: ' + str(response.status_code)
                return err, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies


"""
Edits and writes tooldata to controller.
Remember to overwrite the old cookie with the new returned cookie from this function.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'tool')
    Boolean: robhold (ex. True or False)
    String: tframe (ex. '[0,0,100],[0,0,0,1]')
    String: tload (ex. '[1,[0,0,1],[1,0,0,0],0,0,0]')
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
    message, cookies = edit_and_write_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule', 'tool',
                                                        True, '[0,0,100],[1,0,0,0]', '[1,[0,0,1],[1,0,0,0],0,0,0]')
"""

def edit_and_write_rapid_data(ipaddress, cookies, digest_auth, program, module, variable_name, robhold, tframe, tload):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) \
        and isinstance(program, basestring) and isinstance(module, basestring) \
        and isinstance(variable_name, basestring) and isinstance(tframe, basestring) \
        and isinstance(tload, basestring) and isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80', program, module, variable_name)
        else:
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(), program, module, variable_name)
        try:
            tframe = tframe.translate(None, "[]")
            tload = tload.translate(None, "[]")

            tframe_list = tframe.split(',')
            tload_list = tload.split(',')
            if (robhold == True or robhold == False) and (len(tframe_list) == 7) and (len(tload_list) == 11):
                if robhold == 1: robhold = True
                if robhold == 0: robhold = False
                new_tooldata = '[%s,[[%G,%G,%G],[%G,%G,%G,%G]],[%G,[%G,%G,%G],[%G,%G,%G,%G],%G,%G,%G]]' % (
                    robhold, float(tframe_list[0]), float(tframe_list[1]), float(tframe_list[2]),
                    float(tframe_list[3]), float(tframe_list[4]), float(tframe_list[5]),
                    float(tframe_list[6]), float(tload_list[0]), float(tload_list[1]), float(tload_list[2]),
                    float(tload_list[3]), float(tload_list[4]), float(tload_list[5]), float(tload_list[6]),
                    float(tload_list[7]), float(tload_list[8]), float(tload_list[9]), float(tload_list[10])
                )

                payload = {'value': new_tooldata}
                response = requests.post(url, cookies=cookies, data=payload)
                # If response includes a new cookie to use, set the new cookie.
                if len(response.cookies) > 0:
                    cookies = response.cookies
                # If the user has timed out, need to authenticate again.
                if response.status_code == 401:
                    response = requests.post(url, auth=digest_auth, cookies=cookies, data=payload)
                    if response.status_code == 204:
                        cookies = response.cookies
                if response.status_code == 204:
                    msg = 'Tooldata updated.'
                    return msg, cookies
                else:
                    err = 'Error updating tooldata: ' + str(response.status_code)
                    return err, cookies
            else:
                msg = 'Incorrect format of input data.'
                return msg, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies