class Base_link(object):
    def __init__(self, city=None, type_of_realty=None, type_of_relation=None, is_new=None, count_of_rooms=None):
        self.BASE_URL = 'https://www.avito.ru'
        self.city = city
        self.type_of_relation = type_of_relation
        self.type_of_realty = type_of_realty
        self.is_new = is_new
        self.count_of_rooms = count_of_rooms

    def get_url(self):
        if self.is_new is not None and self.count_of_rooms is not None:
            return self.BASE_URL + '/' + self.city + '/' + self.type_of_realty + '/' + self.type_of_relation + '/' + self.count_of_rooms + '/' + self.is_new + '/'
        if self.is_new is None:
            return self.BASE_URL + '/' + self.city + '/' + self.type_of_realty + '/' + self.type_of_relation + '/'
        else:
            return self.BASE_URL + '/' + self.city + '/' + self.type_of_realty + '/' + self.type_of_relation + '/' + self.is_new + '/'


def main():
    pass


if __name__ == '__main__':
    main()
