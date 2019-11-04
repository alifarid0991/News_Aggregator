# Create your tests here.
from random import randint

from django.test import TestCase
from django.test import Client
import requests
import time
import logging

logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO)


class Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
        response = requests.get(word_site)
        words = response.content.splitlines()  # give dictionary words for testing from above api
        for i in range(0, 500):
            word = str(words[randint(0, 100)])
            start = time.time()
            response = self.client.get('/news/?query={}'.format(word))
            finish = time.time()

            logging.info(
                "request {} took: {} seconds".format(str(i), str(finish - start)))  # show the duration of each request
            logging.info(
                "search key : {} ".format(word)
            )
            logging.info(
                "response is : {} \n".format(response.content.decode('utf-8'))
            )
            self.assertEqual(response.status_code, 200)
