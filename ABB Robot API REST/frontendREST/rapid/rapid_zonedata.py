"""
Module for reading and setting zonedata.
"""

import unicodedata

import requests
import requests.auth
import requests.cookies


# Base zonedata in format 'fine, pzone_tcp, pzone_ori, pzone_eax, zone_ori, zone_leax, zone_reax'.
# First three points are for tool center point movement and last three point for tool reorientation.
base_zonedata_dict = {'z0':     'FALSE, 0.3, 0.3, 0.3, 0.03, 0.3, 0.03',
                      'z1':     'FALSE, 1, 1, 1, 0.1, 1, 0.1',
                      'z5':     'FALSE, 5, 8, 8, 0.8, 8, 0.8',
                      'z10':    'FALSE, 10, 15, 15, 1.5, 15, 1.5',
                      'z15':    'FALSE, 15, 23, 23, 2.3, 23, 2.3',
                      'z20':    'FALSE, 20, 30, 30, 3.0, 30, 3.0',
                      'z30':    'FALSE, 30, 45, 45, 4.5, 45, 4.5',
                      'z40':    'FALSE, 40, 60, 60, 6.0, 60, 6.0',
                      'z50':    'FALSE, 50, 75, 75, 7.5, 75, 7.5',
                      'z60':    'FALSE, 60, 90, 90, 9.0, 90, 9.0',
                      'z80':    'FALSE, 80, 120, 120, 12, 120, 12',
                      'z100':   'FALSE, 100, 150, 150, 15, 150, 15',
                      'z150':   'FALSE, 150, 225, 225, 23, 225, 23',
                      'z200':   'FALSE, 200, 300, 300, 30, 300, 30'}


"""
Gets zonedata and returns it as a string.

Args:
    Dictionary: response_dict
Returns:
    String: The result or error
Examples:
    None
"""


def get_zonedata_tostring(response_dict):
    if response_dict['dattyp'] == 'zonedata':
        try:
            # Get zonedata
            value = response_dict['value']
            # Converts from unicode to normalized string
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
            value = value.translate(None, "[]")
            # Checks if the data is base zonedata values
            for zone in base_zonedata_dict:
                # Takes all uppercase to lowercase, and trims all whitespaces and tabs.
                if value.lower() == base_zonedata_dict[zone].translate(None, " \t").lower():
                    res = 'Base zonedata: %s (%s)' % (zone, response_dict['value'])
                    return res
            # If base zonedata is not found.
            res = 'Zonedata: %s' % response_dict['value']
            return res
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not zonedata.'
        return err


"""
Edits and writes the zonedata. Only supports base zonedata.
Remember to overwrite the old cookie with the new returned cookie from this function.

Base zonedata supported:
0, 1, 5, 10, 15, 20, 30, 40, 50, 60, 80, 100, 150, 200

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'zone')
    String: value (ex, 'z0')
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
    message, cookies = edit_and_write_rapid_data_base('local', cookies, digest_auth, 'T_ROB1',
                                                        'MainModule', 'zone', 'z0')
    message, cookies = edit_and_write_rapid_data_base('local', cookies, digest_auth, 'T_ROB1',
                                                        'MainModule', 'zone', 'z20')
"""


def edit_and_write_rapid_data_base(ipaddress, cookies, digest_auth, program, module, variable_name, value):
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
            # Checks if the first character is z
            if value[:1].lower() == 'z':
                value_list = value.split('z')
                # Checks if what comes after z is a digit. Checks if the value is in the base dictionary.
                # Checks if the value list is of length 2 in case the user inserted a longer string, ex 'z1z10'.
                if value_list[1].isdigit() and (value in base_zonedata_dict) and (len(value_list) == 2):
                    new_zonedata = '[%s]' % base_zonedata_dict[value]

                    payload = {'value': new_zonedata}
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
                        msg = 'Base zonedata updated.'
                        return msg, cookies
                    else:
                        err = 'Error updating base zonedata: ' + str(response.status_code)
                        return err, cookies
                else:
                    msg = 'Something wrong with the input format, or the input is not a valid base zone.'
                    return msg, cookies
            else:
                msg = 'Something wrong with the input. Not in format \'z1\''
                return msg, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies


"""
Edits and writes the zonedata.
Remember to overwrite the old cookie with the new returned cookie from this function.

Args:
    String: IP address
    Requests.cookies.RequestsCookieJar: cookies
    Requests.auth.HTTPDigestAuth: digest_auth
    String: program (name of program, ex 'T_ROB1')
    String: module (name of module, ex 'MainModule')
    String: variable_name (name of variable, ex 'zone')
    Boolean: finep
    Float|Int: pzone_tcp
    Float|Int: pzone_ori
    Float|Int: pzone_eax
    Float|Int: zone_ori
    Float|Int: zone_leax
    Float|Int: zone_reax
Returns:
    String: result message or error
    Requests.cookies.RequestsCookieJar: cookies
Examples:
    message, cookies = edit_and_write_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule',
                                                                            'zone', False, 1, 1, 1, 0.1, 1, 0.1)
"""


def edit_and_write_rapid_data(ipaddress, cookies, digest_auth, program, module, variable_name, finep,
                              pzone_tcp, pzone_ori, pzone_eax, zone_ori, zone_leax, zone_reax):
    if isinstance(ipaddress, basestring) and isinstance(cookies, requests.cookies.RequestsCookieJar) and \
            isinstance(program, basestring) and isinstance(module, basestring) and \
            isinstance(variable_name, basestring) and (finep == True or finep == False) and \
            isinstance(pzone_tcp, (int, float)) and isinstance(pzone_ori, (int, float)) and \
            isinstance(pzone_eax, (int, float)) and isinstance(zone_ori, (int, float)) and \
            isinstance(zone_leax, (int, float)) and isinstance(zone_reax, (int, float)) and \
            isinstance(digest_auth, requests.auth.HTTPDigestAuth):
        # Constructs the url
        if ipaddress.lower() == 'local':
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format('localhost:80', program,
                                                                                               module, variable_name)
        else:
            url = 'http://{0}/rw/rapid/symbol/data/RAPID/{1}/{2}/{3}?json=1&action=set'.format(ipaddress.lower(),
                                                                                               program, module,
                                                                                               variable_name)
        try:
            if finep == 1:
                finep = True
            if finep == 0:
                finep = False
            new_zonedata = '[%s,%G,%G,%G,%G,%G,%G]' % \
                           (finep, float(pzone_tcp), float(pzone_ori), float(pzone_eax), float(zone_ori),
                            float(zone_leax), float(zone_reax))
            payload = {'value': new_zonedata}
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
                msg = 'Zonedata updated.'
                return msg, cookies
            else:
                err = 'Error updating zonedata: ' + str(response.status_code)
                return err, cookies
        except Exception, err:
            return err, cookies
    else:
        err = 'Something wrong with arguments.'
        return err, cookies
