#!/usr/bin/env python3
"""test GithubOrgClient"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """testing public repos"""
        test_payload = [
            {"name": "soap", "license": {"key": "Nafdac"}},
            {"name": "open_source", "license": {"key": "Mit"}},
            {"name": "water", "license": {"key": "None"}}
        ]
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_repo:  # noqa
            expected_url = "https://api.github.com/orgs/google/repos"
            mock_repo.return_value = expected_url
            mock_get.return_value = test_payload
            get_client = GithubOrgClient("abc")
            get_result = get_client.public_repos(license="Nafdac")
            self.assertEqual(get_result, ["soap"])
            mock_repo.assert_called_once()
            mock_get.assert_called_once_with(expected_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_return):
        """testing has_client"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected_return)  # noqa


    org_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
    repos_payload = [
        "license": {
        "key": "bsl-1.0",
        "name": "Boost Software License 1.0",
        "spdx_id": "BSL-1.0",               
        "url": "https://api.github.com/licenses/bsl-1.0",
        "node_id": "MDc6TGljZW5zZTI4"
        },

        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
          "spdx_id": "Apache-2.0",
          "url": "https://api.github.com/licenses/apache-2.0",
          "node_id": "MDc6TGljZW5zZTI="
        }
    ]
    expected_repos = ['episodes.dart', 'cpp-netlib', 'dagger', 'ios-webkit-debug-proxy', 'google.github.io', 'kratu', 'build-debian-cloud', 'traceur-compiler', 'firmata.py'],
    apache2_repos = ["https://api.github.com/licenses/bsl-1.0", "https://api.github.com/licenses/apache-2.0"]
    @parameterized_class([
        {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache_repos": apache2_repos}
    ])
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """testing public_repos in integration"""
        @classmethod
        def setUpClass(self):
            cls.get_patcher = patch('requests.get')
            cls.mock_get = cls.get_patcher.start()

        def tearDownClass(self):

