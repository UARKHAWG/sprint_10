'''
Queries
'''

SELECT_ALL = '''
    SELECT *
    FROM charactercreator_character;
'''

TOTAL_CHARACTERS = '''
    SELECT COUNT(*) 
    FROM charactercreator_character;
'''

TOTAL_SUBCLASS = '''
    SELECT COUNT(*) as necromancers
	FROM charactercreator_necromancer;
'''

TOTAL_ITEMS = '''
    SELECT COUNT(*) as total_items
	FROM armory_item;
'''

WEAPONS = '''
    SELECT COUNT(*)
    FROM armory_weapon;
'''

NON_WEAPONS = '''
    SELECT COUNT(*)
	FROM armory_item
	LEFT JOIN armory_weapon
	ON armory_item.item_id = armory_weapon.item_ptr_id
	WHERE armory_weapon.power IS NULL;
'''

CHARACTER_ITEMS = '''
    SELECT name, COUNT(item_id)
    FROM charactercreator_character
    JOIN charactercreator_character_inventory
    ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	GROUP BY charactercreator_character.character_id
    LIMIT 20;
'''

CHARACTER_WEAPONS = '''
    SELECT charactercreator_character.name, COUNT(armory_item.item_id) AS total_weapons
    FROM armory_item
	JOIN armory_weapon
	ON armory_item.item_id = armory_weapon.item_ptr_id
	JOIN charactercreator_character_inventory
	ON armory_item.item_id = charactercreator_character_inventory.item_id
	JOIN charactercreator_character
	ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	GROUP BY charactercreator_character.character_id
    LIMIT 20;
'''

AVG_CHARACTER_ITEMS = '''
    SELECT AVG(char_items) 
	FROM
	(SELECT name, COUNT(item_id) AS char_items
    FROM charactercreator_character
    JOIN charactercreator_character_inventory
    ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	GROUP BY charactercreator_character.character_id);
'''

AVG_CHARACTER_WEAPONS = '''
    SELECT AVG(total_weapons) 
	FROM
	(SELECT charactercreator_character.name, COUNT(armory_item.item_id) AS total_weapons
    FROM armory_item
	JOIN armory_weapon
	ON armory_item.item_id = armory_weapon.item_ptr_id
	JOIN charactercreator_character_inventory
	ON armory_item.item_id = charactercreator_character_inventory.item_id
	JOIN charactercreator_character
	ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	GROUP BY charactercreator_character.character_id);
'''

AVG_ITEM_WEIGHT_PER_CHARACTER ='''
    SELECT charactercreator_character.name, AVG(armory_item.weight)
    FROM charactercreator_character
    JOIN charactercreator_character_inventory
    ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
    JOIN armory_item
    ON armory_item.item_id = charactercreator_character_inventory.item_id
    GROUP BY charactercreator_character.character_id;
'''

QUERY_LIST = [TOTAL_CHARACTERS
              , TOTAL_SUBCLASS
              , TOTAL_ITEMS
              , WEAPONS
              , NON_WEAPONS
              , CHARACTER_ITEMS
              , CHARACTER_WEAPONS
              , AVG_CHARACTER_ITEMS
              , AVG_CHARACTER_WEAPONS
              , AVG_ITEM_WEIGHT_PER_CHARACTER]
#####################################
# Mod 2
#####################################
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
####################################
# MOD 3
####################################

GET_CHAR_TABLE = '''
    SELECT *
    FROM charactercreator_character;
'''

GET_ITEM_TABLE = '''
    SELECT armory_item.name
    FROM (
    SELECT *
    FROM charactercreator_character
    JOIN charactercreator_character_inventory
    ON charactercreator_character.character_id = charactercreator_character_inventory.character_id) AS char_ci
    JOIN armory_item
    ON armory_item.item_id = char_ci.item_id
    AND char_ci.name = {};
'''

GET_WEAPON_TABLE = '''
    SELECT aw_ai.name
    FROM (
    SELECT *
    FROM armory_item
    JOIN armory_weapon
    WHERE armory_item.item_id = armory_weapon.item_ptr_id) aw_ai
    JOIN (
    SELECT *
    FROM charactercreator_character
    JOIN charactercreator_character_inventory
    WHERE charactercreator_character.character_id = charactercreator_character_inventory.character_id) as char_ci
    WHERE aw_ai.item_id = char_ci.item_id;
'''
