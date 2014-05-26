import sys
from math import sqrt

def distance(a, b):
    x,y = a
    z,w = b
    return sqrt((x-z)**2 + (y-w)**2)
	
def create_graph(count, points):
    pass

# B: calculate best result for a subgraph
def B(start, X, end, graph):
    # X: subset of C (set of all nodes)
    if X == set():
        return graph[start][end]
    else:
        return min([B(start, X.difference(set([x])), x, graph) + graph[x][end] for x in X])

# Main TSP function
def TSP(num_nodes, graph):
    # C: set of all nodes
    C = set([i for i in range(num_nodes)])
    
    #best_paths = [B(0, C.difference(set([0,t])), t, graph) for t in C.difference(set([0]))]
    #print best_paths
    return min([B(0, C.difference(set([0,t])), t, graph) + graph[t][0] for t in C.difference(set([0]))])

def main():
    '''
    graph = {}
    input = []
    
    for line in open(sys.argv[1]):
        entry = line.rstrip('\n').split(' ')
        entry = [float(x) for x in entry]
        input.append(entry)
    num_nodes = int(input.pop(0)[0])
    graph = create_graph(num_nodes, input)
    '''

    num_nodes = 4
    graph = [[0,2,1,3], [2,0,4,5], [1,4,0,6], [3,5,6,0]]

    print num_nodes
    print graph

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                print "%i-->%i: %i" % (i, j, graph[i][j])
    print

    #print B(0, set([1]), 2, graph)

    print TSP(num_nodes, graph)

main()
