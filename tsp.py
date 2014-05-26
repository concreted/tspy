import sys
from math import sqrt

def distance(a, b):
    x,y = a
    z,w = b
    return sqrt((x-z)**2 + (y-w)**2)
	
def create_graph(count, points):
    graph = []

    for i in range(count):
        row = []
        p1 = points[i]
        for j in range(count):
            p2 = points[j]
            row.append(distance(p1, p2))
        graph.append(row)

    return graph

def print_graph(count, graph):
    print "Count: %i" % count
    print graph

    for i in range(count):
        for j in range(count):
            if i != j:
                print "%i-->%i: %i" % (i, j, graph[i][j])
    print
        
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
    if len(sys.argv) > 1:
        points = []
    
        for line in open(sys.argv[1]):
            entry = line.rstrip('\n').split(' ')
            entry = [float(x) for x in entry]
            points.append(entry)
        
        count = int(points.pop(0)[0])

        graph = create_graph(count, points)

    else:
        count = 4
        graph = [[0,2,1,3], [2,0,4,5], [1,4,0,6], [3,5,6,0]]

    print_graph(count, graph)

    print TSP(count, graph)

main()
