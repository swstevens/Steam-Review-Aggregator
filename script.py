import requests

# Take user input
user_input = input("Enter the endpoint: ")

# Construct the API URL
url = f'https://api.example.com/{user_input}'

response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print('Success!')
    data = response.json()
    # Now you can work with the data
else:
    print('Failed to retrieve data')
