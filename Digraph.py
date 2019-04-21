import json

infinity = float('inf')
neg_infinity = float('-inf')

class Digraph:
    _graph = None

    def __init__(self, path):
        infile = open(path, 'r')
        file_string = infile.read()
        self._graph = json.loads(file_string)
        infile.close()

       

    def get_edge_weight(self, source, dest):
        if source not in self._graph.keys() or dest not in self._graph[source].keys():
            return -1
        else:
            return self._graph[source][dest]

    def does_node_exist(self, node):
        return (node in self._graph)

    def get_best_friend_chain(self, source, dest):
        prev = self._get_dijkstra_prev_graph(source)

        path_stack = [dest]
        step = prev[dest]

        while step != source:
            path_stack.append(step)
            step = prev[step]
        path_stack.append(source)

        path_stack.reverse()

        return path_stack
        
        
    def _get_dijkstra_prev_graph(self, source):
        dist = {source: 0}
        unvisited = []
        previous = {}

        for elem in self._graph.keys():
            dist[elem] = infinity
            previous[elem] = None
            unvisited.append(elem)
        dist[source] = 0

        while unvisited:
            min_node = self._get_min_node(source, unvisited)
            if min_node == None:
                min_node = unvisited.pop()
            else:
                unvisited.remove(min_node)
            
            for nb in self._get_neighbors(min_node):
                #if nb in unvisited:
                path = dist[min_node] + self._bfc_cost(min_node, nb)
                if path < dist[nb]:
                    dist[nb] = path
                    previous[nb] = min_node

        return previous

    def _get_min_node(self, dest, lst):
        if dest in lst:
            return dest

        min_val = infinity
        min_node = None

        for elem in lst:
            if self.get_edge_weight(elem, dest) != -1:
                tmp = self._bfc_cost(elem, dest)
                if tmp < min_val:
                    min_val = tmp
                    min_node = elem

        return min_node

    def _bfc_cost(self, source, dest):
        return 10 - self._graph[source][dest]

    def _get_neighbors(self, node):
        return self._graph[node].keys()

    