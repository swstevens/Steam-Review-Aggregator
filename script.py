import requests
import pandas as pd
from collections import Counter
import json

# https://store.steampowered.com/api/appdetails?appids=2519060
# this api lets you see all information about a game

# https://store.steampowered.com/appreviewhistogram/275850?l=english
# this api lets you see the review histogram of a game

# https://steamcommunity.com/actions/SearchApps/{search_term}
# this api lets you search for a game by name and find its appid

# https://store.steampowered.com/appreviews/{user_input}?json=1
# this api lets you see the reviews of a game. Limited to 20, then has to call the next page using cursor field

'''
take in a name, and replace space character with %20, then call searchapps
then list all the response name and let the user choose one
then run the batch review script

review script:
quick look at reviews
process the reviews and remove superfluous reviews. bad review indicators to be decided.
'''
base_url = "https://store.steampowered.com"

def display_results(results):
    print(f"Total reviews analyzed: {results['total_reviews']}")
    print(f"Positive reviews: {results['positive_reviews']} ({results['positive_percentage']:.2f}%)")
    print(f"Negative reviews: {results['negative_reviews']}")
    print("\nMost common words in reviews:")
    for word, count in results['most_common_words']:
        print(f"{word}: {count}")

def analyze_reviews(reviews: list):
    df = pd.DataFrame(reviews)
    total_reviews = len(df)
    positive_reviews = len(df[df['voted_up'] == True])
    negative_reviews = len(df[df['voted_up'] == False])

    # Most common words in reviews
    all_words = ' '.join(df['review']).lower().split()
    word_counts = Counter(all_words)
    most_common_words = word_counts.most_common(10)


    return {
        "total_reviews": total_reviews,
        "positive_reviews": positive_reviews,
        "negative_reviews": negative_reviews,
        "positive_percentage": (positive_reviews / total_reviews) * 100 if total_reviews > 0 else 0,
        "most_common_words": most_common_words
    }

def main():
    while True:
        # Take user input
        user_input = input("Enter: ")
        if user_input == 'exit':    # Exit the program  
            break
        command, user_input = user_input.split(' ', 1)


        if command == 'find': 
            # Construct the API URL
            url = f'{base_url}/actions/SearchApps/{user_input}'

            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                print('Success!')
                data = response.json()
                for item in data:
                    print('{:<50s}{:>12s}'.format(item["name"], item["appid"]))
            else:
                print('Failed to retrieve data')

        if command == 'get': 
            # Construct the API URL
            url = f'{base_url}/appreviewhistogram/{user_input}?l=english'
            url = url.replace('+', '%2B')

            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                print('Success!')
                data = response.json()
            else:
                print('Failed to retrieve data')
        
        if command == 'batch':
            reviews = []

            url = f'{base_url}/appreviews/{user_input}?json=1'

            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                positive_count = 0
                negative_count = 0

                cursor = response.json()['cursor']
                while cursor is not None and len(reviews) < 100:
                    reviews.extend(data["reviews"])

                    url = f'https://store.steampowered.com/appreviews/{user_input}?json=1&cursor={cursor}'
                    url = url.replace('+', '%2B')
                    
                    response = requests.get(url)

                    if response.status_code == 200:
                        data = response.json()
                        cursor = data.get('cursor', None)

                    else:
                        print('Failed to retrieve data, stopping process')
                        break
                display_results(analyze_reviews(reviews))
            else:
                print('Failed to retrieve data')

if __name__ == '__main__':
    main()
