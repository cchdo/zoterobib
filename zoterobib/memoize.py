from time import time


class TimedMemoize:
    """Memoize for time limit."""

    def __init__(self, time_limit=60):
        self.memo = {}
        self.time_limit = time_limit

    def __update(self, *args):
        self.memo[args] = (self.fn(*args), time())

    def __call__(self, fn):
        self.fn = fn
        def wrapped(*args):
            if args not in self.memo:
                self.__update(*args)
            if time() - self.memo[args][1] > self.time_limit:
                self.__update(*args)
            return self.memo[args][0]
        return wrapped

