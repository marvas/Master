"""
Integration test to test rapid_robtarget functionality towards the virtual controller.
"""

import unittest
import sys

import frontendREST.com.communication as com
import frontendREST.rapid.rapid_datatypes as rapid_datatypes
import frontendREST.rapid.rapid_robtarget as rapid_robtarget


class RapidRobtargetTest(unittest.TestCase):

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
            res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                   self.digest_auth, 'T_ROB1',
                                                                                   'MainModule', 'var_rtarget', 'trans',
                                                                                   '[10,10,10]')
            res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                   self.digest_auth, 'T_ROB1',
                                                                                   'MainModule', 'var_rtarget', 'rot',
                                                                                   '[0,0,1,0]')
            res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                   self.digest_auth, 'T_ROB1',
                                                                                   'MainModule', 'var_rtarget',
                                                                                   'robconf', '[0,0,0,0]')
            res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies,
                                                                                   self.digest_auth, 'T_ROB1',
                                                                                   'MainModule', 'var_rtarget', 'extax',
                                                                                   '[9E9,9E9,9E9,9E9,9E9,9E9]')
        elif test_desc == 'Tests edit_and_write_rapid_data with correct input data.':
            res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                          'T_ROB1', 'MainModule', 'var_rtarget',
                                                                          '[10,10,10]', '[0,0,1,0]', '[0,0,0,0]',
                                                                          '[9E9,9E9,9E9,9E9,9E9,9E9]')

        # Cleanup for all test cases.
        _, _ = com.logoff_robot_controller('local', self.cookies)

    # Tests get_trans_tostring with correct input data.
    def test_get_trans_tostring_correct(self):
        """ Tests get_trans_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        trans = rapid_robtarget.get_trans_tostring(resp)
        self.assertEqual(trans, 'Trans: [X,Y,Z] = [10,10,10]')

    # Tests get_trans_tostring with incorrect input data.
    def test_get_trans_tostring_incorrect(self):
        """ Tests get_trans_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        trans = rapid_robtarget.get_trans_tostring(resp)
        self.assertEqual(trans, 'DataType is num and not robtarget.')
        # Checks if wrong data is inserted.
        trans = rapid_robtarget.get_trans_tostring(10)
        self.assertIsInstance(trans, Exception)

    # Tests get_rot_tostring with correct input data.
    def test_get_rot_tostring_correct(self):
        """ Tests get_rot_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        rot = rapid_robtarget.get_rot_tostring(resp)
        self.assertEqual(rot, 'Rot: [Q1,Q2,Q3,Q4] = [0,0,1,0]')

    # Tests get_rot_tostring with incorrect input data.
    def test_get_rot_tostring_incorrect(self):
        """ Tests get_rot_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        rot = rapid_robtarget.get_rot_tostring(resp)
        self.assertEqual(rot, 'DataType is num and not robtarget.')
        # Checks if wrong data is inserted.
        rot = rapid_robtarget.get_rot_tostring(10)
        self.assertIsInstance(rot, Exception)

    # Tests get_robconf_tostring with correct input data.
    def test_get_robconf_tostring_correct(self):
        """ Tests get_robconf_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        robconf = rapid_robtarget.get_robconf_tostring(resp)
        self.assertEqual(robconf, 'Robconf: [Cf1,Cf4,Cf6,Cfx] = [0,0,0,0]')

    # Tests get_robconf_tostring with incorrect input data.
    def test_get_robconf_tostring_incorrect(self):
        """ Tests get_robconf_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        robconf = rapid_robtarget.get_robconf_tostring(resp)
        self.assertEqual(robconf, 'DataType is num and not robtarget.')
        # Checks if wrong data is inserted.
        robconf = rapid_robtarget.get_robconf_tostring(10)
        self.assertIsInstance(robconf, Exception)

    # Tests get_extax_tostring with correct input data.
    def test_get_extax_tostring_correct(self):
        """ Tests get_extax_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        extax = rapid_robtarget.get_extax_tostring(resp)
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
        extax = rapid_robtarget.get_extax_tostring(resp)
        self.assertEqual(extax, 'DataType is num and not robtarget.')
        # Checks if wrong data is inserted.
        robconf = rapid_robtarget.get_robconf_tostring(10)
        self.assertIsInstance(robconf, Exception)

    # Tests get_robtarget_tostring with correct input data.
    def test_get_robtarget_tostring_correct(self):
        """ Tests get_robtarget_tostring with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_rtarget')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        robtarget = rapid_robtarget.get_robtarget_tostring(resp)
        self.assertEqual(robtarget, 'Robtarget: [[10,10,10],[0,0,1,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]]')

    # Tests get_robtarget_tostring with incorrect input data.
    def test_get_robtarget_tostring_incorrect(self):
        """ Tests get_robtarget_tostring with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted.
        robtarget = rapid_robtarget.get_robtarget_tostring(resp)
        self.assertEqual(robtarget, 'DataType is num and not robtarget.')
        # Checks if wrong data is inserted.
        robtarget = rapid_robtarget.get_robtarget_tostring(10)
        self.assertIsInstance(robtarget, Exception)

    # Tests edit_and_write_rapid_data_property with correct input data.
    def test_edit_and_write_rapid_data_property_correct(self):
        """ Tests edit_and_write_rapid_data_property with correct input data. """
        # Checks if updating trans works.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_rtarget',
                                                                               'trans', '[0,0,0]')
        self.assertEqual(res, 'Robtarget trans updated.')
        # Checks if updating rot works.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_rtarget',
                                                                               'rot', '[1,0,0,0]')
        self.assertEqual(res, 'Robtarget rot updated.')
        # Checks if updating robconf works.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_rtarget',
                                                                               'robconf', '[0,1,0,0]')
        self.assertEqual(res, 'Robtarget robconf updated.')
        # Checks if updating extax works.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_rtarget',
                                                                               'extax', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Robtarget extax updated.')

    # Tests edit_and_write_rapid_data_property with incorrect input data.
    def test_edit_and_write_rapid_data_property_incorrect(self):
        """ Tests edit_and_write_rapid_data_property with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('10', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_rtarget',
                                                                               'trans', '[0,0,0]')
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_boolean',
                                                                               'trans', '[0,0,0]')
        self.assertIsInstance(res, Exception)
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property(10, self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_rtarget',
                                                                               'trans', '[0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, 10, 'T_ROB1',
                                                                               'MainModule', 'var_rtarget', 'trans',
                                                                               '[0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               10, 'MainModule', 'var_rtarget', 'trans',
                                                                               '[0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 10, 'var_rtarget', 'trans',
                                                                               '[0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 10, 'trans',
                                                                               '[0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_rtarget',
                                                                               10, '[0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_rtarget',
                                                                               'trans', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T', 'MainModule', 'var_rtarget',
                                                                               'trans', '[0,0,0]')
        self.assertEqual(res, 'Error getting robtarget from controller: 400')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'Mai', 'var_rtarget', 'trans',
                                                                               '[0,0,0]')
        self.assertEqual(res, 'Error getting robtarget from controller: 400')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'va', 'trans',
                                                                               '[0,0,0]')
        self.assertEqual(res, 'Error getting robtarget from controller: 400')
        # Checks if wrong property is specified
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_rtarget',
                                                                               'r', '[0,0,0]')
        self.assertEqual(res, 'Property not of type trans, rot, robconf or extax.')
        # Checks if wrong format of new value
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data_property('local', self.cookies, self.digest_auth,
                                                                               'T_ROB1', 'MainModule', 'var_rtarget',
                                                                               'trans', '[0,0,0,0]')
        self.assertEqual(res, 'Incorrect format of trans. Ex \'[10,0,100]\'')

    # Tests edit_and_write_rapid_data with correct input data.
    def test_edit_and_write_rapid_data_correct(self):
        """ Tests edit_and_write_rapid_data with correct input data. """
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_rtarget', '[0,0,0]',
                                                                      '[1,0,0,0]', '[0,0,0,1]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Robtarget updated.')

    # Tests edit_and_write_rapid_data with incorrect input data.
    def test_edit_and_write_rapid_data_incorrect(self):
        """ Tests edit_and_write_rapid_data with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('10', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_rtarget', '[0,0,0]',
                                                                      '[0,0,0,0]', '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                      'T_ROB1', 'MainModule', 'var_boolean', '[0,0,0]',
                                                                      '[0,0,0,0]', '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error updating robtarget: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_rtarget', '[0,0,0]',
                                                                      '[0,0,0,0]', '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, 10, 'T_ROB1', 'MainModule',
                                                                      'var_rtarget', '[0,0,0]', '[0,0,0,0]',
                                                                      '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 10,
                                                                      'MainModule', 'var_rtarget', '[0,0,0]',
                                                                      '[0,0,0,0]', '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      10, 'var_rtarget', '[0,0,0]', '[0,0,0,0]',
                                                                      '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 10, '[0,0,0]', '[0,0,0,0]',
                                                                      '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_rtarget', 10, '[0,0,0,0]',
                                                                      '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_rtarget', '[0,0,0]', 10,
                                                                      '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_rtarget', '[0,0,0]',
                                                                      '[0,0,0,0]', 10, '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_rtarget', '[0,0,0]',
                                                                      '[0,0,0,0]', '[1,0,0,0]', 10)
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T',
                                                                      'MainModule', 'var_rtarget', '[0,0,0]',
                                                                      '[0,0,0,0]', '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error updating robtarget: 400')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth,
                                                                      'T_ROB1', 'Mai', 'var_rtarget', '[0,0,0]',
                                                                      '[0,0,0,0]', '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error updating robtarget: 400')
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'va', '[0,0,0]', '[0,0,0,0]',
                                                                      '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Error updating robtarget: 400')
        # Checks if trans is specified wrong.
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_rtarget', '[0,0]', '[0,0,0,0]',
                                                                      '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Incorrect format of input data.')
        # Checks if wrong format of rot
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_jtarget', '[0,0,0]', '[0,0,0]',
                                                                      '[1,0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Incorrect format of input data.')
        # Checks if wrong format of robconf
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_jtarget', '[0,0,0]',
                                                                      '[0,0,0,0]', '[0,0,0]', '[0,0,0,0,0,0]')
        self.assertEqual(res, 'Incorrect format of input data.')
        # Checks if wrong format of extax
        res, self.cookies = rapid_robtarget.edit_and_write_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_jtarget', '[0,0,0]',
                                                                      '[0,0,0,0]', '[1,0,0,0]', '[0,0,0,0]')
        self.assertEqual(res, 'Incorrect format of input data.')
