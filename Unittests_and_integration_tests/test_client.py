#!/usr/bin/env python3
"""Test Client File"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Test Github Org Client Class"""

    @parameterized.expand(
        [
            ("google", {"name": "Google", "id": 1}),
            ("abc", {"name": "ABC Corp", "id": 2}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, test_org, expected_output, mock_json):
        """Test Org Method"""
        mock_json.return_value = expected_output

        client = GithubOrgClient(test_org)

        org_data = client.org

        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{test_org}")

        self.assertEqual(org_data, expected_output)


if __name__ == "__main__":
    unittest.main()
