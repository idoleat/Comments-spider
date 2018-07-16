import json

import os
import google.oauth2.credentials
import sys
import subprocess
subprocess.call('pip install --upgrade google-api-python-client',shell=True)
print ("Checking Google API client installment.....")

import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client.tools import argparser


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


print ("---------------")
print ("Welcome to the comment spider! You can use this tool to get more information from Youtube videos.")
title = input("Please enter the title you want to search on Youtube: ")

def youtube_search(options):
  youtube = build("youtube", "v3",developerKey="AIzaSyBgC5WJ4cUQPHiBmTLHx_SKD7A_5EOi5hs")

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

  print("Videos:\n", "\n".join(videos), "\n")
  print("Channels:\n", "\n".join(channels), "\n")
  print("Playlists:\n", "\n".join(playlists), "\n")


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default=title)
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

  try:
    youtube_search(args)
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))


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