import unittest
from ..helper_scrapping import Scrapping_helper


class TestConvertingStringToInt(unittest.TestCase):
    def test_studio(self):
        self.assertEqual(Scrapping_helper.string2float_of_count_rooms('Студия'), 0)

    def test_four_roomes(self):
        self.assertEqual(Scrapping_helper.string2int_of_count_rooms('4-к квартира'), 4)

    def test_more_nine_rooms(self):
        self.assertEqual(Scrapping_helper.string2int_of_count_rooms('> 9-к квартира'), -1)


if __name__ == '__main__':
    unittest.main()
