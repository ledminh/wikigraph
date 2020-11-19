import sys
import gT


def main(argv):
    if(len(argv) == 0):
        return
    id = 0

    nameCode = convertToNameCode(argv[1])


    theList = {
        nameCode : {
            'index': id,
            'link': argv[1],
            'connectedNodes': []
        }
    }
    
    """
    print(theList)
    print(theList[argv[1]])
    print(theList[argv[1]]['index'])
    print(theList[argv[1]]['connectedNodes'])
    """

    tags = gT.getTags(argv[1])
    
    originID = id

    for t in tags:
        articleLink = 'https://en.wikipedia.org/wiki/' + '_'.join(t.split(' '))

        nC = convertToNameCode(articleLink)

        if nC not in theList:
            id += 1

            theList[nC] = {
                'index': id,
                'link': articleLink,
                'connectedNodes': [originID] 
            }
        else:
            theList[nC]['connectedNodes'].append(originID)

    
    
    print(theList)



def convertToNameCode(link):
    nameCode = removeSubstring(link.lower(), '/')
    nameCode = removeSubstring(nameCode, 'https')
    nameCode = removeSubstring(nameCode, 'http')
    nameCode = removeSubstring(nameCode, '.')
    nameCode = removeSubstring(nameCode, ':')
    nameCode = removeSubstring(nameCode, '_')

    return nameCode


def removeSubstring(text, substring):
    result = text
    iS = result.find(substring)

    while(iS != -1):
        result = result[:iS] + result[(iS + len(substring)):]
        iS = result.find(substring)


    return result


if __name__ == "__main__":
    main(sys.argv)





