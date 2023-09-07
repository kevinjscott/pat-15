# Golf Tournament Results Scraper

This Python project uses BeautifulSoup and OpenAI to scrape golf tournament results from the provided URL. The script identifies each player and their associated team (college) from the golfstat tournament page, finds the golf course, city, state for the tournament, and uses this information to find the Course Profile on BlueGolf.com using SerpApi. It then extracts the course rating from the BG page and checks if the player has two 18-hole scores from the tournament that add up to (the course rating * 2) + 15 or less. If so, they pass the PAT. The script also uses SerpApi to find the player's Instagram and/or Twitter and/or LinkedIn accounts by searching their name, team/school, and the term "golf". The results are then compiled and printed out as the script runs.

## Installation

1. Clone the repository
```
git clone https://github.com/yourusername/golf-tournament-results-scraper.git
```
2. Navigate to the project directory
```
cd golf-tournament-results-scraper
```
3. Install the required packages
```
pip install -r requirements.txt
```
## Usage

1. Set the necessary environment variables in your shell:
```
export OPENAI_API_KEY=your_openai_api_key
export SERPAPI_API_KEY=your_serpapi_api_key
```
2. Run the main script:
```
python src/main.py
```
## Files

- `src/main.py`: The main script that runs the program.
- `src/openai_wrapper.py`: Handles queries to the OpenAI API.
- `src/extractor.py`: Extracts data from event data.
- `src/page_scraper.py`: Scrapes web pages.
- `src/serpapi_wrapper.py`: Handles queries to the SerpApi.
- `src/player.py`: Defines the Player class.
- `src/course.py`: Defines the Course class.
- `src/results_compiler.py`: Compiles the results.
- `src/progress_printer.py`: Prints out details and progress updates.
- `src/constants.py`: Contains shared constants.
- `setup.py`: Contains setup information for the project.
- `requirements.txt`: Lists the required Python packages.
- `.gitignore`: Specifies which files and directories to ignore in git.
- `.vscode/launch.json`: Contains configuration for launching the program in VS Code.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)