import logging
import psycopg2
import os
import datetime

# db settings
db_host = os.environ.get('DB_HOST')
db_username = os.environ.get('DB_USER')
db_user_pwd = os.environ.get('DB_USER_PWD')
db_name = os.environ.get('DB_NAME')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_country_fron_ip(ip, conn):
    query = """select country 
               from country 
               where ip=%s"""

    country = None

    with conn.cursor() as cur:
        cur.execute(query, (ip,))
        row = cur.fetchone()

        if row is not None:
            country = row[0]

        cur.close()

    return country


def save_country(ip, country, conn):
    sql = """insert into country (ip, country) 
             values (%s,%s)"""

    with conn.cursor() as cur:
        cur.execute(sql, (ip, country))
        conn.commit()
        cur.close()

    logger.info(sql.replace("%s", "{}").format(ip, country))


def get_connetion():
    conn_string = "host=%s user=%s password=%s dbname=%s" % \
                  (db_host, db_username, db_user_pwd, db_name)
    conn = psycopg2.connect(conn_string)
    return conn
