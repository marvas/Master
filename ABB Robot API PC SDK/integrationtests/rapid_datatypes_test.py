"""
Integration test to test rapid_datatypes functionality towards the virtual controller.
RobotStudio must run with the RAPID test program made for the integration tests
"""

import unittest
import sys

import frontendPCSDK.com.communication as com
import frontendPCSDK.user.user_authorization as user_auth
import frontendPCSDK.rapid.rapid_datatypes as rapid_datatypes


class RapidDatatypesTest(unittest.TestCase):

    controller = None

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

    # Ending test
    def tearDown(self):
        """ Cleaning after test """

        # Cleaning for all the test cases
        _, _ = user_auth.logoff_robot_controller(self.controller)
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests get_rapid_data with correct input data.
    def test_get_rapid_data_correct(self):
        """ Tests get_rapid_data with correct input data. """
        got_const, _ = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        self.assertTrue(got_const)

    # Tests get_rapid_data with incorrect input data.
    def test_get_rapid_data_incorrect(self):
        """ Tests get_rapid_data with incorrect input data. """
        # Tests if controller is not inserted.
        got_const, _ = rapid_datatypes.get_rapid_data(10, 'T_ROB1', 'MainModule', 'const_number')
        self.assertFalse(got_const)
        # Checks if the input data is not correct.
        got_const, _ = rapid_datatypes.get_rapid_data(self.controller, 'Wrong', 'MainModule', 'const_number')
        self.assertFalse(got_const)
