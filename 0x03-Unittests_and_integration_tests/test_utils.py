#!/usr/bin/env python3
"""Parameterize a unit test"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """Access a nested map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Ensure that this method returns a value from the nested map given"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b"),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test that a `KeyError` is raised"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)

        message = str(cm.exception)
        self.assertEqual(message[1:-1], expected)
