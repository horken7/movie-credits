"""
This file is part of imdb-data-parser.

imdb-data-parser is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

imdb-data-parser is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with imdb-data-parser.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import urllib


class FreebaseAgent(object):
    """Helper class to retrieve IMDb ids from freebase.

    Currently only supports movies. TV series support will 
    hopefully be added if need arises.
    """

    def __init__(self):
        super(FreebaseAgent, self).__init__()
        self.API_KEY = 'YOUR-API-KEY-GOES-HERE' #TODO read these values from config
        self.topic_service_url = 'https://www.googleapis.com/freebase/v1/topic' 
        self.search_service_url = 'https://www.googleapis.com/freebase/v1/search'

    def get_imdb_id(self, movie_name):
        """Returns the IMDb id of a movie, given its title.

        The returned title is the one with the highest
        freebase confidence score.

        Returns None if no such movie exists in freebase.
        """
        mid = self.get_topic_id(movie_name)
        topic = self.get_topic(mid)
        return topic

    def get_topic_id(self, name, entity_type='/film/film'):
        """Gets the topic id (aka mid, freebase id) of a title. 
        """
        params = {
            'query': name,
            'type': entity_type,
            'limit': 1
        }
        url = self.search_service_url + '?' + urllib.urlencode(params)
        response = json.loads(urllib.urlopen(url).read())

        for result in response.get('result'):
            mid = result.get('mid', None)
            return mid
        return None

    def get_topic(self, mid):
        """Gets the IMDb id of a freebase topic. Returns None if no
        such thing exists.
        """
        params = {
            'filter': '/type/object/key'
        }
        url = self.topic_service_url + mid + '?' + urllib.urlencode(params)
        topic = json.loads(urllib.urlopen(url).read())

        for property in topic['property']:
            for value in topic['property'][property]['values']:
                if value['text'].startswith('/authority/imdb/title'):
                    return value['text'].split('/')[-1]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Retrieve imdb id from freebase.")
    parser.add_argument('movieName', help='The name of the movie')
    args = parser.parse_args()

    agent = FreebaseAgent()
    mid = agent.getTopicId(args.movieName)
    print 'freebase topic id (mid) is', mid
    topic = agent.getTopic(mid)
    print 'imdb id is', topic, 'so the url is http://www.imdb.com/title/'+topic
    print agent.getImdbId(args.movieName)