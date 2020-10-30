import logging
import repository

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    question = event["question"]

    return repository.get_questions(question)