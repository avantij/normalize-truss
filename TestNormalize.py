import unittest
import pandas as pd
from normalize import NormalizeCSV

class TestNormalize(unittest.TestCase):

    def setup(self):
        normalize = NormalizeCSV("test_data/unit_test_data.csv")
        normalize.read_csv()
        return normalize

    def test_format_name(self):
        normalize = self.setup()
        normalize.format_name()
        self.assertEqual(normalize.data["FullName"][0], 'JANE DOE')

    def test_format_timestamp(self):
        normalize = self.setup()
        normalize.format_timestamp()
        self.assertEqual(normalize.data["Timestamp"][0], '2011-04-01T14:00:00-04:00')
    
    def test_helper_zipcode(self):
        normalize = NormalizeCSV("test_data/unit_test_data.csv")
        updated_zip = normalize.helper_zip_code(1)
        self.assertEqual(len(str(updated_zip)), 5)

    def test_foo_bar_total(self):
        normalize = self.setup()
        normalize.time_to_seconds("FooDuration")
        self.assertEqual(normalize.data['FooDuration'][0], 3661.0)
        normalize.time_to_seconds("BarDuration")
        self.assertEqual(normalize.data['BarDuration'][0], 3661.0)
        normalize.calc_total_duration()
        self.assertEqual(normalize.data['TotalDuration'][0], normalize.data['FooDuration'][0] + normalize.data['BarDuration'][0])

if __name__ == '__main__':
    unittest.main()