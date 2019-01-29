import requests
import json
from time import sleep
from random import uniform
from bs4 import BeautifulSoup

from src.helper_scrapping import Scrapping_helper
from src.data_carrier import Data_carrier
from src.link import Base_link

LOGGING = False


class Scrappler(object):

    @staticmethod
    def get_html(url):
        try:
            r = requests.get(url)
        except:
            print('lost connection')
            return None
        return r.text

    @staticmethod
    def get_total_pages(html):
        soup = BeautifulSoup(html, 'lxml')
        try:
            pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
        except AttributeError:
            return 1
        total_pages = pages.split('=')[1]
        return int(total_pages)

    @staticmethod
    def get_count_ads(html):
        soup = BeautifulSoup(html, 'lxml')
        count = soup.find('div', class_='page-title').find('span', class_='page-title-count').text
        return int(count)

    @staticmethod
    def get_data_from_ad(ad, logging=False, is_new='FALSE'):
        print(is_new)
        try:
            title = ad.find('div', class_='description').find(
                'h3').text.strip()
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find(
                'h3').find('a').get('href')
            try:
                avg_cost = json.loads(ad.find('div', class_='about').find('div', class_='popup-prices').get('data-prices'))[1]['currencies']['RUB']
            except Exception as e:
                print(e)
                avg_cost = 0
            tmp_soup = BeautifulSoup(Scrappler.get_html(url), 'lxml')
            lat = tmp_soup.find('div', class_='b-search-map').get('data-map-lat')
            lon = tmp_soup.find('div', class_='b-search-map').get('data-map-lon')
            try:
                count_of_rooms = Scrapping_helper.string2int_of_count_rooms(title.split(',')[0])
                square = Scrapping_helper.string2float_of_square_meters(title.split(',')[1])
            except Exception as e:
                square = 0
                print(title)
                print(e)
            if is_new == 'novostroyka':
                is_new = True
            else:
                is_new = False
        except Exception as e:
            print(e)
        data = {'title': title,
                'is_new': is_new,
                'avg_cost': avg_cost,
                'square': square,
                'count_of_rooms': count_of_rooms,
                'lat': lat,
                'lon': lon}
        if logging: print(data)
        return data

    @staticmethod
    def write_row_to_csv(row, filename, logging=False):
        Scrapping_helper.write_csv(row, filename, logging)

    @staticmethod
    def write_row_to_bd(db, row):
        db.insert_row_to_db(row)

    @staticmethod
    def get_page_data_and_write(html, logging=False, db=False, csv=False, csv_filename='tmp.csv', is_new='FALSE'):
        soup = BeautifulSoup(html, 'lxml')
        ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
        print(len(ads))
        if db: db = Data_carrier(logging)
        for ad in ads:
            Scrappler.get_pause(3, 10, logging=True)
            data = Scrappler.get_data_from_ad(ad, logging=logging, is_new=is_new)
            if db: Scrappler.write_row_to_bd(db, data)
            if csv: Scrappler.write_row_to_csv(data, csv_filename)
        if db: db.close_conn()

    @staticmethod
    def get_pause(a, b, logging=False):
        a = uniform(a, b)
        if logging: print(a)
        sleep(a)

    @staticmethod
    def main(url, logging=False, db=False, csv=False):
        html = Scrappler.get_html(url)
        total_pages = Scrappler.get_total_pages(html)
        Scrappler.get_pause(6, 10, logging=logging)
        # count = Scrappler.get_count_ads(html)
        is_new = url.split('/')[-2]
        for i in range(1, total_pages + 1):
            print('Pages proceding: ' + str(i))
            Scrappler.get_pause(6, 10, logging=logging)
            tmp_url = url + '?p=' + str(i)
            try:
                html = Scrappler.get_html(tmp_url)
            except Exception as e:
                print(e)
                continue
            Scrappler.get_page_data_and_write(html, logging=logging, db=db, csv=csv, is_new=is_new)


def main():
    # novostroyka vtorichka studii 3-komnatnye mnogokomnatnye
    # novostroyka studii
    # vtorichka studii

    # novostroyka 1-komnatnye
    # vtorichka 1-komnatnye

    # vtorichka 2-komnatnye
    # novostroyka 2-komnatnye

    # vtorichka 3-komnatnye
    # novostroyka 3-komnatnye

    # vtorichka 4-komnatnye
    # novostroyka 4-komnatnye
    # url = Base_link(city='magnitogorsk', type_of_realty='kvartiry', type_of_relation='prodam').get_url()

    # url = Base_link(city='magnitogorsk', type_of_realty='kvartiry', type_of_relation='prodam',
    #                 is_new='vtorichka', count_of_rooms='3-komnatnye').get_url()
    url = Base_link(city='magnitogorsk', type_of_realty='kvartiry', type_of_relation='prodam',
                    is_new='novostroyka', count_of_rooms='4-komnatnye').get_url()
    print(url)
    Scrappler.main(url, logging=True, db=True)


if __name__ == "__main__":
    main()
