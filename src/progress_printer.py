```python
class ProgressPrinter:
    def __init__(self):
        pass

    def print_progress(self, message):
        print(message)

    def print_player_info(self, player):
        print(f"Processing player: {player['name']}, Team: {player['team']}")

    def print_course_info(self, course):
        print(f"Processing course: {course['name']}, Location: {course['city']}, {course['state']}")

    def print_course_rating(self, rating):
        print(f"Course rating: {rating}")

    def print_pat_result(self, player, result):
        print(f"{player['name']} has {'passed' if result else 'failed'} the PAT.")

    def print_social_media_info(self, player, social_media):
        print(f"Found social media for {player['name']}: {social_media}")

    def print_compilation_status(self, status):
        print(f"Compilation status: {status}")

    def print_extraction_status(self, status):
        print(f"Extraction status: {status}")
```