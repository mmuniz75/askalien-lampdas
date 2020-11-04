import question_repository


def lambda_handler(event, context):
    id = event["id"]
    creator = event["creator"]
    email = event["email"]
    feedback = event["feedback"]

    question_repository.add_feedback(id, creator, email, feedback)

    return {"statusCode": 200}
