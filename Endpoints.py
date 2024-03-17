import backoff
import streamlit as st
import requests
import os
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

class ForbiddenError(Exception):
    pass

@backoff.on_exception(backoff.expo, ForbiddenError, max_tries=20)
def Leetcode(username):
    url = 'https://leetcode.com/graphql'


    headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'cookies' : 'asdfads',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

    }
    
    query = '''
        query combinedQueries($username: String!) {
            matchedUser(username: $username) {
                submitStatsGlobal {
                    acSubmissionNum {
                        difficulty
                        count
                    }
                }
            }
        }
    '''

    variables = {
        "username": f"{username}"
    }

    payload = {
        'query': query,
        'variables': variables
    }

    response = requests.post(url, json=payload, headers=headers)


    if response.status_code == 200:
        json_dict = response.json()

        if not json_dict:
            return None

        matchedUser = json_dict['data']['matchedUser']

        total = 0

        if matchedUser:
            problems_solved = matchedUser['submitStatsGlobal']['acSubmissionNum']

            for pair in problems_solved:
                if pair['difficulty'] == 'All':
                    total = pair['count']

            

        else:
            return {}, False

        return total, True

    
    elif response == 404:
        return {}, False
        
    else :
        print(username)
        raise ForbiddenError("Received a 403 Forbidden response")
    
