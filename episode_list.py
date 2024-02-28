import requests
import json

url = 'https://api.simplecast.com/podcasts/ba397791-02e1-4b24-b31a-bea1c74a0e64/episodes?preview=true'

# send http get request
response = requests.get(url)

# convert json to python dict & prettify
data = response.json()
pretty_data = json.dumps(data, indent=4)


# # Loop through episode collection and create lists for relevant metadata
# titles = []
# transcript_urls = []
# audio_urls = []
# descriptions = []

#
# for episode in data['collection']:
#     titles.append(episode['title'])
#     transcript_urls.append(episode['href'])
#     audio_urls.append(episode['enclosure_url'])
#     descriptions.append(episode['description'])


# print(titles)
# print(transcript_urls)
# print(audio_urls)
# print(descriptions)

# # Export titles list into .txt for easy editing (reversed for chronological order)
# # Open a text file in write mode
# with open('output.txt', 'w') as file:
#     # Iterate over the list and write each item to the file
#     for item in reversed(titles):
#         file.write(item + '\n')


def get_value_from_data(key: str):
    """
    Returns a list in chronological order (oldest podcast first) of the given key, eg "description" or "title", etc.
    :param key: The dict key of data['collection'] whose values you want to return for each entry.
    :return: A list with an entry for each podcast for the given key.
    """
    my_list = []
    my_reversed_list = []
    for episode in data['collection']:
        my_list.append(episode[key])
    for item in reversed(my_list):
        my_reversed_list.append(item)
    return my_reversed_list

