import copy


class Route:
    def __init__(self, current_map, starting_node):
        self.__number_of_nodes = current_map.get_number_of_locations()
        self.__acctual_list_of_nodes = current_map.get_location_names()
        self.__list_of_nodes = [i for i in range(len(self.__acctual_list_of_nodes))]
        self.__mapping = {}
        for index in range(len(current_map.get_location_names())):
            self.__mapping[index] = self.__acctual_list_of_nodes[index]
        self.__matrix_map = current_map.get_map()
        self.__starting_node = starting_node
        self.__route = [self.__starting_node]
        self.__graph = {}
        self.__paths = []

    def generate_mapping(self):
        acctual_route = []
        for index in range(len(self.__route)):
            acctual_route.append(self.__mapping[self.__route[index]])
        return acctual_route

    def get_min_path_value(self, current_node, nodes):
        if (current_node, nodes) in self.__graph:
            return self.__graph[current_node, nodes]
        costs = []
        reamining_nodes = []
        for node in nodes:
            copy_of_nodes = copy.deepcopy(list(nodes))
            copy_of_nodes.remove(node)
            reamining_nodes.append((node, tuple(copy_of_nodes)))
            calling_node = reamining_nodes[(len(reamining_nodes) - 1)][0]
            remaining_nodes = reamining_nodes[(len(reamining_nodes) - 1)][1]
            cost = self.get_min_path_value(calling_node, remaining_nodes)
            costs.append(self.__matrix_map[current_node - 1][node - 1] + cost)
        self.__graph[current_node, nodes] = min(costs)
        index = costs.index(min(costs))
        self.__paths.append(((current_node, nodes), reamining_nodes[index]))
        return self.__graph[current_node, nodes]

    def get_optimal_cycle(self):
        for node in range(1, self.__number_of_nodes):
            self.__graph[node, ()] = self.__matrix_map[node][0]
        self.get_min_path_value(self.__list_of_nodes[0], tuple(self.__list_of_nodes[1:]))
        next_node = self.__paths[len(self.__paths) - 1]
        self.__route.append(next_node[1][0])
        for x in range(len(self.__list_of_nodes) - 2):
            for new_next_node in self.__paths:
                if next_node[1] == new_next_node[0]:
                    next_node = new_next_node
                    self.__route.append(next_node[1][0])
        self.__route.append(self.__starting_node)
        return self.generate_mapping()
