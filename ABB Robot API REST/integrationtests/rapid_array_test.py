"""
Integration test to test rapid_array functionality towards the virtual controller.
"""

import unittest
import sys

import frontendREST.com.communication as com
import frontendREST.rapid.rapid_datatypes as rapid_datatypes
import frontendREST.rapid.rapid_array as rapid_array

##### Used when testing statement and branch coverage. ########
# sys.path.insert(1, 'C:\Users\Marius Vasshus\Dropbox\Programmering\Python\Master\ABB Robot API REST')
###############################################################


class RapidArrayTest(unittest.TestCase):

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
        if test_desc == 'Tests edit_and_write_rapid_data_num_index with correct input data.':
            _, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                              'T_ROB1', 'MainModule', 'var_array', 0, 0)
        elif test_desc == 'Tests edit_and_write_rapid_data_num with correct input data.':
            _, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth,
                                                                        'T_ROB1', 'MainModule', 'var_array', [])

        # Cleanup for all test cases
        _, _ = com.logoff_robot_controller('local', self.cookies)

    # Tests get_length with correct input data.
    def test_get_length_correct(self):
        """ Tests get_length with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_array')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        length = rapid_array.get_length(resp)
        self.assertEqual(length, 3)

    # Tests get_length with incorrect input data.
    def test_get_length_incorrect(self):
        """ Tests get_length with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid variable is inserted.
        length = rapid_array.get_length(resp)
        self.assertIsInstance(length, basestring)
        # Checks if rapid_data is not inserted.
        length = rapid_array.get_length(10)
        self.assertIsInstance(length, Exception)

    # Tests get_dimension with correct input data.
    def test_get_dimension_correct(self):
        """ Tests get_dimension with correct input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'var_array')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        dimension = rapid_array.get_dimensions(resp)
        self.assertEqual(dimension, 1)

    # Tests get_dimension with incorrect input data.
    def test_get_dimension_incorrect(self):
        """ Tests get_dimension with incorrect input data. """
        got_var, resp, self.cookies = rapid_datatypes.get_rapid_data('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                     'MainModule', 'const_number')
        if not got_var:
            print 'Couldn\'t get variable. Test will not run.'
            sys.exit()
        # Checks if wrong rapid data is inserted
        dimension = rapid_array.get_dimensions(resp)
        self.assertIsInstance(dimension, basestring)
        # Checks if wrong input.
        dimension = rapid_array.get_dimensions(10)
        self.assertIsInstance(dimension, Exception)

    # Tests edit_and_write_rapid_data_num_index with correct input data.
    def test_edit_and_write_rapid_data_num_index_correct(self):
        """ Tests edit_and_write_rapid_data_num_index with correct input data. """
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'var_array', 0, 1)
        self.assertEqual(res, 'Array index 0 updated.')

    # Tests edit_and_write_rapid_data_num_index with incorrect input data.
    def test_edit_and_write_rapid_data_num_index_incorrect(self):
        """ Tests edit_and_write_rapid_data_num_index with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('10', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'var_array', 0, 1)
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'var_boolean', 0, 1)
        self.assertEqual(res, 'Error updating array: 400')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index(10, self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'var_array', 0, 1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, 10, 'T_ROB1',
                                                                            'MainModule', 'var_array', 0, 1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth, 10,
                                                                            'MainModule', 'var_array', 0, 1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 10, 'var_array', 0, 1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 10, 0, 1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'var_array', 'h', 1)
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'var_array', 0, 'h')
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                            'T', 'MainModule', 'var_array', 0, 1)
        self.assertEqual(res, 'Error getting array from controller: 400')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'Mai', 'var_array', 0, 1)
        self.assertEqual(res, 'Error getting array from controller: 400')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'va', 0, 1)
        self.assertEqual(res, 'Error getting array from controller: 400')
        # Checks if index is out of bounds.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num_index('local', self.cookies, self.digest_auth,
                                                                            'T_ROB1', 'MainModule', 'var_array', 4, 1)
        self.assertEqual(res, 'Index is not valid.')

    # Tests edit_and_write_rapid_data_num with correct input data.
    def test_edit_and_write_rapid_data_num_correct(self):
        """ Tests edit_and_write_rapid_data_num with correct input data. """
        # Tests to write with array is not filled up.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_array', [1])
        self.assertEqual(res, 'Array updated.')
        # Tests to write with full array.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_array', [1, 1, 1])
        self.assertEqual(res, 'Array updated.')

    # Tests edit_and_write_rapid_data_num with incorrect input data.
    def test_edit_and_write_rapid_data_num_incorrect(self):
        """ Tests edit_and_write_rapid_data_num with incorrect input data. """
        # Checks if wrong ip address is specified.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('10', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_array', [1])
        self.assertIsInstance(res, Exception)
        # Checks if wrong rapid data is edited.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_boolean', [1])
        self.assertEqual(res, 'Specified variable is not an array.')
        # Checks if wrong data is inserted.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num(10, self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_array', [1])
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, 10, 'T_ROB1', 'MainModule',
                                                                      'var_array', [1])
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 10,
                                                                      'MainModule', 'var_array', [1])
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      10, 'var_array', [1])
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 10, [1])
        self.assertEqual(res, 'Something wrong with arguments.')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_array', 'h')
        self.assertEqual(res, 'Something wrong with arguments.')
        # Checks if wrong variable with wrong format is inserted.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T',
                                                                      'MainModule', 'var_array', [1])
        self.assertEqual(res, 'Error getting array from controller: 400')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'Mai', 'var_array', [1])
        self.assertEqual(res, 'Error getting array from controller: 400')
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'va', [1])
        self.assertEqual(res, 'Error getting array from controller: 400')
        # Checks if input list is larger than rapid list.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_array', [1, 1, 1, 1])
        self.assertEqual(res, 'Input list is larger than RAPID list.')
        # Checks if the list contains something else than numbers.
        res, self.cookies = rapid_array.edit_and_write_rapid_data_num('local', self.cookies, self.digest_auth, 'T_ROB1',
                                                                      'MainModule', 'var_array', ['h'])
        self.assertEqual(res, 'Something wrong in list.')
