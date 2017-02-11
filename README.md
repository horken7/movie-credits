### Running Andrew's Code (Works on Macs/Linux Only):
**It will work on windows but I will need to make some fine adjustments...**

Inside `datacleaning.py`
1. make sure to change the path to your tsv file:
```python
filename = "2017-02-09_223251_ImdbParserOutput/actors.list.tsv" # please change this path to your own file path to the tsv file
```

2. and comment out: 

```python
if index > 1000:  # remove these two lines if you want to run through the whole file
    break
```

3. Run it `python datacleaning.py`





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