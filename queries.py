# GET_CHARACTERS = 'SELECT * FROM charactercreator_character;'

# AVG_ITEM_WEIGHT_PER_CHARACTER = '''SELECT  cc_char.name, avg( ai.weight) AS avg_item_weight from charactercreator_character AS cc_char
# JOIN charactercreator_character_inventory AS cc_inv
# ON cc_char.character_id  = cc_inv.character_id
# JOIN armory_item AS ai
# ON ai.item_id = cc_inv.item_id
# GROUP By cc_char. character_id'''

# TOTAL_CHARACTERS ='SELECT SUM(character_id) AS TOTAL_CHARACTER FROM charactercreator_character'

# TOTAL_SUBCLASS = 'SELECT SUM(mage_ptr_id) AS TOTAL_SUBCLASS FROM charactercreator_necromancer'

# TOTAL_ITEMS = 'SELECT SUM(item_id) AS TOTAL_ITEMS FROM charactercreator_character_inventory'

# WEAPONS = 'SELECT SUM(item_ptr_id) AS WEAPONS FROM armory_weapon'

# NON_WEAPONS = 'SELECT COUNT(DISTINCT cci.item_id) AS TOTAL_NON_WEAPON_ITEMS FROM charactercreator_character_inventory cci LEFT JOIN armory_weapon aw ON cci.item_id = aw.item_ptr_id WHERE aw.item_ptr_id IS NULL;'

# CHARACTER_ITEMS = 'SELECT cc.character_id, COUNT(DISTINCT  cci.item_id) AS CHARACTER_ITEMS FROM charactercreator_character cc LEFT JOIN charactercreator_character_inventory cci ON cc.character_id = cci.character_id GROUP BY cc.character_id LIMIT 20;'

# CHARACTER_WEAPONS = 'SELECT sub1.WEAPONS, sub2.TOTAL_CHARACTER FROM (SELECT SUM(item_ptr_id) AS WEAPONS FROM armory_weapon) sub1, (SELECT SUM(character_id) AS TOTAL_CHARACTER FROM charactercreator_character) sub2;'

# AVG_CHARACTER_ITEMS = 'SELECT AVG(item_count) AS avg_character_items FROM (SELECT cc.character_id, COUNT(cci.item_id) AS item_count FROM charactercreator_character cc LEFT JOIN charactercreator_character_inventory cci ON cc.character_id = cci.character_id GROUP BY cc.character_id) subquery;'

# AVG_CHARACTER_WEAPONS = '''WITH WeaponCount AS ( SELECT COUNT (item_ptr_id) AS total_weapons FROM armory_weapon),
# CHARACTERCOUNT AS ( SELECT COUNT ( character_id) AS total_characters 
# FROM charactercreator_character)
# SELECT( 1.0 * total_weapons)  / total_characters AS avg_weapons_per_character
# FROM WeaponCount, CharacterCount;'''

# CREATE_TEST_TABLE = '''CREATE TABLE IF NOT EXISTS test_table
# ("id" SERIAL NOT NULL PRIMARY KEY,
# "name" VARCHAR(200) NOT NULL,
# "age" INT NOT NULL, 
# "country_of_origin" VARCHAR(200) NOT NULL);'''

# INSERT_TEST_TABLE = '''
# INSERT INTO test_table ("name", "age", "country_of_origin")
# VALUES ('Ryan Allred', 30, 'USA');
# '''


# CREATE_CHARACTER_TABLE = '''
# CREATE TABLE IF NOT EXISTS characters
# ("character_id" SERIAL NOT NULL PRIMARY KEY,
# "name" VARCHAR(30) NOT NULL,
# "level" INT NOT NULL,
# "exp" INT NOT NULL,
# "hp" INT NOT NULL,
# "strength" INT NOT NULL,
# "intelligence" INT NOT NULL,
# "dexterity" INT NOT NULL,
# "wisdom" INT NOT NULL
# );
# '''

# INSERT_RYAN = '''
# INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
# VALUES('Ryan Allred', 50, 100, 10000, 900, 4, -5, 12);

# '''

# DROP_TEST_TABLE = '''DROP TABLE IF EXISTS test_table'''

# ROWS = 'SELECT COUNT(*) FROM titanic'

# SURVIVAL_RATE = '''SELECT survived, COUNT(*) 
# FROM titanic 
# GROUP BY survived;
# '''
# CLASS_SURVIVAL = '''SELECT pclass, 
#        100.0 * SUM(survived) / COUNT(survived) AS survival_rate 
# FROM titanic 
# GROUP BY pclass 
# ORDER BY pclass;
# '''


