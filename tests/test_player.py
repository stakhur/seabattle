import pytest

from seabattle.player import Player
from seabattle.player_ai_guess_the_number import AiGuessTheNumber as Ai
from seabattle.guess_the_number_rules import GuessTheNumberRules as Rules

class TestNewPlayer():

    def test_new_player(self):
        name = "Jura"
        player = Player(name)
        assert player.name == name
        assert player._rules == None
        assert player._ai == False
        assert player.state == Player.State.WAITING_FOR_RULES

    def test_new_player_ai(self):
        player = Player("AI", True)
        assert player._ai == True
        assert player.state == Player.State.WAITING_FOR_RULES

def test_set_rules():
    player = Player("Jura")
    player.set_rules(dict())
    assert player.state == Player.State.READY_TO_PREPARE


class TestPrepareToGame:

    @pytest.fixture
    def human(self):
        _player = Player("Jura")
        _player.set_rules(Rules())
        return _player
    
    @pytest.fixture
    def ai(self):
        _player = Ai("AI")
        _player.set_rules(Rules())
        return _player


    def test_prepare_to_game_raise_exception(self):
        player = Player("Jurek")
        with pytest.raises(AssertionError) as e:
            player.prepare_to_game()


    def test_prepare_to_game(self, ai: Ai):
        player = ai
        assert player.state == Player.State.READY_TO_PREPARE
        
        player.prepare_to_game()
        assert player.state == Player.State.READY_TO_START