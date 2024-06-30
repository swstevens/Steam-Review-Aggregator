import requests

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

        # Construct the API URL
        url = f'https://steamcommunity.com/actions/SearchApps/{user_input}'

        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            print('Success!')
            data = response.json()
            for item in data:
                print(item['name'])
            # Now you can work with the data
        else:
            print('Failed to retrieve data')
            

if __name__ == '__main__':
    main()
