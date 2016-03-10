"""
Module for getting rapid data information from the robot controller. This data can be shown to user,
or edited and written back to the controller in order to update a data instance.
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
    Dictionary|String: Output depends on the result. Dict if successful and string if error
Examples:
     b, response_dict = rapid_datatypes.get_rapid_data('local', cookies ,'T_ROB1','MainModule','p20')
     b, response_dict = rapid_datatypes.get_rapid_data('10.0.0.10', cookies ,'T_ROB1','MainModule','p20')

"""

def get_rapid_data(ipaddress, cookies, program, module, variable_name):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) \
            and isinstance(program, basestring) and isinstance(module, basestring) \
            and isinstance(variable_name, basestring):
        # Creates the urls based on input
        if ipaddress.lower() == 'local':
            url_value = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format('localhost:80', program, module, variable_name)
            url_prop = 'http://{0}/rw/rapid/symbol/properties/RAPID/{1}/{2}/{3}?json=1'.format('localhost:80', program, module, variable_name)
        else:
            url_value = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format(ipaddress.lower(), program, module, variable_name)
            url_prop = 'http://{0}/rw/rapid/symbol/properties/RAPID/{1}/{2}/{3}?json=1'.format(ipaddress.lower(), program, module, variable_name)

        try:
            response_value = requests.get(url_value, cookies=cookies)
            response_prop = requests.get(url_prop, cookies=cookies)
            if response_value.status_code == 200 and response_prop.status_code == 200:
                response_dict = {'value': response_value.json()['_embedded']['_state'][0]['value'],
                                 'dattyp': response_prop.json()['_embedded']['_state'][0]['dattyp'],
                                 'ndim': response_prop.json()['_embedded']['_state'][0]['ndim'],
                                 'dim': response_prop.json()['_embedded']['_state'][0]['dim']
                                 }
                return True, response_dict
            else:
                err = 'Error getting value and/or property: \nValue status code: %s \nProperty status code: %s' % \
                      (str(response_value.status_code), str(response_prop.status_code))
                return False, err
        except Exception, err:
            return False, err
    else:
        err = 'Something wrong with arguments.'
        return False, err