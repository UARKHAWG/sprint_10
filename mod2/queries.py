'''
Queries MOD 2
'''


CREATE_TEST_TABLE = '''
    CREATE TABLE IF NOT EXISTS test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL,
    "age" INT NOT NULL,
    "country" VARCHAR(200) NOT NULL);
'''


INSERT_TEST_TABLE = '''
    INSERT INTO test_table ("name", "age", "country")
    VALUES ('John Dough', 30, 'Sweden');
'''


DROP_TEST_TABLE = '''
    DROP TABLE IF EXISTS test_table;
'''


CREATE_CHARACTER_TABLE = '''
    CREATE TABLE IF NOT EXISTS characters
    ("character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "level" INT NOT NULL,
    "exp" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dexterity" INT NOT NULL,
    "wisdom" INT NOT NULL);
'''


INSERT_JOHN = '''
    INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
    VALUES ('John Dough', 100, 1, 100, 1000, 7777, 1000, 77);
'''


DROP_CHARACTER_TABLE = '''
    DROP TABLE IF EXISTS test_table;
'''


GET_CHARACTERS = '''
    SELECT *
    FROM charactercreator_character;
'''
