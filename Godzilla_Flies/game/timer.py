class Timer():
    def __init__(self):
        self._time = 0
    
    def get_time(self):
        return self._time

    def set_time(self, seconds):
        self._time = seconds
        
    def add_time(self, time):
        self._time += time

    def lose_time(self, time):
        self._time -= time