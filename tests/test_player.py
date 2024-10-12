import pytest

from seabattle.player import Player


class TestNewPlayer():

    def test_new_player(self):
        name = "Jura"
        player = Player(name)
        assert player.name == name
        assert player._rules == None
        assert player._ai == False

    def test_new_player_ai(self):
        player = Player("AI", True)
        assert player._ai == True


def test_set_rules():
    player = Player("Jura")
    player.set_rules(dict())
    # assert player.



class TestPrepareToGame:

    @pytest.fixture
    def human(self):
        _player = Player("Jura")
        return _player
    
    @pytest.fixture
    def ai(self):
        _player = Player("AI", False)
        return _player


    def test_prepare_to_game(self, human):
        human.prepare_to_game()