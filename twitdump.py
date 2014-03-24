import sys
import time
import urllib2
from BeautifulSoup import BeautifulSoup


def parse_twitter_page(url):
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page)

	'''
	tweets = soup.findAll("div", {"class": "tweet-text"})
	for tweet in tweets:
		print tweet["data-id"], "\n", tweet.find("div").text.encode('utf-8')
	'''

	tweets = soup.findAll("table", {"class": "tweet  "}) # yep, with two spaces

	for tweet in tweets:
		timestamp  = tweet.find("td", {"class": "timestamp"}).text
		data_id    = tweet.find("div")["data-id"]
		tweet_text = tweet.find("div", {"class": "dir-ltr"}).text.encode('utf-8')

		print tweet_text, "\n#", timestamp, data_id, "\n"

	try:
		older_tweets_link = soup.find("div", {"class": "w-button-more"}).find("a").get('href')
		parse_twitter_page(older_tweets_link)
	except (AttributeError):
		print "Reached the last tweet. Finalizing."

if __name__ == '__main__':
	twitter_username = sys.argv[1]

	print "@"+twitter_username, " ", time.strftime("%c"), "\n\n"
	parse_twitter_page("https://mobile.twitter.com/"+twitter_username)
