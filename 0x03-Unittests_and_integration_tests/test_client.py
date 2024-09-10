#!/usr/bin/env python3
"""test GithubOrgClient"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
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

    def test_public_repos_url(self):
        """testing the public repo property"""
        test_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}  # noqa
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_props:  # noqa
            mock_props.return_value = test_payload
            test_client = GithubOrgClient("google")
            get_result = test_client._public_repos_url
            self.assertEqual(get_result, test_payload["repos_url"])
