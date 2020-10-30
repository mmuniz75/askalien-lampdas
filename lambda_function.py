import logging
import repository

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    question = event["question"]
    question = format_db_search(question)
    return repository.get_questions(question)


def format_db_search(question):
    question = question.replace("\"", "'")
    question = question.replace("AND", "&")
    question = question.replace("OR", "|")
    question = question.replace("NOT", "!")
    question = question.replace("*", ":*")

    if "&" not in question and "|" not in question and "!" not in question:
        question = question.replace(" ", " | ")

    return question
