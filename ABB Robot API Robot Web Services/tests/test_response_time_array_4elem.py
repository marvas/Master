"""
Tests the response time of frontend REST
"""

import sys
import time

import frontendRWS.com.communication as communication
import frontendRWS.rapid.rapid_array as rapid_array


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
    msg, cookies = rapid_array.edit_and_write_rapid_data_num(ipaddr, cookies, digest_auth, 'T_ROB1',
                                                             'MainModule', 'arr4elem', [1, 2, 1, 2])
    # Stop timestamp
    stop_time = time.clock()
    # Gets the value from the controller in order to see if it is updated
    if msg != 'Array updated.':
        print 'Error updating variable'
        sys.exit()
    # Calculates the time taken
    elap_time = stop_time - start_time
    # Writes the time to the specified text file
    with open('output/response_time_array_4elem_rws.txt', 'a+') as f:
        f.write('%d %g\n' % (i, elap_time))
    f.close()
_, msg = communication.logoff_robot_controller(ipaddr, cookies)
print msg
