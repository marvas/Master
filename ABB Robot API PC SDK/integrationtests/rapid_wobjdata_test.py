"""
Integration test to test rapid_wobjdata functionality towards the virtual controller.
"""

import unittest
import sys

import frontendPCSDK.com.communication as com
import frontendPCSDK.user.user_authorization as user_auth
import frontendPCSDK.user.user_mastership as user_mastership
import frontendPCSDK.rapid.rapid_datatypes as rapid_datatypes
import frontendPCSDK.rapid.rapid_wobjdata as rapid_wobjdata


class RapidWobjdataTest(unittest.TestCase):

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

        # Additional cleanup after some test cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests edit_and_write_rapid_data_property with correct input data.':
            got_var, var_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_wobj')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'robhold', False)
            _ = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'ufprog', True)
            _ = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'ufmec', '')
            _ = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'uframe', '[10,10,10],[1,0,0,0]')
            _ = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'oframe', '[10,10,10],[1,0,0,0]')
            is_released, _ = user_mastership.release_and_dispose_master_access(self.mastership)
            if not is_released:
                print 'Couldn\'t release mastership. Test will not run.'
                sys.exit()
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            got_var, var_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_wobj')
            if not got_var:
                print 'Couldn\'t get variable. Test will not run.'
                sys.exit()
            _ = rapid_wobjdata.edit_and_write_rapid_data(var_wobj, False, True, '', '[10,10,10],[1,0,0,0]',
                                                         '[10,10,10],[1,0,0,0]')
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
        got_var, const_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        robhold = rapid_wobjdata.get_robhold_tostring(const_wobj)
        self.assertEqual(robhold, 'Robhold = False')

    # Tests get_robhold_tostring with incorrect input data.
    def test_get_robhold_tostring_incorrect(self):
        """ Tests get_robhold_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        robhold = rapid_wobjdata.get_robhold_tostring(const_number)
        self.assertEqual(robhold, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        robhold = rapid_wobjdata.get_robhold_tostring(10)
        self.assertIsInstance(robhold, Exception)

    # Tests get_ufprog_tostring with correct input data.
    def test_get_ufprog_tostring_correct(self):
        """ Tests get_ufprog_tostring with correct input data. """
        got_var, const_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        ufprog = rapid_wobjdata.get_ufprog_tostring(const_wobj)
        self.assertEqual(ufprog, 'Ufprog = True')

    # Tests get_ufprog_tostring with incorrect input data.
    def test_get_ufprog_tostring_incorrect(self):
        """ Tests get_ufprog_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        ufprog = rapid_wobjdata.get_ufprog_tostring(const_number)
        self.assertEqual(ufprog, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        ufprog = rapid_wobjdata.get_ufprog_tostring(10)
        self.assertIsInstance(ufprog, Exception)

    # Tests get_ufmec_tostring with correct input data.
    def test_get_ufmec_tostring_correct(self):
        """ Tests get_ufmec_tostring with correct input data. """
        got_var, const_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        ufmec = rapid_wobjdata.get_ufmec_tostring(const_wobj)
        self.assertEqual(ufmec, 'Ufmec = ')

    # Tests get_ufmec_tostring with incorrect input data.
    def test_get_ufmec_tostring_incorrect(self):
        """ Tests get_ufmec_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        ufmec = rapid_wobjdata.get_ufmec_tostring(const_number)
        self.assertEqual(ufmec, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        ufmec = rapid_wobjdata.get_ufmec_tostring(10)
        self.assertIsInstance(ufmec, Exception)

    # Tests get_uframe_tostring with correct input data.
    def test_get_uframe_tostring_correct(self):
        """ Tests get_uframe_tostring with correct input data. """
        got_var, const_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        uframe = rapid_wobjdata.get_uframe_tostring(const_wobj)
        self.assertEqual(uframe, 'Uframe: [Trans,Rot] = [[10,10,10],[1,0,0,0]]')

    # Tests get_uframe_tostring with incorrect input data.
    def test_get_uframe_tostring_incorrect(self):
        """ Tests get_uframe_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        uframe = rapid_wobjdata.get_uframe_tostring(const_number)
        self.assertEqual(uframe, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        uframe = rapid_wobjdata.get_uframe_tostring(10)
        self.assertIsInstance(uframe, Exception)

    # Tests get_oframe_tostring with correct input data.
    def test_get_oframe_tostring_correct(self):
        """ Tests get_oframe_tostring with correct input data. """
        got_var, const_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        oframe = rapid_wobjdata.get_oframe_tostring(const_wobj)
        self.assertEqual(oframe, 'Oframe: [Trans,Rot] = [[10,10,10],[1,0,0,0]]')

    # Tests get_oframe_tostring with incorrect input data.
    def test_get_oframe_tostring_incorrect(self):
        """ Tests get_oframe_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        oframe = rapid_wobjdata.get_oframe_tostring(const_number)
        self.assertEqual(oframe, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        oframe = rapid_wobjdata.get_oframe_tostring(10)
        self.assertIsInstance(oframe, Exception)

    # Tests get_wobjdata_tostring with correct input data.
    def test_get_wobjdata_tostring_correct(self):
        """ Tests get_wobjdata_tostring with correct input data. """
        got_var, const_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        wobjdata = rapid_wobjdata.get_wobjdata_tostring(const_wobj)
        self.assertEqual(wobjdata, 'Wobjdata: [FALSE,TRUE,"",[[10,10,10],[1,0,0,0]],[[10,10,10],[1,0,0,0]]]')

    # Tests get_wobjdata_tostring with incorrect input data.
    def test_get_wobjdata_tostring_incorrect(self):
        """ Tests get_wobjdata_tostring with incorrect input data. """
        got_var, const_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        wobjdata = rapid_wobjdata.get_wobjdata_tostring(const_number)
        self.assertEqual(wobjdata, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        wobjdata = rapid_wobjdata.get_wobjdata_tostring(10)
        self.assertIsInstance(wobjdata, Exception)

    # Tests edit_and_write_rapid_data_property with correct input data.
    def test_edit_and_write_rapid_data_property_correct(self):
        """ Tests edit_and_write_rapid_data_property with correct input data. """
        got_var, var_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if robhold is updated.
        _ = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'robhold', True)
        self.assertEqual(var_wobj.Value.Robhold, True)
        # Checks if ufprog is updated.
        _ = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'ufprog', False)
        self.assertEqual(var_wobj.Value.Ufprog, False)
        # Checks if ufmec is updated.
        _ = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'ufmec', 'h')
        self.assertEqual(var_wobj.Value.Ufmec, 'h')
        # Checks if uframe is updated.
        _ = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'uframe', '[0,0,0],[0,0,1,0]')
        self.assertEqual(var_wobj.Value.Uframe.ToString(), '[[0,0,0],[0,0,1,0]]')
        # Checks if oframe is updated.
        _ = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'oframe', '[0,0,0],[0,0,1,0]')
        self.assertEqual(var_wobj.Value.Oframe.ToString(), '[[0,0,0],[0,0,1,0]]')

    # Tests edit_and_write_rapid_data_property with incorrect input data.
    def test_edit_and_write_rapid_data_property_incorrect(self):
        """ Tests edit_and_write_rapid_data_property with incorrect input data. """
        got_var, var_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(var_number, 'robhold', False)
        self.assertEqual(msg, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted into rapid data.
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(10, 'robhold', False)
        self.assertIsInstance(msg, Exception)
        # Checks if wrong property is specified.
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'r', False)
        self.assertEqual(msg, 'Property not of type robhold, ufprog, ufmec, uframe or oframe.')
        # Checks if wrong data is inserted into property.
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 10, False)
        self.assertIsInstance(msg, Exception)
        # Checks if wrong data in new value
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'robhold', 10)
        self.assertEqual(msg, 'Input is not boolean.')
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'ufprog', 10)
        self.assertEqual(msg, 'Input is not boolean.')
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'ufmec', 10)
        self.assertEqual(msg, 'Input is not string.')
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'uframe', 10)
        self.assertEqual(msg, 'Input is not string.')
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'oframe', 10)
        self.assertEqual(msg, 'Input is not string.')
        # Checks if format of new value is incorrect
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'uframe', '10')
        self.assertEqual(msg, 'Input is not a valid Uframe.')
        msg = rapid_wobjdata.edit_and_write_rapid_data_property(var_wobj, 'oframe', '10')
        self.assertEqual(msg, 'Input is not a valid Oframe.')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        got_var, var_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        _ = rapid_wobjdata.edit_and_write_rapid_data(var_wobj, True, False, 'h', '[0,0,0],[0,0,1,0]',
                                                     '[0,0,0],[0,1,0,0]')
        self.assertEqual(var_wobj.Value.ToString(), '[TRUE,FALSE,"h",[[0,0,0],[0,0,1,0]],[[0,0,0],[0,1,0,0]]]')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        got_var, var_number = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, var_wobj = rapid_datatypes.get_rapid_data(self.controller, 'T_ROB1', 'MainModule', 'var_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Check if wrong rapid data is inserted.
        msg = rapid_wobjdata.edit_and_write_rapid_data(var_number, True, False, 'h', '[0,0,0],[0,0,1,0]',
                                                       '[0,0,0],[0,1,0,0]')
        self.assertEqual(msg, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted into rapid data.
        msg = rapid_wobjdata.edit_and_write_rapid_data(10, True, False, 'h', '[0,0,0],[0,0,1,0]',
                                                       '[0,0,0],[0,1,0,0]')
        self.assertIsInstance(msg, Exception)
        # Checks if wrong value is inserted into properties.
        msg = rapid_wobjdata.edit_and_write_rapid_data(var_wobj, 10, False, 'h', '[0,0,0],[0,0,1,0]',
                                                       '[0,0,0],[0,1,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_wobjdata.edit_and_write_rapid_data(var_wobj, True, 10, 'h', '[0,0,0],[0,0,1,0]',
                                                       '[0,0,0],[0,1,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_wobjdata.edit_and_write_rapid_data(var_wobj, True, False, 10, '[0,0,0],[0,0,1,0]',
                                                       '[0,0,0],[0,1,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_wobjdata.edit_and_write_rapid_data(var_wobj, True, False, 'h', 10, '[0,0,0],[0,1,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_wobjdata.edit_and_write_rapid_data(var_wobj, True, False, 'h', '[0,0,0],[0,0,1,0]', 10)
        self.assertEqual(msg, 'Incorrect format of input data.')
        # Checks if new value is incorrect
        msg = rapid_wobjdata.edit_and_write_rapid_data(var_wobj, True, False, 'h', '[0,0,1,0]',
                                                       '[0,0,0],[0,1,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
        msg = rapid_wobjdata.edit_and_write_rapid_data(var_wobj, True, False, 'h', '[0,0,0],[0,0,1,0]',
                                                       '[0,0,0]')
        self.assertEqual(msg, 'Incorrect format of input data.')
