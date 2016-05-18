"""
Integration test to test rapid_tooldata functionality towards the virtual controller.
"""

import unittest
import sys

import frontendIronPy.com.communication as com
import frontendIronPy.user.user_authorization as user_auth
import frontendIronPy.user.user_mastership as user_mastership
import frontendIronPy.rapid.rapid_datatypes as rapid_datatypes
import frontendIronPy.rapid.rapid_tooldata as rapid_tooldata


class RapidTooldataTest(unittest.TestCase):

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
            got_var, var_tool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_tool')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'robhold', True)
            _ = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'tframe', '[10,10,10],[0,0,1,0]')
            _ = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'tload', '1,[0,0,1],[1,0,0,0],0,0,0]')
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            got_var, var_tool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_tool')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_tooldata.edit_and_write_rapid_data(var_tool, True, '[10,10,10],[0,0,1,0]',
                                                         '[1,[0,0,1],[1,0,0,0],0,0,0]]')
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()

        # Cleaning for all the test cases
        _, _ = user_auth.logoff_robot_controller(self.controller)
        _, _ = com.disconnect_robot_controller(self.controller)

    # Tests get_robhold_tostring with correct input data.
    def test_get_robhold_tostring_correct(self):
        """ Tests get_robhold_tostring with correct input data. """
        got_var, const_tool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        robhold = rapid_tooldata.get_robhold_tostring(const_tool)
        self.assertEqual(robhold, 'Robhold = True')

    # Tests get_robhold_tostring with incorrect input data.
    def test_get_robhold_tostring_incorrect(self):
        """ Tests get_robhold_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        robhold = rapid_tooldata.get_robhold_tostring(const_number)
        self.assertEqual(robhold, 'DataType is num and not tooldata.')
        # Checks if wrong data is inserted.
        robhold = rapid_tooldata.get_robhold_tostring(10)
        self.assertIsInstance(robhold, Exception)

    # Tests get_tframe_tostring with correct input data.
    def test_get_tframe_tostring_correct(self):
        """ Tests get_tframe_tostring with correct input data. """
        got_var, const_tool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        tframe = rapid_tooldata.get_tframe_tostring(const_tool)
        self.assertEqual(tframe, 'Tframe: [Trans,Rot] = [[10,10,10],[0,0,1,0]]')

    # Tests get_tframe_tostring with incorrect input data.
    def test_get_tframe_tostring_incorrect(self):
        """ Tests get_tframe_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        tframe = rapid_tooldata.get_tframe_tostring(const_number)
        self.assertEqual(tframe, 'DataType is num and not tooldata.')
        # Checks if wrong data is inserted.
        tframe = rapid_tooldata.get_tframe_tostring(10)
        self.assertIsInstance(tframe, Exception)

    # Tests get_tload_tostring with correct input data.
    def test_get_tload_tostring_correct(self):
        """ Tests get_tload_tostring with correct input data. """
        got_var, const_tool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        tload = rapid_tooldata.get_tload_tostring(const_tool)
        self.assertEqual(tload, 'Tload: [Mass,Cog,Aom,Ix,Iy,Iz] = [1,[0,0,1],[1,0,0,0],0,0,0]')

    # Tests get_tload_tostring with incorrect input data.
    def test_get_tload_tostring_incorrect(self):
        """ Tests get_tload_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        tload = rapid_tooldata.get_tload_tostring(const_number)
        self.assertEqual(tload, 'DataType is num and not tooldata.')
        # Checks if wrong data is inserted.
        tload = rapid_tooldata.get_tload_tostring(10)
        self.assertIsInstance(tload, Exception)

    # Tests get_tooldata_tostring with correct input data.
    def test_get_tooldata_tostring_correct(self):
        """ Tests get_tooldata_tostring with correct input data. """
        got_var, const_tool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        tooldata = rapid_tooldata.get_tooldata_tostring(const_tool)
        self.assertEqual(tooldata, 'Tooldata: [TRUE,[[10,10,10],[0,0,1,0]],[1,[0,0,1],[1,0,0,0],0,0,0]]')

    # Tests get_tooldata_tostring with incorrect input data.
    def test_get_tooldata_tostring_incorrect(self):
        """ Tests get_tooldata_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        tooldata = rapid_tooldata.get_tooldata_tostring(const_number)
        self.assertEqual(tooldata, 'DataType is num and not tooldata.')
        # Checks if wrong data is inserted.
        tooldata = rapid_tooldata.get_tooldata_tostring(10)
        self.assertIsInstance(tooldata, Exception)

    # Tests edit_and_write_rapid_data_property with correct input data.
    def test_edit_and_write_rapid_data_property_correct(self):
        """ Tests edit_and_write_rapid_data_property with correct input data. """
        got_var, var_tool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if robhold is updated.
        _ = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'robhold', False)
        self.assertFalse(var_tool.Value.Robhold)
        # Checks if tframe is updated.
        _ = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'tframe', '[0,0,0],[1,0,0,0]')
        self.assertEqual(var_tool.Value.Tframe.ToString(), '[[0,0,0],[1,0,0,0]]')
        # Checks if tload is updated.
        _ = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'tload', '[0,[1,0,0],[0,0,1,0],1,1,1]')
        self.assertEqual(var_tool.Value.Tload.ToString(), '[0,[1,0,0],[0,0,1,0],1,1,1]')

    # Tests edit_and_write_rapid_data_property with incorrect input data.
    def test_edit_and_write_rapid_data_property_incorrect(self):
        """ Tests edit_and_write_rapid_data_property with incorrect input data. """
        got_var, var_tool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        msg = rapid_tooldata.edit_and_write_rapid_data_property(var_number, 'robhold', False)
        self.assertEqual(msg, 'DataType is num and not tooldata.')
        # Checks if wrong data is inserted into rapid data.
        msg = rapid_tooldata.edit_and_write_rapid_data_property(10, 'robhold', False)
        self.assertIsInstance(msg, Exception)
        # Checks if wrong property is specified.
        msg = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'r', False)
        self.assertEqual(msg, 'Property not of type robhold, tframe, tload.')
        # Checks if wrong data is inserted into property.
        msg = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 10, False)
        self.assertIsInstance(msg, Exception)
        # Checks if wrong data in new value
        msg = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'robhold', 10)
        self.assertEqual(msg, 'Input is not boolean.')
        msg = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'tframe', 10)
        self.assertEqual(msg, 'Input is not string.')
        msg = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'tload', 10)
        self.assertEqual(msg, 'Input is not string.')
        # Checks if format of new value is incorrect
        msg = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'tframe', '10')
        self.assertEqual(msg, 'Input is not a valid Tframe.')
        msg = rapid_tooldata.edit_and_write_rapid_data_property(var_tool, 'tload', '10')
        self.assertEqual(msg, 'Input is not a valid Tload.')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        got_var, var_tool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        _ = rapid_tooldata.edit_and_write_rapid_data(var_tool, False, '[0,0,0],[1,0,0,0]',
                                                     '[0,[1,0,0],[0,0,1,0],1,1,1]')
        self.assertEqual(var_tool.Value.ToString(), '[FALSE,[[0,0,0],[1,0,0,0]],[0,[1,0,0],[0,0,1,0],1,1,1]]')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_tool = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Check if wrong rapid data is inserted.
        msg = rapid_tooldata.edit_and_write_rapid_data(var_number, False, '[0,0,0],[1,0,0,0]',
                                                       '[0,[1,0,0],[0,0,1,0],1,1,1]')
        self.assertEqual(msg, 'DataType is num and not tooldata.')
        # Checks if wrong data is inserted into rapid data.
        msg = rapid_tooldata.edit_and_write_rapid_data(10, False, '[0,0,0],[1,0,0,0]',
                                                       '[0,[1,0,0],[0,0,1,0],1,1,1]')
        self.assertIsInstance(msg, Exception)
        # Checks if wrong value is inserted into properties.
        msg = rapid_tooldata.edit_and_write_rapid_data(var_tool, 10, '[0,0,0],[1,0,0,0]',
                                                       '[0,[1,0,0],[0,0,1,0],1,1,1]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_tooldata.edit_and_write_rapid_data(var_tool, False, 10, '[0,[1,0,0],[0,0,1,0],1,1,1]')
        self.assertEqual(msg, 'Input is not string.')
        msg = rapid_tooldata.edit_and_write_rapid_data(var_tool, False, '[0,0,0],[1,0,0,0]', 10)
        self.assertEqual(msg, 'Input is not string.')
        # Checks if new value is incorrect
        msg = rapid_tooldata.edit_and_write_rapid_data(var_tool, False, '[0,0,0]', '[0,[1,0,0],[0,0,1,0],1,1,1]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_tooldata.edit_and_write_rapid_data(var_tool, False, '[0,0,0],[1,0,0,0]', '[0,0,1]')
        self.assertEqual(msg, 'Incorrect format of input data.')
