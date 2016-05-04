"""
Integration test to test rapid_datatypes functionality towards the virtual controller.
"""

import unittest
import sys

##### Used when testing statement and branch coverage. ########
# sys.path.insert(1, 'C:\Users\Marius Vasshus\Dropbox\Programmering\Python\Master\ABB Robot API REST')
###############################################################

import frontendREST.com.communication as com
import frontendREST.rapid.rapid_datatypes as rapid_datatypes



class RapidDatatypesTest(unittest.TestCase):

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

        _, _ = com.logoff_robot_controller('local', self.cookies)

    # Tests get_rapid_data with correct input data.
    def test_get_rapid_data_correct(self):
        """ Tests get_rapid_data with correct input data. """
        got_const, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                                       'T_ROB1', 'MainModule', 'const_number')
        self.assertTrue(got_const)

    # Tests get_rapid_data with incorrect input data.
    def test_get_rapid_data_incorrect(self):
        """ Tests get_rapid_data with incorrect input data. """
        # Tests if ip address is wrong.
        _, resp, self.cookies = rapid_datatypes.get_rapid_data('10', self.cookies, self.digest_auth,
                                                               'T_ROB1', 'MainModule', 'const_number')
        self.assertIsInstance(resp, Exception)
        # Checks if the input data is not correct.
        _, resp, self.cookies = rapid_datatypes.get_rapid_data(10, self.cookies, self.digest_auth,
                                                               'T_ROB1', 'MainModule', 'const_number')
        self.assertEqual(resp, 'Something wrong with arguments.')
        _, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, 10,
                                                               'T_ROB1', 'MainModule', 'const_number')
        self.assertEqual(resp, 'Something wrong with arguments.')
        _, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                               10, 'MainModule', 'const_number')
        self.assertEqual(resp, 'Something wrong with arguments.')
        _, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                               'T_ROB1', 10, 'const_number')
        self.assertEqual(resp, 'Something wrong with arguments.')
        _, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                               'T_ROB1', 'MainModule', 10)
        self.assertEqual(resp, 'Something wrong with arguments.')
        # Checks if variable name is wrong
        _, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth,
                                                               'T', 'MainModule', 'const_number')
        self.assertEqual(resp, 'Error getting value and/or property: \nValue status code: 400 \n'
                               'Property status code: 400')
