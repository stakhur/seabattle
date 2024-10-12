class Player:
    
    def __init__(self, name, ai=False):
        self._name = name
        self._ai = ai
        self._rules = None

    @property
    def name(self):
        return self._name
    

    def set_rules(self, rules):
        self._rules = rules

    
    def prepare_to_game(self):
        pass