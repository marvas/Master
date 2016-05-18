"""
Times the execution of drawing flowers.
"""


import math
import sys
import time

import frontendPCSDK.com.communication as communication
import frontendPCSDK.user.user_authorization as user_authorization
import frontendPCSDK.user.user_mastership as user_mastership
import frontendPCSDK.rapid.rapid_datatypes as rapid_datatypes
import frontendPCSDK.rapid.rapid_num as rapid_num
import frontendPCSDK.rapid.rapid_bool as rapid_bool
import frontendPCSDK.rapid.rapid_speeddata as rapid_speeddata
import frontendPCSDK.rapid.rapid_zonedata as rapid_zonedata


start_time = time.clock()

# Discovers all controllers on network
controllers = communication.discover_controllers_on_network()
# Connects to the specified controller Rudolf
rudolf, msg, connected = communication.connect_robot_with_name(controllers, 'RudolfEGM')
print msg
# Logs onto the specified controller with default user
logon, msg = user_authorization.logon_robot_controller_default(rudolf)
print msg

# Gets all the variables needed.
_, rapid_x = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'x')
_, rapid_y = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'y')
_, rapid_run = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'run')
_, rapid_drawing = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'drawing')
_, rapid_new_point = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'new_point')
_, rapid_sim_started = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'sim_started')
_, rapid_speed = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'speed')
_, rapid_zone = rapid_datatypes.get_rapid_data(rudolf, 'T_ROB1', 'MainModule', 'zone')


# Checks if rapid simulation has started first.
if rapid_bool.get_state(rapid_sim_started) == False:
    print 'Start rapid simulation first.'
    # Logs of the controller and disposes.
    print user_authorization.logoff_robot_controller(rudolf)
    print communication.disconnect_robot_controller(rudolf)
    sys.exit()

# Editing the speeddata and the zonedata.
_, msg, mastership = user_mastership.get_master_access_to_controller_rapid(rudolf)
print msg
msg = rapid_speeddata.edit_and_write_rapid_data_base(rapid_speed, 'v100')
print msg
# Finep is set to True in order to not get corner path failure warning
msg = rapid_zonedata.edit_and_write_rapid_data(rapid_zone, True, 0.3, 0.3, 0.3, 0.03, 0.3, 0.03)
print msg
_, msg = user_mastership.release_and_dispose_master_access(mastership)
print msg

# Properties of the drawn flower
amplitude = 100  # Length of the petals
theta = 0  # Current angle
k = 4  # Petal properties, can only be integers
del_theta = 2  # Step
num_flowers = 0  # Number of flowers drawn
max_degrees = 0

# Checks if integer is even or odd
if isinstance(k, int):
    if k == 0:
        print 'K can\'t be 0'
        print user_authorization.logoff_robot_controller(rudolf)
        print communication.disconnect_robot_controller(rudolf)
        sys.exit()
    if k % 2 == 0:
        max_degrees = 360
    else:
        max_degrees = 180
else:
    print 'Float not supported.'
    print user_authorization.logoff_robot_controller(rudolf)
    print communication.disconnect_robot_controller(rudolf)
    sys.exit()


# Draws a specified amount of flowers
while num_flowers < 3:
    while theta < max_degrees:
        if rapid_bool.get_state(rapid_drawing) == False:
            x = amplitude*math.cos(math.radians(k*theta))*math.cos(math.radians(theta))
            y = amplitude*math.cos(math.radians(k*theta))*math.sin(math.radians(theta))
            theta += del_theta
            status, msg, mastership = user_mastership.get_master_access_to_controller_rapid(rudolf)
            print status, msg
            if status == False:
                print 'Could not get mastership'
                break
            msg = rapid_num.edit_and_write_rapid_data(rapid_x, x)
            print msg
            msg = rapid_num.edit_and_write_rapid_data(rapid_y, y)
            print msg
            msg = rapid_bool.edit_and_write_rapid_data(rapid_new_point, True)
            print msg
            status, msg = user_mastership.release_and_dispose_master_access(mastership)
            print status, msg
            if status == False:
                print 'Could not release mastership'
                break
    theta = 0
    num_flowers += 1

_, msg, mastership = user_mastership.get_master_access_to_controller_rapid(rudolf)
print msg
# Stops the RAPID execution.
_ = rapid_bool.edit_and_write_rapid_data(rapid_run, False)
print 'Stopped RAPID code.'
_, msg = user_mastership.release_and_dispose_master_access(mastership)
print msg

# Logs of the controller and disposes.
print user_authorization.logoff_robot_controller(rudolf)
print communication.disconnect_robot_controller(rudolf)

stop_time = time.clock()
elap_time = stop_time - start_time

# Writes the time to the specified text file
with open('output/flower_time_pcsdk.txt', 'a+') as f:
    f.write('%g\n' % elap_time)
f.close()
