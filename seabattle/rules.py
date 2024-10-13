class Rules:

    def __init__(self, limits: dict):
        self._limits = limits
        self._LIMITS = tuple(limits.keys())


    @property
    def LIMITS(self):
        return self._LIMITS


    @property
    def limits(self):
        return self._limits
    

    def set_limit(self, name, value):
        self._limits[name] = value


    def make_preparations(self):
        pass


    def make_turn(self):
        pass

class GuessTheNumberRules(Rules):
    
    def __init__(self):
        super.__init__(limits = {
            "min": 0,
            "max": 10,
            "players": 2,
        })

        self._target = None

    def make_preparations(self):
        input_str = f"Enter the target between {self.limits["min"]} and {self.limits["max"]}: "
        target = input(input_str)
        while ((not target.isdigit()) or
               (int(target) < self.limits["min"] or int(target) > self.limits["max"])):
            target = input(input_str)

        self._target = int(target)