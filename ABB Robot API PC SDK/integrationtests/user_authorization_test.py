"""
Integration test to test user_authorization functionality towards the virtual controller.
"""

import unittest
import sys

import frontendIronPy.com.communication as com
import frontendIronPy.user.user_authorization as user_auth


class UserAuthorizationTest(unittest.TestCase):

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

        # Additional setup for some test cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests logoff_robot_controller with correct input data.':
            is_logged_in, _ = user_auth.logon_robot_controller_default(self.controller)
            if not is_logged_in:
                print 'Couldn\'t log in. Test will not be run.'
                sys.exit()

    # Ending test
    def tearDown(self):
        """ Cleaning after test """

        # Cleanup after specific test cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests logon_robot_controller_default with correct input data.':
            is_logged_off, _ = user_auth.logoff_robot_controller(self.controller)
            if not is_logged_off:
                print 'Couldn\'t log off controller. Test will not be run.'
                sys.exit()
        elif test_desc == 'Tests logon_robot_controller_with_username with correct input data.':
            is_logged_off, _ = user_auth.logoff_robot_controller(self.controller)
            if not is_logged_off:
                print 'Couldn\'t log off controller. Test will not be run.'
                sys.exit()

        # Cleanup for all test cases.
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests logon_robot_controller_default with correct input data.
    def test_logon_robot_controller_default_correct(self):
        """ Tests logon_robot_controller_default with correct input data. """
        is_logged_in, _ = user_auth.logon_robot_controller_default(self.controller)
        self.assertTrue(is_logged_in)

    # Tests logon_robot_controller_default with correct input data.
    def test_logon_robot_controller_default_incorrect(self):
        """ Tests logon_robot_controller_default with correct input data. """
        is_logged_in, _ = user_auth.logon_robot_controller_default(10)
        self.assertFalse(is_logged_in)

    # Tests logon_robot_controller_with_username with correct input data.
    def test_logon_robot_controller_with_username_correct(self):
        """ Tests logon_robot_controller_with_username with correct input data. """
        is_logged_in, _ = user_auth.logon_robot_controller_with_username(self.controller, 'Default User', 'robotics')
        self.assertTrue(is_logged_in)

    # Tests logon_robot_controller_with_username with incorrect input data.
    def test_logon_robot_controller_with_username_incorrect(self):
        """ Tests logon_robot_controller_with_username with incorrect input data. """
        is_logged_in, _ = user_auth.logon_robot_controller_with_username(self.controller, 'Wrong user', 'robotics')
        self.assertFalse(is_logged_in)
        is_logged_in, _ = user_auth.logon_robot_controller_with_username(10, 'Default User', 'robotics')
        self.assertFalse(is_logged_in)
        is_logged_in, _ = user_auth.logon_robot_controller_with_username(self.controller, 'Default User', 'wrong')
        self.assertFalse(is_logged_in)

    # Tests logoff_robot_controller with correct input data.
    def test_logoff_robot_controller_correct(self):
        """ Tests logoff_robot_controller with correct input data. """
        is_logged_off, _ = user_auth.logoff_robot_controller(self.controller)
        self.assertTrue(is_logged_off)

    # Tests logoff_robot_controller with incorrect input data.
    def test_logoff_robot_controller_incorrect(self):
        """ Tests logoff_robot_controller with incorrect input data. """
        is_logged_off, _ = user_auth.logoff_robot_controller(10)
        self.assertFalse(is_logged_off)
