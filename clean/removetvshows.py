# import requests
from typing import List
import re

"""
look up online movie database to check if its a movie

argument movie, expects a String
return Boolean
"""

non_movie = re.compile('".*"')  # pattern: "xxxx"
character_name = re.compile('\[.*\]', re.DOTALL)


# r = requests.get('http://www.omdbapi.com/?t=Sofies+verden')
# print(r.status_code)
# print(r.json())

def remove_empty(string):
    return [item for item in string if item]


def clean(tv: List):
    """
    The database has `""` for TV shows
    :param tv: list
    :return: new list
    """

    for item in tv:
        # item is a string of the whole row

        # skip "xxxx"
        unwanted = non_movie.search(item)
        if unwanted:  # skip line
            return

        # remove [xxxx]
        newline = character_name.sub("", item)
        string = newline.split('\t')
        newlist = remove_empty(string)
        return newlist
