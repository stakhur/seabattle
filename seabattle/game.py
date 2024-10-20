from rules import Rules, State
from guess_the_number_rules import GuessTheNumberRules
from player import Player

class Game:
    def __init__(self, rules: Rules):
        self._rules = rules
        self._num_of_players = rules.limits["players"]
        self._players = []