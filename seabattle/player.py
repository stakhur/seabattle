from enum import Enum

from .rules import Rules

class Player:
    
    class State(Enum):
        WAITING_FOR_RULES = 1
        READY_TO_PREPARE = 2
    
    def __init__(self, name, ai=False):
        self._name = name
        self._ai = ai
        self._rules = None
        self._turns = []

    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        _state = self.State.WAITING_FOR_RULES
        if (self._rules != None):
            _state = self.State.READY_TO_PREPARE

        return _state

    def set_rules(self, rules: Rules):
        self._rules = rules

    
    def prepare_to_game(self):
        self._rules.make_preparations()


    def make_turn(self):
        self._turns.append(self._rules.make_turn())