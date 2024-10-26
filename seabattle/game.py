from enum import Enum

from .rules import Rules, State
from .guess_the_number_rules import GuessTheNumberRules
from .player import Player

class Game:
    class State(Enum):
        WAITING_FOR_PLAYERS = 2
        WAITING_FOR_PLAYERS_READY = 3
        READY_FOR_GAME = 4

    def __init__(self, rules: Rules):
        self._players = []
        self.change_rules(rules)
        self._state = self.State.WAITING_FOR_PLAYERS

    
    def change_rules(self, rules: Rules):
        self._rules = rules
        self._min_num_of_players = rules.limits["min_players"]
        self._max_num_of_players = rules.limits["max_players"]
        if (len(self._players) > self._max_num_of_players):
            self._players = self._players[:self._max_num_of_players]

        if (len(self._players) < self._min_num_of_players):
            self._state = self.State.WAITING_FOR_PLAYERS
        else:
            self._state = self.State.WAITING_FOR_PLAYERS_READY

        for player in self._players:
            player.set_rules(self._rules)


    def add_player(self, player: Player):
        is_player_added = False

        if (len(self._players) < self._max_num_of_players):
            player.set_rules(self._rules)
            self._players.append(player)
            is_player_added = True

        if (len(self._players) >= self._min_num_of_players):
            self._state = self.State.WAITING_FOR_PLAYERS_READY

        return is_player_added


    def prepare_players(self):
        for player in self._players:
            player.prepare_to_game()
            
        self._state = self.State.READY_FOR_GAME

    @property
    def state(self):
        return self._state