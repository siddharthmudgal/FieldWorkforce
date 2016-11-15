
# coding: utf-8

# In[107]:

import re


# http://user:pass@NetLoc:80/path;parameters/path2;parameters2?query=argument#fragment

#returns if the url passed is a valid url
def isURL(url):  
    regex1 = r"(((https|http|ftp)\:\/\/)|(mailto:\s))(www\.)*"
    regex2 = r"[\w\d\-\.\:]+[/@]{0,1}([\w\d\.\-\/\?\=\#\&])*"
    if (re.search(regex1+regex2,url)):
        return True
    return False

#returns the scheme of the url https, http, ftp
def getScheme(url):
    regex = r"(http|ftp|https)(:\/\/)"
    result = re.search(regex,url)
    if (result):
        return result.group(1)
    return "Invalid scheme"

#returns location of the url
def getLocation(url):
    pattern = re.search("mailto|@",url)
    if (pattern):
        regex = r"(?:(?:mailto\:\s)*[^@]*@)([^\/]*)"
        result = re.search(regex,url)
        if (result):
            return result.group(1)
    else:
        regex1 = r"(?:(?:(https|http|ftp):\/\/))"
        regex2 = r"((www\.){0,1}[\w\d\-]+\.[\w\d]+:*[\d]*)(?=\/)*"
        result = re.search(regex1+regex2,url)
        if (result):
            return result.group(2)
    return "Invalid Location"

#returns path in the url
def getPath(url):
    regex1 = r"(?:(?:(?:https|http|ftp)\:\/\/[^\/]*)"
    regex2 = r"|(?:mailto\:\s))([^\s?#=]*)"
    result = re.search(regex1+regex2,url)    
    if (result):
        return result.group(1)
    return "Path Absent"

#returns params as a set in url
def getParams(url):
    regex = r"(?:\?|\&)([^=]+)\=([^&/#]+)"
    result = re.findall(regex,url)
    if (result):
        return result
    return "No params found"

#returns fragment in the url
def getFragment(url):
    regex = "(?:\#)(.*)"
    result = re.search(regex,url)
    if (result):
        return result.group(1)
    return "No fragment found"

#returns the port number in the url
def getPort(url):
    regex = "(?:\:)(\d+)"
    result = re.search(regex,url)
    if (result):
        return result.group(1)
    return "No port number found"
    
#returns username and password present in the url
def getUsernamePassword(url):
    regex = r"(?:(?:http|ftp|https)(?:\:\/\/))([^\:]+)(?:\:)([^@]+)"
    result = re.search(regex,url)
    if (result):        
        usrPass = {'username':result.group(1),'password':result.group(2)} 
        return usrPass;
    return 'No username password found'

#defrags the url
def defrag(url):
    regex = r"(.*)(?=#)"
    result = re.search(regex,url)
    if (result):
        return result.group(1)
    return url

#returns the host in the url
def getHost(url):
    regex1 = r"(?:\@)([\w\d]*)"
    result = re.search(regex1,url)
    if (result):
        return result.group(1)
    regex2 = r"(?:(?:https|http|ftp)\:\/\/(?:www\.)*)([\w\d\-]*)"
    result = re.search(regex2,url)
    if (result):
        return result.group(1)
    return "Invalid hostname"

