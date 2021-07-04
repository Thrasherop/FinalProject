class Score:
    def __init__(self):
        self._score = 0
    
    def get_score(self):
        return self._score

    def add_score(self, score):
        self._score += score