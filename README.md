Scrapr
======

By Maury Quijada, created on August 2, 2013

This program is a quick and dirty soltuion to scraping an HTML
table on college profiles listed on a website (namely ASEE.org) 
and outputting the results of that scraping to a CSV file.
Used Python, BeautifulSoup, and urllib for fetching the URL and
extracting the necessary information. Used Flask and Bootstrap
to make a barebones server and a pretty interface for interacting
with the script. Flask hosted via reverse proxy on Nginx, and static
file directory served, well, statically, using Nginx.

This is a *very* quick and dirty script with no error handling. But
given that it took only a few hours to write (my first Flask application),
it gets the job done.