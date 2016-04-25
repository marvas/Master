"""
Integration test to test rapid_robtarget functionality towards the virtual controller.
"""

import unittest
import sys

import frontendIronPy.com.communication as com
import frontendIronPy.user.user_authorization as user_auth
import frontendIronPy.user.user_mastership as user_mastership
import frontendIronPy.rapid.rapid_datatypes as rapid_datatypes
import frontendIronPy.rapid.rapid_robtarget as rapid_robtarget


class RapidRobtargetTest(unittest.TestCase):

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

        # Additional cleanup for some test cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests edit_and_write_rapid_data_property with correct input data.':
            got_var, var_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_rtarget')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'trans', '[10,10,10]')
            _ = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'rot', '[0,0,1,0]')
            _ = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'robconf', '[0,0,0,0]')
            _ = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'extax', '[9E9,9E9,9E9,9E9,9E9,9E9]')
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            got_var, var_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_rtarget')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_robtarget.edit_and_write_rapid_data(var_rtar, '[10,10,10]', '[0,0,1,0]',
                                                          '[0,0,0,0]', '[9E9,9E9,9E9,9E9,9E9,9E9]')
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()

        # Cleaning for all the test cases
        _, _ = user_auth.logoff_robot_controller(self.controller)
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests get_trans_tostring with correct input data.
    def test_get_trans_tostring_correct(self):
        """ Tests get_trans_tostring with correct input data. """
        got_var, const_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        trans = rapid_robtarget.get_trans_tostring(const_rtar)
        self.assertEqual(trans, 'Trans: [X,Y,Z] = [10,10,10]')

    # Tests get_trans_tostring with incorrect input data.
    def test_get_trans_tostring_incorrect(self):
        """ Tests get_trans_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        trans = rapid_robtarget.get_trans_tostring(const_number)
        self.assertEqual(trans, 'DataType is num and not robtarget.')
        # Checks if wrong data is inserted.
        trans = rapid_robtarget.get_trans_tostring(10)
        self.assertIsInstance(trans, Exception)

    # Tests get_rot_tostring with correct input data.
    def test_get_rot_tostring_correct(self):
        """ Tests get_rot_tostring with correct input data. """
        got_var, const_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        rot = rapid_robtarget.get_rot_tostring(const_rtar)
        self.assertEqual(rot, 'Rot: [Q1,Q2,Q3,Q4] = [0,0,1,0]')

    # Tests get_rot_tostring with incorrect input data.
    def test_get_rot_tostring_incorrect(self):
        """ Tests get_rot_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        rot = rapid_robtarget.get_rot_tostring(const_number)
        self.assertEqual(rot, 'DataType is num and not robtarget.')
        # Checks if wrong data is inserted.
        rot = rapid_robtarget.get_rot_tostring(10)
        self.assertIsInstance(rot, Exception)

    # Tests get_robconf_tostring with correct input data.
    def test_get_robconf_tostring_correct(self):
        """ Tests get_robconf_tostring with correct input data. """
        got_var, const_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        robconf = rapid_robtarget.get_robconf_tostring(const_rtar)
        self.assertEqual(robconf, 'Robconf: [Cf1,Cf4,Cf6,Cfx] = [0,0,0,0]')

    # Tests get_robconf_tostring with incorrect input data.
    def test_get_robconf_tostring_incorrect(self):
        """ Tests get_robconf_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        robconf = rapid_robtarget.get_robconf_tostring(const_number)
        self.assertEqual(robconf, 'DataType is num and not robtarget.')
        # Checks if wrong data is inserted.
        robconf = rapid_robtarget.get_robconf_tostring(10)
        self.assertIsInstance(robconf, Exception)

    # Tests get_extax_tostring with correct input data.
    def test_get_extax_tostring_correct(self):
        """ Tests get_extax_tostring with correct input data. """
        got_var, const_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        extax = rapid_robtarget.get_extax_tostring(const_rtar)
        self.assertEqual(extax, 'Extax: [Eax_a,Eax_b,Eax_c,Eax_d,Eax_e,Eax_f] = [9E9,9E9,9E9,9E9,9E9,9E9]')

    # Tests get_extax_tostring with incorrect input data.
    def test_get_extax_tostring_incorrect(self):
        """ Tests get_extax_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        extax = rapid_robtarget.get_extax_tostring(const_number)
        self.assertEqual(extax, 'DataType is num and not robtarget.')
        # Checks if wrong data is inserted.
        robconf = rapid_robtarget.get_robconf_tostring(10)
        self.assertIsInstance(robconf, Exception)

    # Tests get_robtarget_tostring with correct input data.
    def test_get_robtarget_tostring_correct(self):
        """ Tests get_robtarget_tostring with correct input data. """
        got_var, const_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        robtarget = rapid_robtarget.get_robtarget_tostring(const_rtar)
        self.assertEqual(robtarget, 'Robtarget: [[10,10,10],[0,0,1,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]]')

    # Tests get_robtarget_tostring with incorrect input data.
    def test_get_robtarget_tostring_incorrect(self):
        """ Tests get_robtarget_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        robtarget = rapid_robtarget.get_robtarget_tostring(const_number)
        self.assertEqual(robtarget, 'DataType is num and not robtarget.')
        # Checks if wrong data is inserted.
        robtarget = rapid_robtarget.get_robtarget_tostring(10)
        self.assertIsInstance(robtarget, Exception)

    # Tests edit_and_write_rapid_data_property with correct input data.
    def test_edit_and_write_rapid_data_property_correct(self):
        """ Tests edit_and_write_rapid_data_property with correct input data. """
        got_var, var_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if trans is updated
        _ = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'trans', '[0,0,0]')
        self.assertEqual(var_rtar.Value.Trans.ToString(), '[0,0,0]')
        # Checks if rot is updated
        _ = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'rot', '[1,0,0,0]')
        self.assertEqual(var_rtar.Value.Rot.ToString(), '[1,0,0,0]')
        # Checks if robconf is updated
        _ = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'robconf', '[0,1,0,0]')
        self.assertEqual(var_rtar.Value.Robconf.ToString(), '[0,1,0,0]')
        # Checks if extax is updated.
        _ = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'extax', '[0,0,0,0,0,0]')
        self.assertEqual(var_rtar.Value.Extax.ToString(), '[0,0,0,0,0,0]')

    # Tests edit_and_write_rapid_data_property with incorrect input data.
    def test_edit_and_write_rapid_data_property_incorrect(self):
        """ Tests edit_and_write_rapid_data_property with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        msg = rapid_robtarget.edit_and_write_rapid_data_property(var_number, 'trans', '[0,0,0]')
        self.assertEqual(msg, 'DataType is num and not robtarget.')
        # Checks if wrong property name is inserted
        msg = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 't', '[0,0,0]')
        self.assertEqual(msg, 'Property not of type trans, rot, robconf or extax.')
        # Checks if wrong data is inserted in property
        msg = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 10, '[0,0,0]')
        self.assertIsInstance(msg, Exception)
        # Checks if rapid data is not inserted.
        msg = rapid_robtarget.edit_and_write_rapid_data_property(10, 'trans', '[0,0,0]')
        self.assertIsInstance(msg, Exception)
        # Checks if trans is not valid.
        msg = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'trans', '[0,0]')
        self.assertEqual(msg, 'Incorrect format of x,y,z: ex. \'10,50,0\'.')
        # Checks if rot is not valid.
        msg = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'rot', '[0,0]')
        self.assertEqual(msg, 'Incorrect format of q1,q2,q3,q4: ex. \'0,0,1,0\'.')
        # Checks if robconf is not valid.
        msg = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'robconf', '[0,0]')
        self.assertEqual(msg, 'Incorrect format of Cf1,Cf4,Cf6,Cfx: ex. \'1,0,1,0\'.')
        # Checks if extax is not valid.
        msg = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'extax', '[0,0]')
        self.assertEqual(msg, 'Incorrect format of Eax_a,Eax_b,Eax_c,Eax_d,Eax_e,Eax_f: '
                              'ex \'9E9,9E9,9E9,9E9,9E9,9E9\'.')
        # Check if new value is not string.
        msg = rapid_robtarget.edit_and_write_rapid_data_property(var_rtar, 'extax', 10)
        self.assertEqual(msg, 'Input is not string.')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        got_var, var_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        _ = rapid_robtarget.edit_and_write_rapid_data(var_rtar, '[0,0,0]', '[1,0,0,0]', '[0,1,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(var_rtar.Value.ToString(), '[[0,0,0],[1,0,0,0],[0,1,0,0],[0,0,0,0,0,0]]')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_rtar = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Check if wrong rapid data is inserted.
        msg = rapid_robtarget.edit_and_write_rapid_data(var_number, '[0,0,0]', '[0,0,0,0]', '[0,0,0,0]',
                                                        '[0,0,0,0,0,0]')
        self.assertEqual(msg, 'DataType is num and not robtarget.')
        # Check if wrong trans, rot, robconf and extax is inserted.
        msg = rapid_robtarget.edit_and_write_rapid_data(var_rtar, '[0,0]', '[0,0,0,0]', '[0,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_robtarget.edit_and_write_rapid_data(var_rtar, '[0,0,0]', '[0,0,0]', '[0,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_robtarget.edit_and_write_rapid_data(var_rtar, '[0,0,0]', '[0,0,0,0]', '[0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_robtarget.edit_and_write_rapid_data(var_rtar, '[0,0,0]', '[0,0,0,0]', '[0,0,0,0]', '[0,0,0,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        # Check if wrong data is inserted instead of rapid data.
        msg = rapid_robtarget.edit_and_write_rapid_data(10, '[0,0,0]', '[0,0,0,0]', '[0,0,0,0]', '[0,0,0,0,0]')
        self.assertIsInstance(msg, Exception)
        # Checks if wrong data is inserted into trans.
        msg = rapid_robtarget.edit_and_write_rapid_data(var_rtar, 10, '[0,0,0,0]', '[0,0,0,0]', '[0,0,0,0,0]')
        self.assertEqual(msg, 'Input is not string.')
