'''
sqlite connection to northwind.sqlite3 and querying the data
'''


import sqlite3


# SQLite connection
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


results = curs.execute('''
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name;
''').fetchall()


schema_behind_any_table = curs.execute('''
    SELECT sql 
    FROM sqlite_master 
    WHERE name="Customer";
''').fetchall()


expensive_items = curs.execute('''
    SELECT *
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
''').fetchall()


avg_hire_age = curs.execute('''
    SELECT
    ROUND(AVG(ROUND((julianday(HireDate) - julianday(BirthDate)) / 365))) AS date_average
    FROM Employee;
''').fetchall()


# avg_hire_age = curs.execute('''
# SELECT
#     id,
#     HireDate,
#     BirthDate,
#     ROUND((julianday(HireDate) - julianday(BirthDate)) / 365) AS date_difference,
#     AVG(ROUND((julianday(HireDate) - julianday(BirthDate)) / 365)) AS date_average
#     FROM Employee;
# ''').fetchall()


ten_most_expensive = curs.execute('''
    SELECT ProductName, UnitPrice, CompanyName
    FROM Product
	JOIN Supplier
	ON Product.Id == Supplier.Id
    ORDER BY UnitPrice DESC
    LIMIT 10;
''').fetchall()


largest_category = curs.execute('''
    SELECT COUNT(ProductName) 'category with most unique products'
    FROM Product
    GROUP BY CategoryId
    ORDER BY COUNT(ProductName) DESC;
''').fetchall()
