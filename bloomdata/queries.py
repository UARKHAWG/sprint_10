'''
Queries MOD 1
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
