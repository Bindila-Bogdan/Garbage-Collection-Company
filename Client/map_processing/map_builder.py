from map_processing.map import Map


class MapBuilder:
    @staticmethod
    def build_map(map_size, locations):
        current_map = Map(map_size, locations)
        current_map.generate_map()
        return current_map
