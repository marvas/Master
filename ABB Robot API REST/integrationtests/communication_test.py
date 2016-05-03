"""
Integration test to test communication functionality towards the virtual controller.
"""

import unittest
import sys

import frontendREST.com.communication as com

##### Used when testing statement and branch coverage. ########
# sys.path.insert(1, 'C:\Users\Marius Vasshus\Dropbox\Programmering\Python\Master\ABB Robot API REST')
###############################################################


class CommunicationTest(unittest.TestCase):

    cookies = None

    # Preparing test
    def setUp(self):
        """ Setting up for test """

    # Ending test
    def tearDown(self):
        """ Cleaning after test """

        test_desc = self.shortDescription()
        if test_desc == 'Tests connect_robot_with_ipaddr_and_user with correct input data.':
            com.logoff_robot_controller('local', self.cookies)
        elif test_desc == 'Tests connect_robot_with_ipaddr_def_user with correct input data.':
            com.logoff_robot_controller('local', self.cookies)

    # Tests connect_robot_with_ipaddr_and_user with correct input data.
    def test_connect_robot_with_ipaddr_and_user_correct(self):
        """ Tests connect_robot_with_ipaddr_and_user with correct input data. """
        connected, _, _, self.cookies = com.connect_robot_with_ipaddr_and_user('local', 'Default User', 'robotics')
        self.assertTrue(connected)

    # Tests connect_robot_with_ipaddr_and_user with incorrect input data
    def test_connect_robot_with_ipaddr_and_user_incorrect(self):
        """ Tests connect_robot_with_ipaddr_and_user with incorrect input data """
        # Checks if wrong ip address.
        _, err, _, _ = com.connect_robot_with_ipaddr_and_user('10', 'Default User', 'robotics')
        self.assertIsInstance(err, Exception)
        # Checks if wrong user name.
        _, err, _, _ = com.connect_robot_with_ipaddr_and_user('local', 'Wrong user', 'robotics')
        self.assertEqual(err, 'Something went wrong. Status code: 401')
        # Checks if wrong password
        _, err, _, _ = com.connect_robot_with_ipaddr_and_user('local', 'Default User', 'wrong')
        self.assertEqual(err, 'Something went wrong. Status code: 401')
        # Checks if wrong input.
        _, err, _, _ = com.connect_robot_with_ipaddr_and_user(10, 'Default User', 'wrong')
        self.assertEqual(err, 'Something wrong with arguments. Needs to be string.')
        _, err, _, _ = com.connect_robot_with_ipaddr_and_user('local', 10, 'wrong')
        self.assertEqual(err, 'Something wrong with arguments. Needs to be string.')
        _, err, _, _ = com.connect_robot_with_ipaddr_and_user('local', 'Default User', 10)
        self.assertEqual(err, 'Something wrong with arguments. Needs to be string.')

    # Tests connect_robot_with_ipaddr_def_user with correct input data.
    def test_connect_robot_with_ipaddr_def_user_correct(self):
        """ Tests connect_robot_with_ipaddr_def_user with correct input data. """
        connected, _, _, self.cookies = com.connect_robot_with_ipaddr_def_user('local')
        self.assertTrue(connected)

    # Tests connect_robot_with_ipaddr_def_user with incorrect input data.
    def test_connect_robot_with_ipaddr_def_user_incorrect(self):
        """ Tests connect_robot_with_ipaddr_def_user with incorrect input data. """
        # Checks if wrong ip address.
        _, err, _, _ = com.connect_robot_with_ipaddr_def_user('10')
        self.assertIsInstance(err, Exception)
        # Checks if wrong input.
        _, err, _, _ = com.connect_robot_with_ipaddr_def_user(10)
        self.assertEqual(err, 'Something wrong with argument. Needs to be string.')

    # Tests logoff_robot_controller with correct input data.
    def test_logoff_robot_controller_correct(self):
        """ Tests logoff_robot_controller with correct input data. """
        connected, _, _, self.cookies = com.connect_robot_with_ipaddr_def_user('local')
        if not connected:
            print 'Couldn\'t connect to controller. Test will not be run'
            sys.exit()
        is_logoff, _ = com.logoff_robot_controller('local', self.cookies)
        self.assertTrue(is_logoff)

    # Tests logoff_robot_controller with incorrect input data.
    def test_logoff_robot_controller_incorrect(self):
        """ Tests logoff_robot_controller with incorrect input data. """
        # Checks if input is wrong data
        _, err = com.logoff_robot_controller('local', 10)
        self.assertEqual(err, 'Something wrong with arguments.')
        _, err = com.logoff_robot_controller(10, self.cookies)
        self.assertEqual(err, 'Something wrong with arguments.')
