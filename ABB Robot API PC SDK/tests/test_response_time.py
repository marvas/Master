"""
Tests the response time of frontend REST
"""


import sys
import time

import frontendIronPy.com.communication as communication
import frontendIronPy.user.user_authorization as user_authorization
import frontendIronPy.user.user_mastership as user_mastership
import frontendIronPy.rapid.rapid_datatypes as rapid_datatypes
import frontendIronPy.rapid.rapid_num as rapid_num


# Gets all the controllers on the network
controllers = communication.discover_controllers_on_network()
# Connects to the specified robot controller
ctrl, _, connected = communication.connect_robot_with_name(controllers, 'RudolfEGM')
if connected == False:
    print 'Error connecting to controller'
    sys.exit()
# Logs onto the controller with default user
logon, _ = user_authorization.logon_robot_controller_default(ctrl)
if logon == False:
    print 'Error logging on to controller'
    sys.exit()
# Gets the rapid data from controller
_, rapid_number = rapid_datatypes.get_rapid_data(ctrl, 'T_ROB1', 'MainModule', 'number')
# Get mastership on controller
master, msg, mastership = user_mastership.get_master_access_to_controller_rapid(ctrl)
if master == False:
    print 'Error getting mastership'
    sys.exit()
for i in range(100):
    start_time = time.clock()
    # Edit variable on controller
    msg = rapid_num.edit_and_write_rapid_data(rapid_number, 10)
    stop_time = time.clock()
    if msg != 'Changed the value':
        print 'Error updating variable'
        break
    elap_time = stop_time - start_time
    # Writes the time to the specified text file
    with open('output/response_time_irpy.txt', 'a+') as f:
        f.write('%d %g\n' % (i, elap_time))
    f.close()
# Release mastership on controller
released, msg = user_mastership.release_and_dispose_master_access(mastership)
if released == False:
    print 'Error releasing mastership'
    sys.exit()
# Logs off the controller
logoff, _ = user_authorization.logoff_robot_controller(ctrl)
if not logoff:
    print 'Error logging off'
    sys.exit()
