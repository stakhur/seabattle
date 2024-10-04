import copy
import pytest
import seabattle.guess_the_number as gtn
from seabattle.guess_the_number import GuessNumber, State


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


def test_update_state(gn):
    assert gn.state == State.UNKNOWN

    target = gn._target
    first_try = 5 if target != 5 else 6

    state = gn._update_state(first_try)
    assert state == State.MISSED
    assert state == gn.state

    state = gn._update_state(target)
    assert state == State.WON
    assert state == gn.state

    gn.new_game()
    assert gn.state == State.UNKNOWN

    gn = GuessNumber(0, 10, 1)
    gn.new_game()
    assert gn.state == State.UNKNOWN
    
    first_try = 5 if target != 5 else 6
    state = gn._update_state(first_try)
    assert state == State.LOST
    assert state == gn.state






# def test_loose():
#     gn = GuessNumber(0, 10, 5)
#     gn.new_game()

#     target = gn._target
#     inp = {target, 1, 2, 3, 4, 5, 6, 7}
#     inp.remove(target)
#     set_input(list(inp))

#     while gn.next_try() != 'L':
#         pass

#     assert gn.state == 'L'