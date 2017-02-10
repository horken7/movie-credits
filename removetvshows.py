import requests


"""
look up online movie database to check if its a movie

argument movie, expects a String
return Boolean
"""

r = requests.get('http://www.omdbapi.com/?t=buffy')
print(r.status_code)
print(r)


def check(movie):
    pass
