from time import process_time, time

class MyTimer:
    def __init__(self):
        self._time_func = process_time
        self.restart()

    def restart(self):
        self._start = self._time_func()
        self._pause_sum = 0

    def pause(self):
        self._wpause = self._time_func()

    def resume(self):
        self._pause_sum += self._time_func() - self._wpause

    def get_elapsed_time(self):
        return self._time_func() - self._start - self._pause_sum
