import copy
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

        if prev[dest] == None:
            return None

        else:
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
            unvisited.sort(key= lambda elem: dist[elem])
            min_node = unvisited.pop(0)
            
            for nb in Digraph._get_neighbors(self._graph, min_node):
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

    def _get_neighbors(graph, node):
        return graph[node].keys()

    def get_degrees_of_seperation(self, source):
        que = [source]
        visited = [source]
        degrees = {source: 0}

        while que:
            cur = que.pop(0)
            for nb in Digraph._get_neighbors(self._graph, cur):
                if nb not in visited:
                    que.append(nb)
                    visited.append(nb)
                    degrees[nb] = degrees[cur] + 1

        return degrees

    def group_into(self, target):
        gr = copy.deepcopy(self._graph)
        num = Digraph.get_num_islands(gr)
        
        if len(gr) < target:
            target = len(gr)

        while num < target:
            Digraph._degrade(gr)
            num = Digraph.get_num_islands(gr)        

        Digraph._display_cliques(gr)

    def get_num_islands(graph):
        unvisited = list(graph.keys())
        num_islands = 0

        while unvisited:
            num_islands += 1
            node = unvisited[0]
            Digraph._traverse_island(node, graph, unvisited)

        return num_islands

    def _traverse_island(node, graph, unvisited):
        unvisited.remove(node)
        for nb in Digraph._get_neighbors(graph, node):
            if Digraph._is_mutual_connection_present(graph, node, nb) and nb in unvisited:
                Digraph._traverse_island(nb, graph, unvisited)

    def _is_mutual_connection_present(graph, node_a, node_b):
        a_to_b = node_b in graph[node_a].keys() and graph[node_a][node_b] > 0
        b_to_a = node_a in graph[node_b].keys() and graph[node_b][node_a] > 0

        return a_to_b and b_to_a

    def _degrade(graph):
        for node in graph:
            dead_connections = []
            for nb in Digraph._get_neighbors(graph, node):
                graph[node][nb] -= 1

                if graph[node][nb] == 0:
                    dead_connections.append(nb)
            
            for nb in dead_connections:
                graph[node].pop(nb)
        
    def _display_cliques(graph):
        print('Cliques:')
        unvisited = list(graph.keys())
        cur_island_num = 0
        
        while unvisited:
            cur_island_num += 1
            node = unvisited[0]
            print(' -Clique ' + str(cur_island_num) + '-')
            Digraph._print_island(node, graph, unvisited)
            print()
    
    def _print_island(node, graph, unvisited):
        unvisited.remove(node)
        print(' ' + node)

        for nb in Digraph._get_neighbors(graph, node):
            if Digraph._is_mutual_connection_present(graph, node, nb) and nb in unvisited:
                Digraph._print_island(nb, graph, unvisited)
