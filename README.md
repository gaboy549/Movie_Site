# Movie Trailer Website

### What is it?


 Server-side Python code to store a list of favorite movies, 
 including box art imagery and a movie trailer URL. The code 
 generates a static web page allowing visitors to browse movies. The 
 movie information is queried from IMDB and the trailer URL queried
 from Youtube. Only the movie title needs specified to be added to
 the page.


### Installation & Usage


1. Download Python version 2.7.13 from the [Python site](https://www.python.org/downloads/)
2. Follow Python installation instructions based on operating system using [Python's Documentation](https://docs.python.org/2/using/)
3. Place the three *.py files in the same directory together. 
	* *start_website.py*
	* *media.py*
	* *fresh_tomatoes.py*
4. Run file *start_website.py*

This should cause *start_website.py* to be run in Python's IDLE app. The file will generate the *fresh_tomatoes.html* file in the same directory as the *.py files. The *.html website should be automatically opened in your default browser. 

Steps 1 through 4 are not required once the *fresh_tomatoes.html* file has been generated, *fresh_tomatoes.html* can be opened directly.

If you wish to change the displayed movies, edit movie_title_list on line 20 of *start_website.py*. Then simply run file *start_website.py* again to generate a new *.HTML file.

```python
movie_title_list=["Back to the Future","Blazing Saddles","The Dark Knight",
                      "Deadpool","Die Hard","Fear and Loathing in Las Vegas",
                      "Forbidden Zone","Guardians of the Galaxy",
                      "The Last Dragon","Pulp Fiction","They Live"]
```


### Contacts

* If you have a concrete bug report or have questions please email at zgrauer@wgu.edu
 

### License

The MIT License (MIT)

Copyright (c) 2016 Zachary Grauerholz

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the  Software is furnished to d so, subject to the following conditions:

The above copyright notice and this permission notice shall be included  in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR  THE USE OR OTHER DEALINGS IN THE SOFTWARE


