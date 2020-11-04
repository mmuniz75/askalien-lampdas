import logging
import question_repository
import country_repository
import webclient
import sys


def lambda_handler(event, context):
    conn = None
    try:
        question = event["question"]
        id = event["id"]
        ip = event["ip"]

        conn = question_repository.get_connetion()
        country = get_country_from_ip(ip, conn)
        question_id = question_repository.save_question(id, question, ip, country, conn)

        answer = question_repository.get_detail(id, conn)
        answer['questionId'] = question_id
        return answer

    except Exception as inst:
        logging.error("ERROR: {}".format(inst))
        sys.exit()
    finally:
        if conn is not None:
            conn.close()


def get_country_from_ip(ip, conn):
    country = country_repository.get_country_fron_ip(ip, conn)

    if country is None:
        country = webclient.get_country_from_ip(ip)
        country_repository.save_country(ip, country, conn)

    return country

