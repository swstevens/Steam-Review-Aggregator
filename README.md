# Steam Review Analyzer

This Python script aggregates Steam game reviews using the Steam API and analyzes the most common words and phrases found in the reviews.

## Features

- Fetches reviews for a specified game using Steam API
- Processes and cleans review text
- Identifies and ranks most common words and phrases
- Outputs results in a readable format

## Requirements

- Python 3.6+
- `requests` library
- `nltk` library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/swstevens/Steam-Review-Aggregator .git
   ```
2. Install required libraries:
   ```
   pip install requests nltk
   ```

## Usage

1. Run the script:
   ```
   python script.py
   ```
2. Enter the AppID of the Steam game when prompted
3. View the analysis results in the console output

## Configuration

- Modify `MAX_REVIEWS` in the script to change the number of reviews fetched
- Adjust `MIN_WORD_LENGTH` to filter out shorter words
- Edit `COMMON_WORDS` list to exclude additional words from the analysis

## License

This project is open source and available under the MIT License.
