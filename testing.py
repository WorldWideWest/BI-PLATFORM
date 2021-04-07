import unittest
import pandas as pd
from scripts.parser import Application

# Required data
app = Application()
columns = ['Date', 'City', 'Customer type', 'Gender','Product line', 'Unit price',
           'Quantity', 'Tax 5%', 'Total', 'Payment', 'cogs', 'gross margin percentage',
           'gross income','Rating']



class Testing(unittest.TestCase):

    def test_import(self):
        path = 'dataSet/rawData'
        data = app.Import(path)
        self.assertTrue(type(data) == pd.core.frame.DataFrame)

        
    def test_columns(self):
        data = app.Import('dataSet/rawData')
        for index in range(len(data.columns)):
            self.assertEqual(data.columns[index], columns[index])

if __name__ == "__main__":
    unittest.main()
