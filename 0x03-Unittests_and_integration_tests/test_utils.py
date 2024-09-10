#!/usr/bin/env python3
"""unittesting"""
import unittest
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict)
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize)


class TestAccessNestedMap(unittest.TestCase):
    """....Testing...."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        """testing nested dict with inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected_error: Any) -> None:
        """test with raise exception"""
        with self.assertRaises(expected_error):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """testing get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str,
                      json_xpected: Dict,
                      mock_get: Dict) -> None:
        """testing http call with mock object"""
        mock_response = Mock()
        mock_response.json.return_value = json_xpected
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, json_xpected)
