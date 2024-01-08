"""Test module"""
import unittest
from unittest.mock import Mock
from main import parse_json


class Test(unittest.TestCase):
    """Test class"""

    def setUp(self) -> None:
        """Set up function"""
        self.json_string1 = (
            '{"key1": "Word1 word2", "key2":' ' "word2 word3", "key3": "word word"}'
        )
        self.json_string2 = "{}"
        self.json_string3 = (
            '{"key11": "Word1 word2", "key22":' ' "word2 word3", "key33": "rods rods"}'
        )
        self.parse_json = parse_json
        self.mock_function = Mock()

    def test_parsing_mock_calls1(self) -> None:
        """Test parsing function"""
        self.parse_json(
            self.json_string1,
            self.mock_function,
            ["key1", "key2", "key3"],
            ["word", "word2"],
        )
        self.assertEqual(self.mock_function.call_count, 4)

    def test_parsing_mock_calls2(self) -> None:
        """Teset mock calls"""
        self.parse_json(self.json_string2, self.mock_function, ["foo, boo"], ["foo"])
        self.assertEqual(self.mock_function.call_count, 0)

    def test_parsing_mock_calls3(self) -> None:
        """Test mock calls"""
        self.parse_json(
            self.json_string3,
            self.mock_function,
            ["key22", "key33"],
            ["word2", "word3", "rods"],
        )
        self.assertEqual(self.mock_function.call_count, 4)
