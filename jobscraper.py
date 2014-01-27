import urllib2
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from multiprocessing.dummy import Pool as ThreadPool

# This is a small program to narrow down the list of HackerNews 'Now Hiring'
# posts to the locations you want to work.
# You'll have to install beautifulsoup4 with pip install beautifulsoup4
# github.com/sunwooz

job_list = []
url_list = []

##############
# HOW TO USE #
##############

# 1. Install beautifulsoup4 with $ pip install beautifulsoup4
# 2. Change the three variables, text_file, hackernews_page, keywords to your liking
# 3. Run the script using python (I used python2.7-32)
# 4. Let me know how it worked out at yangsunwoo@gmail.com or on github

# Name of file you want to create. Creates the file if it doesn't exist.
text_file = 'jobsNov2013.txt' 

#url of hacker news job page
hackernews_page = 'https://news.ycombinator.com/item?id=6653437' 

#Change the keywords for your location
keywords = ['nyc', 'New York', 'NewYork', 'NYC', 'NY', 'new york']


def create_url_list(initial_link):
    if len(url_list) == 0:
		url_list.append(initial_link)

    request = urllib2.Request(initial_link, headers={'User-Agent' : "Magic Browser"})
    url_soup = BeautifulSoup( urllib2.urlopen( request ).read() )
    more_link = url_soup.find('a', text='More')
    if more_link:
    	href = more_link.get('href')
        hacker_url = 'https://news.ycombinator.com' + href
        url_list.append(hacker_url)
        create_url_list(hacker_url)

def print_urls():
    for url in url_list:
    	print 'Found ' + url

def pool_jobs():
    print 'Gathering jobs...'
    pool = ThreadPool(20)

    results = pool.map(gather_job, url_list)

    pool.close()
    pool.join()

def gather_job(url):
    request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    soup = BeautifulSoup( urllib2.urlopen( request ).read() )

    for span in soup.find_all('span', class_='comment'): #find the comment span
    	text = span.get_text()
     	if any(job in text for job in keywords):
        	job_list.append(text)
        	print 'Added Job.'

def write_jobs():
    print 'Writing jobs to ' + text_file
    file = open(text_file, 'w')

    for single_job in job_list:
        file.write(single_job.encode("utf-8"))
        file.write('\n\n\n===========================================================================================\n\n\n')

    print 'Done.'

create_url_list(hackernews_page)

print_urls()

pool_jobs()

write_jobs()