"""
The user mastership module is a module for setting mastership on controller.
"""

import requests


"""
Gets the user access as master on the robot controller. This will make it possible to edit and write RAPID data.
Remember to call this method before editing and writing data to controller.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
Returns:
    Boolean OR string: Output depends on the result of getting the mastership
Examples:
    None
"""

def get_master_access_to_controller(ipaddress, cookies):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar):
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/mastership?action=request'.format('localhost:80')
        else:
            url = 'http://{0}/rw/mastership?action=request'.format(ipaddress.lower())
        try:
            header = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(url, headers=header, cookies=cookies)
            print response.headers
            if response.status_code == 204:
                return True
            else:
                return False
        except Exception, err:
            return err
    else:
        err = 'Something wrong with arguments.'
        return err


"""
Releases any master access granted on the controller.
Remember to call this method after editing and writing data to controller.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
Returns:
    Boolean or string: Output depends on the result of releasing the mastership
Examples:
    None
"""

def release_master_access_to_controller(ipaddress, cookies):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar):
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/mastership?action=release'.format('localhost:80')
        else:
            url = 'http://{0}/rw/mastership?action=release'.format(ipaddress.lower())
        try:
            header = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(url, headers=header, cookies=cookies)
            print response.headers
            if response.status_code == 204:
                return True
            else:
                return False
        except Exception, err:
            return err
    else:
        err = 'Something wrong with arguments.'
        return err