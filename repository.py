import logging
import psycopg2
import os

# db settings
db_host = os.environ.get('DB_HOST')
db_username = os.environ.get('DB_USER')
db_user_pwd = os.environ.get('DB_USER_PWD')
db_name = os.environ.get('DB_NAME')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_questions(question):
    conn = get_connetion()
    query = """select a.id,a.subject 
               from Answer a 
               where to_tsvector(subject || ' ' || content) @@ to_tsquery(%s) 
               order by ts_rank_cd(to_tsvector(subject || ' ' || content), to_tsquery(%s)) desc"""
    questions = []

    with conn.cursor() as cur:
        cur.execute(query, (question, question))
        for row in cur:
            questions.append(dict(number=row[0], question=row[1]))
        cur.close()

    conn.close()

    return questions


def get_connetion():
    conn_string = "host=%s user=%s password=%s dbname=%s" % \
                  (db_host, db_username, db_user_pwd, db_name)
    conn = psycopg2.connect(conn_string)
    return conn
