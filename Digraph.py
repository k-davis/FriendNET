import json


class Digraph:
    _graph = None

    def __init__(self, path):
        infile = open(path, 'r')
        file_string = infile.read()
        self._graph = json.loads(file_string)
        infile.close()

    def get_edge_weight(self, node_a, node_b):
        if node_a not in self._graph or node_b not in self._graph[node_a]:
            return -1
        else:
            return self._graph[node_a][node_b]

    def does_node_exist(self, node):
        return (node in self._graph)
