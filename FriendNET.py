#!/usr/bin/env python3

'''
Algorithm Specification:
BF Chain - derived via Dijkstra's Algorithm

Killer Feature 1 - Cliquer
    The user provides a number of groups that everyone will be 
     grouped into, and they will be grouped into the closest number
     of groups possible.

    Finds the number of groups with breadth first. Changes the number
     independent groups by decreasing the mutual weights of the connection
     (where a connection can wholly disappear) until the ideal number of 
     groups has been achieved.
    

Killer Feature 2 - Degrees of Seperation
    List the degrees of seperation of all people from the given person
    Implemented with breadth first traversal




'''


import Digraph
import Menu


class FriendNET:
    _graph = None
    _menu = None
    _menu_loop_sentinal = True

    def __init__(self, path):
        self._load_graph(path)
        self._menu = Menu.Menu()
        self._menu.create_menu_option('View connection',  self.view_edge)
        self._menu.create_menu_option(
            'Check if user exists', self.check_if_exists)
        self._menu.create_menu_option('View best friend chain', self.view_bfc)
        self._menu.create_menu_option('Degrees of seperation', self.degrees_of_seperation)
        self._menu.create_menu_option('Cliquer', self.cliquer)
        self._menu.create_menu_option('Quit', self.menu_quit)

        while self._menu_loop_sentinal:
            self._menu.display()
            self._menu.handle_input()

    def _load_graph(self, path):
        self._graph = Digraph.Digraph(path)

    def view_edge(self):
        both_people = input('What users (sep. by a space): ')
        people = both_people.split(' ')

        if len(people) != 2:
            print('Invalid input')
            return

        weight = self._graph.get_edge_weight(people[0], people[1])

        if weight == -1:
            print('Invalid pairing, connection or users may not exist')
        else:
            print('The connection between ' +
                  people[0] + ' and ' + people[1] + ' has weight ' + str(weight))

    def check_if_exists(self):
        person = input('What user: ')
        they_do_exist = self._graph.does_node_exist(person)

        if they_do_exist:
            print(person + ' exists')
        else:
            print(person + ' does not exist')

    def view_bfc(self):
        people = input('What two people? ').split(' ')
        chain = self._graph.get_best_friend_chain(people[0], people[1])
        if chain:
            for name in chain:
                print(name)
        else:
            print("No path exists between " + people[0] + " and " + people[1])

    def degrees_of_seperation(self):
        person = input("From who? ")
        degrees = self._graph.get_degrees_of_seperation(person)
        degrees = sorted(degrees.items(), key= lambda elem : elem[1])
        for elem in degrees:
            print(elem)

    def cliquer(self):
        is_bad_input = True
        num = -1

        while(is_bad_input):
            num = input('Group into how many cliques? ')
            try:
                num = int(num)
                is_bad_input = False
            except ValueError:
                print('Type must be int type.')
        
        self._graph.group_into(num)

    def menu_quit(self):
        self._menu_loop_sentinal = False


if __name__ == '__main__':
    FriendNET('network.json')
    pass
