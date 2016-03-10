"""
Script used to test communication with controller. Can easily be modify part of it to test getting and editing
all the different rapid types.
"""


import frontendREST.com.communication as communication
import frontendREST.rapid.rapid_num as rapid_num
import frontendREST.user.user_mastership as user_mastership
import frontendREST.rapid.rapid_datatypes as rapid_datatypes


# Connects to the specified controller and logs on with default user.
_, msg, digest_auth, cookies = communication.connect_robot_with_ipaddr_def_user('local')
print msg
# Gets information of specified rapid variable
_, response_dict = rapid_datatypes.get_rapid_data('local', cookies, 'T_ROB1', 'MainModule', 'number')
print rapid_num.get_value_tostring(response_dict)
# Gets mastership on specified controller.
res = user_mastership.get_master_access_to_controller('local', cookies)
print 'Got mastership: %s' % res
# Edits and writes the new value of num to controller
msg = rapid_num.edit_and_write_rapid_data('local', cookies, 'T_ROB1', 'MainModule', 'number', 10)
print msg
# Releases mastership of controller after it is finished writing.
res = user_mastership.release_master_access_to_controller('local', cookies)
print 'Released mastership: %s' % res
# Gets information of specified rapid variable
_, response_dict = rapid_datatypes.get_rapid_data('local', cookies, 'T_ROB1', 'MainModule', 'number')
print rapid_num.get_value_tostring(response_dict)
# Logs of the controller.
print communication.logoff_robot_controller('local', cookies)