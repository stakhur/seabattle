import pytest
import seabattle.guess_the_number as gtn
from seabattle.guess_the_number import GuessNumber


@pytest.fixture
def gn():
    gnum = GuessNumber(0, 10)
    gnum.new_game()
    return gnum


def test_constructor():
    min = 0
    max = 10
    tries = 5
    g = GuessNumber(min, max, tries)

    assert isinstance(g, GuessNumber)

    assert g._target == min - 1


def test_new_game(gn):    
    assert len(gn.tries) == 0

    assert gn._target >= gn.min and gn._target <= gn.max


def test_next_try(gn):
    gtn.input = lambda _: '5'
    gn.next_try()
    assert len(gn.tries) == 1
    assert gn.tries[0] == 5

    gtn.input = lambda _: '3'
    gn.next_try()
    assert len(gn.tries) == 2
    assert gn.tries == [5, 3]
    
    gtn.input = lambda _: '5'
    gn.next_try()
    assert len(gn.tries) == 2
    assert gn.tries == [5, 3]