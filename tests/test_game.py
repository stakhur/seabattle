import pytest

from seabattle.rules import Rules
from seabattle.game import Game
from seabattle.player import Player

@pytest.fixture
def game():
    _game = Game(Rules({"players": 3}))
    return _game


@pytest.fixture
def game_with_3_players():
    _game = Game(Rules({"players": 3}))
    _game.add_player(Player("Jurek"))
    _game.add_player(Player("Kostek"))
    _game.add_player(Player("Tusik"))
    return _game


# init
# change_rules
# test_add_player
# test_prepare_players
# test_start_game
# test_next_turn
# test_check_state

def test_game(game):
    assert isinstance(game, Game)
    assert not game._players
    assert game._min_num_of_players == 3
    assert game.state == Game.State.WAITING_FOR_PLAYERS


def test_change_rules(game):
    class RulesForTest(Rules):
        def __init__(self):
            super().__init__(limits={
                "a": 1,
                "players": 2,
                })

    game.change_rules(RulesForTest())
    assert game._rules.limits["a"] == 1
    assert game._min_num_of_players == 2
    assert game._max_num_of_players == 2


def test_add_player(game):
    is_added = game.add_player(Player("Jurek"))
    assert is_added == True
    assert len(game._players) == 1
    assert game.state == Game.State.WAITING_FOR_PLAYERS

    is_added = game.add_player(Player("Kostek"))
    assert is_added == True
    assert len(game._players) == 2
    assert game.state == Game.State.WAITING_FOR_PLAYERS

    is_added = game.add_player(Player("Tusik"))
    assert is_added == True
    assert len(game._players) == 3
    assert game.state == Game.State.READY_FOR_START

    is_added = game.add_player(Player("Valera"))
    assert is_added == False
    assert len(game._players) == 3
    assert game.state == Game.State.READY_FOR_START


def test_add_player_change_rule(game_with_3_players):
    assert game_with_3_players.state == Game.State.READY_FOR_START
    assert game_with_3_players._min_num_of_players == 3
    assert len(game_with_3_players._players) == 3

    class RulesWith2Players(Rules):
        def __init__(self):
            super().__init__(limits={"players": 2,})

    game_with_3_players.change_rules(RulesWith2Players())
    assert game_with_3_players.state == Game.State.READY_FOR_START
    assert game_with_3_players._min_num_of_players == 2
    assert len(game_with_3_players._players) == 2


    class RulesWith4Players(Rules):
        def __init__(self):
            super().__init__(limits={"players": 4,})

    game_with_3_players.change_rules(RulesWith4Players())
    assert game_with_3_players.state == Game.State.WAITING_FOR_PLAYERS
    assert game_with_3_players._min_num_of_players == 4
    assert len(game_with_3_players._players) == 2
