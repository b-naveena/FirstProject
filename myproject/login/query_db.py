import psycopg2
from login.conf import DB_USER ,DB_NAME ,DB_PASSWORD, DB_HOST

def update_db(cmd):
    try:
        db_conn = "dbname = %s password =%s host=%s user=%s"%(DB_NAME,DB_PASSWORD ,DB_HOST ,DB_USER)
        database = psycopg2.connect(db_conn)
        cursor = database.cursor()
        try:
            cursor.execute(cmd)
            database.commit()
        except Exception as e:
            database.rollback()
            print str(e)
        cursor.close()
        database.close()
    except Exception as e:
        print str(e)
        cursor.close()
        database.close()
