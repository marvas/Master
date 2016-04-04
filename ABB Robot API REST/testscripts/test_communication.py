"""
Script used to test communication with controller. Can easily be modify part of it to test getting and editing
all the different rapid types.
"""


import frontendREST.com.communication as communication
import frontendREST.rapid.rapid_num as rapid_num
import frontendREST.rapid.rapid_datatypes as rapid_datatypes


# Connects to the specified controller and logs on with default user.
_, msg, digest_auth, cookies = communication.connect_robot_with_ipaddr_def_user('local')
print msg
# Gets information of specified rapid variable
_, response_dict, cookies = rapid_datatypes.get_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule', 'number')
print 'Got the variable: ', rapid_num.get_value_tostring(response_dict)
print 'Tests that get value works: ', rapid_num.get_value(response_dict)
# Edits and writes the new value of num to controller
msg, cookies = rapid_num.edit_and_write_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule', 'number', 11)
print msg
# Gets information of specified rapid variable
_, response_dict, cookies = rapid_datatypes.get_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule', 'number')
print 'The changed variable: ', rapid_num.get_value_tostring(response_dict)
# Logs of the controller.
_, msg = communication.logoff_robot_controller('local', cookies)
print msg