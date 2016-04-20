"""
The communication module has communication with robot through Robot Web Services. Robot Web Services uses REST to
identify resources and HTTP to communicate.
"""

import requests
import requests.cookies
from requests.auth import HTTPDigestAuth


def connect_robot_with_ipaddr_and_user(ipaddress, username, password):
    """
    Connects to a robot with the specified ip address, username and password.
    Local means the VC.

    Input:
        String: IP address
        String: username
        String: password
    Output:
        Boolean: Indicates if connection to robot was successful.
        String: Message with the outcome
        Requests.auth.HTTPDigestAuth: digest_auth
        Requests.cookies.RequestsCookieJar: cookies
    Examples:
        None
    """
    if isinstance(ipaddress, basestring) and isinstance(username, basestring) and isinstance(password, basestring):
        # Inserts ip address into the url
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/system?json=1'.format('localhost:80')
        else:
            url = 'http://{0}/rw/system?json=1'.format(ipaddress.lower())
        digest_auth = HTTPDigestAuth(username, password)
        try:
            response = requests.get(url, auth=digest_auth)
            if response.status_code == 200:
                # Gets the system information
                rob_info_dict = response.json()['_embedded']['_state'][0]
                rob_info = 'System name: %s, Controller Version: %s' % \
                           (rob_info_dict['name'], rob_info_dict['rwversion'])
                return True, rob_info, digest_auth, response.cookies
            else:
                err = 'Something went wrong. Status code: ' + str(response.status_code)
                return False, err, None, None
        except Exception:
            err = 'Can\'t connect to the specified robot. Something may be wrong with input arguments.'
            return False, err, None, None
    else:
        err = 'Something wrong with arguments. Needs to be string.'
        return False, err, None, None


def connect_robot_with_ipaddr_def_user(ipaddress):
    """
    Connects to a robot with the specified ip address and default user.
    Local means the VC.

    Input:
        String: IP address
    Output:
        Boolean: Indicates if connection to robot was successful.
        String: Message with the outcome
        Requests.auth.HTTPDigestAuth: digest_auth
        Requests.cookies.RequestsCookieJar: cookies
    Examples:
        None
    """
    if isinstance(ipaddress, basestring):
        # Inserts ip address into the url
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/system?json=1'.format('localhost:80')
        else:
            url = 'http://{0}/rw/system?json=1'.format(ipaddress.lower())
        digest_auth = HTTPDigestAuth('Default User', 'robotics')
        try:
            response = requests.get(url, auth=digest_auth)
            if response.status_code == 200:
                # Gets the system information
                rob_info_dict = response.json()['_embedded']['_state'][0]
                rob_info = 'System name: %s, Controller Version: %s' % \
                           (rob_info_dict['name'], rob_info_dict['rwversion'])
                return True, rob_info, digest_auth, response.cookies
            else:
                err = 'Something went wrong. Status code: ' + str(response.status_code)
                return False, err, None, None
        except Exception, err:
            return False, err, None, None
    else:
        err = 'Something wrong with arguments. Needs to be string.'
        return False, err, None, None


def logoff_robot_controller(ipaddress, cookies):
    """
    Log off the robot controller and disposes of the cookies.

    Input:
        String: IP address
        Requests.cookies.RequestsCookieJar: cookies
    Output:
        Boolean: Indicates if successful or not
        String: Message with the outcome
    Examples:
        None
    """
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar):
        if ipaddress.lower() == 'local':
                url = 'http://{0}/logout'.format('localhost:80')
        else:
                url = 'http://{0}/logout'.format(ipaddress.lower())
        try:
            response = requests.get(url, cookies=cookies)
            # Error logging out because user is already logged out.
            if response.status_code == 401 or response.status_code == 400:
                return True, 'Already logged out.'
            # If user is not logged out then logout successful.
            elif response.status_code == 200:
                return True, 'Logout successful.'
            else:
                return False, 'Logout failed. ' + str(response.status_code)
        except Exception, err:
            return False, err
    else:
        err = 'Something wrong with arguments'
        return False, err
