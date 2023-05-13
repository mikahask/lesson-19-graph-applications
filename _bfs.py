import matplotlib.pyplot as plt
import networkx as nx
import random
from enum import Enum

class Bfs:
    def __init__(self) -> None:
        '''It's a food festival! '''
        self.foodTruckMap = None

    def run(self) -> None:
        '''
        make a graph which finds the shortest path using 
        the bfs algorithm
        There are a bunch of food trucks and you want to find
        the shortest path to your food truck
        '''
        self.foodTruckMap = nx.Graph()
        foodTrucks = [
            'A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X'
        ]
        
        edges= [
            ("A" , "B", {"distance": random.randint(1,10)}), 
            ("A" , "D", {"distance": random.randint(1,10)}),
            ("B" , "E", {"distance": random.randint(1,10)}),
            ("B" , "C", {"distance": random.randint(1,10)}),
            ("D" , "F", {"distance": random.randint(1,10)}),
            ("D" , "G", {"distance": random.randint(1,10)}),
            ("E" , "G", {"distance": random.randint(1,10)}),
            ("E" , "D", {"distance": random.randint(1,10)}),
            ("E" , "H", {"distance": random.randint(1,10)}),
            ("H" , "M", {"distance": random.randint(1,10)}),
            ("C" , "I", {"distance": random.randint(1,10)}),
            ("C" , "J", {"distance": random.randint(1,10)}),
            ("A" , "K", {"distance": random.randint(1,10)}),
            ("K" , "L", {"distance": random.randint(1,10)}),
            ("L" , "J", {"distance": random.randint(1,10)}),
            ("I" , "M", {"distance": random.randint(1,10)}),
            ("M" , "G", {"distance": random.randint(1,10)}),
            ("J" , "N", {"distance": random.randint(1,10)}),
            ("N" , "O", {"distance": random.randint(1,10)}),
            ("M" , "P", {"distance": random.randint(1,10)}),
            ("P" , "O", {"distance": random.randint(1,10)}),
            ("O" , "K", {"distance": random.randint(1,10)}),
            ("O" , "Q", {"distance": random.randint(1,10)}),
            ("F" , "G", {"distance": random.randint(1,10)}),
            ("P" , "I", {"distance": random.randint(1,10)}),
            ("J" , "Q", {"distance": random.randint(1,10)}),
            ("G" , "R", {"distance": random.randint(1,10)}),
            ("R" , "S", {"distance": random.randint(1,10)}),
            ("O" , "S", {"distance": random.randint(1,10)}),
            ("S" , "T", {"distance": random.randint(1,10)}),
            ("T" , "R", {"distance": random.randint(1,10)}),
            ("R" , "U", {"distance": random.randint(1,10)}),
            ("U" , "V", {"distance": random.randint(1,10)}),
            ("G" , "W", {"distance": random.randint(1,10)}),
            ("W" , "X", {"distance": random.randint(1,10)}),
            ("X" , "V", {"distance": random.randint(1,10)}),
            ("X" , "R", {"distance": random.randint(1,10)})  
        ]

        # add all the food trucks to the graph
        self.foodTruckMap.add_nodes_from(foodTrucks)
        self.foodTruckMap.add_edges_from(edges)

        #graph visual
        bfsGraph = '/lesson-19-graph-applications/graphviz.svg'

        #solution code
        #sorted = nx.all_shortest_paths(self.foodTruckmap)
        solution = [p for p in nx.shortest_path(self.foodTruckMap, source='A', target='X')]
        print(solution)

        """ def shortestPath(self):
        
            nx.bfs_tree(self.foodTruckMap)
            distances = [
                self.foodTruckMap[u][v]['distance'] 
                for u,v 
                in self.foodTruckMap.edges()
            ] """

        
