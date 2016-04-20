"""
Module handling one dimensional arrays in RAPID. This module only supports editing and writing rapid type num.
"""


import unicodedata

import requests


"""
Gets the length of array and returns it. Only shows the length of first dimension.

Args:
    Dictionary: response_dict
Returns:
    Int|String: Output depends on if it is possible to get the length or not
Examples:
    None
"""


def get_length(response_dict):
    if int(response_dict['ndim']) >= 1:
        try:
            # Formatting the length.
            length = response_dict['dim']
            # Converts from unicode to normalized string
            length = unicodedata.normalize('NFKD', length).encode('ascii', 'ignore')
            length_list = length.split(' ')
            return int(length_list[0])
        except Exception, err:
            return err
    else:
        err = 'The input is not an array.'
        return err


"""
Gets the dimension of array and returns it.

Args:
    Dictionary: response_dict
Returns:
    Int|String: Output depends on if it is possible to get the dimension or not
Examples:
    None
"""


def get_dimensions(response_dict):
    if int(response_dict['ndim']) >= 1:
        try:
            return int(response_dict['ndim'])
        except Exception, err:
            return err
    else:
        err = 'The input is not an array.'
        return err


"""
Inserts a value into num array with index and writes it to the controller.
Remember to overwrite the old cookie with the new returned cookie from this function.
Index starts from 0.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'array')
    Integer: Index (array index)
    Float|Int: Value
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
    message, cookies = edit_and_write_rapid_data_array_num_index('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                                        'array', 0, 100)
"""


def edit_and_write_rapid_data_num_index(ipaddress, cookies, digest_auth, program, module, variable_name, index, value):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) and \
            isinstance(program, basestring) and isinstance(module, basestring) and \
            isinstance(variable_name, basestring) and isinstance(index, int) and \
            isinstance(value, (int, float)) and isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        # Checks if index is negative.
        if index < 0:
            err = 'Index can\'t be negative'
            return err, cookies
        # Constructs the urls
        if ipaddress.lower() == 'local':
            url_write = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80',
                                                                                                     program,
                                                                                                     module,
                                                                                                     variable_name)
            url_get = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format('localhost:80',
                                                                                        program, module, variable_name)
        else:
            url_write = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(),
                                                                                                     program,
                                                                                                     module,
                                                                                                     variable_name)
            url_get = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format(ipaddress.lower(),
                                                                                        program, module, variable_name)
        try:
            # Gets the array from controller.
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
                # Gets the array from response.
                rapid_array = response.json()['_embedded']['_state'][0]['value']
                # Formats the array attributes into a list.
                rapid_array = unicodedata.normalize('NFKD', rapid_array).encode('ascii', 'ignore')
                rapid_array = rapid_array.translate(None, "[]")
                rapid_array_list = rapid_array.split(',')
                # Checks if index is out of bounds.
                if index < len(rapid_array_list):
                    rapid_array_list[index] = str(value)
                    # Constructs the rapid array as string.
                    rapid_array = '[' + ','.join(s for s in rapid_array_list) + ']'
                    # Write to controller.
                    payload = {'value': rapid_array}
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
                        msg = 'Array index %d updated.' % index
                        return msg, cookies
                    else:
                        err = 'Error updating array: ' + str(response.status_code)
                        return err, cookies
                else:
                    msg = 'Index is not valid.'
                    return msg, cookies
            else:
                err = 'Error getting array from controller: ' + str(response.status_code)
                return err, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies


"""
Inserts a list of values into num array and writes it to the controller.
Remember to overwrite the old cookie with the new returned cookie from this function.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'array')
    List: values, ex([100,1,2])
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
    If RAPID array is of length 3:
    message, cookies = edit_and_write_rapid_data_num('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'array', []) Formats array to default.
    message, cookies = edit_and_write_rapid_data_num('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'array', [100,1,50])
    message, cookies = edit_and_write_rapid_data_num('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'array', [100,1.1,50])
    message, cookies = edit_and_write_rapid_data_num('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'array', [100])
    If RAPID array is of length 3 this is not possible:
    message, cookies = edit_and_write_rapid_data_num('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                'array', [100,1,50,100])
"""


def edit_and_write_rapid_data_num(ipaddress, cookies, digest_auth, program, module, variable_name, values):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) \
        and isinstance(program, basestring) and isinstance(module, basestring) \
        and isinstance(variable_name, basestring) and isinstance(values, list)\
        and isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        # Constructs the urls
        if ipaddress.lower() == 'local':
            url_write = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80',
                                                                                                     program, module,
                                                                                                     variable_name)
            url_get = 'http://{0}/rw/rapid/symbol/properties/RAPID/{1}/{2}/{3}?json=1'.format('localhost:80',
                                                                                              program, module,
                                                                                              variable_name)
        else:
            url_write = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(),
                                                                                                     program,
                                                                                                     module,
                                                                                                     variable_name)
            url_get = 'http://{0}/rw/rapid/symbol/properties/RAPID/{1}/{2}/{3}?json=1'.format(ipaddress.lower(),
                                                                                              program, module,
                                                                                              variable_name)
        # Checks if all values in input values are of type int or float.
        for value in values:
            if isinstance(value, (int, float)) == False:
                msg = 'Something wrong in list.'
                return msg, cookies
        try:
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
                num_dimensions = int(response.json()['_embedded']['_state'][0]['ndim'])
                # Checks if the specified variable is a rapid array.
                if num_dimensions == 0:
                    err = 'Specified variable is not an array.'
                    return err, cookies
                # Checks if the array is one dimensional.
                try:
                    array_length = int(response.json()['_embedded']['_state'][0]['dim'])
                except ValueError:
                    err = 'Rapid array is not one dimensional.'
                    return err, cookies
                # Check if input list is larger than the rapid list.
                if len(values) > array_length:
                    msg = 'Input list is larger than RAPID list.'
                    return msg, cookies
                # If size of values are smaller than RAPID list, then fill the list
                # with zeroes until they are the same size.
                if len(values) < array_length:
                    diff = array_length - len(values)
                    for _ in range(0, diff):
                        values.append(0)
                    new_array = str(values)
                else:
                    new_array = str(values)
                # Writes to controller.
                payload = {'value': str(new_array)}
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
                    msg = 'Array updated.'
                    return msg, cookies
                else:
                    err = 'Error updating array: ' + str(response.status_code)
                    return err, cookies
            else:
                err = 'Error getting array from controller: ' + str(response.status_code)
                return err, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies
