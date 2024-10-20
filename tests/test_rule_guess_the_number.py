import pytest

import seabattle.guess_the_number_rules as rules
from seabattle.guess_the_number_rules import GuessTheNumberRules
from seabattle.rules import State

from helpers import InputReplacer as IR
IR.set_module(rules)

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


@pytest.mark.parametrize('test_input,target,state', [
    (-5, None, State.NOT_READY_FOR_GAME),
    ("-5", None, State.NOT_READY_FOR_GAME),
    (3, 3, State.READY_FOR_GAME),
    ("7", 7, State.READY_FOR_GAME),
    (11, None, State.NOT_READY_FOR_GAME),
    ("14", None, State.NOT_READY_FOR_GAME)
])
def test_make_preparation_as_ai(rule, test_input, target, state):
    rule.make_preparations(test_input)
    assert rule.target == target
    assert rule.state == state


def test_make_preparation_as_ai_with_save(rule):
    assert rule.target == None
    assert rule.state == State.NOT_READY_FOR_GAME

    rule.make_preparations(3)
    assert rule.target == 3
    assert rule.state == State.READY_FOR_GAME

    rule.make_preparations("7")
    assert rule.target == 7

    rule.make_preparations(11)
    assert rule.target == 7


def test_make_preparation_as_human(rule):
    assert rule.target == None
    assert rule.state == State.NOT_READY_FOR_GAME

    target = 3

    with IR(["-5", "13", 'a', "Hello", str(target), "6"]) as _:
        rule.make_preparations()
        assert rule.target == target
        assert rule.state == State.READY_FOR_GAME


def test_make_not_targeted_turn_as_human(rule):
    target = 5
    rule.make_preparations(target)
    assert rule.target == target
    assert rule.state == State.READY_FOR_GAME

    next_try = 3

    with IR(["-5", "13", 'a', "Hello", str(next_try), '11']) as _:
        value = rule.make_turn()
        assert value == next_try
        assert rule.state == State.TURN_COMPLETED


