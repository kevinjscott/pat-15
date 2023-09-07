```python
import json

class ResultsCompiler:

    def __init__(self):
        self.results = []

    def add_result(self, player, course, social_media):
        result = {
            "player": player,
            "course": course,
            "social_media": social_media
        }
        self.results.append(result)

    def compile_results(self):
        return json.dumps(self.results, indent=4)

    def save_results(self, filename="results.json"):
        with open(filename, 'w') as f:
            f.write(self.compile_results())
```