import random
from enum import Enum

class State(Enum):
    UNKNOWN = 1
    MISSED = 2
    LOST = 3
    WON = 4

class GuessNumber:
    def __init__(self, min, max, max_tries = -1):
        self.min = int(min)
        self.max = int(max)
        self.max_tries = int(max_tries)

        self._target = self.min - 1

        # game states: {(U)nknown, (M)issed, (H)it, (D)estroy, (W)on, (L)ost}


    def _update_state(self, next_try):
        if self.state in (State.WON, State.LOST):
            # The game did not start
            return self.state
        
        self._appendToTries(next_try)
        
        if next_try == self._target:
            self._setState(State.WON)
        elif next_try != self._target:
            self._setState(State.MISSED)


        return self.state


    def new_game(self):
        self._clearTries()
        self._target = random.randint(self.min, self.max)
        self._setState(State.UNKNOWN)


    def next_try(self):
        next_try = input('Enter the target: ')
        while ((not next_try.isdigit()) or
               (int(next_try) < self.min or int(next_try) > self.max) or
               int(next_try) in self.tries):
            next_try = input('Enter the target: ')

        next_try = int(next_try)
        self._appendToTries(next_try)

        # self._update_state(next_try)
        return self.state


    @property
    def state(self):
        return self._state
    
    def _setState(self, value):
        self._state = value

    @property
    def tries(self):
        return self._tries
    
    def _appendToTries(self, value):
        self._tries.append(value)

    def _clearTries(self):
        self._tries = []