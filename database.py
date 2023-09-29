import psycopg2
import os


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(host='26.149.55.96',
                                           database='Cifra',
                                           user=os.environ['postgres'],
                                           password=os.environ['1234'])

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.connection.cursor()