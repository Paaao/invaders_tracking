"""
Used for storing and loading data for radar(s).
"""
from tracker.pattern import Pattern


class RadarStorage:
    def load_radar_map(self):
        pass


class RadarStorageManager(RadarStorage):
    filename_input_map: str
    filename_output_map: str

    def __init__(self, filename_input: str, filename_output: str):
        self.filename_input_map=filename_input
        self.filename_output_map=filename_output

    def load_radar_map(self):
        image = []
        try:
            with open(self.filename_input_map, 'r') as radar_file:
                for line in radar_file:
                    image.append(line.strip())
        except OSError:
            print("Problem reading radar image from", self.filename_input_map)
            exit()

        return image

    def save_radar_with_overlay(self, radar: Pattern):
        try:
            with open(self.filename_output_map, 'w') as out:
                for line in radar.image:
                    out.write(line + '\n')
        except OSError:
            print("Problem saving radar overlay image to", self.filename_output_map)
            exit()