"""
Module for handling rapid datatype jointtarget. This module makes it possible to edit and write the rapid datatype
jointtarget, as well as displaying the different properties of the jointtarget.
"""


import unicodedata

import requests


"""
Gets RobAx from jointtarget and returns it as a string

Args:
    Dictionary: response_dict
Returns:
    String: RobAx or error
Examples:
    None
"""


def get_robax_tostring(response_dict):
    if response_dict['dattyp'] == 'jointtarget':
        try:
            # Formatting the jointtarget to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Jointtarget should consist of 12 numbers.
            if len(value_list) == 12:
                res = 'Robax: [Rax_1,Rax_2,Rax_3,Rax_4,Rax_5,Rax_6] = [%s,%s,%s,%s,%s,%s]' % \
                      (value_list[0], value_list[1], value_list[2], value_list[3], value_list[4], value_list[5])
                return res
            else:
                err = 'Something wrong with the jointtarget: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not jointtarget.'
        return err


"""
Gets the extax data from jointtarget and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Extax or error
Examples:
    None
"""


def get_extax_tostring(response_dict):
    if response_dict['dattyp'] == 'jointtarget':
        try:
            # Formatting the jointtarget to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Jointtarget should consist of 12 numbers.
            if len(value_list) == 12:
                res = 'Extax: [Eax_a,Eax_b,Eax_c,Eax_d,Eax_e,Eax_f] = [%s,%s,%s,%s,%s,%s]' % \
                      (value_list[6], value_list[7], value_list[8], value_list[9],
                       value_list[10], value_list[11])
                return res
            else:
                err = 'Something wrong with the jointtarget: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not jointtarget.'
        return err


"""
Gets jointtarget and returns it as a string

Args:
    Dictionary: response_dict
Returns:
    String: Jointtarget or error
Examples:
    None
"""


def get_jointtarget_tostring(response_dict):
    if response_dict['dattyp'] == 'jointtarget':
        try:
            # Formatting the jointtarget to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Jointtarget should consist of 12 numbers.
            if len(value_list) == 12:
                res = 'Jointtarget: %s' % response_dict['value']
                return res
            else:
                err = 'Something wrong with the jointtarget: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not jointtarget.'
        return err


"""
Edits the specified property of the jointtarget and writes it to the controller.
Remember to overwrite the old cookie with the new returned cookie from this function.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'x')
    String: property (properties: robax or extax)
    String: new_value (new value, ex '[0,0,0,0,0,0]' for robax)
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                            'jtarget', 'robax', '[0,0,0,0,0,0]')
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                            'jtarget', 'extax', '[9E9,9E9,9E9,9E9,9E9,9E9]')
"""


def edit_and_write_rapid_data_property(ipaddress, cookies, digest_auth, program, module,
                                       variable_name, property, new_value):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) and \
            isinstance(program, basestring) and isinstance(module, basestring) and \
            isinstance(variable_name, basestring) and isinstance(property, basestring) and \
            isinstance(new_value, basestring) and isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        # Constructs the urls
        if ipaddress.lower() == 'local':
            url_write = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80',
                                                                                                     program, module,
                                                                                                     variable_name)
            url_get = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format('localhost:80', program, module,
                                                                                        variable_name)
        else:
            url_write = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(),
                                                                                                     program, module,
                                                                                                     variable_name)
            url_get = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format(ipaddress.lower(), program,
                                                                                        module, variable_name)
        try:
            # Gets the jointtarget from controller.
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
                # Gets the jointtarget form response.
                jointtarget = response.json()['_embedded']['_state'][0]['value']
                # Formats the jointtargets attributes into a list.
                jointtarget = unicodedata.normalize('NFKD', jointtarget).encode('ascii', 'ignore')
                jointtarget = jointtarget.translate(None, "[]")
                jointtarget_list = jointtarget.split(',')
                new_value = new_value.translate(None, "[]")
                if property.lower() == 'robax':
                    robax_list = new_value.split(',')
                    if len(robax_list) == 6:
                        # Creates the new jointtarget.
                        jointtarget = '[[%G,%G,%G,%G,%G,%G],[%G,%G,%G,%G,%G,%G]]' % \
                            (float(robax_list[0]), float(robax_list[1]), float(robax_list[2]), float(robax_list[3]),
                             float(robax_list[4]), float(robax_list[5]), float(jointtarget_list[6]),
                             float(jointtarget_list[7]), float(jointtarget_list[8]), float(jointtarget_list[9]),
                             float(jointtarget_list[10]), float(jointtarget_list[11]))
                        payload = {'value': jointtarget}
                    else:
                        err = 'Incorrect format of robax. Ex \'[0,0,0,0,0,0]\''
                        return err, cookies
                elif property.lower() == 'extax':
                    extax_list = new_value.split(',')
                    if len(extax_list) == 6:
                        # Creates the new jointtarget.
                        jointtarget = '[[%G,%G,%G,%G,%G,%G],[%G,%G,%G,%G,%G,%G]]' % \
                            (float(jointtarget_list[0]), float(jointtarget_list[1]), float(jointtarget_list[2]),
                             float(jointtarget_list[3]), float(jointtarget_list[4]), float(jointtarget_list[5]),
                             float(extax_list[0]), float(extax_list[1]), float(extax_list[2]), float(extax_list[3]),
                             float(extax_list[4]), float(extax_list[5]))
                        payload = {'value': jointtarget}
                    else:
                        err = 'Incorrect format of extax. Ex \'[9E9,9E9,9E9,9E9,9E9,9E9]\''
                        return err, cookies
                else:
                    msg = 'Property not of type robax or extax.'
                    return msg, cookies
                # Tries to update variable on controller.
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
                    msg = 'Jointtarget %s updated.' % property.lower()
                    return msg, cookies
                else:
                    err = 'Error updating jointtarget: ' + str(response.status_code)
                    return err, cookies
            else:
                err = 'Error getting jointtarget from controller: ' + str(response.status_code)
                return err, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies


"""
Edits and writes the jointtarget.
Remember to overwrite the old cookie with the new returned cookie from this function.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'x')
    String: robax (ex '[0,0,0,0,0,0]')
    String: extax (ex '[9E9,9E9,9E9,9E9,9E9,9E9]')
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
    message, cookies = edit_and_write_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                            'jtarget', '[0,0,0,0,0,0], '[9E9,9E9,9E9,9E9,9E9,9E9]')
"""


def edit_and_write_rapid_data(ipaddress, cookies, digest_auth, program, module, variable_name, robax, extax):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) and \
            isinstance(program, basestring) and isinstance(module, basestring) and \
            isinstance(variable_name, basestring) and isinstance(robax, basestring) and \
            isinstance(extax, basestring) and isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        # Constructs the url
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80',
                                                                                               program, module,
                                                                                               variable_name)
        else:
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(),
                                                                                               program, module,
                                                                                               variable_name)
        try:
            robax = robax.translate(None, "[]")
            extax = extax.translate(None, "[]")

            robax_list = robax.split(',')
            extax_list = extax.split(',')
            if len(robax_list) == 6 and len(extax_list) == 6:
                jointtarget = '[[%G,%G,%G,%G,%G,%G],[%G,%G,%G,%G,%G,%G]]' % \
                            (float(robax_list[0]), float(robax_list[1]), float(robax_list[2]), float(robax_list[3]),
                             float(robax_list[4]), float(robax_list[5]), float(extax_list[0]), float(extax_list[1]),
                             float(extax_list[2]), float(extax_list[3]), float(extax_list[4]), float(extax_list[5]))
                payload = {'value': jointtarget}
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
                    msg = 'Jointtarget updated.'
                    return msg, cookies
                else:
                    err = 'Error updating jointtarget: ' + str(response.status_code)
                    return err, cookies
            else:
                err = 'Incorrect format of input data.'
                return err, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies
