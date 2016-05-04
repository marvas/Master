"""
Integration test to test rapid_wobjdata functionality towards the virtual controller.
"""

import unittest
import sys

##### Used when testing statement and branch coverage. ########
# sys.path.insert(1, 'C:\Users\Marius Vasshus\Dropbox\Programmering\Python\Master\ABB Robot API REST')
###############################################################

import frontendREST.com.communication as com
import frontendREST.rapid.rapid_datatypes as rapid_datatypes
import frontendREST.rapid.rapid_wobjdata as rapid_wobjdata



class RapidWobjdataTest(unittest.TestCase):

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
            res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                  self.digest_auth, 'T_ROB1',
                                                                                  'MainModule', 'var_wobj', 'robhold',
                                                                                  False)
            res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                  self.digest_auth, 'T_ROB1',
                                                                                  'MainModule', 'var_wobj', 'ufprog',
                                                                                  True)
            res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                  self.digest_auth, 'T_ROB1',
                                                                                  'MainModule', 'var_wobj', 'ufmec', '')
            res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                  self.digest_auth, 'T_ROB1',
                                                                                  'MainModule', 'var_wobj', 'uframe',
                                                                                  '[10,10,10],[1,0,0,0]')
            res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                  self.digest_auth, 'T_ROB1',
                                                                                  'MainModule', 'var_wobj', 'oframe',
                                                                                  '[10,10,10],[1,0,0,0]')

        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                         'T_ROB1', 'MainModule', 'var_wobj', False,
                                                                         True, '', '[10,10,10],[1,0,0,0]',
                                                                         '[10,10,10],[1,0,0,0]')

        # Cleanup for all test cases.
        _, _ = com.logoff_robot_controller('local', self.cookies)

    # Tests get_robhold_tostring with correct input data.
    def test_get_robhold_tostring_correct(self):
        """ Tests get_robhold_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        robhold = rapid_wobjdata.get_robhold_tostring(resp)
        self.assertEqual(robhold, 'Robhold = FALSE')

    # Tests get_robhold_tostring with incorrect input data.
    def test_get_robhold_tostring_incorrect(self):
        """ Tests get_robhold_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        robhold = rapid_wobjdata.get_robhold_tostring(resp)
        self.assertEqual(robhold, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        robhold = rapid_wobjdata.get_robhold_tostring(10)
        self.assertIsInstance(robhold, Exception)

    # Tests get_ufprog_tostring with correct input data.
    def test_get_ufprog_tostring_correct(self):
        """ Tests get_ufprog_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        ufprog = rapid_wobjdata.get_ufprog_tostring(resp)
        self.assertEqual(ufprog, 'Ufprog = TRUE')

    # Tests get_ufprog_tostring with incorrect input data.
    def test_get_ufprog_tostring_incorrect(self):
        """ Tests get_ufprog_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        ufprog = rapid_wobjdata.get_ufprog_tostring(resp)
        self.assertEqual(ufprog, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        ufprog = rapid_wobjdata.get_ufprog_tostring(10)
        self.assertIsInstance(ufprog, Exception)

    # Tests get_ufmec_tostring with correct input data.
    def test_get_ufmec_tostring_correct(self):
        """ Tests get_ufmec_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        ufmec = rapid_wobjdata.get_ufmec_tostring(resp)
        self.assertEqual(ufmec, 'Ufmec = ""')

    # Tests get_ufmec_tostring with incorrect input data.
    def test_get_ufmec_tostring_incorrect(self):
        """ Tests get_ufmec_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        ufmec = rapid_wobjdata.get_ufmec_tostring(resp)
        self.assertEqual(ufmec, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        ufmec = rapid_wobjdata.get_ufmec_tostring(10)
        self.assertIsInstance(ufmec, Exception)

    # Tests get_uframe_tostring with correct input data.
    def test_get_uframe_tostring_correct(self):
        """ Tests get_uframe_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        uframe = rapid_wobjdata.get_uframe_tostring(resp)
        self.assertEqual(uframe, 'Uframe: [Trans,Rot] = [[10,10,10],[1,0,0,0]]')

    # Tests get_uframe_tostring with incorrect input data.
    def test_get_uframe_tostring_incorrect(self):
        """ Tests get_uframe_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        uframe = rapid_wobjdata.get_uframe_tostring(resp)
        self.assertEqual(uframe, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        uframe = rapid_wobjdata.get_uframe_tostring(10)
        self.assertIsInstance(uframe, Exception)

    # Tests get_oframe_tostring with correct input data.
    def test_get_oframe_tostring_correct(self):
        """ Tests get_oframe_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        oframe = rapid_wobjdata.get_oframe_tostring(resp)
        self.assertEqual(oframe, 'Oframe: [Trans,Rot] = [[10,10,10],[1,0,0,0]]')

    # Tests get_oframe_tostring with incorrect input data.
    def test_get_oframe_tostring_incorrect(self):
        """ Tests get_oframe_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        oframe = rapid_wobjdata.get_oframe_tostring(resp)
        self.assertEqual(oframe, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        oframe = rapid_wobjdata.get_oframe_tostring(10)
        self.assertIsInstance(oframe, Exception)

    # Tests get_wobjdata_tostring with correct input data.
    def test_get_wobjdata_tostring_correct(self):
        """ Tests get_wobjdata_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_wobj')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        wobjdata = rapid_wobjdata.get_wobjdata_tostring(resp)
        self.assertEqual(wobjdata, 'Wobjdata: [FALSE,TRUE,"",[[10,10,10],[1,0,0,0]],[[10,10,10],[1,0,0,0]]]')

    # Tests get_wobjdata_tostring with incorrect input data.
    def test_get_wobjdata_tostring_incorrect(self):
        """ Tests get_wobjdata_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        wobjdata = rapid_wobjdata.get_wobjdata_tostring(resp)
        self.assertEqual(wobjdata, 'DataType is num and not wobjdata.')
        # Checks if wrong data is inserted.
        wobjdata = rapid_wobjdata.get_wobjdata_tostring(10)
        self.assertIsInstance(wobjdata, Exception)

    # Tests edit_and_write_rapid_data_property with correct input data.
    def test_edit_and_write_rapid_data_property_correct(self):
        """ Tests edit_and_write_rapid_data_property with correct input data. """
        # Checks if updating robhold works.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj',
                                                                              'robhold', True)
        self.assertEqual(res, 'Wobjdata robhold updated.')
        # Checks if updating ufprog works.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj',
                                                                              'ufprog', False)
        self.assertEqual(res, 'Wobjdata ufprog updated.')
        # Checks if updating ufmec works.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj',
                                                                              'ufmec', 'h')
        self.assertEqual(res, 'Wobjdata ufmec updated.')
        # Checks if updating uframe works.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj',
                                                                              'uframe', '[0,0,0],[0,0,1,0]')
        self.assertEqual(res, 'Wobjdata uframe updated.')
        # Checks if updating oframe works.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj',
                                                                              'oframe', '[0,0,0],[0,0,1,0]')
        self.assertEqual(res, 'Wobjdata oframe updated.')

    # Tests edit_and_write_rapid_data_property with incorrect input data.
    def test_edit_and_write_rapid_data_property_incorrect(self):
        """ Tests edit_and_write_rapid_data_property with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('10', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj',
                                                                              'robhold', False)
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_boolean',
                                                                              'robhold', False)
        self.assertIsInstance(res, Exception)
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property(10, self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj',
                                                                              'robhold', False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, 10, 'T_ROB1',
                                                                              'MainModule', 'var_wobj', 'robhold',
                                                                              False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              10, 'MainModule', 'var_wobj', 'robhold',
                                                                              False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 10, 'var_wobj', 'robhold',
                                                                              False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 10, 'robhold',
                                                                              False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj',
                                                                              10, False)
        self.assertEqual(res, 'Something wrong with arguments.')

        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T', 'MainModule', 'var_wobj',
                                                                              'robhold', False)
        self.assertEqual(res, 'Error getting wobjdata from controller: 400')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'Mai', 'var_wobj', 'robhold',
                                                                              False)
        self.assertEqual(res, 'Error getting wobjdata from controller: 400')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'va', 'robhold',
                                                                              False)
        self.assertEqual(res, 'Error getting wobjdata from controller: 400')
        # Checks if wrong property is specified
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj', 'r',
                                                                              False)
        self.assertEqual(res, 'Property not of type robhold, ufprog, ufmec, uframe or oframe.')
        # Checks if wrong format of new value
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj',
                                                                              'uframe', '[0,0]')
        self.assertEqual(res, 'Input is not a valid uframe.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_wobj',
                                                                              'robhold', 10)
        self.assertEqual(res, 'Input is not boolean.')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_wobj', True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Wobjdata updated.')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('10', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_wobj', True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                     'T_ROB1', 'MainModule', 'var_boolean', True, False,
                                                                     'h', '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Error updating wobjdata: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_wobj', True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, 10, 'T_ROB1', 'MainModule',
                                                                     'var_wobj', True, False, 'h', '[0,0,0],[0,0,1,0]',
                                                                     '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 10,
                                                                     'MainModule', 'var_wobj', True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     10, 'var_wobj', True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 10, True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong data is inserted into properties.
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_wobj', 10, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Incorrect format of input data.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_wobj', True, 10, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Incorrect format of input data.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_wobj', True, False, 10,
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_wobj', True, False, 'h', 10,
                                                                     '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_wobj', True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T',
                                                                     'MainModule', 'var_wobj', True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Error updating wobjdata: 400')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                     'T_ROB1', 'Mai', 'var_wobj', True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Error updating wobjdata: 400')
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'va', True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Error updating wobjdata: 400')
        # Checks if wrong format of uframe
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_wobj', True, False, 'h',
                                                                     '[0,0,0]', '[0,0,0],[0,1,0,0]')
        self.assertEqual(res, 'Incorrect format of input data.')
        # Checks if wrong format of oframe
        res, self.cookies = rapid_wobjdata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_wobj', True, False, 'h',
                                                                     '[0,0,0],[0,0,1,0]', '[0,0,0]')
        self.assertEqual(res, 'Incorrect format of input data.')
