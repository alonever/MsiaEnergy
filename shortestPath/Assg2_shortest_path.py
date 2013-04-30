
import random
import numpy as np

class node:
    def __init__(self, idnum, loc):
        self.id = "id: node" + str(idnum)
        self.location = loc
    def __repr__(self):
        return "The node has %s and %s" % (self.id, self.location)

def randomNetwork(prob = 0.33):
    node_num = random.randint(500,1000)
    arc = {}
    nodes = {}
    for i in range(2,node_num):
        temp = node(i, "location: "+str(i))
        nodes[i] = (temp.id, temp.location)
        for j in range(i+1, node_num):
            if random.random() < prob:
                arc[(i,j)] = random.randint(-1,500000)
                arc[(j,i)] = arc[(i,j)]
    nodeS = node("Start", "location: S")
    nodeT = node("Terminal", "location: T")
    nodes[0] = (nodeS.id, nodeS.location)
    nodes[1] = (nodeT.id, nodeT.location)
    for i in range(2,12):
        arc[(0,i)] = random.randint(-1,500000)
        arc[(i,0)] = arc[(0,i)]
    for i in range(node_num-10, node_num):
        arc[(1,i)] = random.randint(-1,500000)
        arc[(i,1)] = arc[(1,i)]
    return (nodes, arc)
      
def shortestPath(network, s=0, t=1):
    nodes, arc= network
    node_num = nodes.__len__()
    print "Validating the network..."
##### Delete arcs with non-positive costs #####
#     to_del = []
#     for i in arc:
#         if arc[i] <= 0:
#             to_del.append(i)
#     for i in to_del:
#         print "Deleting arc between node %d and %d because of invalid cost: %d" % (i[0], i[1], arc[i])
#         del arc[i]
###############################################

##### Abort task if non-positive costs exist in network #####
    for i in arc:
        if arc[i] <= 0:
            print "Invalid cost of %d has been detected between node %d and %d. Task aborted. Please try again." % (arc[i], i[0], i[1])
            return False
    print "The network costs are valid."
#############################################################
    print "Calculating the shortest path... Please wait..."
    label = np.empty(node_num)
    label.fill(np.inf)
    label[s] = 0
    predecessor = np.empty(node_num);
    predecessor.fill(np.inf)
    predecessor[s] = 0
    temp = set(range(node_num))
    temp.remove(s)
    W = s
    while temp.__len__() > 0:
        predecessor[list(temp)] = map(lambda x:W if arc.has_key((W, x)) 
                                   and arc[(W, x)] + label[W] < label[x] 
                                   else predecessor[x], list(temp))
        label[list(temp)] = map(lambda x:arc[(W, x)] + label[W] if arc.has_key((W, x)) 
                             and arc[(W, x)] + label[W] < label[x] 
                             else label[x], list(temp))
        if(min(label[list(temp)]) == np.inf):
            print "No possible path from node S to T"
            return False
        W = list(temp)[np.where(label[list(temp)] == min(label[list(temp)]))[0][0]]
        temp.remove(W)
    print "The minimum cost of the path is %s" % label[t]
    path = []
    current = t
    while predecessor[current] != s:
        path.append((nodes[current], arc[(current, predecessor[current])]))
        current = predecessor[current]
    path.append((nodes[current], arc[(current, predecessor[current])]))
    path.append((nodes[s], s))
    return path

# output result
path = shortestPath(randomNetwork())
if path:
    print ">>The shortest path is the following:"
    total = 0
    while path.__len__() >0:
        node, cost = path.pop()
        total = total + cost
        print ">>%s, cost: %d, cumulative cost: %d" % (node[1], cost, total)
    print ">>Terminal node reached."
