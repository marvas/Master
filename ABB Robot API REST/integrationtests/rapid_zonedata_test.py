"""
Integration test to test rapid_zonedata functionality towards the virtual controller.
"""

import unittest
import sys

##### Used when testing statement and branch coverage. ########
# sys.path.insert(1, 'C:\Users\Marius Vasshus\Dropbox\Programmering\Python\Master\ABB Robot API REST')
###############################################################

import frontendREST.com.communication as com
import frontendREST.rapid.rapid_datatypes as rapid_datatypes
import frontendREST.rapid.rapid_zonedata as rapid_zonedata


class RapidZonedataTest(unittest.TestCase):

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
            _, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'var_basezone',
                                                                            'z0')
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            _, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                       'T_ROB1', 'MainModule', 'var_zone',
                                                                       False, 0.3, 0.3, 0.3, 0.5, 0.3, 0.5)

        # Cleanup for all test cases.
        _, _ = com.logoff_robot_controller('local', self.cookies)

    # Tests get_zonedata_tostring with correct input data.
    def test_get_zonedata_tostring_correct(self):
        """ Tests get_zonedata_tostring with correct input data. """
        got_var, const_bzone, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'const_basezone')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        got_var, const_zone, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                                           'T_ROB1', 'MainModule', 'const_zone')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks base zonedata
        bzone = rapid_zonedata.get_zonedata_tostring(const_bzone)
        self.assertEqual(bzone, 'Base zonedata: z0 ([FALSE,0.3,0.3,0.3,0.03,0.3,0.03])')
        # Checks zonedata
        zone = rapid_zonedata.get_zonedata_tostring(const_zone)
        self.assertEqual(zone, 'Zonedata: [FALSE,0.3,0.3,0.3,0.5,0.3,0.5]')

    # Tests get_zonedata_tostring with incorrect input data.
    def test_get_zonedata_tostring_incorrect(self):
        """ Tests get_zonedata_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        speed = rapid_zonedata.get_zonedata_tostring(resp)
        self.assertEqual(speed, 'DataType is num and not zonedata.')
        # Checks if wrong data is inserted.
        speed = rapid_zonedata.get_zonedata_tostring(10)
        self.assertIsInstance(speed, Exception)

    # Tests edit_and_write_rapid_data_base with correct input data.
    def test_edit_and_write_rapid_data_base_correct(self):
        """ Tests edit_and_write_rapid_data_base with correct input data. """
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'var_basezone', 'z10')
        self.assertEqual(res, 'Base zonedata updated.')

    # Tests edit_and_write_rapid_data_base with incorrect input data.
    def test_edit_and_write_rapid_data_base_incorrect(self):
        """ Tests edit_and_write_rapid_data_base with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('10', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'var_basezone', 'z10')
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'var_boolean', 'z10')
        self.assertEqual(res, 'Error updating base zonedata: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                          'MainModule', 'var_basezone', 'z10')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, 10, 'T_ROB1',
                                                                          'MainModule', 'var_basezone', 'z10')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth, 10,
                                                                          'MainModule', 'var_basezone', 'z10')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 10, 'var_basezone', 'z10')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 10, 'z10')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'var_basezone', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth, 'T',
                                                                          'MainModule', 'var_basezone', 'z10')
        self.assertEqual(res, 'Error updating base zonedata: 400')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'Mai', 'var_basezone', 'z10')
        self.assertEqual(res, 'Error updating base zonedata: 400')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'va', 'z10')
        self.assertEqual(res, 'Error updating base zonedata: 400')
        # Checks if wrong base zone is specified
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'var_basezone', 'r')
        self.assertEqual(res, 'Something wrong with the input. Not in format \'z1\'')
        # Checks if invalid base zone is specified
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data_base('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'var_basezone',
                                                                          'z1050')
        self.assertEqual(res, 'Something wrong with the input format, or the input is not a valid base zone.')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_zone', False, 1, 1, 1, 0.1, 1,
                                                                     0.1)
        self.assertEqual(res, 'Zonedata updated.')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('10', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_zone', False, 1, 1, 1, 0.1, 1,
                                                                     0.1)
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                     'T_ROB1', 'MainModule', 'var_boolean', False, 1, 1,
                                                                     1, 0.1, 1, 0.1)
        self.assertEqual(res, 'Error updating zonedata: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_zone', False, 1, 1, 1, 0.1, 1,
                                                                     0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, 10, 'T_ROB1', 'MainModule',
                                                                     'var_zone', False, 1, 1, 1, 0.1, 1, 0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 10,
                                                                     'MainModule', 'var_zone', False, 1, 1, 1, 0.1, 1,
                                                                     0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     10, 'var_zone', False, 1, 1, 1, 0.1, 1, 0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 10, False, 1, 1, 1, 0.1, 1, 0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_zone', 10, 1, 1, 1, 0.1, 1, 0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_zone', False, 'h', 1, 1, 0.1, 1,
                                                                     0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_zone', False, 1, 'h', 1, 0.1, 1,
                                                                     0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_zone', False, 1, 1, 'h', 0.1, 1,
                                                                     0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_zone', False, 1, 1, 1, 'h', 1,
                                                                     0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_zone', False, 1, 1, 1, 0.1, 'h',
                                                                     0.1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_zone', False, 1, 1, 1, 0.1, 1,
                                                                     'h')
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T',
                                                                     'MainModule', 'var_zone', False, 1, 1, 1, 0.1, 1,
                                                                     0.1)
        self.assertEqual(res, 'Error updating zonedata: 400')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                     'T_ROB1', 'Mai', 'var_zone', False, 1, 1, 1, 0.1,
                                                                     1, 0.1)
        self.assertEqual(res, 'Error updating zonedata: 400')
        res, self.cookies = rapid_zonedata.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'va', False, 1, 1, 1, 0.1, 1, 0.1)
        self.assertEqual(res, 'Error updating zonedata: 400')
