import sys
from math import sqrt
from itertools import chain, combinations

def TSP(nodes, graph):
	A = {}
	for size in range(1, nodes+1):
		A[size] = {}
		for i in (y for y in powerset(range(1, nodes+1)) if 1 in y and len(y) == size):
			A[size][i] = {}
			if i == (1,):
				A[size][i][1] = 0
			else:
				A[size][i][1] = float('inf')
			#print i
	#A[1][(1,)][1] = 0
	#print A
	
	for m in range(2, nodes+1):
		#print A[m]
		for S in A[m]:
			#print S
			for j in S:
				if j != 1:
					#print j
					minimum = float('inf')
					for k in S:
						if k != j:
							#print k
							localmin = A[m-1][tuple_delete(S, j)][k] + graph[k][j]
							#print "dist:", graph[k][j]
							if localmin < minimum:
								minimum = localmin
					A[m][S][j] = minimum	
		if m >= 3:
			A.pop(m-1, None)
					
	candidates = A[nodes]
	#return candidates
	best = float('inf')
	#print graph
	for x in candidates:
		for dest in candidates[x]:
			if dest != 1:
				dist = candidates[x][dest]
				returndist = dist + graph[dest][1]
				#print dest, dist, returndist
				
				if returndist < best:
					best = returndist
	#for line in A:
		#print line, A[line]
	return best
			
def tuple_delete(t, val):
	return tuple(y for y in t if y != val)
	
def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range (len(s) + 1))
	
def distance(a, b):
	#print a, b
	x,y = a
	z,w = b
	return sqrt((x-z)**2 + (y-w)**2)
	
def create_graph(count, points):
	graph = {}
	
	for i in range(1, count + 1):
		graph[i] = {}
	for i in range(0, count):
		for j in range(0, count):
			if i != j:
				a = points[i]
				b = points[j]
				graph[i+1][j+1] = distance(a, b)
				
	return graph
		
def main():
	graph = {}
	input = []
	for line in open(sys.argv[1]):
		entry = line.rstrip('\n').split(' ')
		entry = [float(x) for x in entry]
		input.append(entry)
			
	num_nodes = int(input.pop(0)[0])
	graph = create_graph(num_nodes, input)
	'''
	for i in range(1, num_nodes + 1):
		graph[i] = {}
	for entry in input:
		start, end, dist = entry
		graph[start][end] = dist
		graph[end][start] = dist
	'''
	print num_nodes
	'''
	for node in graph:
		print node, graph[node]
	'''
	print TSP(num_nodes, graph)

main()