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


def set_input(inp = list()):
    def input_gen():
        ret = copy.copy(inp)
        while ret:
            yield ret.pop(0)
    i = input_gen()
    gtn.input = lambda _: next(i)
    # TODO: Need to teardown, gtn.input = input


def test_set_target_randomly():
    min = 0
    g = GuessNumber(min, 10, 5)
    assert g._target == min - 1

    g._set_target_randomly()
    assert g._target != min - 1


def test_set_target_manually():
    min = 0
    max = 10
    g = GuessNumber(min, max, 5)
    assert g._target == min - 1

    target = 3
    set_input([str(min - 1), str(max + 1), 'Hello', str(target), '5'])
    g._set_target_manually()
    assert g._target == target


def test_new_game_random_target(gn):    
    assert len(gn.tries) == 0

    assert gn._target >= gn._min and gn._target <= gn._max


def test_new_game_manual_target():
    min = 0
    max = 10
    g = GuessNumber(min, max)

    target = 3
    set_input([str(min - 1), str(max + 1), 'Hello', str(target), '5'])
    g.new_game(is_random=False)
    assert g._target == target


def test_next_try(gn):
    set_input(['4'])
    gn.new_game(False)

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
    
    target = gn._target
    first_try = 5 if target != 5 else 6
    state = gn._update_state(first_try)
    assert state == State.LOST
    assert state == gn.state


def test_game_win():
    min = 0
    max = 10
    gn = GuessNumber(min, max)

    set_input([str(i) for i in range(min, max+1)])

    state = gn.game()
    assert state == State.WON


def test_game_loose():
    min = 0
    max = 10
    target = 9
    gn = GuessNumber(min, max, 5)

    set_input([str(i) for i in range(min, max+1)])

    state = gn.game(set_target_manually=True)
    assert state == State.LOST


def test_get_current_status():
    min, max = 0, 10
    target = 5
    gn = GuessNumber(min, max, 5)

    set_input([str(i) for i in [target, max, min, target, min+1]])
    gn.new_game(is_random=False)
    assert gn.get_current_status() == f"Status: State.UNKNOWN\nTries: []"

    gn.next_try()
    assert gn.get_current_status() == f"Status: State.MISSED\nTries: [{max}]"

    gn.next_try()
    assert gn.get_current_status() == f"Status: State.MISSED\nTries: [{min}, {max}]"

    gn.next_try()
    assert gn.get_current_status() == f"Status: State.WON\nTries: [{min}, {target}, {max}]"

    gn.next_try()
    assert gn.get_current_status() == f"Status: State.WON\nTries: [{min}, {target}, {max}]"
