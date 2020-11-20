import sys
import gT


def main(argv):
    if(len(argv) == 0):
        return
    id = 0

    
    firstKey = codify(argv[1])
    
    theList = {
        firstKey : {
            'index': id,
            'link': argv[1],
            'connectedNodes': []
        }
    }
    
    tags = gT.getTags(argv[1])
    
    d = toDict(tags)

    originID = id

    for key in d.keys():
        if key not in theList:
            id += 1

            theList[key] = {
                'index': id,
                'link': d[key],
                'connectedNodes': [originID]
            }
        else:
            theList[key]['connectedNodes'].append(originID)

    


def codify(text):
    return removeSubstring(text.lower(), [' ', '.', ':', '_', '(', ')', '-']) 
    

def removeSubstring(text, substrings):
    result = text

    for sString in substrings:
        iS = result.find(sString)

        while(iS != -1):
            result = result[:iS] + result[(iS + len(sString)):]
            iS = result.find(sString)
        

        
    return result

def toDict(tags):
    l = {}

    for t in tags:
        articleLink = 'https://en.wikipedia.org/wiki/' + '_'.join(t.split(' '))
        key = codify(t)

        if key not in l:
            l[key] = articleLink

    return l


if __name__ == "__main__":
    main(sys.argv)
    





