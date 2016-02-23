"""
Tests the communication and connection with the controller over time, by sending new coordinates that
the robot needs to move to. The coordinates will be points on a flower.
"""


import math
import time

import backendIronPy.com.communication as communication
import backendIronPy.user.user_authorization as user_authorization
import backendIronPy.user.user_mastership as user_mastership
import backendIronPy.rapid.rapid_datatypes as rapid_datatypes
import backendIronPy.rapid.rapid_num as rapid_num
import backendIronPy.rapid.rapid_speeddata as rapid_speeddata
import backendIronPy.rapid.rapid_zonedata as rapid_zonedata


# """
# Function that calculates the x and y coordinates of a flower.
# Amplitude should not exceed 100 as it will draw outside of the paper.
#
# Args:
#     Float: k, petal coefficient
#     Float: delta_theta, step size
# Returns:
# Examples:
# """
#
# def calculate_flower_coordinates(k, delta_theta, amplitude):
#     theta = 0
#     x = []
#     y = []
#     for i in range(0,10000):
#         x.append(amplitude*math.cos(k*theta)*math.cos(theta))
#         y.append(amplitude*math.cos(k*theta)*math.sin(theta))
#         theta += delta_theta
#
#     return x, y


# Discovers all controllers on network
controllers = communication.discover_controllers_on_network()
# Connects to the specified controller Rudolf
rudolf, msg, connected = communication.connect_robot_with_name(controllers, 'Rudolf')
print msg
# Logs onto the specified controller with default user
logon, msg = user_authorization.logon_robot_controller_default(rudolf)
print msg

_, rapid_x = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'x')
_, rapid_y = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'y')

amplitude = 100
theta = 0
k = 4
del_theta = 2
while True:
    x = amplitude*math.cos(k*theta)*math.cos(theta)
    y = amplitude*math.cos(k*theta)*math.sin(theta)
    theta += del_theta
    status, msg, mastership = user_mastership.get_master_access_to_controller_rapid(rudolf)
    print status, msg
    if status == False:
        print 'Could not get mastership'
        break
    status, msg = rapid_num.edit_and_write_rapid_data(rapid_x, x)
    print msg
    if status == False:
        print 'Could not write x'
        break
    status, msg = rapid_num.edit_and_write_rapid_data(rapid_y, y)
    print msg
    if status == False:
        print 'Could not write y'
        break
    status, msg = user_mastership.release_and_dispose_master_access(mastership)
    print status, msg
    if status == False:
        print 'Could not release mastership'
        break
    time.sleep(5)

print user_authorization.logoff_robot_controller(rudolf)
