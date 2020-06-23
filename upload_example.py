import requests
import os
import csv
import json

'''
For more details: https://hystakeapialpha.docs.apiary.io/#
A download query has 3 components:
1. required: API key
2. required: dataset code
'''

# To find / regenerate your API token in Account Info -> Developer Info
apikey = "Enter your API token here"

# To find dataset ID, go to the product page and copy the dataset ID
dataset_id = "Enter the dataset ID here"

file_path = "Enter your .csv file path"
url = 'http://dev.hystake.com/api/v1/dataset/' + dataset_id + '/'
mode = 'append'  # append / overwrite
skiprows = 1  # skip the first n rows of the csv
url_params = {'key': apikey, 'mode': mode, 'skiprows': skiprows}

# upload
file = open(file_path)
csv_reader = csv.reader(file)
request_data = {'dataset': list(csv_reader)}

r = requests.post(url, params=url_params, json=request_data)
