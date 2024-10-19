import pytest

from seabattle.rules import GuessTheNumberRules

@pytest.fixture
def rule():
    _rule = GuessTheNumberRules()
    return _rule


def test_rule(rule):
    assert isinstance(rule, GuessTheNumberRules)
    assert len(rule.AVAILABLE_LIMITS) == 3


def test_set_target(rule):
    assert rule.target == None

    rule._set_target(-5)
    assert rule.target == None

    rule._set_target(4)
    assert rule.target == 4
    
    rule._set_target(11)
    assert rule.target == 4


def test_make_preparation_as_ai(rule):
    assert rule.target == None

    rule.make_preparations(-5)
    assert rule.target == None

    rule.make_preparations("-5")
    assert rule.target == None

    rule.make_preparations(3)
    assert rule.target == 3

    rule.make_preparations("7")
    assert rule.target == 7

    rule.make_preparations(11)
    assert rule.target == 7

    rule.make_preparations("14")
    assert rule.target == 7


def test_make_preparation_as_human(rule):
    assert rule.target == None

    