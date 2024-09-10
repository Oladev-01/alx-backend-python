#!/usr/bin/env python3
"""test GithubOrgClient"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """testing GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, test_url: str, mock_get):
        """testing org method"""
        json_expected = {"result": f"mocked call for {test_url}"}
        mock_get.return_value = json_expected
        get_client = GithubOrgClient(test_url)
        get_result = get_client.org
        expected_url = f"https://api.github.com/orgs/{test_url}"
        self.assertEqual(get_result, json_expected)
        mock_get.assert_called_once_with(expected_url)
