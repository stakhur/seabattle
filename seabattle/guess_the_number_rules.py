from .rules import Rules, State

class GuessTheNumberRules(Rules):
    
    def __init__(self):
        super().__init__(limits = {
            "min": 0,
            "max": 10,
            "players": 2,
        })

        self._target = None

    def _is_data_in_limits(self, value):
        return (value.isdigit() and
            (int(value) >= self.limits["min"]) and
            (int(value) <= self.limits["max"]))


    def _set_target(self, target):
        if self._is_data_in_limits(str(target)):
            self._target = target
            super().make_preparations()


    def _input_limited_data(self, prompt):
        value = input(prompt)
        while (not self._is_data_in_limits(value)):
            value = input(prompt)
        return value


    @property
    def target(self):
        return self._target


    def make_preparations(self, target=None):
        if target is None:
            target = self._input_limited_data(
                f"Enter the target between {self.limits["min"]} and {self.limits["max"]}: ")
        else:
            target = str(target)
            if not self._is_data_in_limits(target):
                return

        self._set_target(int(target))


    def _last_turn(self, next_try):
        if self._is_data_in_limits(next_try):
            next_try = int(next_try)
            self._state = State.TURN_COMPLETED
            return next_try
        
        self._state = State.TURN_INCOMPLETED
        return None


    def make_turn(self, next_try=None):
        target = self._input_limited_data(
            f"Enter next try between {self.limits["min"]} and {self.limits["max"]}: ")
        
        return self._last_turn(target)