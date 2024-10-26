from random import randint

from seabattle.player import Player

class AiGuessTheNumber(Player):

    def __init__(self, name):
        super().__init__(name, ai=True)

    def _gen_input_from_ai(self):
        assert self._rules != None, "The rules must be set"

        return randint(self._rules.limits["min"], self._rules.limits["max"])