#implemented a db-like app (queries, insertions, etc) but without actually using a database (hold it all in memory and write an program to interface with the data).

''' 
spreadsheet in python 
'''
import sys
import numpy
import unittest

class SQLTable:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # self.mtx = numpy.random.random((self.rows, self.cols))
        self.mtx = fill_matrix_by_counter()

        def fill_matrix_by_counter():
            for 

    def get_row(row_id):
        return self.mtx[row_id]

    def get_col(col_id):
        return [row[col_id] for row in self.mtx]

    def get_grid(first_row, firt_col, second_row, second_col):
        res = []



class MyTest(unittest.TestCase):
    def setUp(self):
        self.table = SQLTable(5,5)

    def tearDown(self):
        pass 

    def test_gets_row(self, row_id):
        row = self.table.get_row(row_id)
        assert len(row) == self.table.rows

    def test_gets_row(self, row_id):
        row = self.table.get_row(row_id)
        assert len(row) == self.table.rows

if __name__ == '__main__':
    unittest.main()

