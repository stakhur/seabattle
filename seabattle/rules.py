from enum import Enum

class State(Enum):
    UNKNOWN = 1
    NOT_READY_FOR_GAME = 2
    READY_FOR_GAME = 3
    LOSE = 5
    WIN = 6
    NEED_TO_TURN_AGAIN = 10
    TURN_COMPLETED = 11
    TURN_INCOMPLETED = 12


class Rules:

    def __init__(self, limits: dict):
        self._state = State.NOT_READY_FOR_GAME
        self._limits = limits
        if "players" not in limits:
            self._limits["players"] = 1


    @property
    def state(self):
        return self._state


    @property
    def AVAILABLE_LIMITS(self):
        return list(self._limits.keys())


    @property
    def limits(self):
        return self._limits
    

    def change_limit(self, name, value):
        if name in self._limits:
            self._limits[name] = value


    def make_preparations(self, target=None):
        self._state = State.READY_FOR_GAME
        return None


    def make_turn(self, next_try=None):
        self._state = State.TURN_COMPLETED
        return None