
import requests
import os
import csv
import json

'''
For more details: https://hystakeapialpha.docs.apiary.io/

A download query has 3 components:
1. required: API key
2. required: dataset code
3. optional: filter/sort criteria
'''

# find / regenerate your API key in Account Info -> Developer Info
apikey = "Enter your API token here"

# dataset code can be found in the product page, right under the table name
dataset_code = "Enter the dataset code here"

# query with URI parameters: filter, sort, limit, etc. API doc link: https://hystakenewapi.docs.apiary.io/#/reference/0/read-dataset
query = "(optional) Enter the query here, or leave it blank"

# request data (see examples below)
r = requests.get('http://dev.hystake.com/api/v1/dataset/' + dataset_code + '?key=' + apikey + query)

# example 1: return the last 3 day's crude oil prices
r1 = requests.get('http://dev.hystake.com/api/v1/dataset/HYSTAKE-CMEFUT-CL1/?key=' + apikey + '&sort=date.desc&limit=3')

# example 2: return the gold futures price since May 1, 2020
r2 = requests.get('http://dev.hystake.com/api/v1/dataset/HYSTAKE-CMEFUT-GC1/?key=' + apikey + '&filter=date__gt=05-01-2020')

# example 3: return the latest closing price of Eurodollar futures
r3 = requests.get('http://dev.hystake.com/api/v1/dataset/HYSTAKE-CMEFUT-ED1/?key=' + apikey + '&field=close&last=true')

# read data
json_data = json.loads(r.text)
product_name = json_data['product_name']        # product name
dataset_name = json_data['dataset_name']        # dataset name
raw_data = json_data['dataset']                 # data returned
