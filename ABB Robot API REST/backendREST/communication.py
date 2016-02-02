"""
The communication module has communication with robot through Robot Web Services. Robot Web Services uses REST to
identify resources and HTTP to communicate. Application data can be sent as XML or JSON back to client
through WebSockets.
"""

import requests
from requests.auth import HTTPDigestAuth
from ws4py.client.threadedclient import WebSocketClient

"""
"""
def subscribe(ipaddress,username,password):
    # if ipaddress == 'default':
    #     system_url = 'http://{0}/rw/system?json=1'.format('localhost:8080')
    # else:
    #     system_url = 'http://{0}/rw/system?json=1'.format(ipaddress)
    system_url = 'http://{0}/rw/system?json=1'.format(ipaddress)
    digest_auth = HTTPDigestAuth(username, password)
    # payload = {'resources':['1','2','3'],
    #            '1':'/rw/panel/speedratio',
    #            '1-p':'1',
    #            '2':'/rw/panel/ctrlstate',
    #            '2-p':'1',
    #            '3':'/rw/panel/opmode',
    #            '3-p':'1'}
    response = requests.get(system_url, auth=digest_auth)
    print response.json()
    if response.status_code == 200:
        # location = response.headers['Location']
        cookie = 'ABBCX={0}'.format(response.cookies['ABBCX'])
        return True
    else:
        print 'Error subscribing: ' + str(response.status_code)
        return False

print subscribe('152.94.0.38','Default User','robotics')