"""

"""

import requests


"""
Gets the rapid data information from the controller and returns it as json.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    String: Program (name of the program, typically "T_ROB1")
    String: Module (name of the module, ex "MainModule")
    String: Name of the variable to get (ex "target_10")
Returns:
    Boolean: Indicates if able to get the information or not
Examples:
     = rapid_datatypes.get_rapid_data('local', cookies ,'T_ROB1','MainModule','p20')
     = rapid_datatypes.get_rapid_data('10.0.0.10', cookies ,'T_ROB1','MainModule','p20')

"""

def get_rapid_data(ipaddress, cookies, program, module, variable_name):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) \
            and isinstance(program, basestring) and isinstance(module, basestring) \
            and isinstance(variable_name, basestring):
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format('localhost:80', program, module, variable_name)
        else:
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format(ipaddress.lower(), program, module, variable_name)
        try:
            response = requests.get(url, cookies=cookies)
            print response._content
            if response.status_code == 200:
                msg = 'Got variable'
                return True, msg
            else:
                err = 'Error getting variable: ' + str(response.status_code)
                return False, err
        except Exception, err:
            return False, err
    else:
        err = 'Something wrong with arguments.'
        return False, err