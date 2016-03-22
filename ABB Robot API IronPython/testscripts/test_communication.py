"""
Script used to test communication with controller. Can easily be modify part of it to test getting and editing
all the different rapid types.
"""

import frontendIronPy.rapid.rapid_datatypes as rapid_datatypes
import frontendIronPy.user.user_mastership as user_mastership
import frontendIronPy.com.communication as communication
import frontendIronPy.rapid.rapid_num as rapid_num
import frontendIronPy.user.user_authorization as user_authorization

# Gets all the controllers on the network
controllers = communication.discover_controllers_on_network()
# Connects to the specified robot controller
rudolf, msg, connected = communication.connect_robot_with_name(controllers, 'IRB_140_6kg_0.81m')
print msg
# Logs onto the controller with default user
logon, msg = user_authorization.logon_robot_controller_default(rudolf)
print msg
# Gets the specified rapid variable
_, variable = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'number')
print 'Got the variable: ', rapid_num.get_value_tostring(variable)
print 'Tests that get value works: ', rapid_num.get_value(variable)
# Gets mastership to controller in order to write
_, msg, mastership = user_mastership.get_master_access_to_controller_rapid(rudolf)
print msg
# Edits and writes the specified rapid variable
msg = rapid_num.edit_and_write_rapid_data(variable, 10)
print msg
# Releases mastership when the editing and writing is performed
_, msg = user_mastership.release_and_dispose_master_access(mastership)
print msg
# Gets the variable again to check if it is updated
_, variable = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'number')
print 'The changed variable: ', rapid_num.get_value_tostring(variable)
# Logs off the controller and disposes of controller
_, msg = user_authorization.logoff_robot_controller(rudolf)
print msg
_, msg = communication.disconnect_robot_controller(rudolf)
print msg
