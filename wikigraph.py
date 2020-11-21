import sys
import gT
import json

def main(argv):
    if(len(argv) == 0):
        return
    
    theList = crawling(argv[1], int(argv[2]))
    
    print("----------------------------")
    print(len(theList.keys()), "nodes are generated!")
    input("Press ENTER to scan " + str(len(theList.keys())) + " nodes for second round to add edges ...")
    print("----------------------------")
    print("Second Round (adding edges): ")

    for kList in theList.keys():
        tags = gT.getTags(theList[kList]['link'])
        d = toDict(tags)

        for kD in d.keys():
            if kD in theList:
                theList[kList]['connectedNodes'].append(theList[kD]['index'])

        print("Scanning node", theList[kList]['index'], "done!")
    

    print("----------------------------")
    print("SCANNING DONE!")

    print("Writing to file ...")
    
    with open(argv[3], 'w') as fp:
        json.dump(theList, fp)
        print("The dict is written to", argv[3])




def crawling(link, depth):
    id = 0

    done = False

    originalKey = codify(link)

    theList = {
        originalKey: {
            'index': id,
            'link': link,
            'connectedNodes': [],
            'level': 0,
            'done': False
        }
    }

    count = 0
    print("Start crawling node:")

    while(done != True):
        thisLevel = theList[originalKey]['level'] + 1

        tags = gT.getTags(theList[originalKey]['link'])

        d = toDict(tags)

        for key in d.keys():
            if key not in theList:
                id += 1

                theList[key] = {
                    'index': id,
                    'link': d[key],
                    'connectedNodes': [],
                    'level': thisLevel,
                    'done': False
                }
            
        theList[originalKey]['done'] = True

        done = True  # first, suppose that we're all done

        for k in theList.keys():
            if(theList[k]['level'] < depth
                    and theList[k]['done'] == False):
                done = False  # well, turn out, we're not done yet
                originalKey = k
                break
        
        count += 1
        print("Node", count, "done!")


    return theList


def codify(text):
    return removeSubstring(text.lower(), ['https://en.wikipedia.org/wiki/',' ', '.', ':', '_', '(', ')', '-']) 
    

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
    





