"""
The communication module has basic functions for initial communication with robot through ABB PC SDK.
"""


import clr
clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs



"""
Scans the network for controllers.

Args:
    None
Returns:
    ABB.Robotics.Controllers: Controllers found on the network
Examples:
    None
"""

def discover_controllers_on_network():
    net_scan = ctrlrs.Discovery.NetworkScanner()
    net_scan.Scan()
    controllers = net_scan.Controllers
    for controller in controllers:
        print("System name: " + str(controller.SystemName),
              "System ID: " + str(controller.SystemId),
              "IP Address: " + str(controller.IPAddress),
              "Controller Version: " + str(controller.Version))
    return controllers


"""
Creates a controller instance based on the robot name.

Args:
    ABB.Robotics.Controllers: Controllers
    String: Name of the robot
Returns:
    ABB.Robotics.Controllers.Controller OR 0: Output depends on if the connection is successful or not.
    String: Message with the outcome
Examples:
    None
"""

def connect_robot_with_name(controllers, robot_name):
    controller_found = False
    ctrl = 0
    msg = ''
    try:
        for controller in controllers:
            if robot_name.lower() == str(controller.SystemName).lower():
                ctrl = ctrlrs.ControllerFactory.CreateFrom(controller)
                controller_found = True
                msg = 'Found controller with name: ' + robot_name
                break
        if controller_found is False:
            msg = 'Could not find controller with name: ' + robot_name
    except SystemError:
        msg = 'Remember to discover the controllers first before trying to connect to one'
    return ctrl, msg


"""
Creates a controller instance based on the specified IP address. If no controller can be found
with the specified IP address the controller instance will not be created.

Args:
    ABB.Robotics.Controllers: Controllers
    String: IP address
Returns:
    ABB.Robotics.Controllers.Controller OR 0: Output depends on if the connection is successful or not.
    String: Message with the outcome
Examples:
    None
"""

def connect_robot_with_ipaddr(controllers, IPAddress):
    controller_found = False
    ctrl = 0
    msg = ''
    try:
        for controller in controllers:
            if IPAddress == str(controller.IPAddress):
                ctrl = ctrlrs.ControllerFactory.CreateFrom(controller)
                controller_found = True
                msg = 'Found controller with specified IP address: ' + IPAddress
                break
        if controller_found is False:
            msg = 'Could not find controller with the specified IP address: ' + IPAddress
    except SystemError:
        msg = 'Remember to discover the controllers first before trying to connect to one'
    return ctrl, msg


"""
Checks if there is a connection to the controller

Args:
    ABB.Robotics.Controllers: Controllers
Returns:
    Boolean: Indicates if connected or not
    String: Message with the result
Examples:
    None
"""

def is_connected_to_controller(controller):
    try:
        if controller.Connected == 1:
            msg = 'Connected to controller'
            return True, msg
        else:
            msg = 'Not connected to controller'
            return False, msg
    except Exception:
        msg = 'Controller object is not set up correctly. Controller may not exist.'
        return False, msg