Hacker-News-Job-Parser
======================

This small python program scrapes data off of a 'Hiring Now' page on Hacker News and only saves the jobs with certain keywords. Ie 'New York', 'San Francisco' etc
You can also use the keywords to find specific jobs ie 'Machine Learning'

You need to install Beautiful Soup 4 in order to use this program

$ pip install beautifulsoup4

tested with python2.7-32


Problems
========

- It will grab jobs that mention any of the keywords in your list.
- It will break if someone creates a link with 'More' as the text :(


Updates
=======

== October 1, 2013 ==
- Program can now accept multiple urls (redacted)
- Program can now determine all the child pages with just the initial hacker news job page
- Organized code for easier use
