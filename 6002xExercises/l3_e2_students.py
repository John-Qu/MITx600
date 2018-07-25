# utf-8

class Node(object):
    def __init__(self, name):
        """假设name是字符串"""
        #虽然没有更多信息和方法，但是为Node建一个类，是给将来留更大的灵活空间。
        #比如可能增加一个子类，是还有港口的节点。
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """假设src和dest是节点，注意Edge有方向。"""
        #Edge很简单，只是记录了头尾两个节点。
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        """假设src和dest是节点，weight是个数值"""
        self.src = src
        self.dest = dest
        #上面这两句也可以写成：Edge.__init__(self, src, dect)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
         return self.src.getName() + '->(' + str(self.weight) + ')'\
                + self.dest.getName()


class Digraph(object):
    #nodes是图中节点的列表
    #edges是一个字典，将每个节点映射到其子节点列表
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node) #加入nodes池，顾名思义当然要做。
            self.edges[node] = [] #注意同时在edges池里打好关系的框架。
    def addEdge(self, edge):
        #拆分出edge中的头尾节点信息
        src = edge.getSource()
        dest = edge.getDestination()
        #然后确认头尾节点已经建立过了。
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        #在edges字典池中创建/更新信息。
        self.edges[src].append(dest)
    def childrenOf(self, node):
        #问子节点，在edges关系中提取信息。
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] #输出时不要最后的新行符。

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        #建立另一条反方向的Edge。虽然复制了Node资源，但是直观易懂。
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)


for i in range(len(nodes)):
    src = nodes[i].getName()
    for j in range(i+1, len(nodes)):
        des = nodes[j].getName()
        for k in range(len(src)-1):
            if src[k] != des[k]:
                if src[k+1] == des[k] and src[k] == des[k+1]:
                    g.addEdge(Edge(nodes[i], nodes[j]))  # note that src and des are strings not Node.
                else:
                    break  # donn't need to check further. Go to check next node.


print(g)

# ABC->ACB
# ABC->BAC
# ACB->ABC
# ACB->CAB
# BAC->ABC
# BAC->BCA
# BCA->BAC
# BCA->CBA
# CAB->ACB
# CAB->CBA
# CBA->BCA
# CBA->CAB

