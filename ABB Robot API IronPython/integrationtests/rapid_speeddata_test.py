"""
Integration test to test rapid_robtarget functionality towards the virtual controller.
"""

import unittest
import sys

import frontendIronPy.com.communication as com
import frontendIronPy.user.user_authorization as user_auth
import frontendIronPy.user.user_mastership as user_mastership
import frontendIronPy.rapid.rapid_datatypes as rapid_datatypes
import frontendIronPy.rapid.rapid_speeddata as rapid_speeddata


class RapidSpeeddataTest(unittest.TestCase):

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
        if test_desc == 'Tests edit_and_write_rapid_data_base with correct input data.':
            is_master, _, self.mastership = user_mastership.get_master_access_to_controller_rapid(self.controller)
            if not is_master:
                print 'Couldn\'t get mastership. Test will not run.'
                sys.exit()
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            is_master, _, self.mastership = user_mastership.get_master_access_to_controller_rapid(self.controller)
            if not is_master:
                print 'Couldn\'t get mastership. Test will not run.'
                sys.exit()

    # Ending test
    def tearDown(self):
        """ Cleaning after test """

        # Additional cleaning after some test cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests edit_and_write_rapid_data_base with correct input data.':
            got_var, var_bspeed = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule',
                                                                 'var_basespeed')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_speeddata.edit_and_write_rapid_data_base(var_bspeed, 'v10')
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            got_var, var_speed = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_speed')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_speeddata.edit_and_write_rapid_data(var_speed, 20, 1000, 5000, 1000)
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()

        # Cleaning for all the test cases
        _, _ = user_auth.logoff_robot_controller(self.controller)
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests get_speeddata_tostring with correct input data.
    def test_get_speeddata_tostring_correct(self):
        """ Tests get_speeddata_tostring with correct input data. """
        got_var, const_bspeed = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule',
                                                               'const_basespeed')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, const_speed = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_speed')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks base speeddata
        bspeed = rapid_speeddata.get_speeddata_tostring(const_bspeed)
        self.assertEqual(bspeed, 'Base speeddata: v10 ([10,500,5000,1000])')
        # Checks speeddata
        speed = rapid_speeddata.get_speeddata_tostring(const_speed)
        self.assertEqual(speed, 'Speeddata: [20,1000,5000,1000]')

    # Tests get_speeddata_tostring with incorrect input data.
    def test_get_speeddata_tostring_incorrect(self):
        """ Tests get_speeddata_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        speed = rapid_speeddata.get_speeddata_tostring(const_number)
        self.assertEqual(speed, 'DataType is num and not speeddata.')
        # Checks if wrong data is inserted.
        speed = rapid_speeddata.get_speeddata_tostring(10)
        self.assertIsInstance(speed, Exception)

    # Tests edit_and_write_rapid_data_base with correct input data.
    def test_edit_and_write_rapid_data_base_correct(self):
        """ Tests edit_and_write_rapid_data_base with correct input data. """
        got_var, var_bspeed = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_basespeed')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        _ = rapid_speeddata.edit_and_write_rapid_data_base(var_bspeed, 'v100')
        self.assertEqual(var_bspeed.Value.ToString(), '[100,500,5000,1000]')

    # Tests edit_and_write_rapid_data_base with incorrect input data.
    def test_edit_and_write_rapid_data_base_incorrect(self):
        """ Tests edit_and_write_rapid_data_base with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_bspeed = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_basespeed')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        speed = rapid_speeddata.edit_and_write_rapid_data_base(var_number, 'v100')
        self.assertEqual(speed, 'DataType is num and not speeddata.')
        # Checks if wrong speeddata is inserted.
        speed = rapid_speeddata.edit_and_write_rapid_data_base(var_bspeed, 10)
        self.assertEqual(speed, 'Input has to be string. (ex. \'v100\')')
        # Checks if wrong data is inserted.
        speed = rapid_speeddata.edit_and_write_rapid_data_base(10, 'v100')
        self.assertIsInstance(speed, Exception)
        # Checks if speeddata is not valid.
        speed = rapid_speeddata.edit_and_write_rapid_data_base(var_bspeed, '100')
        self.assertEqual(speed, 'Something wrong with the input. Not in format \'v100\'')
        # Checks if not base speeddata
        speed = rapid_speeddata.edit_and_write_rapid_data_base(var_bspeed, 'v350')
        self.assertEqual(speed, 'Something wrong with the input format, or the input is not a valid base speed.')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        got_var, var_speed = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_speed')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        _ = rapid_speeddata.edit_and_write_rapid_data(var_speed, 25, 400, 1000, 300)
        self.assertEqual(var_speed.Value.ToString(), '[25,400,1000,300]')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_speed = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_speed')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        speed = rapid_speeddata.edit_and_write_rapid_data(var_number, 20, 20, 20, 20)
        self.assertEqual(speed, 'DataType is num and not speeddata.')
        # Checks if wrong data is inserted.
        speed = rapid_speeddata.edit_and_write_rapid_data(10, 20, 20, 20, 20)
        self.assertIsInstance(speed, Exception)
        # Checks if wrong data is inserted into values
        speed = rapid_speeddata.edit_and_write_rapid_data(var_speed, 'h', 20, 20, 20)
        self.assertEqual(speed, 'Invalid input in one or more of the arguments')
        speed = rapid_speeddata.edit_and_write_rapid_data(var_speed, 20, 'h', 20, 20)
        self.assertEqual(speed, 'Invalid input in one or more of the arguments')
        speed = rapid_speeddata.edit_and_write_rapid_data(var_speed, 20, 20, 'h', 20)
        self.assertEqual(speed, 'Invalid input in one or more of the arguments')
        speed = rapid_speeddata.edit_and_write_rapid_data(var_speed, 20, 20, 20, 'h')
        self.assertEqual(speed, 'Invalid input in one or more of the arguments')
