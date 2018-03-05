import numpy as np
import random

nAnchor = 512
Group_size = 500

mappings = np.loadtxt('./small/A.map')
groupA = np.loadtxt('./A.group')
groupB = np.loadtxt('./B.group')

n1_nodes = groupA.shape[0]
n2_nodes = groupB.shape[0]

n1_groups = n1_nodes / Group_size + 1
n2_groups = n2_nodes / Group_size + 1


count = 0
anchor = []
while count != nAnchor:
	nodeId = random.randint(0,n2_nodes-1)
	pair = [int(mappings[nodeId]),nodeId]
	if pair[0]!=-1 and pair not in anchor:
		anchor.append(pair)
		count += 1

# Calculate Jaccard Similarity
sim = [([0] * n2_groups) for i in range(n1_groups)]

for pair in anchor:
	g1 = int(groupA[pair[0]])
	g2 = int(groupB[pair[1]])
	sim[g1][g2] += 1

#find hit-rate
hit = 0

for B in range(n2_nodes):
	if int(mappings[B]) == -1 or (int(mappings[B]), B) in anchor:
		continue
	gA = int(groupA[int(mappings[B])])
	gB = int(groupB[B])
	if sim[gA][gB]>0:
		hit += 1

print hit

hitRate = float(hit) / (min(n1_nodes,n2_nodes) - nAnchor)

print hitRate




