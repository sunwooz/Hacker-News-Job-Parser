import urllib2
from bs4 import BeautifulSoup

#This is a small program to narrow down the list of HackerNews 'Now Hiring'
#posts to the locations you want to work.
#You'll have to install beautifulsoup4 with pip install beautifulsoup4
#github.com/sunwooz


#Change the keywords for your location
locations_to_check = ['nyc', 'New York', 'NewYork', 'NYC', 'NY', 'new york']

job_list = []

#Change the url of the HackerNews 'Now Hiring' page
url_list = [
	'https://news.ycombinator.com/item?id=6475879',
	'https://news.ycombinator.com/x?fnid=EZY1yngR9sl47pHiQ0KpaH',
	'https://news.ycombinator.com/x?fnid=9WfKpXenzsn320MGUYFTJL',
	'https://news.ycombinator.com/x?fnid=Jh1ZyMhLTlsmJYX0vuR1Ys',
	'https://news.ycombinator.com/x?fnid=uMBV53CUcAjA9bGlE7eaHi'
]

for url in url_list:
	soup = BeautifulSoup( urllib2.urlopen( url ).read() )

	for span in soup.find_all('span', class_='comment'): #find the comment span
		text = span.get_text()
		if any(job in text for job in locations_to_check):
			job_list.append(text)

#Change the name of the file to your liking
file = open('jobsOct2013.txt', 'w')

for single_job in job_list:
	file.write(single_job.encode("utf-8"))
	file.write('\n\n\n=============================')
	file.write('===============================')
	file.write('===============================\n\n\n')