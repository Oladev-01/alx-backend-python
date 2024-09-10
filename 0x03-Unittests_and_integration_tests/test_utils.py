#!/usr/bin/env python3
"""testing utils"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json, memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """testing utils"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nest_map, path, expected):
        """testing access_nested_map"""
        self.assertEqual(access_nested_map(nest_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """testing access_nested_map"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """testing json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, expect, get_mock):
        """testing json"""
        mock_response = Mock()
        mock_response.json.return_value = expect
        get_mock.return_value = mock_response
        get_result = get_json(url)
        self.assertEqual(get_result, expect)
