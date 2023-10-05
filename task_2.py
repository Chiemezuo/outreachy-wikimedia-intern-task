import csv
# You have to make sure requests is installed.
# If not, you could run 'pip install requests'
import requests


# reusable method for getting status code from any url
def get_status_code(url):
    try:
        # get the server response
        res = requests.get(url)
        return f'({res.status_code}) {url}'
    except requests.exceptions.RequestException as e:
        return f'(None) {url}'


# extract the list from any csv file path within the project folder
def get_list_from_csv(csvFileLocation):
    # we will store the csv rows in a list, for easy handling
    list_of_urls = []
    # open the file
    with open(csvFileLocation, 'r', newline='') as csv_for_urls:
        reader = csv.reader(csv_for_urls)

        next(reader)
        for row in reader:
            list_of_urls.append(row[0])

    return list_of_urls


# The code that performs the task proper
# in this case, the arg is the name of the csv file within the project folder
for item in get_list_from_csv('Task 2 - Intern.csv'):
    print(get_status_code(item))
