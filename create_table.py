import logging
import psycopg2
from psycopg2 import Error

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

URL = input("Enter DATABASE_URL : ")

try:
    conn = psycopg2.connect(URL)
    cur = conn.cursor()
    sql = "CREATE TABLE users (uid bigint, sudo boolean DEFAULT FALSE);"
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    print("Done !")
except Error as e :
    LOGGER.error(e)
    exit(1)
        