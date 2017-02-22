### Running Andrew's Code works on Windows/Linux/MacOSX


### Getting a cleaned up version of the tsv in csv format.
1. Place your tsv file or directory in movie_credits.
2.  In moviecredits folder (where the main.py is) run `python3 main.py`

##### output
* your **actors.list.tsv.csv** will be located where the tsv file is. 
* A pairing of `top ators` will be outputed

### Results

lines in the file 18435200

no. of actors 2010940

no. of movies 1042622

# movie_credits
Machine learning program to flag new credits

 RULES:
 1       Movies and recurring TV roles only, no TV guest appearances
 2       Please submit entries in the format outlined at the end of the list
 3       Feel free to submit new actors

 "xxxxx"        = a television series
 "xxxxx" (mini) = a television mini-series
 [xxxxx]        = character name
 <xx>           = number to indicate billing position in credits
 (TV)           = TV movie, or made for cable movie
 (V)            = made for video movie (this category does NOT include TV
                  episodes repackaged for video, guest appearances in
                  variety/comedy specials released on video, or
				  self-help/physical fitness videos)


Please look at this in **Raw**


### Observations
* A television series is placed inside a string `""`
* we do not need *character names* which are placed inside `[]`
* (TV) and (V) seem to be still considered movies
	* Documentaries lie in (TV), [A documentary is a broad term to describe a non-fiction movie](http://www.desktop-documentaries.com/what-is-a-documentary.html)
	* (V) Music feature films lie in (V) 
* Do we keep uncredited?
* The first element always seems to be the name of the actor
