from enum import Enum

from .rules import Rules

class Player:
    
    class State(Enum):
        WAITING_FOR_RULES = 1
        READY_TO_PREPARE = 2
        READY_TO_START = 3
        IN_GAME = 4
    
    def __init__(self, name, ai=False):
        self._name = name
        self._ai = ai
        self._rules = None
        self._turns = []
        self._state = self.State.WAITING_FOR_RULES

        self._mydata = None

    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        return self._state

    def set_rules(self, rules: Rules):
        self._rules = rules
        self._turns = []
        self._mydata = None

        self._state = self.State.READY_TO_PREPARE


    def _gen_input_from_ai(self):
        return None

    
    def prepare_to_game(self):
        assert self._rules != None, "The rules must be set"

        inp = None

        inp = self._gen_input_from_ai()
        
        self._mydata = self._rules.make_preparations(target=inp)
        self._state = self.State.READY_TO_START


    def start_game(self):
        assert self._state == self.State.READY_TO_START, "Player must be ready to start"

        self._state = self.State.IN_GAME


    def make_turn(self):
        turn = self._rules.make_turn()

        self._turns.append(turn)
        return turn
