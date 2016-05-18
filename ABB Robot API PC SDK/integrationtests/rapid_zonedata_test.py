"""
Integration test to test rapid_zonedata functionality towards the virtual controller.
"""

import unittest
import sys

import frontendPCSDK.com.communication as com
import frontendPCSDK.user.user_authorization as user_auth
import frontendPCSDK.user.user_mastership as user_mastership
import frontendPCSDK.rapid.rapid_datatypes as rapid_datatypes
import frontendPCSDK.rapid.rapid_zonedata as rapid_zonedata


class RapidZonedataTest(unittest.TestCase):

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
            got_var, var_bzone = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_basezone')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_zonedata.edit_and_write_rapid_data_base(var_bzone, 'z0')
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            got_var, var_zone = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_zone')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_zonedata.edit_and_write_rapid_data(var_zone, False, 0.3, 0.3, 0.3, 0.5, 0.3, 0.5)
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()

        # Cleaning for all the test cases
        _, _ = user_auth.logoff_robot_controller(self.controller)
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests get_zonedata_tostring with correct input data.
    def test_get_zonedata_tostring_correct(self):
        """ Tests get_zonedata_tostring with correct input data. """
        got_var, const_bzone = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_basezone')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, const_zone = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_zone')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks base zonedata
        bzone = rapid_zonedata.get_zonedata_tostring(const_bzone)
        self.assertEqual(bzone, 'Base zonedata: z0 ([False,0.3,0.3,0.3,0.03,0.3,0.03])')
        # Checks zonedata
        zone = rapid_zonedata.get_zonedata_tostring(const_zone)
        self.assertEqual(zone, 'Zonedata: [False,0.3,0.3,0.3,0.5,0.3,0.5]')

    # Tests get_zonedata_tostring with incorrect input data.
    def test_get_zonedata_tostring_incorrect(self):
        """ Tests get_zonedata_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        zone = rapid_zonedata.get_zonedata_tostring(const_number)
        self.assertEqual(zone, 'DataType is num and not zonedata.')
        # Checks if wrong data is inserted.
        zone = rapid_zonedata.get_zonedata_tostring(10)
        self.assertIsInstance(zone, Exception)

    # Tests edit_and_write_rapid_data_base with correct input data.
    def test_edit_and_write_rapid_data_base_correct(self):
        """ Tests edit_and_write_rapid_data_base with correct input data. """
        got_var, var_bzone = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_basezone')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        _ = rapid_zonedata.edit_and_write_rapid_data_base(var_bzone, 'z10')
        self.assertEqual(var_bzone.Value.ToString(), '[False,10,15,15,1.5,15,1.5]')

    # Tests edit_and_write_rapid_data_base with incorrect input data.
    def test_edit_and_write_rapid_data_base_incorrect(self):
        """ Tests edit_and_write_rapid_data_base with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_bzone = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_basezone')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        zone = rapid_zonedata.edit_and_write_rapid_data_base(var_number, 'z10')
        self.assertEqual(zone, 'DataType is num and not zonedata.')
        # Checks if wrong zonedata is inserted.
        zone = rapid_zonedata.edit_and_write_rapid_data_base(var_bzone, 10)
        self.assertEqual(zone, 'Input has to be string. (ex. \'z1\')')
        # Checks if wrong data is inserted.
        zone = rapid_zonedata.edit_and_write_rapid_data_base(10, 'z10')
        self.assertIsInstance(zone, Exception)
        # Checks if zonedata is not valid.
        zone = rapid_zonedata.edit_and_write_rapid_data_base(var_bzone, '10')
        self.assertEqual(zone, 'Something wrong with the input. Not in format \'z1\'')
        # Checks if not base zonedata
        zone = rapid_zonedata.edit_and_write_rapid_data_base(var_bzone, 'z350')
        self.assertEqual(zone, 'Something wrong with the input format, or the input is not a valid base zone.')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        got_var, var_zone = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_zone')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        _ = rapid_zonedata.edit_and_write_rapid_data(var_zone, True, 1, 1, 1, 0.5, 1, 0.5)
        self.assertEqual(var_zone.Value.ToString(), '[True,1,1,1,0.5,1,0.5]')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_zone = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_zone')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        zone = rapid_zonedata.edit_and_write_rapid_data(var_number, True, 1, 1, 1, 0.5, 1, 0.5)
        self.assertEqual(zone, 'DataType is num and not zonedata.')
        # Checks if wrong data is inserted.
        zone = rapid_zonedata.edit_and_write_rapid_data(10, True, 1, 1, 1, 0.5, 1, 0.5)
        self.assertIsInstance(zone, Exception)
        # Checks if wrong data is inserted into values
        zone = rapid_zonedata.edit_and_write_rapid_data(var_zone, 10, 1, 1, 1, 0.5, 1, 0.5)
        self.assertEqual(zone, 'Invalid input in one or more of the arguments.')
        zone = rapid_zonedata.edit_and_write_rapid_data(var_zone, True, 'h', 1, 1, 0.5, 1, 0.5)
        self.assertEqual(zone, 'Invalid input in one or more of the arguments.')
        zone = rapid_zonedata.edit_and_write_rapid_data(var_zone, True, 1, 'h', 1, 0.5, 1, 0.5)
        self.assertEqual(zone, 'Invalid input in one or more of the arguments.')
        zone = rapid_zonedata.edit_and_write_rapid_data(var_zone, True, 1, 1, 'h', 0.5, 1, 0.5)
        self.assertEqual(zone, 'Invalid input in one or more of the arguments.')
        zone = rapid_zonedata.edit_and_write_rapid_data(var_zone, True, 1, 1, 1, 'h', 1, 0.5)
        self.assertEqual(zone, 'Invalid input in one or more of the arguments.')
        zone = rapid_zonedata.edit_and_write_rapid_data(var_zone, True, 1, 1, 0.5, 'h', 1, 0.5)
        self.assertEqual(zone, 'Invalid input in one or more of the arguments.')
        zone = rapid_zonedata.edit_and_write_rapid_data(var_zone, True, 1, 1, 0.5, 0.5, 'h', 0.5)
        self.assertEqual(zone, 'Invalid input in one or more of the arguments.')
        zone = rapid_zonedata.edit_and_write_rapid_data(var_zone, True, 1, 1, 0.5, 0.5, 1, 'h')
        self.assertEqual(zone, 'Invalid input in one or more of the arguments.')
