import repository


def lambda_handler(event, context):
    question = event["question"]
    id = event["id"]
    return repository.get_detail(id)
