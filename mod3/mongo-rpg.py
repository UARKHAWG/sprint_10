'''
Inserting rpg db into mongodb
'''
import pymongo
import sqlite3
from os import getenv
import queries as q


DBNAME = getenv('MONGO.DBNAME')
PASSWORD = getenv('MONGO.PASSWORD')


def mongo_connect(dbname=DBNAME
                , password=PASSWORD
                , collection_name='rpg_data'):
    ''' func for connecting to mongo database'''
    client = pymongo.MongoClient(f'mongodb+srv://uarkhawg:{password}@cluster0.nufpacs.mongodb.net/{dbname}?retryWrites=true&w=majority')
    mongo_db = client[dbname]
    collection = mongo_db[collection_name]
    return collection


def connect_to_db(db_name='rpg_db.sqlite3'):
    '''
    connecting to database
    '''
    return sqlite3.connect(db_name)


def execute_query(curs, query):
    '''
    return query with database as list of tuples
    '''
    return curs.execute(query).fetchall()

def doc_creation(db, sl_curs, character_table_query, item_table_query, weapon_table_query):
    '''
    create format for character insertion
    '''
    characters = execute_query(sl_curs, character_table_query)
    weapons = execute_query(sl_curs, weapon_table_query)
    for character in characters:
        item_character_query = item_table_query.format("\'%s'" % character[1])
        item_names = execute_query(sl_curs, item_character_query)
        weapons_names = []
        for item in item_names:
            if item in weapons:
                weapons_names.append(item[0])
        doc = {
            'name': character[1],
            'level': character[2],
            'exp': character[3],
            'hp': character[4],
            'strength': character[5],
            'intelligence': character[6],
            'dexterity': character[7],
            'wisdom': character[8],
            'items': item_names,
            'weapons': weapons_names
        }

        db.insert_one(doc)


def show_all(db):
    '''
    look at all the documents
    '''
    all_docs = list(db.find())
    return all_docs



if __name__ == '__main__':
    sl_conn = connect_to_db()
    sl_curs = sl_conn.cursor()
    client = mongo_connect(DBNAME, PASSWORD)
    sl_characters = execute_query(sl_conn, q.GET_CHAR_TABLE)

    # connect to collection that we want to add documents to
    db = client.rpg_data
    col = db['rpg_data']
    #col.drop({})
    doc_creation(col, sl_curs,  q.GET_CHAR_TABLE, q.GET_ITEM_TABLE, q.GET_WEAPON_TABLE)

    print(show_all(col))
