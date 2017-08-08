#!/usr/bin/env python
''' Script to retrieve grades from Ellucian Banner Web '''
import requests
from lxml import html
import os
from settings import settings

# Create and establish session
s = requests.Session()
request = s.get(settings['BASE_URL'] + 'twbkwbis.P_WWWLogin')

# POST login information
response = s.post(settings['BASE_URL'] + 'twbkwbis.P_ValLogin',
                  data=dict(sid=settings['USERNAME'],
                            PIN=settings['PASSWORD']))

# POST semester to retrieve (Fall 2017)
response = s.post(settings['BASE_URL'] + 'bwskflib.P_SelDefTerm',
                  data=dict(term_in=settings['SEMESTER']))

# GET add a class page
response = s.get(settings['BASE_URL'] + 'bwskfreg.P_AltPin')

# Create parseable HTML from response
content = html.fromstring(response.content)

print(str(content))
