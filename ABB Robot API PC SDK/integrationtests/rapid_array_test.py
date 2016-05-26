"""
Integration test to test rapid_array functionality towards the virtual controller.
RobotStudio must run with the RAPID test program made for the integration tests
"""

import unittest
import sys

import frontendPCSDK.com.communication as com
import frontendPCSDK.user.user_authorization as user_auth
import frontendPCSDK.user.user_mastership as user_mastership
import frontendPCSDK.rapid.rapid_datatypes as rapid_datatypes
import frontendPCSDK.rapid.rapid_array as rapid_array


class RapidArrayTest(unittest.TestCase):

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

        # Additional setup before some test cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests edit_and_write_rapid_data_num_index with correct input data.':
            is_master, _, self.mastership = user_mastership.get_master_access_to_controller_rapid(self.controller)
            if not is_master:
                print 'Couldn\'t get mastership. Test will not run.'
                sys.exit()
        elif test_desc == 'Tests edit_and_write_rapid_data_num with correct input data.':
            is_master, _, self.mastership = user_mastership.get_master_access_to_controller_rapid(self.controller)
            if not is_master:
                print 'Couldn\'t get mastership. Test will not run.'
                sys.exit()

    # Ending test
    def tearDown(self):
        """ Cleaning after test """

        # Additional cleanup for some test cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests edit_and_write_rapid_data_num_index with correct input data.':
            got_var, var_array = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_array')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_array.edit_and_write_rapid_data_num_index(var_array, 0, 0)
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()
        elif test_desc == 'Tests edit_and_write_rapid_data_num with correct input data.':
            got_var, var_array = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_array')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_array.edit_and_write_rapid_data_num(var_array, [])
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()

        # Cleaning for all the test cases
        _, _ = user_auth.logoff_robot_controller(self.controller)
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests get_length with correct input data.
    def test_get_length_correct(self):
        """ Tests get_length with correct input data. """
        got_var, var_array = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_array')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        length = rapid_array.get_length(var_array)
        self.assertEqual(length, 3)

    # Tests get_length with incorrect input data.
    def test_get_length_incorrect(self):
        """ Tests get_length with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid variable is inserted.
        length = rapid_array.get_length(var_number)
        self.assertIsInstance(length, basestring)
        # Checks if rapid_data is not inserted.
        length = rapid_array.get_length(10)
        self.assertIsInstance(length, Exception)

    # Tests get_dimension with correct input data.
    def test_get_dimension_correct(self):
        """ Tests get_dimension with correct input data. """
        got_var, var_array = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_array')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        dimension = rapid_array.get_dimensions(var_array)
        self.assertEqual(dimension, 1)

    # Tests get_dimension with incorrect input data.
    def test_get_dimension_incorrect(self):
        """ Tests get_dimension with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        dimension = rapid_array.get_dimensions(var_number)
        self.assertIsInstance(dimension, basestring)
        # Checks if wrong input.
        dimension = rapid_array.get_dimensions(10)
        self.assertIsInstance(dimension, Exception)

    # Tests edit_and_write_rapid_data_num_index with correct input data.
    def test_edit_and_write_rapid_data_num_index_correct(self):
        """ Tests edit_and_write_rapid_data_num_index with correct input data. """
        got_var, var_array = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_array')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        _ = rapid_array.edit_and_write_rapid_data_num_index(var_array, 0, 1)
        self.assertEqual(var_array.Value.ToString(), '[1,0,0]')

    # Tests edit_and_write_rapid_data_num_index with incorrect input data.
    def test_edit_and_write_rapid_data_num_index_incorrect(self):
        """ Tests edit_and_write_rapid_data_num_index with incorrect input data. """
        got_var, var_array = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_array')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        msg = rapid_array.edit_and_write_rapid_data_num_index(var_number, 0, 1)
        self.assertEqual(msg, 'Datatype is not array of num.')
        # Checks if wrong input data
        msg = rapid_array.edit_and_write_rapid_data_num_index(var_array, 'h', 1)
        self.assertEqual(msg, 'Index is not valid.')
        msg = rapid_array.edit_and_write_rapid_data_num_index(var_array, 0, 'h')
        self.assertEqual(msg, 'Value is not a number.')
        # Checks if wrong data is inserted into rapid data
        msg = rapid_array.edit_and_write_rapid_data_num_index(10, 0, 1)
        self.assertIsInstance(msg, Exception)
        # Checks if index is out of bounds.
        msg = rapid_array.edit_and_write_rapid_data_num_index(var_array, 10, 1)
        self.assertEqual(msg, 'Index is not valid.')

    # Tests edit_and_write_rapid_data_num with correct input data.
    def test_edit_and_write_rapid_data_num_correct(self):
        """ Tests edit_and_write_rapid_data_num with correct input data. """
        got_var, var_array = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_array')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Tests to write with array is not filled up.
        _ = rapid_array.edit_and_write_rapid_data_num(var_array, [1])
        self.assertEqual(var_array.Value.ToString(), '[1,0,0]')
        # Tests to write with full array.
        _ = rapid_array.edit_and_write_rapid_data_num(var_array, [1, 1, 1])
        self.assertEqual(var_array.Value.ToString(), '[1,1,1]')

    # Tests edit_and_write_rapid_data_num with incorrect input data.
    def test_edit_and_write_rapid_data_num_incorrect(self):
        """ Tests edit_and_write_rapid_data_num with incorrect input data. """
        got_var, var_array = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_array')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Tests if wrong rapid data.
        msg = rapid_array.edit_and_write_rapid_data_num(var_number, [1, 1])
        self.assertEqual(msg, 'Datatype is not array of num.')
        # Tests if list is too big compared to the one defined on controller.
        msg = rapid_array.edit_and_write_rapid_data_num(var_array, [1, 1, 1, 1])
        self.assertEqual(msg, 'Input list is larger than RAPID list.')
        # Tests if list contains wrong values
        msg = rapid_array.edit_and_write_rapid_data_num(var_array, [1, '2', True])
        self.assertEqual(msg, 'Something wrong in list.')
        # Checks if input is no list
        msg = rapid_array.edit_and_write_rapid_data_num(var_array, 10)
        self.assertEqual(msg, 'Values is not a list.')
        # Checks if rapid data is not inserted.
        msg = rapid_array.edit_and_write_rapid_data_num(10, [1, 1, 1])
        self.assertIsInstance(msg, Exception)
