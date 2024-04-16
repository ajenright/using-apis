api_key = "paste key here"

import requests
import json
import pprint


##### Useful URLS
# Base URL for accessing the TMBD API
movies_base= "https://api.themoviedb.org/3/"

# URL for getting information about the the Marvels (movie id 609681)
marvels = movies_base + "movie/609681"

# Additional URLS for searching
people_search = movies_base + "search/person"
movie_search = movies_base + "search/movie"

# URL for getting the cast and crew lists for movie 24428 (Avengers)
movie_credits = movies_base + "movie/24428/credits"


##### Code for accessing TMBD

# Request information about the Marvels, and pass the api_key as a parameter
parameter = {"api_key": api_key}
result_json = requests.get(marvels, parameter)

# Convert the results from JSON to a dictionary
results = json.loads(result_json.text)

# Pretty print the dictionary so we can see what it looks like
pprint.pprint(results)


