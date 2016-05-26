"""
Integration test to test rapid_tooldata functionality towards the virtual controller.
RobotStudio must run with the RAPID test program made for the integration tests
"""

import unittest
import sys

##### Used when testing statement and branch coverage. ########
# sys.path.insert(1, 'C:\Users\Marius Vasshus\Dropbox\Programmering\Python\Master\ABB Robot API Robot Web Services')
###############################################################

import frontendRWS.com.communication as com
import frontendRWS.rapid.rapid_datatypes as rapid_datatypes
import frontendRWS.rapid.rapid_tooldata as rapid_tooldata



class RapidTooldataTest(unittest.TestCase):

    cookies = None
    digest_auth = None

    # Preparing test
    def setUp(self):
        """ Setting up for test """

        connected, _, self.digest_auth, self.cookies = com.connect_robot_with_ipaddr_def_user('local')
        if not connected:
            print 'Couldn\'t connect to controller. Test will not be run.'
            sys.exit()

    # Ending test
    def tearDown(self):
        """ Cleaning after test """

        # Checks for any additional cleaning for some cases.
        test_desc = self.shortDescription()
        if test_desc == 'Tests edit_and_write_rapid_data_property with correct input data.':
            _, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                                'T_ROB1', 'MainModule', 'var_tool',
                                                                                'robhold', True)
            _, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                                'T_ROB1', 'MainModule', 'var_tool',
                                                                                'tframe', '[10,10,10],[0,0,1,0]')
            _, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                                'T_ROB1', 'MainModule', 'var_tool',
                                                                                'tload', '1,[0,0,1],[1,0,0,0],0,0,0')
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            _, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                       'T_ROB1', 'MainModule', 'var_tool', True,
                                                                       '[10,10,10],[0,0,1,0]',
                                                                       '1,[0,0,1],[1,0,0,0],0,0,0')

        # Cleanup for all test cases.
        _, _ = com.logoff_robot_controller('local', self.cookies)

    # Tests get_robhold_tostring with correct input data.
    def test_get_robhold_tostring_correct(self):
        """ Tests get_robhold_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        robhold = rapid_tooldata.get_robhold_tostring(resp)
        self.assertEqual(robhold, 'Robhold = TRUE')

    # Tests get_robhold_tostring with incorrect input data.
    def test_get_robhold_tostring_incorrect(self):
        """ Tests get_robhold_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        robhold = rapid_tooldata.get_robhold_tostring(resp)
        self.assertEqual(robhold, 'DataType is num and not tooldata.')
        # Checks if wrong data is inserted.
        robhold = rapid_tooldata.get_robhold_tostring(10)
        self.assertIsInstance(robhold, Exception)

    # Tests get_tframe_tostring with correct input data.
    def test_get_tframe_tostring_correct(self):
        """ Tests get_tframe_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        tframe = rapid_tooldata.get_tframe_tostring(resp)
        self.assertEqual(tframe, 'Tframe: [Trans,Rot] = [[10,10,10],[0,0,1,0]]')

    # Tests get_tframe_tostring with incorrect input data.
    def test_get_tframe_tostring_incorrect(self):
        """ Tests get_tframe_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        tframe = rapid_tooldata.get_tframe_tostring(resp)
        self.assertEqual(tframe, 'DataType is num and not tooldata.')
        # Checks if wrong data is inserted.
        tframe = rapid_tooldata.get_tframe_tostring(10)
        self.assertIsInstance(tframe, Exception)

    # Tests get_tload_tostring with correct input data.
    def test_get_tload_tostring_correct(self):
        """ Tests get_tload_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        tload = rapid_tooldata.get_tload_tostring(resp)
        self.assertEqual(tload, 'Tload: [Mass,Cog,Aom,Ix,Iy,Iz] = [1,[0,0,1],[1,0,0,0],0,0,0]')

    # Tests get_tload_tostring with incorrect input data.
    def test_get_tload_tostring_incorrect(self):
        """ Tests get_tload_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        tload = rapid_tooldata.get_tload_tostring(resp)
        self.assertEqual(tload, 'DataType is num and not tooldata.')
        # Checks if wrong data is inserted.
        tload = rapid_tooldata.get_tload_tostring(10)
        self.assertIsInstance(tload, Exception)

    # Tests get_tooldata_tostring with correct input data.
    def test_get_tooldata_tostring_correct(self):
        """ Tests get_tooldata_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_tool')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        tooldata = rapid_tooldata.get_tooldata_tostring(resp)
        self.assertEqual(tooldata, 'Tooldata: [TRUE,[[10,10,10],[0,0,1,0]],[1,[0,0,1],[1,0,0,0],0,0,0]]')

    # Tests get_tooldata_tostring with incorrect input data.
    def test_get_tooldata_tostring_incorrect(self):
        """ Tests get_tooldata_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        tooldata = rapid_tooldata.get_tooldata_tostring(resp)
        self.assertEqual(tooldata, 'DataType is num and not tooldata.')
        # Checks if wrong data is inserted.
        tooldata = rapid_tooldata.get_tooldata_tostring(10)
        self.assertIsInstance(tooldata, Exception)

    # Tests edit_and_write_rapid_data_property with correct input data.
    def test_edit_and_write_rapid_data_property_correct(self):
        """ Tests edit_and_write_rapid_data_property with correct input data. """
        # Checks if updating robhold works.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_tool',
                                                                              'robhold', False)
        self.assertEqual(res, 'Tooldata robhold updated.')
        # Checks if updating tframe works.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_tool',
                                                                              'tframe', '[0,0,0],[1,0,0,0]')
        self.assertEqual(res, 'Tooldata tframe updated.')
        # Checks if updating tload works.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_tool',
                                                                              'tload', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Tooldata tload updated.')

# Tests edit_and_write_rapid_data_property with incorrect input data.
    def test_edit_and_write_rapid_data_property_incorrect(self):
        """ Tests edit_and_write_rapid_data_property with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('10', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_tool',
                                                                              'robhold', False)
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_boolean',
                                                                              'robhold', False)
        self.assertIsInstance(res, Exception)
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property(10, self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_tool',
                                                                              'robhold', False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, 10, 'T_ROB1',
                                                                              'MainModule', 'var_tool', 'robhold',
                                                                              False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              10, 'MainModule', 'var_tool', 'robhold',
                                                                              False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 10, 'var_tool', 'robhold',
                                                                              False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 10, 'robhold',
                                                                              False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_tool',
                                                                              10, False)
        self.assertEqual(res, 'Something wrong with arguments.')

        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T', 'MainModule', 'var_tool',
                                                                              'robhold', False)
        self.assertEqual(res, 'Error getting tooldata from controller: 400')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'Mai', 'var_tool', 'robhold',
                                                                              False)
        self.assertEqual(res, 'Error getting tooldata from controller: 400')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'va', 'robhold',
                                                                              False)
        self.assertEqual(res, 'Error getting tooldata from controller: 400')
        # Checks if wrong property is specified
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_tool', 'r',
                                                                              False)
        self.assertEqual(res, 'Property not of type robhold, tframe, tload.')
        # Checks if wrong format of new value
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_tool',
                                                                              'tframe', '[0,0,0,0]')
        self.assertEqual(res, 'Input is not a valid Tframe.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_tool',
                                                                              'robhold', 10)
        self.assertEqual(res, 'Input is not boolean.')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_tool', False,
                                                                     '[0,0,0],[1,0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Tooldata updated.')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('10', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_tool', False,
                                                                     '[0,0,0],[1,0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                     'T_ROB1', 'MainModule', 'var_boolean', False,
                                                                     '[0,0,0],[1,0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Error updating tooldata: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_tool', False,
                                                                     '[0,0,0],[1,0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, 10, 'T_ROB1', 'MainModule',
                                                                     'var_tool', False,
                                                                     '[0,0,0],[1,0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 10,
                                                                     'MainModule', 'var_tool', False,
                                                                     '[0,0,0],[1,0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     10, 'var_tool', False, '[0,0,0],[1,0,0,0]',
                                                                     '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 10, False, '[0,0,0],[1,0,0,0]',
                                                                     '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong data is inserted into properties.
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_tool', 10,
                                                                     '[0,0,0],[1,0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Incorrect format of input data.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_tool', False, 10,
                                                                     '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_tool', False,
                                                                     '[0,0,0],[1,0,0,0]', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T',
                                                                     'MainModule', 'var_tool', False,
                                                                     '[0,0,0],[1,0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Error updating tooldata: 400')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                     'T_ROB1', 'Mai', 'var_tool', False,
                                                                     '[0,0,0],[1,0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Error updating tooldata: 400')
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'va', False,
                                                                     '[0,0,0],[1,0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Error updating tooldata: 400')
        # Checks if wrong format of tframe
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_tool', False,
                                                                     '[0,0,0]', '0,[0,0,0],[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Incorrect format of input data.')
        # Checks if wrong format of tload
        res, self.cookies = rapid_tooldata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_tool', False,
                                                                     '[0,0,0],[1,0,0,0]', '[0,1,0,0],1,1,1')
        self.assertEqual(res, 'Incorrect format of input data.')
