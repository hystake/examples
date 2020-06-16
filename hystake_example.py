import requests
import os
import csv
import json

# API token is used for both download and upload.
# Find / regenerate your API token in Account Info -> Developer Info
token = "Enter your API token here"

# the full dataset ID is composed of 3 parts: user ID, product ID, 
user_id = "Enter your user ID here"
product_id = "Enter your product ID here"
table_id = "Enter your table ID here"
datasetCode = user_id + "-" + product_id + "-" + table_id

file_path = "Enter your .csv location"
url = 'http://dev.hystake.com/api/v1/dataset/' + datasetCode + '/'
mode = 'append'  # append / overwrite
skiprows = 1  # skip the first n rows of the csv
url_params = {'token': token, 'mode': mode, 'skiprows': skiprows}

# upload
file = open(file_path)
csv_reader = csv.reader(file)
request_data = {

    'dataset': list(csv_reader)

}
r = requests.post(url, params=url_params, json=request_data)

# download
datasetCode_download = 'HYSTAKE-CMEFUT-CL1'
request_data = {'meta': True}

# return data since May1, 2020
filter1 = "&filter=date__gt=05-01-2020"
# return data since May1, 2020, with top 3 results
filter2 = "&filter=date__gt=05-01-2020&limit=3"
# return data from the "open" column since May1, 2020, and sort the date in descending order 
filter3 = "&filter=date__gt=05-01-2020&fields=open&sort=date.desc"

r = requests.get('http://dev.hystake.com/api/v1/dataset/' + datasetCode_download + '?token=' + token + filter1)
json_data = json.loads(r.text)

pass
