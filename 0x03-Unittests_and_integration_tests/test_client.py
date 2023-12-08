#!/usr/bin/env python3
"""Test GithubOrgClient class"""
from typing import Dict
import unittest
from unittest.mock import PropertyMock, patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test that `GithubOrgClient` is working"""

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch('client.get_json')
    def test_org(
        self, org: str, expected_result: Dict, mock_get_json: MagicMock
    ) -> None:
        """Test that `GithubOrgClient.org` returns the correct value"""
        mock_get_json.return_value = expected_result
        client = GithubOrgClient(org)
        result = client.org
        self.assertEqual(result, expected_result)
        expected_arg = "https://api.github.com/orgs/{}".format(org)
        mock_get_json.assert_called_once_with(expected_arg)

    def test_public_repos_url(self):
        """Mock `GithubOrgClient._public_repos_url` property"""
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "login": "google",
                "id": 99999,
                "repos_url": "https://example.com/google_repos",
            }
            client = GithubOrgClient('google')
            self.assertEqual(
                client._public_repos_url, "https://example.com/google_repos"
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock):
        """Test `GithubOrgClient.public_repos`"""
        mock_get_json.return_value = [{"name": "truth"}, {"name": "flutter"}]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://example.com/google_repos"
            )
            client = GithubOrgClient('google')
            self.assertEqual(client.public_repos(), ["truth", "flutter"])

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(
        self, repo: Dict[str, Dict], license_key: str, expected: bool
    ) -> None:
        """Test that `GithubOrgClient.has_license` returns
        whether a repo has license or not
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
