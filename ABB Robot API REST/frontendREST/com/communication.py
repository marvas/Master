"""
The communication module has communication with robot through Robot Web Services. Robot Web Services uses REST to
identify resources and HTTP to communicate.
"""

import requests
from requests.auth import HTTPDigestAuth


"""
Connects to a robot with the specified ip address, username and password.
Local means the VC.

Args:
    String: IP address
    String: username
    String: password
Returns:
    Boolean: Indicates if connection to robot was successful.
    String: Message with the outcome
Examples:
    None
"""

def connect_robot_with_ipaddr(ipaddress, username, password):
    if isinstance(ipaddress, basestring) and isinstance(username, basestring) and isinstance(password, basestring):
        # Inserts ip address into the url
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/system?json=1'.format('localhost:80')
        else:
            url = 'http://{0}/rw/system?json=1'.format(ipaddress.lower())
        digest_auth = HTTPDigestAuth(username, password)
        try:
            response = requests.get(url, auth = digest_auth)
            if response.status_code == 200:
                # Gets the system information
                rob_info_dict = response.json()['_embedded']['_state'][0]
                rob_info = 'System name: %s, System ID: %s, Controller Version: %s' % \
                           (rob_info_dict['name'], rob_info_dict['sysid'], rob_info_dict['rwversion'])
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


"""
Connects to a robot with the specified ip address and default user.
Local means the VC.

Args:
    String: IP address
Returns:
    Boolean: Indicates if connection to robot was successful.
    String: Message with the outcome
Examples:
    None
"""

def connect_robot_with_ipaddr_def_user(ipaddress):
    if isinstance(ipaddress, basestring):
        # Inserts ip address into the url
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/system?json=1'.format('localhost:80')
        else:
            url = 'http://{0}/rw/system?json=1'.format(ipaddress.lower())
        digest_auth = HTTPDigestAuth('Default User', 'robotics')
        try:
            response = requests.get(url, auth = digest_auth)
            if response.status_code == 200:
                # Gets the system information
                rob_info_dict = response.json()['_embedded']['_state'][0]
                rob_info = 'System name: %s, System ID: %s, Controller Version: %s' % \
                           (rob_info_dict['name'], rob_info_dict['sysid'], rob_info_dict['rwversion'])
                return True, rob_info, digest_auth, response.cookies
            else:
                err = 'Something went wrong. Status code: ' + str(response.status_code)
                return False, err, None, None
        except Exception, err:
            # err = 'Can\'t connect to robot with the specified ip address.'
            return False, err, None, None
    else:
        err = 'Something wrong with arguments. Needs to be string.'
        return False, err, None, None


"""
Log off the robot controller and disposes of the cookies.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
Returns:
    String: Message with the outcome
Examples:
    None
"""

def logoff_robot_controller(ipaddress, cookies):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar):
        if ipaddress.lower() == 'local':
                url = 'http://{0}/logout'.format('localhost:80')
        else:
                url = 'http://{0}/logout'.format(ipaddress.lower())
        try:
            response = requests.get(url, cookies = cookies)
            if response.status_code == 200:
                return 'Logout successful.'
            else:
                return 'Logout failed. ' + str(response.status_code)
        except Exception, err:
            return err
    else:
        err = 'Something wrong with arguments'
        return err


