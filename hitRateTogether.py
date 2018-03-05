# Calculate hit-rate
import numpy as np

#read mappings from ./small/A.map
mappings = np.loadtxt('./small/A.map')

groups = np.loadtxt('./AplusB.group')

n2_nodes = mappings.shape[0]
n1_nodes = groups.shape[0]-n2_nodes

print n1_nodes,n2_nodes

hit = 0

for B in range(n2_nodes):
	if int(mappings[B]) == -1:
		continue
	if groups[int(mappings[B])] == groups[B + n1_nodes]:
		hit += 1

print hit

hitRate = hit / min(n1_nodes,n2_nodes)

print hitRate
