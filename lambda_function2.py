import logging
import question_repository
import sys


def get_country_from_ip(ip):
    return "Not implemented"


def lambda_handler(event, context):
    conn = None
    try:
        question = event["question"]
        id = event["id"]
        ip = event["ip"]

        country = get_country_from_ip(ip)

        conn = question_repository.get_connetion()
        question_repository.save_question(id, question, ip, country, conn)

        return question_repository.get_detail(id, conn)

    except Exception as inst:
        logging.error("ERROR: {}".format(inst))
        sys.exit()
    finally:
        if conn is not None:
            conn.close()

