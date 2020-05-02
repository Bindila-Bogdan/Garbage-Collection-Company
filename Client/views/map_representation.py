import matplotlib.pyplot as plt
import networkx as nx


class MapRepresentation:
    def __init__(self):
        self.__graph = nx.Graph()
        self.__best_route = nx.DiGraph()
        self.__iteration = -1

    def plot_map(self, current_map, locations):
        for index in range(len(current_map)):
            self.__graph.add_node(locations[index].get_name(),
                                  pos=(float(locations[index].get_coord_ox()), float(locations[index].get_coord_oy())))
        for row_index in range(len(current_map)):
            for col_index in range(len(current_map)):
                self.__graph.add_edges_from([(locations[row_index].get_name(), locations[col_index].get_name())],
                                            weight=current_map[row_index][col_index])
        pos = nx.get_node_attributes(self.__graph, 'pos')
        nx.draw(self.__graph, pos, with_labels=True, font_weight='bold',
                node_color=[x for x in range(len(locations))], node_size=1000, cmap="YlGn")
        labels = nx.get_edge_attributes(self.__graph, 'weight')
        nx.draw_networkx_edge_labels(self.__graph, pos, edge_labels=labels)

        plt.plot()
        plt.savefig("../views/plot.png", dpi=214)
        plt.close()

    def plot_best_route(self, current_map, locations, best_route):
        self.__best_route = nx.DiGraph()
        for index in range(len(current_map)):
            self.__best_route.add_node(int(best_route[index]),
                                       pos=(locations[index].get_coord_ox(), locations[index].get_coord_oy()))
        self.__iteration += 1
        for index in range(len(best_route) - 1):
            if index <= self.__iteration:
                c = "lightGreen"
            else:
                c = "black"
            self.__best_route.add_edges_from([(int(best_route[index]), int(best_route[index + 1]))], color=c)
        pos = nx.get_node_attributes(self.__best_route, 'pos')
        nx.draw(self.__best_route, pos, with_labels=True, font_weight='bold',
                node_color=range(len(self.__best_route.nodes)), node_size=1000, cmap="YlGn")
        colors = [self.__best_route[u][v]['color'] for u, v in self.__best_route.edges()]
        nx.draw_networkx_edges(self.__best_route, pos, edge_color=colors, width=2)

        plt.plot()
        plt.savefig("../views/plot.png", dpi=214)
        plt.close()
