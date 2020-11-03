import unittest
import lambda_function
import lambda_function2
import logging
import sys


stream_handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)


class LampdaTestCase(unittest.TestCase):

    def test_list_questions(self):
        event = {
                    "question": "mars AND moon"
                }
        print(lambda_function.lambda_handler(event, None))

    def test_get_detail(self):
        event = {
            "id" : 500,
            "question": "mars AND moon",
            "ip" : "1.1.187.76"
        }
        print(lambda_function2.lambda_handler(event, None))


if __name__ == '__main__':
    unittest.main()