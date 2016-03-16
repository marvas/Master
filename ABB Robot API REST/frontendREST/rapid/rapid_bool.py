"""
Module for handling rapid datatype bool. This module makes it possible to edit and write a rapid datatype bool,
as well as displaying the value of the bool.
"""


import requests


"""
Gets the state of bool and returns it as a string

Args:
    Dictionary: response_dict
Returns:
    String: The state or error
Examples:
    None
"""

def get_state_tostring(response_dict):
    if response_dict['dattyp'] == 'bool':
        try:
            res = 'State = %s' % response_dict['value']
            return res
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not bool.'
        return err


"""
Gets the state of bool and returns it

Args:
    Dictionary: response_dict
Returns:
    Boolean OR String: Output depends on if it is successful or not
Examples:
    None
"""

def get_state(response_dict):
    if response_dict['dattyp'] == 'bool':
        try:
            if response_dict['value'] == 'TRUE':
                return True
            elif response_dict['value'] == 'FALSE':
                return False
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not bool.'
        return err


"""
Edits and writes the boolean variable to the specified state.
Remember to get mastership before calling this function, and release the mastership right after.
Remember to overwrite the old cookie with the new returned cookie from this function.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of the program, ex 'T_ROB1')
    String: module (name of the module, ex 'MainModule')
    String: variable_name (name of the variable to update, ex 'x')
    Boolean: new_value (ex True or False)
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Example:
    message, cookies = edit_and_write_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule', 'run', True)
    message, cookies = edit_and_write_rapid_data('10.0.0.20', cookies, digest_auth, 'T_ROB1', 'MainModule', 'run', False)
"""

def edit_and_write_rapid_data(ipaddress, cookies, digest_auth, program, module, variable_name, new_value):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) \
            and isinstance(program, basestring) and isinstance(module, basestring) \
            and isinstance(variable_name, basestring) and isinstance(new_value, bool)\
            and isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        # Constructs the url
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80', program, module, variable_name)
        else:
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(), program, module, variable_name)
        try:
            # Construct payload with the new value
            payload = {'value': str(new_value)}
            response = requests.post(url, cookies=cookies, data=payload)
            # If response includes a new cookie to use, set the new cookie.
            if len(response.cookies) > 0:
                cookies = response.cookies
            # If the user has timed out, need to authenticate again.
            if response.status_code == 401:
                response = requests.post(url, auth=digest_auth, cookies=cookies, data=payload)
                if response.status_code == 200:
                    cookies = response.cookies
            if response.status_code == 204:
                msg = 'Value updated.'
                return msg, cookies
            else:
                err = 'Error updating value: ' + str(response.status_code)
                return err, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies