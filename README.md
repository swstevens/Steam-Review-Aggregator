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
2. Use find to get the App ID of a game by searching its name:
   ```
   find [game name]
   ```
3. Use batch to run the aggregator and fetch information about steam reviews and common words/phrases:
   ```
   batch [appid]
   ```
4. View the analysis results in the console output

## License

This project is open source and available under the MIT License.
