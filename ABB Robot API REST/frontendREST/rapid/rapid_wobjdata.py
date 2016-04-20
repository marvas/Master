"""
Module for handling rapid datatype wobjdata. This module makes it possible to edit and write the rapid datatype
wobjdata, as well as displaying the different properties of the wobjdata.
"""

import unicodedata

import requests
import requests.auth
import requests.cookies


"""
Gets Robhold from wobjdata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Robhold or error
Examples:
    None
"""


def get_robhold_tostring(response_dict):
    if response_dict['dattyp'] == 'wobjdata':
        try:
            # Formatting the wobjdata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Wobjdata should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Robhold: = %s' % (value_list[0])
                return res
            else:
                err = 'Something wrong with wobjdata: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not wobjdata.'
        return err


"""
Gets Ufprog from wobjdata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Ufprog or error
Examples:
    None
"""


def get_ufprog_tostring(response_dict):
    if response_dict['dattyp'] == 'wobjdata':
        try:
            # Formatting the wobjdata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Wobjdata should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Ufprog: = %s' % (value_list[1])
                return res
            else:
                err = 'Something wrong with wobjdata: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not wobjdata.'
        return err


"""
Gets Ufmec from wobjdata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Ufmec or error
Examples:
    None
"""


def get_ufmec_tostring(response_dict):
    if response_dict['dattyp'] == 'wobjdata':
        try:
            # Formatting the wobjdata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Wobjdata should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Ufmec: = %s' % (value_list[2])
                return res
            else:
                err = 'Something wrong with wobjdata: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not wobjdata.'
        return err


"""
Gets Uframe from wobjdata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Uframe or error
Examples:
    None
"""


def get_uframe_tostring(response_dict):
    if response_dict['dattyp'] == 'wobjdata':
        try:
            # Formatting the wobjdata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Wobjdata should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Uframe: [Trans,Rot] = [[%s,%s,%s],[%s,%s,%s,%s]]' % (
                    value_list[3], value_list[4], value_list[5], value_list[6], value_list[7],
                    value_list[8], value_list[9]
                )
                return res
            else:
                err = 'Something wrong with wobjdata: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not wobjdata.'
        return err


"""
Gets Oframe from wobjdata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Oframe or error
Examples:
    None
"""


def get_oframe_tostring(response_dict):
    if response_dict['dattyp'] == 'wobjdata':
        try:
            # Formatting the wobjdata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Wobjdata should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Oframe: [Trans,Rot] = [[%s,%s,%s],[%s,%s,%s,%s]]' % (
                    value_list[10], value_list[11], value_list[12], value_list[13], value_list[14],
                    value_list[15], value_list[16]
                )
                return res
            else:
                err = 'Something wrong with wobjdata: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not wobjdata.'
        return err


"""
Gets wobjdata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: Wobjdata or error
Examples:
    None
"""


def get_wobjdata_tostring(response_dict):
    if response_dict['dattyp'] == 'wobjdata':
        try:
            # Formatting the wobjdata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Wobjdata should consist of 17 numbers.
            if len(value_list) == 17:
                res = 'Wobjdata: %s' % (response_dict['value'])
                return res
            else:
                err = 'Something wrong with wobjdata: ' + response_dict['value']
                return err
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not wobjdata.'
        return err


"""
Edits and writes specified property of wobjdata on controller.
Remember to overwrite the old cookie with the new returned cookie from this function.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'wobj')
    String: property (accepted types: robhold, ufprog, ufmec, uframe, oframe)
    String|Bool: new_value
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'wobj', 'robhold', True)
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'wobj', 'ufprog', False)
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'wobj', 'ufmec', '')
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'wobj', 'uframe','[0,0,100],[1,0,0,0]')
    message, cookies = edit_and_write_rapid_data_property('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'wobj', 'oframe','[0,0,100],[1,0,0,0]')
"""


def edit_and_write_rapid_data_property(ipaddress, cookies, digest_auth, program, module, variable_name,
                                       property, new_value):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) and \
            isinstance(program, basestring) and isinstance(module, basestring) and \
            isinstance(variable_name, basestring) and isinstance(property, basestring) and \
            isinstance(digest_auth, requests.auth.HTTPDigestAuth):
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
            # Gets wobjdata from controller.
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
                # Gets the wobjdata from response.
                wobjdata = response.json()['_embedded']['_state'][0]['value']
                # Formats the wobjdata attributes into a list.
                wobjdata = unicodedata.normalize('NFKD', wobjdata).encode('ascii', 'ignore')
                wobjdata = wobjdata.translate(None, "[]")
                wobjdata_list = wobjdata.split(',')
                if property.lower() == 'robhold':
                    if new_value == True or new_value == False:
                        if new_value == 1:
                            new_value = True
                        if new_value == 0:
                            new_value = False
                        # Creates the new wobjdata.
                        new_wobjdata = '[%s,%s,%s,[[%s,%s,%s],[%s,%s,%s,%s]],[[%s,%s,%s],[%s,%s,%s,%s]]]' % (
                            new_value, wobjdata_list[1], wobjdata_list[2], wobjdata_list[3], wobjdata_list[4],
                            wobjdata_list[5], wobjdata_list[6], wobjdata_list[7], wobjdata_list[8], wobjdata_list[9],
                            wobjdata_list[10], wobjdata_list[11], wobjdata_list[12], wobjdata_list[13],
                            wobjdata_list[14], wobjdata_list[15], wobjdata_list[16]
                        )

                        payload = {'value': new_wobjdata}
                    else:
                        msg = 'Input is not boolean.'
                        return msg, cookies
                elif property.lower() == 'ufprog':
                    if new_value == True or new_value == False:
                        if new_value == 1:
                            new_value = True
                        if new_value == 0:
                            new_value = False
                        # Creates the new wobjdata.
                        new_wobjdata = '[%s,%s,%s,[[%s,%s,%s],[%s,%s,%s,%s]],[[%s,%s,%s],[%s,%s,%s,%s]]]' % (
                            wobjdata_list[0], new_value, wobjdata_list[2], wobjdata_list[3], wobjdata_list[4],
                            wobjdata_list[5], wobjdata_list[6], wobjdata_list[7], wobjdata_list[8], wobjdata_list[9],
                            wobjdata_list[10], wobjdata_list[11], wobjdata_list[12], wobjdata_list[13],
                            wobjdata_list[14], wobjdata_list[15], wobjdata_list[16]
                        )

                        payload = {'value': new_wobjdata}
                    else:
                        msg = 'Input is not boolean.'
                        return msg, cookies
                elif property.lower() == 'ufmec':
                    if isinstance(new_value, basestring):
                        # Creates the new wobjdata.
                        # Inserting new_value into string would not keep the quotes of string. Need to add
                        # quotes in order to satisfy rapid.
                        new_wobjdata = '[%s,%s,%s,[[%s,%s,%s],[%s,%s,%s,%s]],[[%s,%s,%s],[%s,%s,%s,%s]]]' % \
                                       (wobjdata_list[0], wobjdata_list[1], ('\"%s\"' % new_value), wobjdata_list[3],
                                        wobjdata_list[4], wobjdata_list[5], wobjdata_list[6], wobjdata_list[7],
                                        wobjdata_list[8], wobjdata_list[9], wobjdata_list[10], wobjdata_list[11],
                                        wobjdata_list[12], wobjdata_list[13], wobjdata_list[14], wobjdata_list[15],
                                        wobjdata_list[16])

                        payload = {'value': new_wobjdata}
                    else:
                        msg = 'Input is not string.'
                        return msg, cookies
                elif property.lower() == 'uframe':
                    if isinstance(new_value, basestring):
                        new_value = new_value.translate(None, "[]")
                        uframe_list = new_value.split(',')
                        if len(uframe_list) == 7:
                            # Creates the new wobjdata.
                            new_wobjdata = '[%s,%s,%s,[[%G,%G,%G],[%G,%G,%G,%G]],[[%s,%s,%s],[%s,%s,%s,%s]]]' % (
                                wobjdata_list[0], wobjdata_list[1], wobjdata_list[2], float(uframe_list[0]),
                                float(uframe_list[1]), float(uframe_list[2]), float(uframe_list[3]),
                                float(uframe_list[4]), float(uframe_list[5]), float(uframe_list[6]),
                                wobjdata_list[10], wobjdata_list[11], wobjdata_list[12], wobjdata_list[13],
                                wobjdata_list[14], wobjdata_list[15], wobjdata_list[16]
                            )

                            payload = {'value': new_wobjdata}
                        else:
                            msg = 'Input is not a valid uframe.'
                            return msg, cookies
                    else:
                        msg = 'Input is not string.'
                        return msg, cookies
                elif property.lower() == 'oframe':
                    if isinstance(new_value, basestring):
                        new_value = new_value.translate(None, "[]")
                        oframe_list = new_value.split(',')
                        if len(oframe_list) == 7:
                            # Creates the new wobjdata.
                            new_wobjdata = '[%s,%s,%s,[[%s,%s,%s],[%s,%s,%s,%s]],[[%G,%G,%G],[%G,%G,%G,%G]]]' % (
                                wobjdata_list[0], wobjdata_list[1], wobjdata_list[2], wobjdata_list[3],
                                wobjdata_list[4], wobjdata_list[5], wobjdata_list[6], wobjdata_list[7],
                                wobjdata_list[8], wobjdata_list[9], float(oframe_list[0]), float(oframe_list[1]),
                                float(oframe_list[2]), float(oframe_list[3]), float(oframe_list[4]),
                                float(oframe_list[5]), float(oframe_list[6])
                            )

                            payload = {'value': new_wobjdata}
                        else:
                            msg = 'Input is not a valid oframe.'
                            return msg, cookies
                    else:
                        msg = 'Input is not string.'
                        return msg, cookies
                else:
                    msg = 'Property not of type robhold, ufprog, ufmec, uframe or oframe.'
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
                    msg = 'Wobjdata %s updated.' % property
                    return msg, cookies
                else:
                    err = 'Error updating wobjdata: ' + str(response.status_code)
                    return err, cookies
            else:
                err = 'Error getting wobjdata from controller: ' + str(response.status_code)
                return err, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies


"""
Edits and writes wobjdata on controller.
Remember to overwrite the old cookie with the new returned cookie from this function.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'wobj')
    Boolean: robhold (ex. True or False)
    Boolean: ufprog (ex. True or False)
    String: ufmec (ex. '')
    String: uframe (ex. '[100,100,100],[1,0,0,0]')
    String: oframe (ex. '[0,0,0],[1,0,0,0]')
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
    message, cookies = edit_and_write_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule', 'wobj', True,
                                                            False, '', '[100,100,0],[1,0,0,0]', '[0,0,0],[1,0,0,0]')
"""


def edit_and_write_rapid_data(ipaddress, cookies, digest_auth, program, module, variable_name, robhold, ufprog,
                              ufmec, uframe, oframe):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) and \
            isinstance(program, basestring) and isinstance(module, basestring) and \
            isinstance(variable_name, basestring) and isinstance(ufmec, basestring) and \
            isinstance(uframe, basestring) and isinstance(oframe, basestring) and \
            isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80', program,
                                                                                               module, variable_name)
        else:
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(),
                                                                                               program, module,
                                                                                               variable_name)
        try:
            uframe = uframe.translate(None, "[]")
            oframe = oframe.translate(None, "[]")

            uframe_list = uframe.split(',')
            oframe_list = oframe.split(',')
            if (robhold == True or robhold == False) and (ufprog == True or ufprog == False) and \
                    (len(uframe_list) == 7) and (len(oframe_list) == 7):
                if robhold == 1:
                    robhold = True
                if robhold == 0:
                    robhold = False
                if ufprog == 1:
                    ufprog = True
                if ufprog == 0:
                    ufprog = False
                # Constructs new wobjdata
                # Inserting ufmec into string would not keep the quotes of string. Need to add
                # quotes in order to satisfy rapid.
                new_wobjdata = "[%s,%s,%s,[[%G,%G,%G],[%G,%G,%G,%G]],[[%G,%G,%G],[%G,%G,%G,%G]]]" % \
                               (robhold, ufprog, ('\"%s\"' % ufmec), float(uframe_list[0]), float(uframe_list[1]),
                                float(uframe_list[2]), float(uframe_list[3]), float(uframe_list[4]),
                                float(uframe_list[5]), float(uframe_list[6]), float(oframe_list[0]),
                                float(oframe_list[1]), float(oframe_list[2]), float(oframe_list[3]),
                                float(oframe_list[4]), float(oframe_list[5]), float(oframe_list[6]))

                payload = {'value': new_wobjdata}
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
                    msg = 'Wobjdata updated.'
                    return msg, cookies
                else:
                    err = 'Error updating wobjdata: ' + str(response.status_code)
                    return err, cookies
            else:
                msg = 'Incorrect format of input data.'
                return msg, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies
