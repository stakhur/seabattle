from .rules import Rules

class Player:
    
    def __init__(self, name, ai=False):
        self._name = name
        self._ai = ai
        self._rules = None
        self._turns = []

    @property
    def name(self):
        return self._name
    

    def set_rules(self, rules: Rules):
        self._rules = rules

    
    def prepare_to_game(self):
        self._rules.make_preparations()


    def make_turn(self):
        self._turns.append(self._rules.make_turn())