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


def printPath(path):
    """假设path是节点列表"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        #在中间插入符号，最后不插。
        if i != len(path) - 1:
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest, toPrint = False):
    """假设graph是无向图；start和end是节点；
          path和shortest是节点列表
       返回graph中从start到end的最短路径。"""
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end: #踩到了总目标点，结束递归，返回当前走过的路径
        return path
    for node in graph.childrenOf(start): #没有子节点就不进入循环了，结束递归，返回上次存过的最短路径。
        if node not in path: #没走过的节点才需要再尝试，在path里的就跳过。
           if shortest == None or len(path) < len(shortest): #没有最短路径时，或者还没有超过最短路径时，才执行递归函数。
               newPath = DFS(graph, node, end, path, shortest, #以当前节点为起点，探索新路径。层层递归，直到踩到总目标节点或者没有子节点，返回上次存过的最短路径。
                             toPrint)
               if newPath != None:
                     shortest = newPath #用新的猜到了目标节点的路径更新最短路径，它最多与上一个最短路径一样长，当然可能更短。
    return shortest #返回最短路径。


def shortestPath(graph, start, end, toPrint = False):
    """假设graph是无向图；start和end是节点
       返回graph中从start到end的最短路径。"""
    return DFS(graph, start, end, [], None, toPrint)


def BFS(graph, start, end, toPrint = False):
    """假设graph是无向图；start和end是节点
       返回graph中从start到end的最短路径。"""
    initPath = [start] #包含节点的列表
    pathQueue = [initPath] #节点列表的列表
    if toPrint:
        print('Current BFS path:', printPath(path))
    while len(pathQueue) != 0: #pathQueue的长度可能减到0。
        #从pathQueue这个路径列表里取最老的一个组合，开始探索。
        tmpPath = pathQueue.pop(0)
        print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end: #找到了，返回这个路径就够了。
            return tmpPath
        #向后探索一层
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath: #不走回头路。
                #它会产生很多个newPath，都会被加入pathQueue里面，以备探索。
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None


def testSP():
    nodes = []
    for name in range(6): #建6个节点，节点名字就是索引数字。
        nodes.append(Node(str(name)))
    g = Digraph() #建了有向图，为什么不是无向图？因为，既然路径不必重复，引入对称关系也就没有帮助。
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))
    sp = shortestPath(g, nodes[0], nodes[5], toPrint = True)
    print("Shortest path is", printPath(sp))
    sp = BFS(g, nodes[0], nodes[5])
    print('Shortest path found by BFS:', printPath(sp))


testSP()

