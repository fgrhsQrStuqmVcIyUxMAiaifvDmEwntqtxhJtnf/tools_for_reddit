import praw
import OAuth2Util
import json


def get_creds():
    with open('creds_file.json', 'r') as cred_file:
        creds = json.loads(''.join(cred_file.readlines()))
        
    return creds


def get_client():
    creds = get_creds()
    reddit_client = praw.Reddit(**creds)

    return reddit_client
