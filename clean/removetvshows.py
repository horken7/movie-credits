# import requests
from typing import List
import re

"""
look up online movie database to check if its a movie

argument movie, expects a String
return Boolean
"""

non_movie_pattern = re.compile('".*"') # pattern: "xxxx"

character_name_pattern = re.compile('\[.*\]')

# r = requests.get('http://www.omdbapi.com/?t=Sofies+verden')
# print(r.status_code)
# print(r.json())

def clean(tv: List):
    """
    The database has `""` for TV shows
    :param tv: list
    :return: new list
    """
    newlist = []

    for item in tv:
        #item is a string

        match1 = non_movie_pattern.search(item)
        if match1: #skip line
            return

    # remove element on line
        # find the element position which is not None
        print(character_name_pattern.sub("", item))




    #print([item for item in tv if character_name_pattern.search(item) is None])














