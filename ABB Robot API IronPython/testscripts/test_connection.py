"""
Script used to test the connection with the controller. Tests to see if the connection can be held for a period
of time. In this script it is set to 15 minutes of inactivity.
"""

import time

import backendIronPy.rapid.rapid_datatypes as rapid_datatypes
import backendIronPy.user.user_mastership as user_mastership
import backendIronPy.com.communication as communication
import backendIronPy.rapid.rapid_num as rapid_num
import backendIronPy.user.user_authorization as user_authorization

# Gets all the controllers on the network
controllers = communication.discover_controllers_on_network()
# Connects to the specified robot controller
ctrl, msg, connected = communication.connect_robot_with_name(controllers, 'Rudolf')
print msg
# Logs onto the controller with default user
logon, msg = user_authorization.logon_robot_controller_default(ctrl)
print msg
# Pauses the execution for 15 minutes and the proceeds.
time.sleep(60*15)
# Gets the specified rapid variable
_, variable = rapid_datatypes.get_rapid_data(ctrl, 'T_ROB1', 'MainModule', 'number')
print 'Got the variable: ', rapid_num.get_value_tostring(variable)
# Gets mastership to controller in order to write
_, msg, mastership = user_mastership.get_master_access_to_controller_rapid(ctrl)
print msg
# Edits and writes the specified rapid variable
msg = rapid_num.edit_and_write_rapid_data(variable, 11)
print msg
# Releases mastership when the editing and writing is performed
_, msg = user_mastership.release_and_dispose_master_access(mastership)
print msg
# Gets the variable again to check if it is updated
_, variable = rapid_datatypes.get_rapid_data(ctrl, 'T_ROB1', 'MainModule', 'number')
print 'The changed variable: ', rapid_num.get_value_tostring(variable)
# Logs off the controller and disposes of controller
_, msg = user_authorization.logoff_robot_controller(ctrl)
print msg
