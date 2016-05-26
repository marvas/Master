"""
Integration test to test communication functionality towards the virtual controller.
RobotStudio must run with the RAPID test program made for the integration tests
"""

import unittest
import sys

import frontendPCSDK.com.communication as com


class CommunicationTest(unittest.TestCase):

    controller = None
    # Change robot name if a different robot name is used.
    robot_name = 'IRB_140_6kg_0.81m'

    # Preparing test
    def setUp(self):
        """ Setting up for test """

    # Ending test
    def tearDown(self):
        """ Cleaning after test """

        test_desc = self.shortDescription()
        if test_desc == 'Tests connect_robot_with_name with correct input data.':
            _, _ = com.disconnect_robot_controller(self.controller)
        elif test_desc == 'Tests connect_robot_with_ipaddr with correct input data.':
            _, _ = com.disconnect_robot_controller(self.controller)
        elif test_desc == 'Tests is_connected_to_controller with correct input data.':
            _, _ = com.disconnect_robot_controller(self.controller)

    # Tests connect_robot_with_name with correct input data.
    def test_connect_robot_with_name_correct(self):
        """ Tests connect_robot_with_name with correct input data """
        controllers = com.discover_controllers_on_network()
        self.controller, _, connected = com.connect_robot_with_name(controllers, self.robot_name)
        self.assertTrue(connected)

    # Tests connect_robot_with_name with incorrect input data
    def test_connect_robot_with_name_incorrect(self):
        """ Tests connect_robot_with_name with incorrect input data """
        controllers = com.discover_controllers_on_network()
        # Checks if wrong input for robot_name.
        self.controller, res, connected = com.connect_robot_with_name(controllers, True)
        self.assertIsInstance(res, Exception)
        # Checks if wrong input for the discovered controllers.
        self.controller, res, connected = com.connect_robot_with_name(10, self.robot_name)
        self.assertIsInstance(res, Exception)

    # Tests connect_robot_with_ipaddr with correct input data.
    def test_connect_robot_with_ipaddr_correct(self):
        """ Tests connect_robot_with_ipaddr with correct input data. """
        controllers = com.discover_controllers_on_network()
        self.controller, _, connected = com.connect_robot_with_ipaddr(controllers, '127.0.0.1')
        self.assertTrue(connected)

    # Tests connect_robot_with_ipaddr with incorrect input data.
    def test_connect_robot_with_ipaddr_incorrect(self):
        """ Tests connect_robot_with_ipaddr with incorrect input data. """
        controllers = com.discover_controllers_on_network()
        # Checks if wrong input for robot_name.
        self.controller, res, connected = com.connect_robot_with_ipaddr(controllers, True)
        self.assertIsInstance(res, Exception)
        # Checks if wrong input for the discovered controllers.
        self.controller, res, connected = com.connect_robot_with_ipaddr(10, '127.0.0.1')
        self.assertIsInstance(res, Exception)

    # Tests disconnect_robot_controller with correct input data.
    def test_disconnect_robot_controller_correct(self):
        """ Tests disconnect_robot_controller with correct input data. """
        controllers = com.discover_controllers_on_network()
        self.controller, _, connected = com.connect_robot_with_ipaddr(controllers, '127.0.0.1')
        if not connected:
            print 'Couldn\'t connect to controller. Test will not be run'
            sys.exit()
        is_disconnected, _ = com.disconnect_robot_controller(self.controller)
        self.assertTrue(is_disconnected)

    # Tests disconnect_robot_controller with incorrect input data.
    def test_disconnect_robot_controller_incorrect(self):
        """ Tests disconnect_robot_controller with incorrect input data. """
        is_disconnected, _ = com.disconnect_robot_controller(True)
        self.assertFalse(is_disconnected)

    # Tests is_connected_to_controller with correct input data.
    def test_is_connected_to_controller_correct(self):
        """ Tests is_connected_to_controller with correct input data. """
        controllers = com.discover_controllers_on_network()
        self.controller, _, connected = com.connect_robot_with_ipaddr(controllers, '127.0.0.1')
        if not connected:
            print 'Couldn\'t connect to controller. Test will not be run'
            sys.exit()
        res = com.is_connected_to_controller(self.controller)
        self.assertTrue(res)

    # Tests is_connected_to_controller with incorrect input data.
    def test_is_connected_to_controller_incorrect(self):
        """ Tests is_connected_to_controller with incorrect input data. """
        res = com.is_connected_to_controller(10)
        self.assertIsInstance(res, Exception)
