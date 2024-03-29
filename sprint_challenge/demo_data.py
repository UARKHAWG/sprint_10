''' sqlite connection to northwind.sqlite3 and querying the data '''
import sqlite3


# SQLite connection
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


drop_table = '''
DROP TABLE IF EXISTS demo;
'''


create_demo_table = '''
    CREATE TABLE demo (
          S VARCHAR(26) NOT NULL
        , X INT NOT NULL
        , Y INT NOT NULL
    )
'''


insert_data = '''
    INSERT INTO demo (S, X, Y)
    VALUES
      ("'g'", 3, 9)
    , ("'v'", 5, 7)
    , ("'f'", 8, 7)
'''


row_count = '''
    SELECT COUNT(*)
    FROM demo;
'''


xy_at_least_5 = '''
    SELECT COUNT(*)
    FROM demo
    WHERE X >= 5;
'''


unique_y = '''
    SELECT COUNT(DISTINCT Y)
    FROM demo;
'''

curs.execute(drop_table)
print('Drop successfull')

curs.execute(create_demo_table)
print('Table created successfully')


curs.execute(insert_data)
print('Insert completed successfully')

conn.commit()
conn.close()
