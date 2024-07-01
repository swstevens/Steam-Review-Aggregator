import requests
from tabulate import tabulate
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

def main():
    while True:
        # Take user input
        user_input = input("Enter: ")
        if user_input == 'exit':    # Exit the program  
            break
        command, user_input = user_input.split(' ', 1)


        if command == 'find': 
            # Construct the API URL
            url = f'https://steamcommunity.com/actions/SearchApps/{user_input}'

            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                print('Success!')
                data = response.json()
                for item in data:
                    print('{:<50s}{:>12s}'.format(item["name"], item["appid"]))
                # Now you can work with the data
            else:
                print('Failed to retrieve data')

        if command == 'get': 
            # Construct the API URL
            url = f'https://store.steampowered.com/appreviewhistogram/{user_input}?l=english'
            url = url.replace('+', '%2B')

            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                print('Success!')
                data = response.json()
                print(data)
                # Now you can work with the data
            else:
                print('Failed to retrieve data')
        
        if command == 'batch':
            url = f'https://store.steampowered.com/appreviews/{user_input}?json=1'

            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                positive_count = 0
                negative_count = 0
                # print(data)

                cursor = response.json()['cursor']
                while cursor is not None:
                    for item in response.json()['reviews']:
                        if item['voted_up']:
                            positive_count += 1
                        else:
                            negative_count += 1
                    
                    url = f'https://store.steampowered.com/appreviews/{user_input}?json=1&cursor={cursor}'
                    url = url.replace('+', '%2B')
                    
                    response = requests.get(url)

                    if response.status_code == 200:
                        data = response.json()
                        cursor = data.get('cursor', None)

                    else:
                        print('Failed to retrieve data, stopping process')
                        break
                print('Review Ratio:    {:<8d}{:>8d}'.format(positive_count, negative_count))
            else:
                print('Failed to retrieve data')

if __name__ == '__main__':
    main()
