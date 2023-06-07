'''
Inserting rpg database into PostgreSQL database
'''
import sqlite3
import csv
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

def sqlite_to_csv(rpg_db.sqlite3, charactercreator_character, charactercreator_character.csv):
    conn = sqlite3.connect(rpg_db)
    cursor = conn.cursor()

    cursor.execute(f'SELECT * from {charactercreator_character}')
    rows = cursor.fetchall()

CREATE_CC_CHAR_TABLE = '''
    CREATE TABLE IF NOT EXISTS charactercreator_character(
        character_id SERIAL PRIMARY KEY,
        name VARCHAR(30) NOT NULL,
        level INT NOT NULL,
        exp VARCHAR(100) NOT NULL,
        hp VARCHAR(10) NOT NULL,
        strength INT NOT NULL,
        intelligence INT NOT NULL,
        dexterity INT NOT NULL,
        wisdom INT NOT NULL
    );
'''

CREATE_CC_INV = '''
    CREATE TABLE IF NOT EXISTS charactercreator_character_inventory(
        id SERIAL PRIMARY KEY,
        character_id INT NOT NULL,
        item_id INT NOT NULL
    );
'''



if __name__ == '__main__':
    # Create table with associated schema
    # create charactercreator_character table
    execute_query_pg(pg_curs, pg_conn, CREATE_CC_CHAR_TABLE)
    # Create  charactercreator_character_inventory table
    execute_query_pg(pg_curs, pg_conn, CREATE_CC_INV)

    characters = df.values.tolist()

    for character in characters:
        insert_statement = f'''
            INSERT INTO charactercreator_character (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES {tuple(character)};
        '''
        # .format(tuple(record))

        execute_query_pg(pg_curs, pg_conn, insert_statement)
