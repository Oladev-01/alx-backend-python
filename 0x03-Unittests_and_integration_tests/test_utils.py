#!/usr/bin/env python3
"""unittesting"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """....Testing...."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mappping, path: Sequence,
                               expected: Any) -> None:
        """testing nested dict with inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
