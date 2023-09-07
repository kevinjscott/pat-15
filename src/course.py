```python
from src.openai_wrapper import OpenAIQueryHandler

class Course:
    def __init__(self, openai_key):
        self.openai = OpenAIQueryHandler(openai_key)

    def extract_course_info(self, page_text):
        system_prompt = """
        Given the following web page text, extract the golf course name, city, and state.
        """
        course_info = self.openai.chat(system_prompt, page_text)
        return course_info

    def extract_course_rating(self, page_text):
        system_prompt = """
        Given the following web page text, extract the golf course rating.
        """
        course_rating = self.openai.chat(system_prompt, page_text)
        return course_rating

    def check_player_score(self, player_score, course_rating):
        if player_score <= (course_rating * 2) + 15:
            return True
        else:
            return False
```