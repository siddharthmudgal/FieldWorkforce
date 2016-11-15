
# coding: utf-8

# In[9]:

from urllib2 import urlopen
from bs4 import BeautifulSoup
from cmd import Cmd
import re


#returns number of results in the page
def getCount(url):
    page = urlopen(url)
    soup = BeautifulSoup(page,"lxml")
    divs = soup.select("div h2 a.productName")
    count = len(divs)
    if (count>0):
        return len(divs)
    else:
        return 'No results found'

#prints the results in the page
def getResults(url):
    page = urlopen(url)
    soup = BeautifulSoup(page,"lxml")
    divs = soup.select("div h2 a.productName")
    for div in divs:
        if (div):
            title = div.get('title')
            if (title):
                print div.get('title')
            else:                
                print div.find('span').get('title')

class MyPrompt(Cmd):

    def do_count(self,args):
        """gets count of results of the page"""
        if (len(args) == 0):
            print "please pass a url"
        keyword = re.search(r"(?:http\:\/\/www\.shopping\.com\/products\?KW=)(.*)",args)
        if (keyword):
            print getCount(args)
        else:
            print "invalid url"
            
    def do_result(self,args):
        """prints results of the page"""
        if (len(args) == 0):
            print "please pass a url"
        keyword = re.search(r"(?:http:\/\/www\.shopping\.com\/products\~PG\-)(\d*)(?:\?KW=)(.*)(?:\"*)",args)
        if (keyword):
            getResults(args)
        else:
            print "invalid url"
        
    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Enter query -> 1. count \'url\' for getting count\n2. result \'url\' for getting results')

