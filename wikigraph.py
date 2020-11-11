import sys
import gT


def main(argv):
    if(len(argv) == 0):
        return
    
    tags = gT.getTags(argv[1])

    for t in tags:
        print(t)
    



if __name__ == "__main__":
    main(sys.argv)





