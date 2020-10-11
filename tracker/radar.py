"""
Class for working with radar. Using RadarManager for loading and storing radar's data.
"""
from tracker.radarstorage import RadarStorageManager
from tracker.radarsearch import RadarSearchUsingDiff
from tracker.pattern import Pattern


class Radar(Pattern, RadarSearchUsingDiff):
    manager: RadarStorageManager

    def __init__(self, filename_input: str, filename_output: str):
        self.manager = RadarStorageManager(filename_input, filename_output)
        image = self.load_radar_image()
        Pattern.__init__(self, image)

    def load_radar_image(self):
        return self.manager.load_radar_map()

    def search(self, pattern: Pattern, overlay_character: str = '#'):
        matches_found = self.search_for_pattern(self, pattern, overlay_character)
        return matches_found

    def save_radar_image_with_overlay(self):
        self.manager.save_radar_with_overlay(self)
