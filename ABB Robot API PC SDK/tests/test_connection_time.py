"""
Module for testing the time it takes to connect and logon to a controller with IronPython API.
The result is written to file.
"""


import time

import frontendPCSDK.com.communication as communication
import frontendPCSDK.user.user_authorization as user_authorization


# Connects and logs onto the controller a set amount of times and writes the result to a file.
for i in range(100):
    # Timestamp start
    start_time = time.clock()
    # Gets all the controllers on the network
    controllers = communication.discover_controllers_on_network()
    # Connects to the specified robot controller
    ctrl, _, connected = communication.connect_robot_with_name(controllers, 'RudolfEGM')
    # Logs onto the controller with default user
    logon, _ = user_authorization.logon_robot_controller_default(ctrl)
    # Timestamp stop
    stop_time = time.clock()
    # Calculate elapsed time
    elap_time = stop_time - start_time
    # Checks if everything went ok.
    if not connected:
        print 'Error connecting to controller'
        break
    if not logon:
        print 'Error logging on'
        break
    # Logs off the controller
    logoff, _ = user_authorization.logoff_robot_controller(ctrl)
    if not logoff:
        print 'Error logging off'
        break
    # Disconnects by disposing of the controller
    disconnected, _ = communication.disconnect_robot_controller(ctrl)
    if not disconnected:
        print 'Error disconnecting from controller'
        break
    # Writes the time to the specified text file
    with open('output/connection_time_pcsdk.txt', 'a+') as f:
        f.write('%d %g\n' % (i, elap_time))
    f.close()
