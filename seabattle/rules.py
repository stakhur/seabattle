class Rules:

    def __init__(self, limits: dict):
        self._limits = limits


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
        pass


    def make_turn(self):
        pass

class GuessTheNumberRules(Rules):
    
    def __init__(self):
        super().__init__(limits = {
            "min": 0,
            "max": 10,
            "players": 2,
        })

        self._target = None


    def _set_target(self, target):
        if target in range(self.limits["min"], self.limits["max"]+1):
            self._target = target


    @property
    def target(self):
        return self._target


    def make_preparations(self, target=None):
        if target is None:
            input_str = f"Enter the target between {self.limits["min"]} and {self.limits["max"]}: "
            target = input(input_str)
            while ((not target.isdigit()) or
                (int(target) < self.limits["min"] or int(target) > self.limits["max"])):
                target = input(input_str)

        self._set_target(int(target))
