import copy
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

def set_input(inp = list()):
    def input_gen():
        ret = copy.copy(inp)
        while ret:
            yield ret.pop(0)
    i = input_gen()
    gtn.input = lambda _: next(i)
    # TODO: Need to teardown, gtn.input = input


def test_next_try(gn):
    set_input(['5', '3', 'Hello', '-1', '5', '13', '7', '0'])

    gn.next_try()
    assert gn.tries == [5]

    gn.next_try()
    assert gn.tries == [5, 3]
    
    gn.next_try()
    assert gn.tries == [5, 3, 7]

    gn.next_try()
    assert gn.tries == [5, 3, 7, 0]
