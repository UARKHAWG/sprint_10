'''
buddymove_holidayiq database conn and queries
'''

import sqlite3
import pandas as pd

# SQLite connection
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# load in CSV to pandas DataFrame
df = pd.read_csv('buddymove_holidayiq.csv')

if __name__ == '__main__':
    # turn DF into a table 'review'
    df.to_sql('review', conn, if_exists='replace')

    # query
    curs.execute('''SELECT * FROM review;''')
    print(curs.fetchall())

    # num of rows
    TOTAL_ROWS = '''
        SELECT COUNT(*)
        FROM review;
    '''

    # nature & shopping both >= 100
    NATURE_SHOPPING='''
        SELECT COUNT(*) AS greater_100
        FROM review
        WHERE Nature >= 100 AND Shopping >= 100;
    '''

    # average num of reviews for each category
    AVG_NUM_REV = '''
        SELECT 'index'
        , AVG(review.Nature)
        , AVG(review.Picnic)
        , AVG(review.Religious)
        , AVG(review.Shopping)
        , AVG(review.Sports)
        , AVG(review.Theatre)
        FROM review

    '''
    