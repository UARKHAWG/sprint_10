'''
Sprint 10 Mod 3 Mongo Database
'''

import pymongo
from sqlite_example import connect_to_db, execute_q
import queries as q
from os import getenv

DBNAME ='test'
PASSWORD = getenv('MONGO.PASSWORD')

def mongo_connect(dbname=DBNAME
                , password=PASSWORD
                , collection_name='characters'):
    ''' func for connecting to mongo database'''
    client = pymongo.MongoClient(f'mongodb+srv://uarkhawg:{password}@cluster0.05rk49j.mongodb.net/{dbname}?retryWrites=true&w=majority')
    mongo_db = client[dbname]
    collection = mongo_db[collection_name]
    return collection

test_characters = [
    (1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1),
    (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1),
    (3, 'Minus c', 0, 0, 10, 1, 1, 1, 1),
    (4, 'Sit ut repr', 0, 0, 10, 1, 1, 1, 1),
    (5, 'At id recusandae expl', 0, 0, 10, 1, 1, 1, 1)
]


characters_documents = [
{
    'character_id': 1,
    'name': 'Aliquid iste optio reiciendi',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom': 1,
},
{
    'character_id': 1,
    'name': 'Optio dolorem ex a',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom': 1,
}
]

if __name__ == '__main__':
    # Get data from SQLite
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn, q.SELECT_ALL)
    #print(sl_characters[:3])

    # connect to specific mongodb collection
    collection = mongo_connect(collection_name='characters')

    for character in sl_characters:
        doc = {
        'character_id': character[0],
        'name': character[1],
        'level': character[2],
        'exp': character[3],
        'hp': character[4],
        'strength': character[5],
        'intelligence': character[6],
        'dexterity': character[7],
        'wisdom': character[8],
        }
    collection.insert_one(doc)
    # result = collection.find_one({'name': 'John'})
    # print(result)
