import urllib2
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

#This is a small program to narrow down the list of HackerNews 'Now Hiring'
#posts to the locations you want to work.
#You'll have to install beautifulsoup4 with pip install beautifulsoup4
#github.com/sunwooz

job_list = []
url_list = []

# Name of file you want to create. Creates the file if it doesn't exist.
text_file = 'jobsOct2013.txt' 

#url of hacker news job page
hackernews_page = 'https://news.ycombinator.com/item?id=6475879' 

#Change the keywords for your location
locations_to_check = ['nyc', 'New York', 'NewYork', 'NYC', 'NY', 'new york']


def create_url_list(initial_link):
	if len(url_list) == 0:
		url_list.append(initial_link)

	url_soup = BeautifulSoup( urllib2.urlopen( initial_link ).read() )
	more_link = url_soup.find('a', text='More')
	if more_link:
		href = more_link.get('href')
		hacker_url = 'https://news.ycombinator.com' + href
		url_list.append(hacker_url)
		create_url_list(hacker_url)

def print_urls():
	for url in url_list:
		print 'Found ' + url

def gather_jobs():
	print 'Gathering jobs...'
	for url in url_list:
		soup = BeautifulSoup( urllib2.urlopen( url ).read() )

		for span in soup.find_all('span', class_='comment'): #find the comment span
			text = span.get_text()
			if any(job in text for job in locations_to_check):
				job_list.append(text)
				print 'Added Job.'
	print 'Total of ' + str( len(job_list) ) + ' jobs added.'

def write_jobs():
	print 'Writing jobs to ' + text_file
	#Change the name of the file to your liking
	file = open(text_file, 'w')

	for single_job in job_list:
		file.write(single_job.encode("utf-8"))
		file.write('\n\n\n===========================================================================================\n\n\n')

	print 'Done.'

#Change the url of the HackerNews 'Now Hiring' page (FIRST PAGE)
create_url_list(hackernews_page)

print_urls()

gather_jobs()

write_jobs()