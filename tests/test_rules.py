import pytest

from seabattle.rules import Rules


@pytest.fixture
def rule():
    _rule = Rules({})
    return _rule


def test_rule(rule):
    assert isinstance(rule, Rules)
    assert rule._limits == dict()


def test_set_limits(rule):
    limit_min = "min"
    value = 1
    rule.set_limit(limit_min, value)
    assert limit_min in rule.limits
    assert rule.limits[limit_min] == value

    limit_max = "max"
    value = 10
    rule.set_limit(limit_max, value)
    assert set(rule.limits.keys()) == {limit_min, limit_max}


def test_initial_limits():
    lmin = "min"
    lmax = "max"
    limits = {
        lmin: 0,
        lmax: 10,
    }

    rule = Rules(limits)
    assert len(rule.LIMITS) == 2
    assert lmin in rule.LIMITS
    assert lmax in rule.LIMITS

    new_limit = "new"
    rule.set_limit(new_limit, "Hello")
    assert len(rule.LIMITS) == 2
    assert lmin in rule.LIMITS
    assert lmax in rule.LIMITS


def test_make_preparations(rule):
    rule.make_preparations()


def test_make_turn(rule):
    rule.make_turn()