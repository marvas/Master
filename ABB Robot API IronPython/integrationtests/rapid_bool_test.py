"""
Integration test to test rapid_bool functionality towards the virtual controller.
"""

import unittest
import sys

import frontendIronPy.com.communication as com
import frontendIronPy.user.user_authorization as user_auth
import frontendIronPy.user.user_mastership as user_mastership
import frontendIronPy.rapid.rapid_datatypes as rapid_datatypes
import frontendIronPy.rapid.rapid_bool as rapid_bool


class RapidBoolTest(unittest.TestCase):

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
            got_var, var_bool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_boolean')
            if not got_var:
                print 'Could not get variable from controller. Tests will not be run.'
                sys.exit()
            _ = rapid_bool.edit_and_write_rapid_data(var_bool, True)
            released_master, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not released_master:
                print 'Could\'t release mastership on controller. Tests will not be run.'
                sys.exit()

        # Cleaning for all the test cases
        _, _ = user_auth.logoff_robot_controller(self.controller)
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests get_state_tostring with correct rapid data
    def test_get_state_tostring_correct(self):
        """ Tests get_state_tostring with correct rapid data """
        got_var, const_bool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        self.assertEqual(rapid_bool.get_state_tostring(const_bool), 'State = True')

    # Tests get_state_tostring with incorrect rapid data
    def test_get_state_tostring_incorrect(self):
        """ Tests get_state_tostring with incorrect rapid data """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        self.assertEqual(rapid_bool.get_state_tostring(const_number), 'DataType is num and not bool.')
        # Checks if rapid data is not inserted.
        self.assertIsInstance(rapid_bool.get_state_tostring(10), Exception)

    # Tests get_state with correct rapid data
    def test_get_state_correct(self):
        """ Tests get_state with correct rapid data """
        got_var, const_bool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        self.assertEqual(rapid_bool.get_state(const_bool), True)

    # Tests get_state with incorrect rapid data
    def test_get_state_incorrect(self):
        """ Tests get_state with incorrect rapid data """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        self.assertEqual(rapid_bool.get_state(const_number), 'DataType is num and not bool.')
        # Checks if rapid data is not inserted.
        self.assertIsInstance(rapid_bool.get_state(10), Exception)

    # Tests edit_and_write_rapid_data with correct input data
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data """
        got_var, var_bool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        _ = rapid_bool.edit_and_write_rapid_data(var_bool, False)
        self.assertEqual(var_bool.Value.ToString().lower(), 'false')

    # Tests edit_and_write_rapid_data with incorrect input data
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data """
        # Tests with wrong rapid data input.
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        res = rapid_bool.edit_and_write_rapid_data(var_number, False)
        self.assertEqual(res, 'DataType is num and not bool.')
        # Tests with right rapid data input but wrong value as input.
        got_var, var_bool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        res = rapid_bool.edit_and_write_rapid_data(var_bool, 10)
        self.assertIsInstance(res, Exception)
