"""
Module for getting rapid data information from the robot controller. This data can be shown or used by user.
"""

import requests


"""
Gets the rapid data information from the controller and returns it as json.
Remember to overwrite the old cookie with the new returned cookie from this function.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: Program (name of the program, typically "T_ROB1")
    String: Module (name of the module, ex "MainModule")
    String: Name of the variable to get (ex "target_10")
Returns:
    Boolean: Indicates if able to get the information or not
    Dictionary|String: Output depends on the result. Dict if successful and string if error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
     b, response_dict, cookies = rapid_datatypes.get_rapid_data('local', cookies, digest_auth, 'T_ROB1',
                                                                'MainModule', 'p20')
     b, response_dict, cookies = rapid_datatypes.get_rapid_data('10.0.0.10', cookies, digest_auth, 'T_ROB1',
                                                                'MainModule', 'p20')
"""


def get_rapid_data(ipaddress, cookies, digest_auth, program, module, variable_name):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) \
            and isinstance(program, basestring) and isinstance(module, basestring) \
            and isinstance(variable_name, basestring) and isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        # Creates the urls based on input
        if ipaddress.lower() == 'local':
            url_value = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format('localhost:80', program,
                                                                                          module, variable_name)
            url_prop = 'http://{0}/rw/rapid/symbol/properties/RAPID/{1}/{2}/{3}?json=1'.format('localhost:80', program,
                                                                                               module, variable_name)
        else:
            url_value = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1'.format(ipaddress.lower(), program,
                                                                                          module, variable_name)
            url_prop = 'http://{0}/rw/rapid/symbol/properties/RAPID/{1}/{2}/{3}?json=1'.format(ipaddress.lower(),
                                                                                               program, module,
                                                                                               variable_name)
        try:
            response_value = requests.get(url_value, cookies=cookies)
            # If response includes a new cookie to use, set the new cookie.
            if len(response_value.cookies) > 0:
                cookies = response_value.cookies
            # If the user has timed out, need to authenticate again.
            if response_value.status_code == 401:
                response_value = requests.get(url_value, auth=digest_auth, cookies=cookies)
                if response_value.status_code == 200:
                    cookies = response_value.cookies
            response_prop = requests.get(url_prop, cookies=cookies)
            # If response includes a new cookie to use, set the new cookie.
            if len(response_prop.cookies) > 0:
                cookies = response_prop.cookies
            # If the user has timed out, need to authenticate again.
            if response_prop.status_code == 401:
                response_prop = requests.get(url_prop, auth=digest_auth, cookies=cookies)
                if response_prop.status_code == 200:
                    # requests.utils.add_dict_to_cookiejar(cookies,)
                    cookies = response_prop.cookies
            if response_value.status_code == 200 and response_prop.status_code == 200:
                response_dict = {'value': response_value.json()['_embedded']['_state'][0]['value'],
                                 'dattyp': response_prop.json()['_embedded']['_state'][0]['dattyp'],
                                 'ndim': response_prop.json()['_embedded']['_state'][0]['ndim'],
                                 'dim': response_prop.json()['_embedded']['_state'][0]['dim']
                                 }
                return True, response_dict, cookies
            else:
                err = 'Error getting value and/or property: \nValue status code: %s \nProperty status code: %s' % \
                      (str(response_value.status_code), str(response_prop.status_code))
                return False, err, cookies
        except Exception, err:
            return False, err, cookies
    else:
        err = 'Something wrong with arguments.'
        return False, err, cookies
