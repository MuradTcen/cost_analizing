from ..helper_scrapping import Scrapping_helper
import unittest

class TestConvertingStringToInt(unittest.TestCase):
    def test_square_meters_int(self):
        self.assertEqual(Scrapping_helper.string2float_of_square_meters(' 26 м²'), 26)

    def test_square_meters_float(self):
        self.assertEqual(Scrapping_helper.string2float_of_square_meters(' 26.54 м²'), 26.54)

if __name__ == '__main__':
    unittest.main()
