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

== November 1, 2013 ==
- Fixed HTTP 403 Error by tricking hackernews into thinking the request is coming from a browser.

== December 15, 2013 ==
- Initial threading implemented. Average 2 second improvement.

== January 27, 2014 ==
- Switched from the 'Threading' library to 'Mutliprocessing.dummy' library. Speed increase of 2x from non-threaded version.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/sunwooz/hacker-news-job-parser/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

