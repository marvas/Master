"""
Integration test to test user_mastership functionality towards the virtual controller.
"""

import unittest
import sys

import frontendPCSDK.com.communication as com
import frontendPCSDK.user.user_authorization as user_auth
import frontendPCSDK.user.user_mastership as user_mastership


class UserMastershipTest(unittest.TestCase):

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

        # Additional setup for some test cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests release_and_dispose_master_access with correct input data.':
            is_master, _, self.mastership = user_mastership.get_master_access_to_controller_rapid(self.controller)
            if not is_master:
                print 'Couldn\'t get mastership. Test will not be run.'
                sys.exit()
        elif test_desc == 'Tests is_controller_master with correct input data and mastership is true.':
            is_master, _, self.mastership = user_mastership.get_master_access_to_controller_rapid(self.controller)
            if not is_master:
                print 'Couldn\'t get mastership. Test will not be run.'
                sys.exit()

    # Ending test
    def tearDown(self):
        """ Cleaning after test """

        # Additional cleanup after some test cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests get_master_access_to_controller_rapid with correct input data.':
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()
        elif test_desc == 'Tests is_controller_master with correct input data and mastership is true.':
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()

        # Cleanup for all test cases.
        _, _ = user_auth.logoff_robot_controller(self.controller)
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests get_master_access_to_controller_rapid with correct input data.
    def test_get_master_access_to_controller_rapid_correct(self):
        """ Tests get_master_access_to_controller_rapid with correct input data. """
        is_master, _, self.mastership = user_mastership.get_master_access_to_controller_rapid(self.controller)
        self.assertTrue(is_master)

    # Tests get_master_access_to_controller_rapid with incorrect input data.
    def test_get_master_access_to_controller_rapid_incorrect(self):
        """ Tests get_master_access_to_controller_rapid with incorrect input data. """
        is_master, _, self.mastership = user_mastership.get_master_access_to_controller_rapid(10)
        self.assertFalse(is_master)

    # Tests release_and_dispose_master_access with correct input data.
    def test_release_and_dispose_master_access_correct(self):
        """ Tests release_and_dispose_master_access with correct input data. """
        is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
        self.assertTrue(is_released)

    # Tests release_and_dispose_master_access with incorrect input data.
    def test_release_and_dispose_master_access_incorrect(self):
        """ Tests release_and_dispose_master_access with incorrect input data. """
        is_released, _ = user_mastership.release_and_dispose_master_access(10)
        self.assertFalse(is_released)

    # Tests is_controller_master with correct input data and mastership is true.
    def test_is_controller_master_correct_true(self):
        """ Tests is_controller_master with correct input data and mastership is true. """
        is_master = user_mastership.is_controller_master(self.controller)
        self.assertTrue(is_master)

    # Tests is_controller_master with correct input data and mastership is false.
    def test_is_controller_master_correct_false(self):
        """ Tests is_controller_master with correct input data and mastership is false. """
        is_master = user_mastership.is_controller_master(self.controller)
        self.assertFalse(is_master)

    # Tests is_controller_master with incorrect input data.
    def test_is_controller_master_incorrect(self):
        """ Tests is_controller_master with incorrect input data. """
        is_master = user_mastership.is_controller_master(10)
        self.assertFalse(is_master)
