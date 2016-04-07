"""
Tests the response time of frontend REST
"""

import sys
import time

import frontendREST.com.communication as communication
import frontendREST.rapid.rapid_num as rapid_num
import frontendREST.rapid.rapid_datatypes as rapid_datatypes



ipaddr = 'local'

# Connects to the controller
connected, _, digest_auth, cookies = communication.connect_robot_with_ipaddr_def_user(ipaddr)
if not connected:
    print 'Not connected to controller'
    sys.exit()
for i in range(1000):
    # Start timestamp
    start_time = time.clock()
    # Edits the number on the controller
    _, cookies = rapid_num.edit_and_write_rapid_data(ipaddr, cookies, digest_auth, 'T_ROB1', 'MainModule', 'number', i)
    # Stop timestamp
    stop_time = time.clock()
    # Gets the value from the controller in order to see if it is updated
    _, response_dict, cookies = rapid_datatypes.get_rapid_data(ipaddr, cookies, digest_auth, 'T_ROB1', 'MainModule', 'number')
    if i != rapid_num.get_value(response_dict):
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
