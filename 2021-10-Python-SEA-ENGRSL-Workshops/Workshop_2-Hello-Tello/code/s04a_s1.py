def dijkstra():

	distances = []
	sptree = []
	parents = []

	for i in range(NETWORK_MAX_SIZE):
		distances.append(9999)
		sptree.append(0)
		parent.append(0)

	parent[0] = -1
	distances[SRC] = 0

	for i in range(NETWORK_MAX_SIZE-1):

		minimum = 9999
		minIndx = -1

		for j in range(NETWORK_MAX_SIZE):
			if sptree[j] == 0 and distances[j] <= minimum:
				minimum = distances[j]
				minIndx = j

		sptree[minimum] = 1

		for j in range(NETWORK_MAX_SIZE):

			if (sptree[j] == 0 and cache.topology[minIndx][j] == 1 and
				distances[minIndx] + cache.topology[minIndx][j] < distances[j]):

				parent[j] = minIndx
				distances[j] = distances[minIndx] + cache.topology[minIndx][j]

