'''
PostgreSQL DB connection, cursor, return results 
'''


import psycopg2
from os import getenv
from queries import QUERY_LIST


DBNAME = getenv('DBNAME')
USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')


# make postgres conn & curs
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()


def execute_query_pg(curs, conn, query):
    '''
    connect to postgreSQL db an get results
    '''
    pg_curs.execute(query)
    return pg_curs.fetchall()


def execute_queries(curs, conn, queries):
    '''
    func to execute queries and store in dict
    '''
    answers_dict = {}
    for index, query in enumerate(queries):
        answers_dict[index] = execute_query_pg(curs, conn, query)
    return answers_dict


if __name__ == '__main__':
    answers_dict = execute_queries(pg_conn, pg_curs, QUERY_LIST)
    for index, value in enumerate(answers_dict.values()):
        print(f'{index}: {value}')
