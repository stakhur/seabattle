import copy
import seabattle.guess_the_number as gtn


class InputReplacer:
    def __init__(self, inp: list):
        self._inputs = copy.copy(inp)

    def __enter__(self):
        self._set_input()

    def __exit__(self, exception_type, exception_value, exception_traceback):
        gtn.input = input


    def _set_input(self):
        def input_gen():
            ret = copy.copy(self._inputs)
            while ret:
                yield ret.pop(0)
        i = input_gen()
        gtn.input = lambda _: next(i)