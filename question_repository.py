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


def get_detail(id, conn):
    query = """select  a.id,
                       content,
                       videonumber as number,
                       creationdate as date,
                       url as link 
                       from Answer a INNER JOIN Video v on (a.videonumber=v.id)
               where a.id=%s"""

    with conn.cursor() as cur:
        cur.execute(query, (id, ))
        row = cur.fetchone()
        answer = {
            'id' : row[0],
            "content": row[1],
            "number": row[2],
            "date": row[3].strftime("%m/%d/%Y"),
            "link": row[4]
        }
        cur.close()

    return answer


def save_question(id, question, ip, country, conn):
    sql = """insert into question (answer_id, text, ip, country, creationdate) 
             values (%s,%s,%s,%s,%s)"""

    date = str(datetime.datetime.now())

    with conn.cursor() as cur:
        cur.execute(sql, (id, question, ip, country, date))
        conn.commit()
        cur.close()

    logger.info(sql.replace("%s", "{}").format(id, question, ip, country, date))


def add_feedback(id, creator, email, feedback):
    sql = """update question
             set creator=%s,
                 email=%s,
                 feedback=%s 
             where id=%s"""

    conn = get_connetion()

    with conn.cursor() as cur:
        cur.execute(sql, (creator, email, feedback, id))
        conn.commit()
        cur.close()

    conn.close()
    logger.info(sql.replace("%s", "{}").format(creator, email, feedback, id))


def get_connetion():
    conn_string = "host=%s user=%s password=%s dbname=%s" % \
                  (db_host, db_username, db_user_pwd, db_name)
    conn = psycopg2.connect(conn_string)
    return conn
