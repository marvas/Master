"""
Module for testing the time it takes to connect and logon to a controller with REST API.
The result is written to file.
"""


import time

import frontendREST.com.communication as communication


ipaddr = '152.94.0.39'

# Connects and logs onto the controller a set amount of times and writes the result to a file.
for i in range(100):
    # Timestamp start
    start_time = time.clock()
    # Connects to the specified controller and logs on with default user.
    connected, _, _, cookies = communication.connect_robot_with_ipaddr_def_user(ipaddr)
    # Timestamp stop
    stop_time = time.clock()
    # Calculate elapsed time
    elap_time = stop_time - start_time
    if not connected:
        print 'Error connecting and logging in'
        break
    logoff, _ = communication.logoff_robot_controller(ipaddr, cookies)
    if not logoff:
        print 'Error logging off'
        break
    # Writes the time to the specified text file
    with open('output/connection_time_rest.txt', 'a+') as f:
        f.write('%d %g\n' % (i, elap_time))
    f.close()
