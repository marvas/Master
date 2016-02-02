"""
The communication module has basic functions for initial communication with robot through ABB PC SDK.
"""

import clr

clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')


"""
Scans the network for controllers.

Argument: None
Return: ABB.Robotics.Controllers
"""


def discover_controllers_on_network():
    net_scan = ctrlrs.Discovery.NetworkScanner()
    net_scan.Scan()
    controllers = net_scan.Controllers
    print("Controller count: " + str(controllers.Count))
    for controller in controllers:
        print("System name: " + str(controller.SystemName),
              "System ID: " + str(controller.SystemId),
              "IP Address: " + str(controller.IPAddress),
              "Controller Version: " + str(controller.Version))
    return controllers


"""
Creates a controller instance based on the robot name.

Argument arg1: controllers( ABB.Robotics.Controllers)
Argument arg2: robot name (String)
Return arg1: ABB.Robotics.Controllers.Controller or 0 if no controller is found
Return arg2: Message with the outcome (String)
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
                print('Found controller with name: ' + robot_name)
                break
        if controller_found is False:
            msg = 'Could not find controller with name: ' + robot_name
            print('Could not find controller with name: ' + robot_name)
    except SystemError:
        msg = 'Remember to discover the controllers first before trying to connect to one'
        print('Remember to discover the controllers first before trying to connect to one')
    return ctrl, msg


"""
Creates a controller instance based on the specified IP address. If no controller can be found
with the specified IP address the controller instance will not be created.

Argument arg1: controllers (ABB.Robotics.Controllers)
Argument arg2: IP address (String)
Return arg1: ABB.Robotics.Controllers.Controller or 0 if no controller is found
Return arg2: Message with the outcome (String)
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
                print('Found controller with specified IP address: ' + IPAddress)
                break
        if controller_found is False:
            msg = 'Could not find controller with the specified IP address: ' + IPAddress
            print('Could not find controller with the specified IP address: ' + IPAddress)
    except SystemError:
        msg = 'Remember to discover the controllers first before trying to connect to one'
        print('Remember to discover the controllers first before trying to connect to one')
    return ctrl, msg


"""
Checks if there is a connection to the controller

Argument: controllers (ABB.Robotics.Controllers)
Return arg1: Boolean
Return arg2: Message with result (String)
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