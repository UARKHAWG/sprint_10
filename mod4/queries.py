'''
Queries MOD 4
'''


TOTAL_SURVIVED = '''
    SELECT SUM(survived)
    FROM titanic_table;
'''


TOTAL_DIED = '''
    SELECT COUNT(*) AS died
    FROM titanic_table
    WHERE survived = 0;
'''


TOTAL_PASSENGERS_BYCLASS = '''
    SELECT pclass, COUNT(*) total_passengers_byclass
    FROM titanic_table
    GROUP BY pclass;
'''


TOTAL_SURVIVED_BYCLASS = '''
    SELECT pclass, COUNT(*) total_survived_byclass
    FROM titanic_table
    WHERE survived = 1
    GROUP BY pclass;
'''


TOTAL_DIED_BYCLASS = '''
    SELECT pclass, COUNT(*) total_died_byclass
    FROM titanic_table
    WHERE survived = 0
    GROUP BY pclass;
'''


AVG_AGE_SURVIVED = '''
    SELECT AVG(age)
    FROM titanic_table 
    WHERE survived = 1;
'''


AVG_AGE_DIED = '''
    SELECT AVG(age)
    FROM titanic_table 
    WHERE survived = 0;
'''


AVG_AGE_CLASS = '''
    SELECT pclass, AVG(age)
    FROM titanic_table 
    GROUP BY pclass;
'''


FARE_PER_CLASS = '''
    SELECT pclass, AVG(fare)
    FROM titanic_table 
    GROUP BY pclass;
'''


FARE_PER_OUTCOME = '''
    SELECT survived, AVG(fare)
    FROM titanic_table 
    GROUP BY survived;
'''


SIB_SPOUSE_SURVIVED = '''
    SELECT survived, AVG(siblings_spouses_aboard)
    FROM titanic_table 
    GROUP BY survived;
'''


SIB_SPOUSE_CLASS = '''
    SELECT pclass, AVG(siblings_spouses_aboard)
    FROM titanic_table 
    GROUP BY pclass;
'''

PARENT_CHILD_CLASS = '''
    SELECT pclass, AVG(parents_children_aboard)
    FROM titanic_table
    GROUP BY pclass;
'''


PARENT_CHILD_SURVIVAL = '''
    SELECT survived, AVG(parents_children_aboard)
    FROM titanic_table
    GROUP BY survived;
'''

UNIQUE_PASSENGER_NAMES = '''
    SELECT COUNT(DISTINCT name)
    FROM titanic_table;
'''


QUERY_LIST = [
      TOTAL_SURVIVED
    , TOTAL_DIED
    , TOTAL_PASSENGERS_BYCLASS
    , TOTAL_SURVIVED_BYCLASS
    , TOTAL_DIED_BYCLASS
    , AVG_AGE_SURVIVED
    , AVG_AGE_DIED
    , AVG_AGE_CLASS
    , FARE_PER_CLASS
    , FARE_PER_OUTCOME
    , SIB_SPOUSE_SURVIVED
    , SIB_SPOUSE_CLASS
    , PARENT_CHILD_CLASS
    , PARENT_CHILD_SURVIVAL
    , UNIQUE_PASSENGER_NAMES
]


###############################
# MONGO DB QUERIES
###############################

class MongoAnswers():
    '''
    querying mongodb
    '''
    def __init__(self, col):
        # get all docs
        self.col = col
        self.characters = list(col.find({}))


    def total_characters(self):
        return len(self.characters)


    def total_items(self):
        count = 0
        for character in self.characters:
            count += len(character['items'])
        return count


    def total_weapons(self):
        count = 0
        for character in self.characters:
            count += len(character['weapons'])
        return count


    def total_non_weapons(self):
        return self.total_items() - self.total_weapons()


    def character_items(self):
        item_list = []
        for character in self.characters[:20]:
            num_item = len(character['items'])
            item_list.append((character['name'], num_item))
        return item_list


    def character_weapons(self):
        weapon_list = []
        for character in self.characters[:20]:
            num_weapons = len(character['weapons'])
            weapon_list.append((character['name'], num_weapons))
        return weapon_list


    def average_items(self):
        num_items = []
        for character in self.characters:
            num_items.append(len(character['items']))
        return (sum(num_items) / len(num_items))


    def average_weapons(self):
        num_weapons = []
        for character in self.characters:
            num_weapons.append(len(character['weapons']))
        return (sum(num_weapons) / len(num_weapons))


    def show_results(self):
        return f'''
              Total Number of Characters: {self.total_characters()}
              Total Number of items: {self.total_items()}
              Total Number of weapons: {self.total_weapons()}
              Total Number of non-weapons: {self.total_non_weapons()}
              Total Number of items per character: {self.character_items()}
              Total Number of weapons per character: {self.character_weapons()}
              Average Number of items: {self.average_items()}
              Average Number of weapons: {self.average_weapons()}
              '''
