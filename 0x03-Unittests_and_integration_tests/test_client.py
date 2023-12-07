#!/usr/bin/env python3
"""Test GithubOrgClient class"""
from typing import Dict
import unittest
from unittest.mock import patch, MagicMock
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
