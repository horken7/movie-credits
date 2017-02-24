### Running Andrew's Code works on Windows/Linux/MacOSX


### Getting a cleaned up version of the tsv in csv format.
1. Place your tsv file or directory in movie_credits.
2.  In moviecredits folder (where the main.py is) run `python3 main.py`

##### output
* your **actors.list.tsv.csv** will be located where the tsv file is. 
* A list of `top ators` with the number of times they worked with their colleagues.


##### output Example
```python
actorA, actorB, weight
7411 3626 1
7411 7411 71
7411 9826 3
7411 7005 1
2964 551 1
2964 8713 1
2964 4010 2
2964 1847 1
2964 172 1
2964 7150 5
2964 176 2
2964 2641 2
2964 2964 77
2964 7093 1
2964 6678 1
2964 5719 2
2964 5961 1
1605 4992 1
1605 1440 1
1605 10259 1
1605 1605 77
1605 1991 1
1605 10075 1
1605 4917 1
1605 9903 1
281 5792 1
281 281 76
281 7340 1
281 1784 2
281 6569 1
```

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
