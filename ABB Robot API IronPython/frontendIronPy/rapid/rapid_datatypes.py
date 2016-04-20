"""
Module for getting rapid data from the robot controller. This data can be shown to user, or edited and written
back to the controller in order to update a data instance.
"""


def get_rapid_data(controller, program, module, variable_name):
    """
    Gets a Rapid object that reference a Rapid data instance on the robot controller.

    Input:
        ABB.Robotics.Controllers.Controller: controller
        String: program (name of the program, typically "T_ROB1")
        String: module (name of the module, ex "MainModule")
        String: variable_name, Name of the variable to get (ex "target_10")
    Output:
        Boolean: Indicates if able to get the data or not
        ABB.Robotics.Controllers.RapidDomain.RapidData OR String: Rapid data object if successful and error string if not
    Examples:
        bool, rapid_data = rapid_datatypes.get_rapid_data(controller,'T_ROB1','MainModule','p20')
    """
    try:
        rapid_data = controller.Rapid.GetRapidData(program, module, variable_name)
        return True, rapid_data
    except Exception, err:
        return False, err
