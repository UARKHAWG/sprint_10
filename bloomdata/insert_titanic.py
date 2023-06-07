'''
Inserting titanic.csv into PostgreSQL database
'''

import psycopg2
from os import getenv
import pandas as pd

DBNAME = getenv('DBNAME')
USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')

# make postgres conn & curs
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()

def execute_query_pg(curs, conn, query):
    results = curs.execute(query)
    conn.commit()
    return results

CREATE_TITANIC_TABLE = '''
    CREATE TABLE IF NOT EXISTS titanic_table(
        Passenger_id SERIAL PRIMARY KEY,
        Survived INT NOT NULL,
        Pclass INT NOT NULL,
        Name VARCHAR(100) NOT NULL,
        Sex VARCHAR(10) NOT NULL,
        Age FLOAT NOT NULL,
        Siblings_spouses_aboard INT NOT NULL,
        Parents_children_aboard INT NOT NULL,
        Fare FLOAT NOT NULL
    );
'''

DROP_TITANIC_TABLE = '''
    DROP TABLE IF EXISTS titanic_table;
'''

df = pd.read_csv('titanic.csv')
# remove any single quote in name
df['Name'] = df['Name'].str.replace("'",'')

if __name__ == '__main__':
    # Create table with associated schema
    # DROP table
    execute_query_pg(pg_curs, pg_conn, DROP_TITANIC_TABLE)
    # Create table
    execute_query_pg(pg_curs, pg_conn, CREATE_TITANIC_TABLE)

    records = df.values.tolist()

    for record in records:
        insert_statement = f'''
            INSERT INTO titanic_table (Survived, Pclass, Name, Sex, Age, Siblings_spouses_aboard, Parents_children_aboard, Fare)
            VALUES {tuple(record)};
        '''

        execute_query_pg(pg_curs, pg_conn, insert_statement)
