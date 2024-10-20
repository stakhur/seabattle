import copy


class InputReplacer:
    _module = None

    def __init__(self, inp: list, module = None):
        self._inputs = copy.copy(inp)

        if (module != None):
            InputReplacer._module = module

    def __enter__(self):
        self._set_input()

    def __exit__(self, exception_type, exception_value, exception_traceback):
        InputReplacer._module.input = input

    @classmethod
    def set_module(cls,  module):
        cls._module = module

    def _set_input(self):
        def input_gen():
            ret = copy.copy(self._inputs)
            while ret:
                yield ret.pop(0)
        i = input_gen()
        InputReplacer._module.input = lambda _: next(i)