import random
from enum import Enum

class State(Enum):
    UNKNOWN = 1
    MISSED = 2
    LOST = 3
    WON = 4

class GuessNumber:
    def __init__(self, min, max, max_tries = -1):
        self._min = int(min)
        self._max = int(max)
        self._max_tries = int(max_tries)

        self._target = self._min - 1

        # game states: {(U)nknown, (M)issed, (H)it, (D)estroy, (W)on, (L)ost}

    def get_current_status(self):
        return f"Status: {self.state}\nTries: {sorted(self.tries)}"


    def _set_target_randomly(self):
        self._target = random.randint(self._min, self._max)

    
    def _set_target_manually(self):
        target = input('Enter the target: ')
        while ((not target.isdigit()) or
               (int(target) < self._min or int(target) > self._max)):
            target = input('Enter the target: ')

        self._target = int(target)


    def new_game(self, is_random=True):
        self._clearTries()
        
        if is_random:
            self._set_target_randomly()
        else:
            self._set_target_manually()

        self._setState(State.UNKNOWN)


    def _update_state(self, next_try):
        if self.state in (State.WON, State.LOST):
            # The game did not start
            return self.state
        
        self._appendToTries(next_try)
        
        if next_try == self._target:
            self._setState(State.WON)
        elif next_try != self._target:
            self._setState(State.MISSED)
            if self._max_tries > 0 and len(self.tries) >= self._max_tries:
                self._setState(State.LOST)

        return self.state


    def next_try(self):
        next_try = input('Enter the target: ')
        while ((not next_try.isdigit()) or
               (int(next_try) < self._min or int(next_try) > self._max) or
               int(next_try) in self.tries):
            next_try = input('Enter the target: ')

        next_try = int(next_try)

        self._update_state(next_try)
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


    def game(self, set_target_manually=False, show_status=False):
        self.new_game(is_random = not set_target_manually)
        
        while(self.state not in (State.WON, State.LOST)):
            self.next_try()
            if show_status:
                print(self.get_current_status())

        return self.state
    

if __name__ == "__main__":
    gn = GuessNumber(0, 10, 5)
    gn.game(show_status=True)