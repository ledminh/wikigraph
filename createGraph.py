import json
from igraph import *

def generate(name):
    with open(name) as graph_file:
        data = json.load(graph_file)

    #initialize our wikipedia graph   
    wikiGraph = Graph()

    #populate graph with vertices using page names
    for q in data:
        wikiGraph.add_vertices(q)


    #populate graph with edges from json file
    index = 0
    for q in data:
        for p in data[q]['connectedNodes']:
            wikiGraph.add_edges([(index, p)])
        index += 1

    #save into pajek for R project and Gephi
    wikiGraph.save("wikiGraph.net", format="pajek")
    print("Wiki Graph file has been written.")
