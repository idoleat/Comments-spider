import json

import os
import google.oauth2.credentials
import sys
import subprocess
subprocess.call('pip install --upgrade google-api-python-client',shell=True)

import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

api_key = "ZQq3mvbjbcmGFP04OTCoRTLt"
service = build('youtube', 'v3', developerKey=api_key)

print ("Welcome to the comment spider! You can use this tool to get more information from Youtube videos.")
title = input("Please enter the title you want to search on Youtube: ")

"""# Sample python code for search.list
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs

def print_response(response):
  print(response)

def search_list_by_keyword(service, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = service.search().list(
    **kwargs
  ).execute()

  return print_response(response)

search_list_by_keyword(service,
    part='snippet',
    maxResults=25,
    q=title,
    type='')"""


print ("Please enter the keywords you want to search in the comments(type 'exit' to stop):")
#I will make it unlimited late. I need to do some research on dynamic memory in Python. Or using Stack/Queue library instead.
keywords = [""]

while True:
	tempt = input()
	if tempt== "exit":#Maybe I should use regular expression for this.....
		break
	else:
		keywords.append(tempt)
		
print("Searching....")#I can add something interesting here to make the program juicy. Maybe a joke.
print("Hey! Here is the stuff I found: ")
print("	I haven't finish yet. HEHE")
ShareIt = input("Do you want to share it on Twitter?(N/Y)")
#Maybe I will change it to Facebook if output is too long.
#The probability I will change to Facebook is 0.7
if ShareIt=='Y':
	print("successfully shared!")
	print("Thanks for using this tool!")
	print("You can find the source code on https://github.com/idoleat/Comments-spider")
else:
	print("Thanks for using this tool!")
	print("You can find the source code on https://github.com/idoleat/Comments-spider")