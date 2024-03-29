"""
Module for reading and setting speeddata.
"""

import unicodedata

import requests
import requests.auth
import requests.cookies

base_speeddata_list = [5, 10, 20, 30, 40, 50, 60, 80, 100, 150, 200,
                       300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000]


def get_speeddata_tostring(response_dict):
    """
    Gets speeddata and returns it as a string.

    Input:
        Dictionary: response_dict
    Output:
        String: The result or error
    Examples:
        None
    """
    try:
        if response_dict['dattyp'] == 'speeddata':
            # Formatting the speeddata to check if it is valid.
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            value_list = value.split(',')
            # Speeddata should consist of 4 numbers.
            if len(value_list) == 4:
                try:
                    # Checks if it is base speed.
                    if int(value_list[0]) in base_speeddata_list and int(value_list[1]) == 500 and int(
                            value_list[2]) == 5000 and int(value_list[3]) == 1000:
                        res = 'Base speeddata: v%d (%s)' % (int(value_list[0]), response_dict['value'])
                        return res
                    # If not base speed then custom speed.
                    else:
                        res = 'Speeddata: %s' % response_dict['value']
                        return res
                # If value is of type float then it will fail on base speed check above.
                # Then the speed must be a custom speed with float.
                except ValueError:
                    res = 'Speeddata: %s' % response_dict['value']
                    return res
            else:
                err = 'Something wrong with the speeddata: ' + response_dict['value']
                return err
        else:
            err = 'DataType is ' + response_dict['dattyp'] + ' and not speeddata.'
            return err
    except Exception, err:
        return err


def edit_and_write_rapid_data_base(ipaddress, cookies, digest_auth, program, module, variable_name, value):
    """
    Edits and writes speeddata. Only supports base speeddata.
    Remember to overwrite the old cookie with the new returned cookie from this function.

    Base speeddata supported:
    5, 10, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000, 1500, 2000, 2500, 3000

    Input:
        String: IP address
        Requests.cookies.RequestsCookieJar: cookies
        Requests.auth.HTTPDigestAuth: digest_auth
        String: program (name of program, ex 'T_ROB1')
        String: module (name of module, ex 'MainModule')
        String: variable_name (name of variable, ex 'speed')
        String: value (ex, 'v10')
    Output:
        String: result message or error
        Requests.cookies.RequestsCookieJar: cookies
    Examples:
        message, cookies = edit_and_write_rapid_data_base('local', cookies, digest_auth, 'T_ROB1',
                                                            'MainModule', 'speed', 'v100')
        message, cookies = edit_and_write_rapid_data_base('local', cookies, digest_auth, 'T_ROB1',
                                                            'MainModule', 'speed', 'v10')
    """
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) and \
            isinstance(program, basestring) and isinstance(module, basestring) and \
            isinstance(variable_name, basestring) and isinstance(value, basestring) and \
            isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        # Constructs the urls
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80', program,
                                                                                               module, variable_name)
        else:
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(),
                                                                                               program, module,
                                                                                               variable_name)
        try:
            # Strips value for all leading and trailing whitespaces
            value = value.strip()
            # Checks if the first character is v
            if value[:1].lower() == 'v':
                value = value.split('v')
                # Checks if what comes after v is a digit. Checks if the value is in the base list.
                # Checks if the value list is of length 2 in case the user inserted a longer string, ex 'v100v200'.
                if value[1].isdigit() and (int(value[1]) in base_speeddata_list) and (len(value) == 2):
                    new_speeddata = '[%d,500,5000,1000]' % int(value[1])

                    payload = {'value': new_speeddata}
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
                        msg = 'Base speeddata updated.'
                        return msg, cookies
                    else:
                        err = 'Error updating base speeddata: ' + str(response.status_code)
                        return err, cookies
                else:
                    msg = 'Something wrong with the input format, or the input is not a valid base speed.'
                    return msg, cookies
            else:
                msg = 'Something wrong with the input. Not in format \'v100\''
                return msg, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies


def edit_and_write_rapid_data(ipaddress, cookies, digest_auth, program, module, variable_name, vel_tcp,
                              vel_orient, vel_lin_extax, vel_lin_rot_extax):
    """
    Edits and writes speeddata.
    Remember to overwrite the old cookie with the new returned cookie from this function.

    Input:
        String: IP address
        Requests.cookies.RequestsCookieJar: cookies
        Requests.auth.HTTPDigestAuth: digest_auth
        String: program (name of program, ex 'T_ROB1')
        String: module (name of module, ex 'MainModule')
        String: variable_name (name of variable, ex 'speed')
        Float|Int: vel_tcp
        Float|Int: vel_orient
        Float|Int: vel_lin_extax
        Float|Int: vel_lin_rot_extax
    Output:
        String: result message or error
        Requests.cookies.RequestsCookieJar: cookies
    Examples:
        message, cookies = edit_and_write_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                    'speed', 100, 500, 5000, 1000)
        message, cookies = edit_and_write_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                                    'speed', 100.5, 500, 5000.37, 1000)
    """
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) and \
            isinstance(program, basestring) and isinstance(module, basestring) and \
            isinstance(variable_name, basestring) and isinstance(vel_tcp, (int, float)) and \
            isinstance(vel_orient, (int, float)) and isinstance(vel_lin_extax, (int, float)) and \
            isinstance(vel_lin_rot_extax, (int, float)) and isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        # Constructs the url
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80', program,
                                                                                               module, variable_name)
        else:
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(),
                                                                                               program, module,
                                                                                               variable_name)
        try:
            new_speeddata = '[%G,%G,%G,%G]' % \
                            (float(vel_tcp), float(vel_orient), float(vel_lin_extax), float(vel_lin_rot_extax))
            payload = {'value': new_speeddata}
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
                msg = 'Speeddata updated.'
                return msg, cookies
            else:
                err = 'Error updating speeddata: ' + str(response.status_code)
                return err, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies
