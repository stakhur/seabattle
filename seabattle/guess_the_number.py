import random

class GuessNumber:
    def __init__(self, min, max, max_tries = -1):
        self.min = int(min)
        self.max = int(max)
        self.max_tries = int(max_tries)

        self._target = self.min - 1


    def new_game(self):
        self.tries = []
        self._target = random.randint(self.min, self.max)


    def next_try(self):
        next_try = input('Enter the target: ')
        while (not isinstance(next_try, int) and
               (int(next_try) < self.min or int(next_try) > self.max) and
               int(next_try) in self.tries):
            next_try = input('Enter the target: ')

        next_try = int(next_try)
        self.tries.append(next_try)