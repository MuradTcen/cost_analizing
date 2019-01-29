import csv
import re


class Scrapping_helper(object):

    @staticmethod
    def string2int_of_count_rooms(str):
        if str == "Студия":
            return 0
        elif str == "> 9-к квартира":
            return -1
        else:
            return int(str[0])

    @staticmethod
    def string2float_of_square_meters(str):
        result = re.findall('\d+.?\d*', str)[0]
        return float(result)

    @staticmethod
    def write_csv(data, filename, logging=False):
        with open(filename, 'a', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow((data['title'],
                             data['is_new'],
                             data['avg_cost'],
                             data['count_of_rooms'],
                             data['lat'],
                             data['lon']))
            if logging: print('row writed to csv')


