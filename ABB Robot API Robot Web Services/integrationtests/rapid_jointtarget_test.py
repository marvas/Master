"""
Integration test to test rapid_jointtarget functionality towards the virtual controller.
RobotStudio must run with the RAPID test program made for the integration tests
"""

import unittest
import sys

##### Used when testing statement and branch coverage. ########
# sys.path.insert(1, 'C:\Users\Marius Vasshus\Dropbox\Programmering\Python\Master\ABB Robot API Robot Web Services')
###############################################################

import frontendRWS.com.communication as com
import frontendRWS.rapid.rapid_datatypes as rapid_datatypes
import frontendRWS.rapid.rapid_jointtarget as rapid_jointtarget



class RapidJointtargetTest(unittest.TestCase):

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
            _, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                   self.digest_auth, 'T_ROB1',
                                                                                   'MainModule', 'var_jtarget', 'robax',
                                                                                   '[0,0,0,10,0,0]')
            _, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                   self.digest_auth, 'T_ROB1',
                                                                                   'MainModule', 'var_jtarget', 'extax',
                                                                                   '[9E9,9E9,9E9,9E9,9E9,9E9]')
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            _, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'var_jtarget',
                                                                          '[0,0,0,10,0,0]', '[9E9,9E9,9E9,9E9,9E9,9E9]')

        # Cleanup for all test cases.
        _, _ = com.logoff_robot_controller('local', self.cookies)

    # Tests get_robax_tostring with correct input data.
    def test_get_robax_tostring_correct(self):
        """ Tests get_robax_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_jtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        robax = rapid_jointtarget.get_robax_tostring(resp)
        self.assertEqual(robax, 'Robax: [Rax_1,Rax_2,Rax_3,Rax_4,Rax_5,Rax_6] = [0,0,0,10,0,0]')

    # Tests get_robax_tostring with incorrect input data.
    def test_get_robax_tostring_incorrect(self):
        """ Tests get_robax_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        robax = rapid_jointtarget.get_robax_tostring(resp)
        self.assertEqual(robax, 'DataType is num and not jointtarget.')
        # Checks if wrong data is inserted.
        robax = rapid_jointtarget.get_robax_tostring(10)
        self.assertIsInstance(robax, Exception)

    # Tests get_extax_tostring with correct input data.
    def test_get_extax_tostring_correct(self):
        """ Tests get_extax_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_jtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        extax = rapid_jointtarget.get_extax_tostring(resp)
        self.assertEqual(extax, 'Extax: [Eax_a,Eax_b,Eax_c,Eax_d,Eax_e,Eax_f] = [9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]')

    # Tests get_extax_tostring with incorrect input data.
    def test_get_extax_tostring_incorrect(self):
        """ Tests get_extax_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        extax = rapid_jointtarget.get_extax_tostring(resp)
        self.assertEqual(extax, 'DataType is num and not jointtarget.')
        # Checks if wrong data is inserted.
        extax = rapid_jointtarget.get_extax_tostring(10)
        self.assertIsInstance(extax, Exception)

    # Tests get_jointtarget_tostring with correct input data.
    def test_get_jointtarget_tostring_correct(self):
        """ Tests get_jointtarget_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_jtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        jointtarget = rapid_jointtarget.get_jointtarget_tostring(resp)
        self.assertEqual(jointtarget, 'Jointtarget: [[0,0,0,10,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]]')

    # Tests get_jointtarget_tostring with incorrect input data.
    def test_get_jointtarget_tostring_incorrect(self):
        """ Tests get_jointtarget_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        jointtarget = rapid_jointtarget.get_jointtarget_tostring(resp)
        self.assertEqual(jointtarget, 'DataType is num and not jointtarget.')
        # Checks if wrong data is inserted.
        jointtarget = rapid_jointtarget.get_jointtarget_tostring(10)
        self.assertIsInstance(jointtarget, Exception)

    # Tests edit_and_write_rapid_data_property with correct input data.
    def test_edit_and_write_rapid_data_property_correct(self):
        """ Tests edit_and_write_rapid_data_property with correct input data. """
        # Checks if updating robax works.
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1',
                                                                                 'MainModule', 'var_jtarget', 'robax',
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Jointtarget robax updated.')
        # Checks if updating extax works.
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1',
                                                                                 'MainModule', 'var_jtarget', 'extax',
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Jointtarget extax updated.')

    # Tests edit_and_write_rapid_data_property with incorrect input data.
    def test_edit_and_write_rapid_data_property_incorrect(self):
        """ Tests edit_and_write_rapid_data_property with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('10', self.cookies, self.digest_auth,
                                                                                 'T_ROB1', 'MainModule', 'var_jtarget',
                                                                                 'robax', '[0,0,0,0,0,0]')
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1',
                                                                                 'MainModule', 'var_boolean', 'robax',
                                                                                 '[0,0,0,0,0,0]')
        self.assertIsInstance(res, Exception)
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property(10, self.cookies, self.digest_auth,
                                                                                 'T_ROB1', 'MainModule', 'var_jtarget',
                                                                                 'robax', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies, 10, 'T_ROB1',
                                                                                 'MainModule', 'var_jtarget', 'robax',
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 10, 'MainModule',
                                                                                 'var_jtarget', 'robax',
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1', 10,
                                                                                 'var_jtarget', 'robax',
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1',
                                                                                 'MainModule', 10, 'robax',
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1',
                                                                                 'MainModule', 'var_jtarget', 10,
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1',
                                                                                 'MainModule', 'var_jtarget', 'robax',
                                                                                 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T', 'MainModule',
                                                                                 'var_jtarget', 'robax',
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error getting jointtarget from controller: 400')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1', 'Mai',
                                                                                 'var_jtarget', 'robax',
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error getting jointtarget from controller: 400')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1',
                                                                                 'MainModule', 'va', 'robax',
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error getting jointtarget from controller: 400')
        # Checks if wrong property is specified
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1',
                                                                                 'MainModule', 'var_jtarget', 'r',
                                                                                 '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Property not of type robax or extax.')
        # Checks if wrong format of new value
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                 self.digest_auth, 'T_ROB1',
                                                                                 'MainModule', 'var_jtarget', 'robax',
                                                                                 '[0,0,0,0]')
        self.assertEqual(res, 'Incorrect format of robax. Ex \'[0,0,0,0,0,0]\'')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'MainModule', 'var_jtarget',
                                                                        '[0,0,0,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Jointtarget updated.')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('10', self.cookies, self.digest_auth, 'T_ROB1',
                                                                        'MainModule', 'var_jtarget', '[0,0,0,0,0,0]',
                                                                        '[0,0,0,0,0,0]')
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'MainModule', 'var_boolean',
                                                                        '[0,0,0,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error updating jointtarget: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                        'MainModule', 'var_jtarget', '[0,0,0,0,0,0]',
                                                                        '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, 10, 'T_ROB1',
                                                                        'MainModule', 'var_jtarget',
                                                                        '[0,0,0,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 10,
                                                                        'MainModule', 'var_jtarget', '[0,0,0,0,0,0]',
                                                                        '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 10, 'var_jtarget', '[0,0,0,0,0,0]',
                                                                        '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'MainModule', 10, '[0,0,0,0,0,0]',
                                                                        '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'MainModule', 'var_jtarget', 10,
                                                                        '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'MainModule', 'var_jtarget',
                                                                        '[0,0,0,0,0,0]', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T', 'MainModule', 'var_jtarget',
                                                                        '[0,0,0,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error updating jointtarget: 400')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'Mai', 'var_jtarget', '[0,0,0,0,0,0]',
                                                                        '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error updating jointtarget: 400')
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'MainModule', 'va', '[0,0,0,0,0,0]',
                                                                        '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error updating jointtarget: 400')
        # Checks if wrong robax is specified
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'MainModule', 'var_jtarget', '[0,0]',
                                                                        '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Incorrect format of input data.')
        # Checks if wrong format of extax
        res, self.cookies = rapid_jointtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'MainModule', 'var_jtarget',
                                                                        '[0,0,0,0,0,0]', '[0,0,0,0]')
        self.assertEqual(res, 'Incorrect format of input data.')
