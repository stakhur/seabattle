import pytest

from seabattle.rules import Rules, State


@pytest.fixture
def rule():
    _rule = Rules({})
    return _rule


def test_rule(rule):
    assert isinstance(rule, Rules)
    assert rule._limits == {"players": 1}
    assert rule.state == State.NOT_READY_FOR_GAME


def test_initial_limits():
    lmin = "min"
    lmax = "max"
    p = "players"
    limits = {
        lmin: 0,
        lmax: 10,
        p: 2
    }

    rule = Rules(limits)
    assert len(rule.AVAILABLE_LIMITS) == 3
    assert lmin in rule.AVAILABLE_LIMITS
    assert lmax in rule.AVAILABLE_LIMITS
    assert p in rule.AVAILABLE_LIMITS
    assert len(rule.limits) == 3


def test_change_limits():
    lmin = "min"
    lmax = "max"

    rule = Rules({
        lmin: 0,
        lmax: 5,
    })
    
    value = 1
    rule.change_limit(lmin, value)
    assert lmin in rule.limits
    assert rule.limits[lmin] == value

    value = 10
    rule.change_limit(lmax, value)
    assert set(rule.limits.keys()) == {lmin, lmax, "players"}


def test_adding_new_limit():
    rule = Rules({
        "min": 0,
        "max": 10,
    })

    new_limit = "new"
    rule.change_limit(new_limit, "Hello")
    assert len(rule.AVAILABLE_LIMITS) == 3
    assert new_limit not in rule.limits


def test_make_preparations(rule):
    rule.make_preparations()
    assert rule.state == State.READY_FOR_GAME


def test_make_turn(rule):
    rule.make_turn()
    assert rule.state == State.TURN_COMPLETED