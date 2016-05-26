"""
Integration test to test rapid_num functionality towards the virtual controller.
RobotStudio must run with the RAPID test program made for the integration tests
"""

import unittest
import sys

import frontendPCSDK.com.communication as com
import frontendPCSDK.user.user_authorization as user_auth
import frontendPCSDK.user.user_mastership as user_mastership
import frontendPCSDK.rapid.rapid_datatypes as rapid_datatypes
import frontendPCSDK.rapid.rapid_num as rapid_num


class RapidNumTest(unittest.TestCase):

    controller = None
    mastership = None

    # Preparing test
    def setUp(self):
        """ Setting up for test """

        # Setup for all test cases.
        controllers = com.discover_controllers_on_network()
        self.controller, _, connected = com.connect_robot_with_ipaddr(controllers, '127.0.0.1')
        if not connected:
            print 'Couldn\'t connect to controller. Test will not be run.'
            sys.exit()
        is_logged_in, _ = user_auth.logon_robot_controller_default(self.controller)
        if not is_logged_in:
            print 'Couldn\'t log in. Test will not be run.'
            sys.exit()

        test_desc = self.shortDescription()
        # Checks for additional setup for some cases.
        if test_desc == 'Tests edit_and_write_rapid_data with correct input data':
            is_master, _, self.mastership = user_mastership.get_master_access_to_controller_rapid(self.controller)
            if not is_master:
                print 'Couldn\'t get mastership on controller. Test will not be run.'
                sys.exit()

    # Ending test
    def tearDown(self):
        """ Cleaning after test """

        # Checks for any additional cleaning for some cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests edit_and_write_rapid_data with correct input data':
            got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
            if not got_var:
                print 'Could not get variable from controller. Tests will not be run.'
                sys.exit()
            _ = rapid_num.edit_and_write_rapid_data(var_number, 0)
            released_master, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not released_master:
                print 'Could\'t release mastership on controller. Tests will not be run.'
                sys.exit()

        # Cleaning for all the test cases
        _, _ = user_auth.logoff_robot_controller(self.controller)
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests get_value_tostring with correct rapid data
    def test_get_value_tostring_correct(self):
        """ Tests get_value_tostring with correct rapid data """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        self.assertEqual(rapid_num.get_value_tostring(const_number), 'Value = 1000')

    # Tests get_value_tostring with incorrect rapid data
    def test_get_value_tostring_incorrect(self):
        """ Tests get_value_tostring with incorrect rapid data """
        got_var, const_bool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        self.assertEqual(rapid_num.get_value_tostring(const_bool), 'DataType is bool and not num.')
        # Checks if not rapid data is inserted
        self.assertIsInstance(rapid_num.get_value_tostring(10), Exception)

    # Tests get_value with correct rapid data
    def test_get_value_correct(self):
        """ Tests get_value with correct rapid data """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        self.assertEqual(rapid_num.get_value(const_number), 1000)

    # Tests get_value with incorrect rapid data
    def test_get_value_incorrect(self):
        """ Tests get_value with incorrect rapid data """
        got_var, const_bool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        self.assertEqual(rapid_num.get_value(const_bool), 'DataType is bool and not num.')
        # Checks if rapid data is not inserted.
        self.assertIsInstance(rapid_num.get_value(10), Exception)

    # Tests edit_and_write_rapid_data with correct input data
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        _ = rapid_num.edit_and_write_rapid_data(var_number, 10)
        self.assertEqual(float(var_number.Value), 10)

    # Tests edit_and_write_rapid_data with incorrect input data
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data """
        # Tests with wrong rapid data input.
        got_var, var_boolean = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        res = rapid_num.edit_and_write_rapid_data(var_boolean, 10)
        self.assertEqual(res, 'DataType is bool and not num.')
        # Tests with right rapid data input but wrong value as input.
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        res = rapid_num.edit_and_write_rapid_data(var_number, True)
        self.assertIsInstance(res, Exception)
        # Tests with other than rapid data as input.
        res = rapid_num.edit_and_write_rapid_data(10, 10)
        self.assertIsInstance(res, Exception)
