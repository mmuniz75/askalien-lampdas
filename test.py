import unittest
import lambda_function
import logging
import sys


stream_handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)


class LampdaTestCase(unittest.TestCase):

    def test_create_user_lambda(self):
        event = {
                    "question": "zigs"
                }
        print(lambda_function.lambda_handler(event, None))


if __name__ == '__main__':
    unittest.main()