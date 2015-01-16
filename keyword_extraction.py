__author__ = 'pbmrt'

import bs4
import urllib2
import string
import json


# some exception handling for the import routine of relevant modules/libs

try:
    from bs4 import BeautifulSoup
    from alchemyapi import AlchemyAPI
    from pprint import pprint

except ImportError:
    print("Please Check Your Module Installation . . . ")


# hard coded website url for keyword analysis
url = "http://www.dmv.org"
# call urllib2 module's urlopen function to read the website at the given URL
# and stores the data into a page object.
page = urllib2.urlopen(url)

# store the alchemy api into an alchemyapi object
alchemyapi = AlchemyAPI()

# create a soup object that calls the bs4 module from Beautiful Soup and
# pass in a Beautiful Soup function that reads our page object from above.
soup = bs4.BeautifulSoup(page.read())

# store stripped tags and whitespace content into a list
# paraList = []

# find all paragraphs tagged with <p> in the html code of the page that's been read
# using the findAll() function from Beautiful Soup.
textBody = soup.findAll('p')

# textBody = soup.findAll('body')

# iterate through each of the paragraphs of the web page and extract the keywords and
# their relevance and store it to a response object calling the keyword() function
# from the alchemy api.  Pass in a text type and paragraph as arguments.
# pretty print to console the response object (keywords and relevance) for each key word
# in each paragraph.
for i in textBody:
    # paraList.append(''.join(str(i.string)).split(','))
    # paraList.append(j)
    response = alchemyapi.keywords('text',i)
    pprint(response)









