from enum import Enum

from .rules import Rules, State
from .guess_the_number_rules import GuessTheNumberRules
from .player import Player

class Game:
    class State(Enum):
        WAITING_FOR_PLAYERS = 2
        READY_FOR_START = 3

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


    def add_player(self, player: Player):
        is_player_added = False

        if (len(self._players) < self._min_num_of_players):
            self._players.append(player)
            is_player_added = True

        if (len(self._players) >= self._min_num_of_players):
            self._state = self.State.READY_FOR_START

        return is_player_added


    @property
    def state(self):
        return self._state