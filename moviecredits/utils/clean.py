from typing import List
import re
import unicodedata

"""
look up online movie database to check if its a movie

argument movie, expects a String
return Boolean
"""

"""
patterns:
\(.?V\) (TV) and (V)
\[.*\] character name
".*" TV show
"""

non_movie = re.compile('".*"|\(.?V\)')  # pattern: "xxxx"
character_name = re.compile('\[.*\]', re.DOTALL)
movie_year = re.compile('\(.*\)|\(\?*\)')


def remove_empty(string):
    return [item for item in string if item]

def format(list):
    """
    Check if the actor has a first name (the last name is always given)
    Always assign the 3rd slot as movies
    if there is no first name assign it as None
    :param list: List of strings
    :return: List
    """

    # detecting if the name contains a (year)
    first_name = list[1]
    is_movie = movie_year.search(first_name)

    # split array
    # append to the first array
    # join the arrays

    if is_movie:
        split_a = list[0:1]
        split_b = list[2:]
        split_a.append(None)
        return (split_a + split_b) # new list
    else:
        return list # original list


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

        # remove [xxxx] (TV) (V)
        newline = character_name.sub("", item)
        string = newline.split('\t')
        newlist = remove_empty(string)

        # TODO some lines are still a little strange. We must specify more conditions for the correct lines to pass
        # the list should at least contain (actor and movie)
        if len(newlist) > 2:
            return format(newlist)

def unicode_normalise_movies_actors(row: List):
    """
    Remove diacritic marks for movies titles and actor names
    """

    tmp_movie = remove_end_space(row[2].lower())
    tmp_actor_name = full_name(row[1], row[0]).lower()

    actor_name = shave_marks(tmp_actor_name)
    movie = shave_marks(tmp_movie)
    return movie, actor_name


def shave_marks(text):
    """remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', text)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


def full_name(first_name, last_name):
    if first_name is None:
        name = last_name
        return name
    else:
        name = (first_name + " " + last_name)
        return name

def remove_end_space(text):
    txt = text.rsplit()
    new_txt = ' '.join(word for word in txt)
    return new_txt

