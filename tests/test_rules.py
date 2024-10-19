import pytest

from seabattle.rules import Rules


@pytest.fixture
def rule():
    _rule = Rules({})
    return _rule


def test_rule(rule):
    assert isinstance(rule, Rules)
    assert rule._limits == dict()


def test_initial_limits():
    lmin = "min"
    lmax = "max"
    limits = {
        lmin: 0,
        lmax: 10,
    }

    rule = Rules(limits)
    assert len(rule.AVAILABLE_LIMITS) == 2
    assert lmin in rule.AVAILABLE_LIMITS
    assert lmax in rule.AVAILABLE_LIMITS
    assert len(rule.limits) == 2


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
    assert set(rule.limits.keys()) == {lmin, lmax}


def test_adding_new_limit():
    rule = Rules({
        "min": 0,
        "max": 10,
    })

    new_limit = "new"
    rule.change_limit(new_limit, "Hello")
    assert len(rule.AVAILABLE_LIMITS) == 2
    assert new_limit not in rule.limits


def test_make_preparations(rule):
    rule.make_preparations()


def test_make_turn(rule):
    rule.make_turn()