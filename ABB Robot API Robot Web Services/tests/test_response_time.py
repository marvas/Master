"""
Tests the response time of frontend REST
"""

import sys
import time

import frontendRWS.com.communication as communication
import frontendRWS.rapid.rapid_num as rapid_num


ipaddr = '152.94.0.39'

# Connects to the controller
connected, _, digest_auth, cookies = communication.connect_robot_with_ipaddr_def_user(ipaddr)
if not connected:
    print 'Not connected to controller'
    sys.exit()
for i in range(100):
    # Start timestamp
    start_time = time.clock()
    # Edits the number on the controller
    msg, cookies = rapid_num.edit_and_write_rapid_data(ipaddr, cookies, digest_auth,
                                                       'T_ROB1', 'MainModule', 'number', 10)
    # Stop timestamp
    stop_time = time.clock()
    if msg != 'Value updated.':
        print 'Error updating variable'
        sys.exit()
    # Calculates the time taken
    elap_time = stop_time - start_time
    # Writes the time to the specified text file
    with open('output/response_time_rest.txt', 'a+') as f:
        f.write('%d %g\n' % (i, elap_time))
    f.close()
_, msg = communication.logoff_robot_controller('local', cookies)
print msg
