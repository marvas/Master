"""
Integration test to test rapid_jointtarget functionality towards the virtual controller.
"""

import unittest
import sys

import frontendIronPy.com.communication as com
import frontendIronPy.user.user_authorization as user_auth
import frontendIronPy.user.user_mastership as user_mastership
import frontendIronPy.rapid.rapid_datatypes as rapid_datatypes
import frontendIronPy.rapid.rapid_jointtarget as rapid_jointtarget


class RapidJointtargetTest(unittest.TestCase):

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
        if test_desc == 'Tests edit_and_write_rapid_data_property with correct input data.':
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
        if test_desc == 'Tests edit_and_write_rapid_data_property with correct input data.':
            got_var, var_jtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_jtarget')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_jointtarget.edit_and_write_rapid_data_property(var_jtar, 'robax', '[0,0,0,10,0,0]')
            _ = rapid_jointtarget.edit_and_write_rapid_data_property(var_jtar, 'extax', '[9E9,9E9,9E9,9E9,9E9,9E9]')
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            got_var, var_jtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_jtarget')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_jointtarget.edit_and_write_rapid_data(var_jtar, '[0,0,0,10,0,0]', '[9E9,9E9,9E9,9E9,9E9,9E9]')
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()

        # Cleaning for all the test cases
        _, _ = user_auth.logoff_robot_controller(self.controller)
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests get_robax_tostring with correct input data.
    def test_get_robax_tostring_correct(self):
        """ Tests get_robax_tostring with correct input data. """
        got_var, const_jtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_jtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        robax = rapid_jointtarget.get_robax_tostring(const_jtar)
        self.assertEqual(robax, 'RobAx: [Rax_1,Rax_2,Rax_3,Rax_4,Rax_5,Rax_6] = [0,0,0,10,0,0]')

    # Tests get_robax_tostring with incorrect input data.
    def test_get_robax_tostring_incorrect(self):
        """ Tests get_robax_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        robax = rapid_jointtarget.get_robax_tostring(const_number)
        self.assertEqual(robax, 'DataType is num and not jointtarget.')
        # Checks if wrong data is inserted.
        robax = rapid_jointtarget.get_robax_tostring(10)
        self.assertIsInstance(robax, Exception)

    # Tests get_extax_tostring with correct input data.
    def test_get_extax_tostring_correct(self):
        """ Tests get_extax_tostring with correct input data. """
        got_var, const_jtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_jtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        extax = rapid_jointtarget.get_extax_tostring(const_jtar)
        self.assertEqual(extax, 'Extax: [Eax_a,Eax_b,Eax_c,Eax_d,Eax_e,Eax_f] = [9E9,9E9,9E9,9E9,9E9,9E9]')

    # Tests get_extax_tostring with incorrect input data.
    def test_get_extax_tostring_incorrect(self):
        """ Tests get_extax_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        extax = rapid_jointtarget.get_extax_tostring(const_number)
        self.assertEqual(extax, 'DataType is num and not jointtarget.')
        # Checks if wrong data is inserted.
        extax = rapid_jointtarget.get_extax_tostring(10)
        self.assertIsInstance(extax, Exception)

    # Tests get_jointtarget_tostring with correct input data.
    def test_get_jointtarget_tostring_correct(self):
        """ Tests get_jointtarget_tostring with correct input data. """
        got_var, const_jtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_jtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        jointtarget = rapid_jointtarget.get_jointtarget_tostring(const_jtar)
        self.assertEqual(jointtarget, 'Jointtarget: [[0,0,0,10,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]]')

    # Tests get_jointtarget_tostring with incorrect input data.
    def test_get_jointtarget_tostring_incorrect(self):
        """ Tests get_jointtarget_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        jointtarget = rapid_jointtarget.get_jointtarget_tostring(const_number)
        self.assertEqual(jointtarget, 'DataType is num and not jointtarget.')
        # Checks if wrong data is inserted.
        jointtarget = rapid_jointtarget.get_jointtarget_tostring(10)
        self.assertIsInstance(jointtarget, Exception)

    # Tests edit_and_write_rapid_data_property with correct input data.
    def test_edit_and_write_rapid_data_property_correct(self):
        """ Tests edit_and_write_rapid_data_property with correct input data. """
        got_var, var_jtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_jtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if updating robax works.
        _ = rapid_jointtarget.edit_and_write_rapid_data_property(var_jtar, 'robax', '[0,0,0,0,0,0]')
        self.assertEqual(var_jtar.Value.RobAx.ToString(), '[0,0,0,0,0,0]')
        # Checks if updating extax works.
        _ = rapid_jointtarget.edit_and_write_rapid_data_property(var_jtar, 'extax', '[0,0,0,0,0,0]')
        self.assertEqual(var_jtar.Value.ExtAx.ToString(), '[0,0,0,0,0,0]')

    # Tests edit_and_write_rapid_data_property with incorrect input data.
    def test_edit_and_write_rapid_data_property_incorrect(self):
        """ Tests edit_and_write_rapid_data_property with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_jtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_jtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        msg = rapid_jointtarget.edit_and_write_rapid_data_property(var_number, 'robax', '[0,0,0,0,0,0]')
        self.assertEqual(msg, 'DataType is num and not jointtarget.')
        # Checks if wrong property name is inserted
        msg = rapid_jointtarget.edit_and_write_rapid_data_property(var_jtar, 'r', '[0,0,0,0,0,0]')
        self.assertEqual(msg, 'Incorrect property.')
        # Checks if wrong data is inserted in property
        msg = rapid_jointtarget.edit_and_write_rapid_data_property(var_jtar, 10, '[0,0,0,0,0,0]')
        self.assertIsInstance(msg, Exception)
        # Checks if rapid data is not inserted.
        msg = rapid_jointtarget.edit_and_write_rapid_data_property(10, 'robax', '[0,0,0,0,0,0]')
        self.assertIsInstance(msg, Exception)
        # Checks if robax is not valid.
        msg = rapid_jointtarget.edit_and_write_rapid_data_property(var_jtar, 'robax', '[0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        # Checks if extax is not valid.
        msg = rapid_jointtarget.edit_and_write_rapid_data_property(var_jtar, 'extax', '[0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        # Check if new value is not string.
        msg = rapid_jointtarget.edit_and_write_rapid_data_property(var_jtar, 'extax', 10)
        self.assertEqual(msg, 'Input is not string.')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        got_var, var_jtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_jtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        _ = rapid_jointtarget.edit_and_write_rapid_data(var_jtar, '[0,0,0,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(var_jtar.Value.ToString(), '[[0,0,0,0,0,0],[0,0,0,0,0,0]]')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_jtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_jtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Check if wrong rapid data is inserted.
        msg = rapid_jointtarget.edit_and_write_rapid_data(var_number, '[0,0,0,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(msg, 'DataType is num and not jointtarget.')
        # Check if wrong robax and extax is inserted.
        msg = rapid_jointtarget.edit_and_write_rapid_data(var_jtar, '[0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_jointtarget.edit_and_write_rapid_data(var_jtar, '[0,0,0,0,0,0]', '[0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        # Check if wrong data is inserted instead of rapid data.
        msg = rapid_jointtarget.edit_and_write_rapid_data(10, '[0,0,0,0,0,0]', '[0,0,0,0,0,0]')
        self.assertIsInstance(msg, Exception)
        # Checks if wrong data is inserted into robax.
        msg = rapid_jointtarget.edit_and_write_rapid_data(var_jtar, 10, '[0,0,0,0,0,0]')
        self.assertEqual(msg, 'Input is not string.')
