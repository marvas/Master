"""

"""


"""
Private method that checks if the value is a number.

Args:
    String: value
Returns:
    Boolean: Indicates if the value is number or not
Examples:
    None
"""

def _is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


"""
Gets the value of num from response and returns it as a string

Args:
    Requests.models.Response: response
Returns:
    String: The result or error
Examples:
    None
"""

def get_value_tostring(response_dict):
    if response_dict['dattyp'] == 'num':
        try:
            res = 'Value = %s' % response_dict['value']
            return res
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not num.'
        return err


"""
Gets the value of num from response and returns it

Args:
    Requests.models.Response: response
Returns:
    Float OR String: Output depends on if it is possible to get the value or not
Examples:
    None
"""

def get_value(response_dict):
    if response_dict['dattyp'] == 'num':
        try:
            return float(response_dict['value'])
        except Exception, err:
            return err
    else:
        err = 'DataType is '+response_dict['dattyp']+' and not num.'
        return err


"""
"""

# def edit_and_write_rapid_data():