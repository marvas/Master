"""
Module for testing the time it takes to connect and logon to a controller. The result is written to file.
"""


import time

import frontendIronPy.com.communication as communication
import frontendIronPy.user.user_authorization as user_authorization


# Connects and logs onto the controller a set amount of times and writes the result to a file.
for i in range(100):
    # Gets all the controllers on the network
    controllers = communication.discover_controllers_on_network()
    # Timestamp start
    start_time = time.clock()
    # Connects to the specified robot controller
    ctrl, _, connected = communication.connect_robot_with_name(controllers, 'IRB_140_6kg_0.81m')
    # Logs onto the controller with default user
    logon, _ = user_authorization.logon_robot_controller_default(ctrl)
    # Timestamp stop
    stop_time = time.clock()
    # Calculate elapsed time
    elap_time = stop_time - start_time
    # Checks if everything went ok before writing result.
    if not connected:
        print 'Error connecting to controller'
        break
    if not logon:
        print 'Error logging on'
        break
    # Writes the time to the specified text file
    with open('connection_time_irpy.txt', 'a+') as f:
        f.write('%g\n' % elap_time)
    f.close()
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