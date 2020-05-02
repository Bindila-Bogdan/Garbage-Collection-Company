from map_processing.map_builder import MapBuilder
from map_processing.route import Route
from views.map_representation import MapRepresentation


class RouteGenerator:
    def __init__(self, locations):
        self.__map_size = 1000
        self.__current_map = MapBuilder.build_map(self.__map_size, locations)
        self.__locations = self.__current_map.get_locations()
        self.__number_of_nodes = len(locations)
        self.__route = Route(self.__current_map, 0)
        try:
            if self.__number_of_nodes > 1:
                self.__optimal_path = self.__route.get_optimal_cycle()
        except IndexError:
            pass
        self.__map_representation = MapRepresentation()

    def set_locations_and_regenerate_map(self, locations):
        self.__locations = locations
        self.__number_of_nodes = len(locations)
        self.__current_map = MapBuilder.build_map(self.__map_size, locations)
        self.__locations = self.__current_map.get_locations()
        self.__route = Route(self.__current_map, 0)
        try:
            if self.__number_of_nodes > 1:
                self.__optimal_path = self.__route.get_optimal_cycle()
        except IndexError:
            pass
        self.__map_representation = MapRepresentation()
        self.generate_map()

    def generate_map(self):
        self.__map_representation.plot_map(self.__current_map.get_map(), self.__locations)

    def generate_route(self):
        self.__map_representation.plot_best_route(self.__current_map.get_map(), self.__locations, self.__optimal_path)

    def get_number_of_nodes(self):
        return self.__number_of_nodes
