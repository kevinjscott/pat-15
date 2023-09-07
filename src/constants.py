# src/constants.py

```python
# URL for the golf tournament results
GOLFSTAT_TOURNAMENT_URL = "https://results.golfstat.com/public/leaderboards/gsnav.cfm?pg=teamPlayer&tid=26033"

# Search term for finding player's social media accounts
SOCIAL_MEDIA_SEARCH_TERM = "golf"

# OpenAI models
OPENAI_MODELS = {
    "gpt-4": {"input": 0.03/1000, "output": 0.06/1000},
    "gpt-3.5-turbo": {"input": 0.0015/1000, "output": 0.002/1000},
    "gpt-3.5-turbo-16k": {"input": 0.003/1000, "output": 0.004/1000}
}

# Exponential backoff parameters
BACKOFF_MIN = 1
BACKOFF_MAX = 65
BACKOFF_ATTEMPTS = 6

# OpenAI chat model
OPENAI_CHAT_MODEL = "gpt-3.5-turbo-16k"

# OpenAI chat temperature
OPENAI_CHAT_TEMPERATURE = 0.0
```