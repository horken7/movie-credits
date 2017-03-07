from typing import Set

class Lookup:

    def __init__(self, id2actors, id2movies, movies2id, actors2id, actor2movies, movie2actors):
        """
        :param id2actors: Dict
        :param id2movies: Dict
        :param movies2id: Dict
        :param actors2id: Dict
        :param actor2movies: Defaultdict
        :param movie2actors: Defaultdict
        """
        self.id2actors = id2actors
        self.id2movies = id2movies
        self.movies2id = movies2id
        self.actors2id = actors2id
        self.actor2movies = actor2movies
        self.movie2actors = movie2actors

    def convert_to_actor_name(self, ids: Set):
        return [self.id2actors.get(id) for id in list(ids)]

    def convert_to_movie_name(self, id):
        """id: Integer"""
        return self.id2movies.get(id)

    def movie_cast(self, title):
        """
        Get the cast of relevant movie titles from the given title
        :return List of cast of the movies
        """
        casts_id = []

        # find similar titles
        movie_titles = (movie_title for movie_title in self.movies2id.keys() if title in movie_title)

        # get the id
        for movie in movie_titles:
            movie_id = self.movies2id.get(movie)
            cast_ids = self.movie2actors.get(movie_id)
            casts_id.append((movie, cast_ids))

            print()
            print(movie)
            for cast_id in cast_ids:
                cast = self.id2actors.get(cast_id)
                print(cast)

        return casts_id


    def actor(self, name):
        """find the actor id"""

        actor_id = []

        actors = [actor_name for actor_name in self.actors2id.keys() if name in actor_name]
        if actors:
            for actor in actors:
                print("actor", actor, "id:", self.actors2id.get(actor))
                actor_id.append(self.actors2id.get(actor))
            return actor_id
        else:
            exit("Error: no actors named {}".format(name))



    def as_pairs(self):
        # go through the movies
        for _, movies in top_actors.items():
            for movie in movies:

                # convert to names
                print("movieid: {} movie: {}, actorsid: {}, actors: {}".format(movie,
                                                                               self.convert_to_movie_name(movie),
                                                                               self.movie2actors.get(movie),
                                                                               self.convert_to_actor_name(
                                                                                   self.movie2actors.get(movie))))
                # return actors
                pairs = list(make.pair_actors(movie2actors.get(movie)))
                if pairs:
                    print(pairs)
                else:
                    print("skip, only one actor")

    def example(self):

        # go through the movies
        for _, movies in self.actor2movies.items():
            for movie in movies:

                # convert to names
                print("movieid: {} movie: {}, actorsid: {}, actors: {}".format(movie,
                                                                               self.convert_to_movie_name(movie),
                                                                               self.movie2actors.get(movie),
                                                                               self.convert_to_actor_name(
                                                                                   self.movie2actors.get(movie))))

                # return actors
                pairs = list(make.pair_actors(movie2actors.get(movie)))
                if pairs:
                    print(pairs)
                else:
                    print("skip, only one actor")