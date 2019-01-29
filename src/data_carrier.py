import MySQLdb
import os
from src.fixtures import sample_row


class Data_carrier():

    def __init__(self, logging=False):
        try:
            env = os.environ['CLEARDB_DATABASE_URL']
            self.USERNAME = env.split('@')[0].split('//')[1].split(':')[0]
            self.PASSWORD = env.split('@')[0].split('//')[1].split(':')[1]
            self.SERVER = env.split('@')[1].split('?')[0].split('/')[0]
            self.DATABASE = env.split('@')[1].split('?')[0].split('/')[1]
        except Exception as e:
            print(e)
        self.conn = MySQLdb.connect(self.SERVER, self.USERNAME, self.PASSWORD, self.DATABASE, charset='utf8')
        self.logging = logging
        self.cursor = self.conn.cursor()

    def close_conn(self):
        self.conn.close()

    def insert_row_to_db(self, row):

        # query = "insert into '%s' (title, is_new, avg_cost, count_of_rooms, lat, lon, date) values(%s,%s, $s, %s, %s, %s, now())", (
        #     'flat', data['title'], data['is_new'], data['avg_cost'], data['count_of_rooms'], data['lat'], data['lon'])
        try:

            self.cursor.execute(
                "insert into flat (title, is_new, avg_cost, square, count_of_rooms, lat, lon, date) values(%s,%s, %s, %s, %s, %s, %s, now())",
                (
                    row['title'], row['is_new'], row['avg_cost'], row['square'], row['count_of_rooms'], row['lat'],
                    row['lon']))
            self.conn.commit()
            if self.logging: print('row added to db')
        except Exception as e:
            print(e)
            self.conn.rollback()

    def get_stat_from_db(self):
        result = []
        try:
            self.cursor.execute(
                'select round(avg(square), 2), round(avg(avg_cost)), count_of_rooms, round(avg(avg_cost)*avg(square)) as avg_total, count(*) from flat group by count_of_rooms, is_new;')
            rows = self.cursor.fetchall()
            for row in rows:
                # print(row)
                result.append({'avg_square': row[0],
                               'avg_cost_per_square': row[1],
                               'avg_total': row[2],
                               'count': row[3]})
            print(result)
            if self.logging: print('stats grabbed, sir')
        except Exception as e:
            print(e)
        return result


def insert_to_db_stat(self, row):
    pass


def main():
    # db = Data_carrier(logging=True)
    # print(db.get_stat_from_db())
    # db.close_conn()
    print(os.environ['CLEARDB_DATABASE_URL'])


if __name__ == '__main__':
    main()
