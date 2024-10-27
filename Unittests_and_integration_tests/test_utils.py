#!/usr/bin/env python3
"""Test Access Nested Map File"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test Access Nested Map Class"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Test Access Nested Map Method"""
        real_output = access_nested_map(nested_map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand(
        [
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b")
            ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """Test Access Nested Map Exception Method"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(unittest.TestCase):
    """Test Get JSON Class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        {"http://holberton.io", {"payload": False}}
    ])
    def test_get_json(self, url, payload):
        """Test Get JSON Method"""
        mock_response = Mock()
        mock_response.json.return_value = payload
        with patch('request.get', return_value=mock_response):
            real_response = get_json(url)
            self.assertEqual(real_response, payload)
            mock_response.json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
