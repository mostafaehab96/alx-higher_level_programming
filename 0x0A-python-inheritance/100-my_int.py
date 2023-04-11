#!/usr/bin/python3
"""Defines MyInt class."""


class MyInt(int):
    """Simple MyInt class."""

    def __eq__(self, other):
        """Define == operator inverted!."""
        return self is other

    def __ne__(self, other):
        """Defines != operator inverted."""
        return self is not other
