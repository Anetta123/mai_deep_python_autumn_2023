import unittest
import argparse
from unittest.mock import patch
import server
import client


class Test_Server(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_get_words_from_url_valid(self):
        """ Testing get_words_from_url function with valid url """
        url = "https://academy.yandex.ru/handbook/ml"
        words = server.get_words_from_url(url)
        self.assertIsInstance(words, list)

    def test_get_wrods_from_url_nonvalid(self):
        """ Testing get_words_from_url function with nonvalid url """
        url = "https://acdemy.yandex.ru/handbook/ml"
        words = server.get_words_from_url(url)
        self.assertTrue(len(words) == 0)


class Test_Client(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @patch('argparse.ArgumentParser.parse_args')
    def test_parse_flags(self, mock_args):
        """ Parse_flags function test """
        mock_args.return_value = argparse.Namespace(urls='urls.txt', threads=5)

        urls, threads = client.parse_flags()
        self.assertEqual(urls, 'urls.txt')
        self.assertEqual(threads, 5)
