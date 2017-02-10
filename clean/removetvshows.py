# import requests
from typing import List
import re

"""
look up online movie database to check if its a movie

argument movie, expects a String
return Boolean
"""

p = re.compile('".*"')

# r = requests.get('http://www.omdbapi.com/?t=Sofies+verden')
# print(r.status_code)
# print(r.json())

def clean(tv: List):
    """
    The database has `""` for TV shows
    :param tv: list
    :return: new list
    """

    a = filter(p.match, tv[0])
    print(list(a))

