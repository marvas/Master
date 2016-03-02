"""

"""

import requests


"""
Private method that checks if the value is a number.

Args:
    String: value
Returns:
    Boolean: Indicates if the value is number or not
Examples:
    None
"""

def _is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


"""
Gets the value of num from response and returns it as a string

Args:
    Requests.models.Response: response
Returns:
    String: The result or error
Examples:
    None
"""

def get_value_tostring(response_dict):
    if response_dict['dattyp'] == 'num':
        try:
            res = 'Value = %s' % response_dict['value']
            return res
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not num.'
        return err


"""
Gets the value of num from response and returns it

Args:
    Requests.models.Response: response
Returns:
    Float OR String: Output depends on if it is possible to get the value or not
Examples:
    None
"""

def get_value(response_dict):
    if response_dict['dattyp'] == 'num':
        try:
            return float(response_dict['value'])
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not num.'
        return err


"""
Edits and writes the num variable to the specified value.
Remember to get mastership before calling this function, and release the mastership right after.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    String: program (name of program, ex T_ROB1)
    String: module (name of module, ex MainModule)
    String: variable_name (name of the variable to update, ex x)
    Int or Float: new_value
Returns:
    String: result message or error
Examples:
    message = edit_and_write_rapid_data('local', cookies, 'T_ROB1', 'MainModule', 'x', 10)
    message = edit_and_write_rapid_data('10.0.0.1', cookies, 'T_ROB1', 'MainModule', 'x', 11)
"""

def edit_and_write_rapid_data(ipaddress, cookies, program, module, variable_name, new_value):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) \
            and isinstance(program, basestring) and isinstance(module, basestring) \
            and isinstance(variable_name, basestring) and isinstance(new_value, (float,int)):
        # Constructs the url
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80', program, module, variable_name)
        else:
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(), program, module, variable_name)
        try:
            # Construct payload with the new value
            payload = {'value': str(new_value)}
            response = requests.post(url, cookies=cookies, data=payload)
            if response.status_code == 204:
                msg = 'Value updated.'
                return msg
            else:
                err = 'Error updating value: ' + str(response.status_code)
                return err
        except Exception, err:
            return err
    else:
        err = 'Something wrong with arguments.'
        return err