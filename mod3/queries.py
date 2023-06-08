'''
Queries MOD 3
'''


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
