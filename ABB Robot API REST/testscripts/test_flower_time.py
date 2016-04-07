"""
Times the execution of drawing flowers.
"""


import math
import sys
import time

import frontendREST.com.communication as communication
import frontendREST.rapid.rapid_bool as rapid_bool
import frontendREST.rapid.rapid_num as rapid_num
import frontendREST.rapid.rapid_datatypes as rapid_datatypes
import frontendREST.rapid.rapid_speeddata as rapid_speeddata
import frontendREST.rapid.rapid_zonedata as rapid_zonedata


start_time = time.clock()

ipaddr = 'local'

# Connects to the specified controller and logs on with default user.
_, sys_info, digest_auth, cookies = communication.connect_robot_with_ipaddr_def_user(ipaddr)
print sys_info

# Checks if rapid simulation has started.
_, response, cookies = rapid_datatypes.get_rapid_data(ipaddr, cookies, digest_auth, 'T_ROB1', 'MainModule', 'sim_started')
if rapid_bool.get_state(response) == False:
    print 'Start rapid simulation first.'
    _, msg = communication.logoff_robot_controller(ipaddr, cookies)
    print msg
    sys.exit()

# Editing the speeddata and zonedata
msg, cookies = rapid_speeddata.edit_and_write_rapid_data_base(ipaddr, cookies, digest_auth,
                                                              'T_ROB1', 'MainModule', 'speed', 'v100')
print msg
# Finep is set to True in order to not get corner path failure warning
msg, cookies = rapid_zonedata.edit_and_write_rapid_data(ipaddr, cookies, digest_auth, 'T_ROB1', 'MainModule', 'zone',
                                                        True, 0.3, 0.3, 0.3, 0.03, 0.3 ,0.03)
print msg

# Properties of the drawn flower
amplitude = 100 # Length of the petals
theta = 0 # Current angle
k = 4 # Petal properties, can only be integers
del_theta = 2 # Step
num_flowers = 0 # Number of flowers drawn
max_degrees = 0

if isinstance(k, int):
    if k == 0:
        print 'K can\'t be 0'
        _, msg = communication.logoff_robot_controller(ipaddr, cookies)
        print msg
        sys.exit()
    if k % 2 == 0:
        max_degrees = 360
    else:
        max_degrees = 180
else:
    print 'Float not supported.'
    _, msg = communication.logoff_robot_controller(ipaddr, cookies)
    sys.exit()

# Draws a specified amount of flowers
while num_flowers < 10:
    while theta < max_degrees:
        got_value, response, cookies = rapid_datatypes.get_rapid_data(ipaddr, cookies, digest_auth,
                                                              'T_ROB1', 'MainModule', 'drawing')
        time.sleep(1)
        if got_value:
            if rapid_bool.get_state(response) == False:
                x = amplitude*math.cos(math.radians(k*theta))*math.cos(math.radians(theta))
                y = amplitude*math.cos(math.radians(k*theta))*math.sin(math.radians(theta))
                theta = theta + del_theta
                msg, cookies = rapid_num.edit_and_write_rapid_data(ipaddr, cookies, digest_auth,
                                                                   'T_ROB1', 'MainModule', 'x', x)
                print msg
                msg, cookies = rapid_num.edit_and_write_rapid_data(ipaddr, cookies, digest_auth,
                                                                   'T_ROB1', 'MainModule', 'y', y)
                print msg
                msg, cookies = rapid_bool.edit_and_write_rapid_data(ipaddr, cookies, digest_auth,
                                                                    'T_ROB1', 'MainModule', 'new_point', True)
                print msg
    theta = 0
    num_flowers = num_flowers + 1

# Stops the RAPID execution.
_, cookies = rapid_bool.edit_and_write_rapid_data(ipaddr, cookies, digest_auth, 'T_ROB1', 'MainModule', 'run', False)
print 'Stopped RAPID execution.'

# Logs of the controller
_, msg = communication.logoff_robot_controller(ipaddr, cookies)
print msg

stop_time = time.clock()
elap_time = stop_time-start_time

# Writes the time to the specified text file
with open('output/flower_time_rest.txt', 'a+') as f:
    f.write('%g\n' % elap_time)
f.close()