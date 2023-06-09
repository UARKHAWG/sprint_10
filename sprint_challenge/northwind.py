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
    SELECT AVG(HireDate - BirthDate)
    FROM Employee;
''').fetchall()


ten_most_expensive = curs.execute('''
    SELECT Product.ProductName
    , Product.UnitPrice
    , Supplier.CompanyName
    FROM Product, Supplier
    WHERE Product.SupplierId = Supplier.Id
    ORDER BY Product.UnitPrice DESC
    LIMIT 10;
''').fetchall()


largest_category = curs.execute('''
SELECT Category.CategoryName, COUNT(DISTINCT Product.Id)
FROM Category, Product
WHERE Category.Id = Product.CategoryId
GROUP BY 1 ORDER BY 2 DESC
LIMIT 1;
''').fetchall()
