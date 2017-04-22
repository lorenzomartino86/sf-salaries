import os
import unittest
import pandas as pd


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.file_location = os.path.join(os.path.dirname(__file__), 'Salaries.csv')

    def test_read_csv_into_dataframe(self):
        data_frame = pd.read_csv(self.file_location)


if __name__ == '__main__':
    unittest.main()
