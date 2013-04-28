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
    for i in range(2,node_num+2):
        temp = node(i, "location: "+str(i))
        nodes[i] = (temp.id, temp.location)
        for j in range(i+1, node_num+1):
            if random.random() < prob:
                arc[(i,j)] = random.randint(-1,100)
                arc[(j,i)] = arc[(i,j)]
    nodeS = node("Start", "location: S")
    nodeT = node("Terminal", "location: T")
    nodes[0] = (nodeS.id, nodeS.location)
    nodes[1] = (nodeT.id, nodeT.location)
    for i in range(2,12):
        arc[(0,i)] = random.randint(-1,100)
        arc[(i,0)] = random.randint(-1,100)
    for i in range(node_num-8, node_num+2):
        arc[(1,i)] = random.randint(-1,100)
        arc[(i,1)] = random.randint(-1,100)
    return (nodes, arc)

def dijkstra(G, s=0, t=1):
    nodes, arc = G
    # Check distance
    print "Check arc validity"
    to_del_key = []
    for key in arc:
        if arc[key] <= 0:
            print "Node {0} to {1} has an invalid arc:{2}".format(key[0], key[1], arc[key]) 
            to_del_key.append(key)
    for key in to_del_key:
        del arc[key]
    print "Start Calculating..."    
    node_number = nodes.__len__()
    label = np.empty(node_number);label.fill(np.inf)
    predecessor = np.empty(node_number);predecessor.fill(np.inf)
    label[s] = 0;predecessor[s] = 0
    S = set([s])
    T = set(range(node_number))
    T.remove(s)
    W = s
    while T.__len__() > 0:
        # For each Node in T, check the shortest value
        predecessor[list(T)] = map(lambda x:W if arc.has_key((W, x)) and arc[(W, x)] + label[W] < label[x] else predecessor[x], list(T))
        label[list(T)] = map(lambda x:arc[(W, x)] + label[W] if arc.has_key((W, x)) and arc[(W, x)] + label[W] < label[x] else label[x], list(T))
        if(min(label[list(T)]) == np.inf):
            print "No possible route from s to t"
            return
        W = list(T)[np.where(label[list(T)] == min(label[list(T)]))[0][0]]
        S.add(W)
        T.remove(W)
    print "The shortest distance is {0}".format(label[t])
    print "start packing..."
    route = []
    current = t
    while predecessor[current] != s:
        route.append((nodes[current], arc[(current, predecessor[current])]))
        current = predecessor[current]
    route.append((nodes[current], arc[(current, predecessor[current])]))
    route.append((nodes[s], s))

    return route
    
print "Create Map"
result = dijkstra(randomNetwork())
if result:
    total=0
    while result.__len__() > 0:
        node, distance = result.pop()
        total+=distance
        print "->{0}, distance:{1}, total traveled:{2}".format(node[1], distance,total)