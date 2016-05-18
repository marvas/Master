"""
Integration test to test rapid_bool functionality towards the virtual controller.
"""

import unittest
import sys

##### Used when testing statement and branch coverage. ########
# sys.path.insert(1, 'C:\Users\Marius Vasshus\Dropbox\Programmering\Python\Master\ABB Robot API REST')
###############################################################

import frontendRWS.com.communication as com
import frontendRWS.rapid.rapid_datatypes as rapid_datatypes
import frontendRWS.rapid.rapid_bool as rapid_bool



class RapidBoolTest(unittest.TestCase):

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
        if test_desc == 'Tests edit_and_write_rapid_data with correct input data':
            _, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                   'MainModule', 'var_boolean', True)

        _, _ = com.logoff_robot_controller('local', self.cookies)

    # Tests get_state_tostring with correct rapid data
    def test_get_state_tostring_correct(self):
        """ Tests get_state_tostring with correct rapid data """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        self.assertEqual(rapid_bool.get_state_tostring(resp), 'State = TRUE')

    # Tests get_state_tostring with incorrect rapid data
    def test_get_state_tostring_incorrect(self):
        """ Tests get_state_tostring with incorrect rapid data """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        self.assertEqual(rapid_bool.get_state_tostring(resp), 'DataType is num and not bool.')
        # Checks if rapid data is not inserted.
        self.assertIsInstance(rapid_bool.get_state_tostring(10), Exception)

    # Tests get_state with correct rapid data
    def test_get_state_correct(self):
        """ Tests get_state with correct rapid data """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        self.assertEqual(rapid_bool.get_state(resp), True)

    # Tests get_state with incorrect rapid data
    def test_get_state_incorrect(self):
        """ Tests get_state with incorrect rapid data """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        self.assertEqual(rapid_bool.get_state(resp), 'DataType is num and not bool.')
        # Checks if rapid data is not inserted.
        self.assertIsInstance(rapid_bool.get_state(10), Exception)

    # Tests edit_and_write_rapid_data with correct input data
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data """
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                 'MainModule', 'var_boolean', False)
        self.assertEqual(res, 'Value updated.')

    # Tests edit_and_write_rapid_data with incorrect input data
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('10', self.cookies, self.digest_auth, 'T_ROB1',
                                                                 'MainModule', 'var_boolean', False)
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                 'MainModule', 'var_number', False)
        self.assertEqual(res, 'Error updating value: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_bool.edit_and_write_rapid_data(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                 'MainModule', 'var_boolean', False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, 10, 'T_ROB1',
                                                                 'MainModule', 'var_boolean', False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 10,
                                                                 'MainModule', 'var_boolean', False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                 10, 'var_boolean', False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                 'MainModule', 10, False)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                 'MainModule', 'var_boolean', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T',
                                                                 'MainModule', 'var_boolean', False)
        self.assertEqual(res, 'Error updating value: 400')
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                 'Mai', 'var_boolean', False)
        self.assertEqual(res, 'Error updating value: 400')
        res, self.cookies = rapid_bool.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                 'MainModule', 'va', False)
        self.assertEqual(res, 'Error updating value: 400')
