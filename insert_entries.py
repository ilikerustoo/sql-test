import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_membership(conn, membership):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO membership(member,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, membership)
    conn.commit()
    return cur.lastrowid


def main():
    database = "membership2.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        # membership = ('M1', '1-01-2017', '11-20-2017')
        # membership = ('M1', '12-31-2017', '02-01-2018')
        # membership = ('M1', '02-15-2018', '04-30-2018')
        # membership = ('M1', '06-10-2018', '12-31-2018')

        # membership = ('M2', '01-01-2017', '11-20-2017')
        # membership = ('M2', '12-31-2017', '02-01-2018')
        
        # membership = ('M3', '02-15-2018', '04-30-2018')
        # membership = ('M3', '06-10-2018', '12-31-2018')

        # membership = ('M4', '1-01-2017', '11-20-2017')
        # membership = ('M4', '12-31-2017','02-01-2018')

        # membership = ('M5', '02-15-2018', '04-30-2018')
        # membership = ('M5', '06-10-2018', '12-31-2018')

        # membership = ('M6', '01-01-2017', '12-31-2019')

        # membership = ('M7', '12-31-2017', '12-30-2018')

        # membership = ('M8', '01-01-2019', '06-30-2020')

        # membership = ('M9', '06-30-2018', '01-31-2020')

    #####################

        # membership2 = ('M1', '2017-01-01', '2017-11-20')
        # membership2 = ('M1', '2017-12-31', '2018-02-01')
        # membership2 = ('M1', '2018-02-15', '2018-04-30')
        # membership2 = ('M1', '2018-06-10', '2018-12-31')

        # membership2 = ('M2', '2017-01-01', '2017-11-20')
        # membership2 = ('M2', '2017-12-31', '2018-02-01')
        
        # membership2 = ('M3', '2018-02-15', '2018-04-30')
        # membership2 = ('M3', '2018-06-10', '2018-12-31')

        # membership2 = ('M4', '2017-01-01', '2017-11-20')
        # membership2 = ('M4', '2017-12-31','2018-02-01')

        # membership2 = ('M5', '2018-02-15', '2018-04-30')
        # membership2 = ('M5', '2018-06-10', '2018-12-31')

        # membership2 = ('M6', '2017-01-01', '2019-12-31')

        # membership2 = ('M7', '2017-12-31', '2018-12-30')

        # membership2 = ('M8', '2019-01-01', '2020-06-30')

        # membership2 = ('M9', '2018-06-30', '2020-01-31')




        membership_id = create_membership(conn, membership2)

if __name__ == '__main__':
    main()