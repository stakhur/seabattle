import pytest

from seabattle.rules import Rules

def test_rule():
    rule = Rules()

def test_set_limits():
    rule = Rules(0, 10)


def test_get_available_field():
    rule_gtn = Rules()
    rule_gtn.get_available_positions()