import urllib.request
import urllib.error 
from urllib.parse import quote
from xml.dom import minidom
import re

def getTags(wikiLink):
    tags = fromWikiLinkToTags(wikiLink)
    tags = getFirstOption(tags)
    tags = removeSubstring(tags, '[[')
    tags = removeSubstring(tags, ']]')
    tags = removeSubstring(tags, '.')
    tags = removeTagIncludeSubstring(tags, 'File:')
    tags = removeTagIncludeSubstring(tags, 'Category:')
    tags = removeDuplicates(tags)

    return tags

def toLower(tagsList):
    newTagsList = []

    for t in tagsList:
        newTagsList.append(t.lower())
    
    return newTagsList

def removeTagIncludeSubstring(tagsList, substring):
    newTagsList = []

    for t in tagsList:
        iS = t.find(substring)
        if(iS == -1):
            newTagsList.append(t)
    
    return newTagsList

def removeDuplicates(tagsList):
    return list(dict.fromkeys(tagsList))


def removeSubstring(tagsList, substring):
    newTagsList = []

    for t in tagsList:
        iS = t.find(substring)
        if(iS != -1):
            newTagsList.append(t[:iS] + t[(iS + len(substring)):]) 
        else:
            newTagsList.append(t)
    
    return newTagsList

def getFirstOption(tagsList):
    newTagsList = []

    for t in tagsList:
        iS = t.find('|')
        if(iS != -1):
            newTagsList.append(t[:iS]) 
        else:
            newTagsList.append(t)
    
    return newTagsList


def fromWikiLinkToTags(linkArticle):
    cutIndex = linkArticle.find('/wiki/') + 6
    linkXML = linkArticle[:cutIndex] + 'Special:Export/' + quote(linkArticle[cutIndex:])
    

    response = urllib.request.urlopen(linkXML)
     
    xml_str = response.read()
    xmldoc = minidom.parseString(xml_str)

    

    obs_values = xmldoc.getElementsByTagName('text')

    tags = []

    if(len(obs_values) == 0):
        return tags

    text = obs_values[0].firstChild.nodeValue
    starts = [m.start() for m in re.finditer('\[\[', text)]
    ends = [m.end() for m in re.finditer('\]\]', text)]


    for i in range(len(starts)):
        tags.append(text[starts[i] + 2:ends[i] - 2])

    return tags
