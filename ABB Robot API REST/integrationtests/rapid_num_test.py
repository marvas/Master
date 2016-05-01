"""
Integration test to test rapid_num functionality towards the virtual controller.
"""

import unittest
import sys

import frontendREST.com.communication as com
import frontendREST.rapid.rapid_datatypes as rapid_datatypes
import frontendREST.rapid.rapid_num as rapid_num


class RapidNumTest(unittest.TestCase):

    cookies = None
    digest_auth = None

    # Preparing test
    def setUp(self):
        """ Setting up for test """

        # Setup for all test cases.
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
            _, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                  'MainModule', 'var_number', 0)

        # Cleaning for all the test cases
        _, _ = com.logoff_robot_controller('local', self.cookies)

    # Tests get_value_tostring with correct rapid data
    def test_get_value_tostring_correct(self):
        """ Tests get_value_tostring with correct rapid data """
        got_var, resp_dict, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        self.assertEqual(rapid_num.get_value_tostring(resp_dict), 'Value = 1000')

    # Tests get_value_tostring with incorrect rapid data
    def test_get_value_tostring_incorrect(self):
        """ Tests get_value_tostring with incorrect rapid data """
        got_var, resp_dict, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'const_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        self.assertEqual(rapid_num.get_value_tostring(resp_dict), 'DataType is bool and not num.')
        # Checks if not rapid data is inserted
        self.assertIsInstance(rapid_num.get_value_tostring(10), Exception)

    # Tests get_value with correct rapid data
    def test_get_value_correct(self):
        """ Tests get_value with correct rapid data """
        got_var, resp_dict, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'const_number')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        self.assertEqual(rapid_num.get_value(resp_dict), 1000)

    # Tests get_value with incorrect rapid data
    def test_get_value_incorrect(self):
        """ Tests get_value with incorrect rapid data """
        got_var, resp_dict, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'const_boolean')
        if not got_var:
            print 'Could not get variable from controller. Test will not be run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        self.assertEqual(rapid_num.get_value(resp_dict), 'DataType is bool and not num.')
        # Checks if rapid data is not inserted.
        self.assertIsInstance(rapid_num.get_value(10), Exception)

    # Tests edit_and_write_rapid_data with correct input data
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data """
        res, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                'MainModule', 'var_number', 10)
        self.assertEqual(res, 'Value updated.')

    # Tests edit_and_write_rapid_data with incorrect input data
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_num.edit_and_write_rapid_data('10', self.cookies, self.digest_auth, 'T_ROB1',
                                                                'MainModule', 'var_number', 10)
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                'MainModule', 'var_boolean', 10)
        self.assertEqual(res, 'Error updating value: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_num.edit_and_write_rapid_data(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                'MainModule', 'var_number', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, 10, 'T_ROB1',
                                                                'MainModule', 'var_number', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 10,
                                                                'MainModule', 'var_number', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                10, 'var_number', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                'MainModule', 10, 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                'MainModule', 'var_number', 'h')
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T',
                                                                'MainModule', 'var_number', 10)
        self.assertEqual(res, 'Error updating value: 400')
        res, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                'Mai', 'var_number', 10)
        self.assertEqual(res, 'Error updating value: 400')
        res, self.cookies = rapid_num.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                'MainModule', 'va', 10)
        self.assertEqual(res, 'Error updating value: 400')
