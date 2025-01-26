import pymysql
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # Test Code
    load_dotenv()

    HOST_ENV = os.getenv("mysql_host")
    USER_ENV = os.getenv("mysql_user")
    PASSWORD_ENV = os.getenv("mysql_password")
    DB_ENV = os.getenv("mysql_db")
    CHARSET_ENV = os.getenv("mysql_charset")

    # Connect DB
    conn = pymysql.connect(
            host=HOST_ENV,
            user=USER_ENV,
            password=PASSWORD_ENV,
            db=DB_ENV,
            charset=CHARSET_ENV
            )
    
    # Make Cursor
    cur = conn.cursor()

    # Test SQL
    sql = "select * from testusertable"

    # Execute SQL
    cur.execute(sql)

    # Print 
    for row in cur:
        print(row[0], row[1], row[2], row[3])

    # Close Connection
    conn.close()
