import networkx as nx
import random

class Bfs:
    def __init__(self) -> None:
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
            'Bites on Wheels','The Hungry Truck','Rolling Delights','Foodie Roadster','The Flavor Wagon','Street Grub Hub',
            'Mobile Munchies','Ada Eats','The Roaming Kitchen','Curbside Cuisine','Chowmobile','The Taste Truck','Rolling Kitchen','Food Truckin','Fork in the Road',
            'Eat Street','Tasty Trailers','Grubmobile','Flavor Fleet','Culinary Cruiser',
            'Kitchen on Wheels','Mobile Meals','The Rolling Cookhouse','Truckin Tacos'
        ]
        
        edges= [
            ("Bites on Wheels" , "The Hungry Truck", {"distance": random.randint(1,10)}), 
            ("Bites on Wheels" , "Foodie Roadster", {"distance": random.randint(1,10)}),
            ("The Hungry Truck" , "The Flavor Wagon", {"distance": random.randint(1,10)}),
            ("The Hungry Truck" , "Rolling Delights", {"distance": random.randint(1,10)}),
            ("Foodie Roadster" , "Street Grub Hub", {"distance": random.randint(1,10)}),
            ("Foodie Roadster" , "Mobile Munchies", {"distance": random.randint(1,10)}),
            ("The Flavor Wagon" , "Mobile Munchies", {"distance": random.randint(1,10)}),
            ("The Flavor Wagon" , "Foodie Roadster", {"distance": random.randint(1,10)}),
            ("The Flavor Wagon" , "Ada Eats", {"distance": random.randint(1,10)}),
            ("Ada Eats" , "Rolling Kitchen", {"distance": random.randint(1,10)}),
            ("Rolling Delights" , "The Roaming Kitchen", {"distance": random.randint(1,10)}),
            ("Rolling Delights" , "Curbside Cuisine", {"distance": random.randint(1,10)}),
            ("Bites on Wheels" , "Chowmobile", {"distance": random.randint(1,10)}),
            ("Chowmobile" , "The Taste Truck", {"distance": random.randint(1,10)}),
            ("The Taste Truck" , "Curbside Cuisine", {"distance": random.randint(1,10)}),
            ("The Roaming Kitchen" , "Rolling Kitchen", {"distance": random.randint(1,10)}),
            ("Rolling Kitchen" , "Mobile Munchies", {"distance": random.randint(1,10)}),
            ("Curbside Cuisine" , "Grubmobile", {"distance": random.randint(1,10)}),
            ("Food Truckin" , "Fork in the Road", {"distance": random.randint(1,10)}),
            ("Rolling Kitchen" , "Eat Street", {"distance": random.randint(1,10)}),
            ("Eat Street" , "Fork in the Road", {"distance": random.randint(1,10)}),
            ("Fork in the Road" , "Chowmobile", {"distance": random.randint(1,10)}),
            ("Fork in the Road" , "Tasty Trailers", {"distance": random.randint(1,10)}),
            ("Street Grub Hub" , "Mobile Munchies", {"distance": random.randint(1,10)}),
            ("Eat Street" , "The Roaming Kitchen", {"distance": random.randint(1,10)}),
            ("Curbside Cuisine" , "Tasty Trailers", {"distance": random.randint(1,10)}),
            ("Mobile Munchies" , "Grubmobile", {"distance": random.randint(1,10)}),
            ("Grubmobile" , "Flavor Fleet", {"distance": random.randint(1,10)}),
            ("Fork in the Road" , "Flavor Fleet", {"distance": random.randint(1,10)}),
            ("Flavor Fleet" , "Culinary Cruiser", {"distance": random.randint(1,10)}),
            ("Culinary Cruiser" , "Grubmobile", {"distance": random.randint(1,10)}),
            ("Grubmobile" , "Kitchen on Wheels", {"distance": random.randint(1,10)}),
            ("Kitchen on Wheels" , "Mobile Meals", {"distance": random.randint(1,10)}),
            ("Mobile Munchies" , "The Rolling Cookhouse", {"distance": random.randint(1,10)}),
            ("The Rolling Cookhouse" , "Truckin Tacos", {"distance": random.randint(1,10)}),
            ("Truckin Tacos" , "Mobile Meals", {"distance": random.randint(1,10)}),
            ("Truckin Tacos" , "Grubmobile", {"distance": random.randint(1,10)})  
        ]

        # add all the food trucks to the graph
        self.foodTruckMap.add_nodes_from(foodTrucks)
        self.foodTruckMap.add_edges_from(edges)

        #graph visual
        bfsGraph = 'foodTruckMap.png'
        print(bfsGraph)

        #solution code
        solution = [p for p in nx.shortest_path(self.foodTruckMap, source='Bites on Wheels', target='Truckin Tacos')]
        print('The shortest path to follow is: ')
        print(solution)


        
