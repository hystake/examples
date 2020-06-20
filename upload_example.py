
import requests
import os
import csv
import json

'''
For more details: https://hystakenewapi.docs.apiary.io/

A download query has 3 components:
1. required: API token
2. required: user id code
3. required: product code
4. required: table code
'''

# Find / regenerate your API token in Account Info -> Developer Info
token = "Enter your API token here"

# the full dataset ID is composed of 3 parts: user ID, product ID, table ID
seller_id = "Enter your seller ID here"
product_id = "Enter your product ID here"
table_id = "Enter your table ID here"
datasetCode = seller_id + "-" + product_id + "-" + table_id

file_path = "Enter your .csv file path"
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