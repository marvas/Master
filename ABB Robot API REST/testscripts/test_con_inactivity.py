"""
Script used to test the connection with the controller. Tests to see if the connection can be held for a period
of time. In this script it is set to 15 minutes of inactivity.
"""


import time

import frontendREST.com.communication as communication
import frontendREST.rapid.rapid_num as rapid_num
import frontendREST.rapid.rapid_datatypes as rapid_datatypes


# Connects to the specified controller and logs on with default user.
_, msg, digest_auth, cookies = communication.connect_robot_with_ipaddr_def_user('local')
print msg
# Pauses the execution for 15 minutes and then proceeds.
time.sleep(15*60)
# Gets information of specified rapid variable
_, response_dict, cookies = rapid_datatypes.get_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule', 'number')
print rapid_num.get_value_tostring(response_dict)
# Edits and writes the new value of num to controller
msg, cookies = rapid_num.edit_and_write_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule', 'number', 12)
print msg
# Gets information of specified rapid variable
_, response_dict, cookies = rapid_datatypes.get_rapid_data('local', cookies, digest_auth, 'T_ROB1', 'MainModule', 'number')
print rapid_num.get_value_tostring(response_dict)
# Logs of the controller.
print communication.logoff_robot_controller('local', cookies)