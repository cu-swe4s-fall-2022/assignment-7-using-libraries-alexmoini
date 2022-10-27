import unittest
import data_processor.py
import os
import numpy as np
import pandas as pd

class TestUtils(unittest.TestCase):
    """
    TestUtils is a class that tests the functions in data_processor.py

    get_random_matrix
    -----------------
    Tests that get_random_matrix returns a matrix of random numbers.
    Tests that get_random_matrix returns -1 if the number of rows is not an int.
    Tests that get_random_matrix returns -1 if the number of columns is not an int.

    get_file_dimensions
    -------------------
    Tests that get_file_dimensions returns the correct dimensions of a file.
    Tests that get_file_dimensions returns -1 if the file does not exist.
    Tests that get_file_dimensions returns -1 if the file is not a CSV.

    write_matrix_to_file
    --------------------
    Tests that write_matrix_to_file returns 0 if the matrix is written to a file.
    Tests that write_matrix_to_file returns -1 if the number of rows is not an int.
    Tests that write_matrix_to_file returns -1 if the number of columns is not an int.
    Tests that write_matrix_to_file returns -1 if the file name is not a string.
    Tests that write_matrix_to_file returns -1 if the file name is not a CSV.
    """

    def setUp(self):
        """
        setUp: runs before each test
        """
        X = np.rand.random(3, 3)
        np.savetxt('test.csv', X, delimiter=',')

        return None

    def tearDown(self):
        """
        tearDown: runs after each test
        """
        os.remove('test.csv')
        return None

    def test_get_random_matrix(self):
        """
        test_get_random_matrix tests the get_random_matrix function in data_processor.py
        """
        # test that get_random_matrix returns a matrix of random numbers
        num_rows = 3
        num_columns = 3
        self.assertEqual(data_processor.get_random_matrix(num_rows, num_columns), 0)

        # test that get_random_matrix returns -1 if the number of rows is not an int
        num_rows = '3'
        num_columns = 3
        self.assertEqual(data_processor.get_random_matrix(num_rows, num_columns), -1)

        # test that get_random_matrix returns -1 if the number of columns is not an int
        num_rows = 3
        num_columns = '3'
        self.assertEqual(data_processor.get_random_matrix(num_rows, num_columns), -1)

    def test_get_file_dimensions(self):
        """
        test_get_file_dimensions tests the get_file_dimensions function in data_processor.py
        """
        # test that get_file_dimensions returns the correct dimensions of a file
        file_name = 'test.csv'
        self.assertEqual(data_processor.get_file_dimensions(file_name), (3, 3))
        file_name = 'not_a_file.csv'
        self.assertEqual(data_processor.get_file_dimensions(file_name), -1)

