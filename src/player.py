```python
class Player:
    def __init__(self, name, team, scores):
        self.name = name
        self.team = team
        self.scores = scores

    def calculate_score(self, course_rating):
        total_score = sum(self.scores)
        pat_score = (course_rating * 2) + 15
        return total_score <= pat_score

    def to_dict(self):
        return {
            "name": self.name,
            "team": self.team,
            "scores": self.scores
        }
```