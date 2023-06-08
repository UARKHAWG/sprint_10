import pymongo
from os import getenv
from queries import MongoAnswers

DBNAME = getenv('MONGO.DBNAME')
PASSWORD = getenv('MONGO.PASSWORD')


client = pymongo.MongoClient(f'mongodb+srv://uarkhawg:{PASSWORD}@cluster0.nufpacs.mongodb.net/{DBNAME}?retryWrites=true&w=majority')
db = client.rpg_data.rpg_data.rpg_data
col = db['rpg_data']

#instantiate our class with our characters attribute and query methods
mongo_answers = MongoAnswers(col)


if __name__ == '__main__':
    print(mongo_answers.show_results())
