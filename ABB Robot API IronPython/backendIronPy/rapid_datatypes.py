"""
Module for getting rapid data from the robot controller. This data can be shown to user, or edited and written
back to the controller in order to update a data instance.
"""




"""
Gets a Rapid object that reference a Rapid data instance on the robot controller.

Args:
    ABB.Robotics.Controllers.Controller: Controller
    String: Program (name of the program, typically "T_ROB1")
    String: Module (name of the module, ex "MainModule")
    String: Name of the variable to get (ex "target_10")
Returns:
    Boolean: Indicates if able to get the data or not
    ABB.Robotics.Controllers.RapidDomain.RapidData OR String: Rapid data object if successful and error string if not
Examples:
    bool, rapid_data = rapid_datatypes.get_rapid_data(controller,'T_ROB1','MainModule','p20')
"""

def get_rapid_data(controller, program, module, variable_name):
    try:
        rapid_data = controller.Rapid.GetRapidData(program, module, variable_name)
        return True, rapid_data
    except Exception, err:
        return False, err