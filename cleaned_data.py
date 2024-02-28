# titles = []
#
# # Write modified titles back into list in chronological order
# with open('output.txt', 'r') as file:
#     # Read file and append each title to `titles` list
#     for line in file:
#         # Remove trailing newline characters and leading/trailing whitespaces
#         title = line.strip()
#         # Append the cleaned titles to the title list
#         titles.append(title)

# Func to create list of guests from .txt file of guests
def guest_list(file_name):
    guests = []
    with open(file_name, 'r') as file:
        # Read file and append each guest name to `guests` list
        for line in file:
            guest_name = line.strip()
            # Append to guest list
            guests.append(guest_name)
    return guests

# Func to create list of podcast lengths from `episodes_list.data`
import episode_list
def duration_list():
    lengths = []
    reversed_lengths = []
    for episode in episode_list.data['collection']:
        lengths.append(episode['duration'])
    # Reverse list because we want to start with oldest first
    for length in reversed(lengths):
        reversed_lengths.append(length)
    return reversed_lengths

# Func to create list of publish dates from `episode_list.data`
def date_list():
    dates = []
    reversed_dates = []
    for episode in episode_list.data['collection']:
        dates.append(episode['published_at'])
    # Reverse list because we want to start with oldest first
    for date in reversed(dates):
        reversed_dates.append(date)
    return reversed_dates

# Func to create list of podcast urls from `episode_list.data`
def url_list():
    urls = []
    reversed_urls = []
    for episode in episode_list.data['collection']:
        urls.append(episode['enclosure_url'])
    # Reverse list because we want to start with oldest first
    for url in reversed(urls):
        reversed_urls.append(url)
    return reversed_urls


