# https://data.nsw.gov.au/data/datastore/dump/21304414-1ff1-4243-a5d2-f52778048b29?format=json

from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import urllib.request, json 
from datetime import datetime
import re

urlNsw = 'https://data.nsw.gov.au/data/datastore/dump/21304414-1ff1-4243-a5d2-f52778048b29?format=json'
with urllib.request.urlopen(urlNsw) as url:
    data = json.loads(url.read().decode())

dynamodb = boto3.resource(
    'dynamodb', 
    region_name='us-west-2', 
    aws_access_key_id='AKIA6FOHCMMAE7CPWYHC',
    aws_secret_access_key='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'
)
table = dynamodb.Table('covid19_nsw')

sum_by_citycode = {}
for field in data['fields']:
    print(field)
for case in data['records']:
    city_code = int(case[2])
    city_name = str(case[6])
    sub_name = str(case[4])
    sub_code = str(case[3])
    date_case = re.search('\\d{4}-\\d{2}-\\d{2}', case[1])

    table.update_item(
        TableName='covid19_nsw',
        Key={
            'postcode': city_code
        },
        UpdateExpression="set postname = :pa, subname=:ps, subcode=:pu, date=:da",
        ExpressionAttributeValues={
            ':pa': city_name,
            ':ps': sub_name,
            ':pu': sub_code,
            ':da': date_case
        }
    )
    if city_code in sum_by_citycode:
        sum_by_citycode[city_code] += 1
    else: 
        sum_by_citycode[city_code] = 0

for code in sum_by_citycode:
    if sum_by_citycode[code] > 0: print('Code: {0} Sum: {1}'.format(code,sum_by_citycode[code]))