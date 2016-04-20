"""
The communication module has basic functions for initial communication with robot through ABB PC SDK.
"""


import clr
clr.AddReferenceToFileAndPath(
        'C:\\Program Files (x86)\\ABB Industrial IT\\Robotics IT\\SDK\PCSDK 6.02\\ABB.Robotics.Controllers.PC.dll')
# clr.AddReferenceToFileAndPath('ABB.Robotics.Controllers.PC.dll')
import ABB.Robotics.Controllers as ctrlrs


def discover_controllers_on_network():
    """
    Scans the network for controllers.

    Input:
        None
    Output:
        ABB.Robotics.Controllers: Controllers found on the network
    Examples:
        None
    """
    net_scan = ctrlrs.Discovery.NetworkScanner()
    net_scan.Scan()
    controllers = net_scan.Controllers
    for controller in controllers:
        print("System name: " + str(controller.SystemName),
              "System ID: " + str(controller.SystemId),
              "IP Address: " + str(controller.IPAddress),
              "Controller Version: " + str(controller.Version))
    return controllers


def connect_robot_with_name(controllers, robot_name):
    """
    Creates a controller instance based on the robot name.

    Input:
        ABB.Robotics.Controllers: controllers
        String: robot_name
    Output:
        ABB.Robotics.Controllers.Controller OR None: Output depends on if the connection is successful or not.
        String: Message with the outcome
        Boolean: Indicates if the controller was found and connected to.
    Examples:
        None
    """
    controller_found = False
    try:
        for controller in controllers:
            if robot_name.lower() == str(controller.SystemName).lower():
                ctrl = ctrlrs.ControllerFactory.CreateFrom(controller)
                controller_found = True
                msg = 'Found controller with name: ' + robot_name
                return ctrl, msg, controller_found
        msg = 'Could not find controller with name: ' + robot_name
        return None, msg, controller_found
    except Exception:
        msg = 'Remember to discover the controllers first before trying to connect.'
        return None, msg, controller_found


def connect_robot_with_ipaddr(controllers, ipaddress):
    """
    Creates a controller instance based on the specified IP address. If no controller can be found
    with the specified IP address the controller instance will not be created.

    Input:
        ABB.Robotics.Controllers: controllers
        String: ipaddress
    Output:
        ABB.Robotics.Controllers.Controller OR None: Output depends on if the connection is successful or not.
        String: Message with the outcome
        Boolean: Indicates if the controller was found and connected to.
    Examples:
        None
    """
    controller_found = False
    try:
        for controller in controllers:
            if ipaddress == str(controller.IPAddress):
                ctrl = ctrlrs.ControllerFactory.CreateFrom(controller)
                controller_found = True
                msg = 'Found controller with specified IP address: ' + ipaddress
                return ctrl, msg, controller_found
        msg = 'Could not find controller with the specified IP address: ' + ipaddress
        return None, msg, controller_found
    except Exception:
        msg = 'Remember to discover the controllers first before trying to connect.'
        return None, msg, controller_found


def disconnect_robot_controller(controller):
    """
    Disconnects from the robot controller.

    Input:
        ABB.Robotics.Controllers.Controller: controller
    Output:
        Boolean: Indicates if disconnect is successful
        String: Message with the outcome
    Examples:
        None
    """
    try:
        controller.Dispose()
        msg = 'Disconnect successful'
        return True, msg
    except Exception, err:
        return False, err


def is_connected_to_controller(controller):
    """
    Checks if there is a connection to the controller

    Input:
        ABB.Robotics.Controllers: controller
    Output:
        Boolean: Indicates if connected or not
    Examples:
        None
    """
    try:
        if controller.Connected == 1:
            return True
        else:
            return False
    except Exception:
        return False
