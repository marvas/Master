"""
Tests the response time of frontendPCSDK
"""


import sys
import time

import frontendPCSDK.com.communication as communication
import frontendPCSDK.user.user_authorization as user_authorization
import frontendPCSDK.user.user_mastership as user_mastership
import frontendPCSDK.rapid.rapid_datatypes as rapid_datatypes
import frontendPCSDK.rapid.rapid_array as rapid_array


# Gets all the controllers on the network
controllers = communication.discover_controllers_on_network()
# Connects to the specified robot controller
ctrl, _, connected = communication.connect_robot_with_name(controllers, 'RudolfEGM')
if not connected:
    print 'Error connecting to controller'
    sys.exit()
# Logs onto the controller with default user
logon, _ = user_authorization.logon_robot_controller_default(ctrl)
if not logon:
    print 'Error logging on to controller'
    sys.exit()
# Gets the rapid data from controller
_, rapid_array2elem = rapid_datatypes.get_rapid_data(ctrl, 'T_ROB1', 'MainModule', 'arr2elem')
# Get mastership on controller
master, _, mastership = user_mastership.get_master_access_to_controller_rapid(ctrl)
if not master:
    print 'Error getting mastership'
    sys.exit()
for i in range(100):
    start_time = time.clock()
    # Edits the array on controller
    msg = rapid_array.edit_and_write_rapid_data_num(rapid_array2elem, [1, 2])
    stop_time = time.clock()
    if msg != 'Array updated.':
        print 'Error updating array'
        break
    elap_time = stop_time - start_time
    # Writes the time to the specified text file
    with open('output/response_time_array_2elem_pcsdk.txt', 'a+') as f:
        f.write('%d %g\n' % (i, elap_time))
    f.close()
# Release mastership on controller
released, _ = user_mastership.release_and_dispose_master_access(mastership)
if not released:
    print 'Error releasing mastership'
    sys.exit()
logoff, _ = user_authorization.logoff_robot_controller(ctrl)
if not logoff:
    print 'Error logging off'
    sys.exit()
