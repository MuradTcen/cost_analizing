from ..link import Base_link
import unittest


class TestGettingLinks(unittest.TestCase):
    def test_getting_vtoricka(self):
        self.assertEqual(Base_link(city='magnitogorsk', type_of_realty='kvartiry', type_of_relation='prodam',
                                   is_new='vtorichka').get_url(),
                         'https://www.avito.ru/magnitogorsk/kvartiry/prodam/vtorichka/')

    def test_getting_city_kvartity_prodam_link(self):
        self.assertEqual(Base_link(city='magnitogorsk', type_of_realty='kvartiry', type_of_relation='prodam').get_url(),
                         'https://www.avito.ru/magnitogorsk/kvartiry/prodam/')

    def test_getting_city_kvartity_prodam_studii_vtorichka_link(self):
        self.assertEqual(Base_link(city='magnitogorsk', type_of_realty='kvartiry', type_of_relation='prodam',
                                   count_of_rooms='studii', is_new='vtorichka').get_url(),
                         'https://www.avito.ru/magnitogorsk/kvartiry/prodam/studii/vtorichka/')

    def test_getting_city_kvartity_prodam_3_komnatnye_novostroyka_link(self):
        self.assertEqual(Base_link(city='magnitogorsk', type_of_realty='kvartiry', type_of_relation='prodam',
                                   count_of_rooms='3-komnatnye', is_new='novostroyka').get_url(),
                         'https://www.avito.ru/magnitogorsk/kvartiry/prodam/3-komnatnye/novostroyka/')

    def test_getting_city_kvartity_prodam_mnogokomnatnye_novostroyka_link(self):
        self.assertEqual(Base_link(city='magnitogorsk', type_of_realty='kvartiry', type_of_relation='prodam',
                                   count_of_rooms='3-komnatnye', is_new='novostroyka').get_url(),
                         'https://www.avito.ru/magnitogorsk/kvartiry/prodam/mnogokomnatnye/novostroyka/')


if __name__ == '__main__':
    unittest.main()
