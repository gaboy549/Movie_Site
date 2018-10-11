# -*- coding: cp1252 -*-
import media
import fresh_tomatoes
import json
import urllib
import re

def config_movie_objects():
    """This initializes Movie objects, then send them to fresh_tomatoes to
    create the HTML and open the website.  The movie data is queried from
    IMDB and the trailer URL is queried from YouTube.

    Args:
        none

    Returns:
        none
    """
    movies = []
    movie_title_list=["Back to the Future","Blazing Saddles","The Dark Knight",
                      "Deadpool","Die Hard","Fear and Loathing in Las Vegas",
                      "Forbidden Zone","Guardians of the Galaxy",
                      "The Last Dragon","Pulp Fiction","They Live"]
    #  For every movie title gather info and add to list
    for movie_title in movie_title_list:
        imdb_data = query_imdb(movie_title)
        trailer_url = query_youtube(movie_title)

        if imdb_data["Response"] == "True":  #  Dictionary contains movie info
            movies.append(media.Movie(imdb_data["Title"],
                                      imdb_data["Year"],
                                      imdb_data["Plot"],
                                      imdb_data["Poster"],
                                      trailer_url,
                                      imdb_data["Rated"],
                                      imdb_data["Runtime"]))

    # Send the list of movie objects to the open_movies_page method
    # Generates and opens the fresh_tomatoes website
    fresh_tomatoes.open_movies_page(movies)


def query_imdb(movie_title):
    """This will query and return all data from IMDB based on movie title.

    Args:
        movie_title (str): This is the movie title to search for

    Returns:
        dictionary: dictionary based on response json. Response==False on error
    """
    base_url = "http://omdbapi.com/?t=" #  Only submitting Title
    response = urllib.urlopen(base_url + movie_title)
    if response.getcode() == 200:  #  HTTP status is OK
        imdb_data = json.loads(response.read())  #  Deserialize into dictionary
        return imdb_data
    else:  #  HTTP error
        return {"Response" : "False"}
                            
def query_youtube(movie_title):
    """This will query and return the first youtube URL based
    on movie title.  " trailer" is added to the end of every
    search.

    Args:
        movie_title (str): This is the movie title to search for

    Returns:
        str: The URL for the 1st trailer on Youtube
    """
    #convert movie_title to “percent-encoded” string, then open search
    query_string = urllib.urlencode({"search_query" : movie_title + " trailer"})
    html_content = urllib.urlopen("http://www.youtube.com/results?" +
                                          query_string)
    #use regular expressions to find all 11 character videos IDs
    query_results = re.findall(r'href=\"\/watch\?v=(.{11})',
                                html_content.read())
    return "http://www.youtube.com/watch?v=" + query_results[0]
                        

config_movie_objects()                   
