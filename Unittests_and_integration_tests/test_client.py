#!/usr/bin/env python3
"""Test Client File"""

import unittest
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test Github Org Client Class"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, test_org, mock_json):
        """Test Org Method"""
        client = GithubOrgClient(test_org)
        client.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{test_org}")

    def test_public_repos_url(self):
        """Test Public Repos Url Method"""
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value={"repos_url": "http://example.com/repos"},
        ) as mock_get:
            test_client = GithubOrgClient("google")
            test_return = test_client._public_repos_url
            mock_get.assert_called_once()
            self.assertEqual(
                test_return, mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """Test public repos Method"""
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="http://example.com/repos",
        ) as mock_pub:
            test_client = GithubOrgClient("holberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once()
            mock_pub.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method"""
        test_class = GithubOrgClient("test")
        result = test_class.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url_property(self, mock_org):
        """Test _public_repos_url method"""
        mock_org.return_value = {"repos_url": "http://example.com/repos"}

        test_class = GithubOrgClient("test")
        url = test_class._public_repos_url
        expected_url = "http://example.com/repos"

        self.assertEqual(url, expected_url)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch("requests.get")
        cls.mocked_get = cls.get_patcher.start()

        cls.mocked_get.side_effect = [
            mock.Mock(json=lambda: cls.org_payload),
            mock.Mock(json=lambda: cls.repos_payload),
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public repos method in integration test"""
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public repos method with license filtering"""
        client = GithubOrgClient("google")
        repos_with_license = client.public_repos(
            license_key="apache-2.0"
        )
        self.assertEqual(
            repos_with_license, self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
