"""
Integration test to test rapid_speeddata functionality towards the virtual controller.
"""

import unittest
import sys

##### Used when testing statement and branch coverage. ########
# sys.path.insert(1, 'C:\Users\Marius Vasshus\Dropbox\Programmering\Python\Master\ABB Robot API REST')
###############################################################

import frontendRWS.com.communication as com
import frontendRWS.rapid.rapid_datatypes as rapid_datatypes
import frontendRWS.rapid.rapid_speeddata as rapid_speeddata



class RapidSpeeddataTest(unittest.TestCase):

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
        if test_desc == 'Tests edit_and_write_rapid_data_base with correct input data.':
            _, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                             'T_ROB1', 'MainModule', 'var_basespeed',
                                                                             'v10')
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            _, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'MainModule', 'var_speed', 20, 1000,
                                                                        5000, 1000)

        # Cleanup for all test cases.
        _, _ = com.logoff_robot_controller('local', self.cookies)

    # Tests get_speeddata_tostring with correct input data.
    def test_get_speeddata_tostring_correct(self):
        """ Tests get_speeddata_tostring with correct input data. """
        got_var, const_bspeed, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                                             'T_ROB1', 'MainModule', 'const_basespeed')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, const_speed, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'const_speed')
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
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        speed = rapid_speeddata.get_speeddata_tostring(resp)
        self.assertEqual(speed, 'DataType is num and not speeddata.')
        # Checks if wrong data is inserted.
        speed = rapid_speeddata.get_speeddata_tostring(10)
        self.assertIsInstance(speed, Exception)

    # Tests edit_and_write_rapid_data_base with correct input data.
    def test_edit_and_write_rapid_data_base_correct(self):
        """ Tests edit_and_write_rapid_data_base with correct input data. """
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 'MainModule', 'var_basespeed',
                                                                           'v100')
        self.assertEqual(res, 'Base speeddata updated.')

    # Tests edit_and_write_rapid_data_base with incorrect input data.
    def test_edit_and_write_rapid_data_base_incorrect(self):
        """ Tests edit_and_write_rapid_data_base with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('10', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 'MainModule', 'var_basespeed',
                                                                           'v100')
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 'MainModule', 'var_boolean',
                                                                           'v100')
        self.assertEqual(res, 'Error updating base speeddata: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                           'MainModule', 'var_basespeed', 'v100')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, 10, 'T_ROB1',
                                                                           'MainModule', 'var_basespeed', 'v100')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth, 10,
                                                                           'MainModule', 'var_basespeed', 'v100')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 10, 'var_basespeed', 'v100')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 'MainModule', 10, 'v100')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 'MainModule', 'var_basespeed', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth, 'T',
                                                                           'MainModule', 'var_basespeed', 'v100')
        self.assertEqual(res, 'Error updating base speeddata: 400')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 'Mai', 'var_basespeed', 'v100')
        self.assertEqual(res, 'Error updating base speeddata: 400')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 'MainModule', 'va', 'v100')
        self.assertEqual(res, 'Error updating base speeddata: 400')
        # Checks if wrong base speed is specified
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 'MainModule', 'var_basespeed', 'r')
        self.assertEqual(res, 'Something wrong with the input. Not in format \'v100\'')
        # Checks if invalid base speed is specified
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 'MainModule', 'var_basespeed',
                                                                           'v1050')
        self.assertEqual(res, 'Something wrong with the input format, or the input is not a valid base speed.')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_speed', 25, 400, 1000, 300)
        self.assertEqual(res, 'Speeddata updated.')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('10', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_speed', 25, 400, 1000, 300)
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                      'T_ROB1', 'MainModule', 'var_boolean', 25, 400,
                                                                      1000, 300)
        self.assertEqual(res, 'Error updating speeddata: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_speed', 25, 400, 1000, 300)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, 10, 'T_ROB1', 'MainModule',
                                                                      'var_speed', 25, 400, 1000, 300)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 10,
                                                                      'MainModule', 'var_speed', 25, 400, 1000, 300)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      10, 'var_speed', 25, 400, 1000, 300)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 10, 25, 400, 1000, 300)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_speed', 'h', 400, 1000, 300)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_speed', 25, 'h', 1000, 300)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_speed', 25, 400, 'h', 300)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_speed', 25, 400, 1000, 'h')
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T',
                                                                      'MainModule', 'var_speed', 25, 400, 1000, 300)
        self.assertEqual(res, 'Error updating speeddata: 400')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                      'T_ROB1', 'Mai', 'var_speed', 25, 400, 1000, 300)
        self.assertEqual(res, 'Error updating speeddata: 400')
        res, self.cookies = rapid_speeddata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'va', 25, 400, 1000, 300)
        self.assertEqual(res, 'Error updating speeddata: 400')
