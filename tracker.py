#!/usr/bin/env python3
"""
Application for tracking invaders on provided radar image, revealing possible locations of known types of invaders.
Created as a simple challenge from Marketer.tech

In this version main options are stored in constants in first lines of script bellow,
and only input file (radar sample) can be provided as optional argument:
    tracker.py --sample_file radar_sample.txt
    or
    tracker.py -f radar_sample.txt
    If not provided then filename from RADAR_FILE is used.

Required input is radar image provided as .txt file (like noted above specified in RADAR_FILE or as an argument)
Output of radar image with found invaders overlay is saved into .txt file (specified in OUTPUT_FILE)

Author: Pavel Ondra
Email: ondra.pavel@gmail.com
"""
import difflib
import argparse
from typing import List, Union

RATIO_MATCH = 0.79  # Minimal matching ratio to consider as positive similarity match (between 0-1, where 0.79 == 79%)
MINIMUM_HEIGHT = 5  # Minimum rows for matching, so we are not making match with only one line at the bottom of image...
MINIMUM_DISTANCE = 4  # Minimal "distance" between samples, to avoid multiple positive matches from same invader

RADAR_FILE = 'radar_sample.txt'
OUTPUT_FILE = 'output.txt'

INVADER_ONE = [
    "--o-----o--",
    "---o---o---",
    "--ooooooo--",
    "-oo-ooo-oo-",
    "ooooooooooo",
    "o-ooooooo-o",
    "o-o-----o-o",
    "---oo-oo---"]

INVADER_TWO = [
    "---oo---",
    "--oooo--",
    "-oooooo-",
    "oo-oo-oo",
    "oooooooo",
    "--o--o--",
    "-o-oo-o-",
    "o-o--o-o"]


class Invader:
    """
    Class for storing all important details about invader.
    """
    data: List
    height: int
    width: int

    def __init__(self, invader_data: List):
        self.data = invader_data
        self.height = len(invader_data)
        self.width = len(invader_data[0])


class Radar:
    """
    Class for storing all radar data.
    """
    image: List
    height: int
    width: int

    def __init__(self, radar_image):
        self.image = radar_image
        self.height = len(radar_image)
        self.width = len(radar_image[0])


class Tracker:
    """
    Collection of tools for identifying threat from known invaders on provided radar image.
    """
    known_invaders: List = []
    found_invaders: int = 0
    radar: Radar

    def __init__(self):
        # TODO: collection of invaders may be provided from file(s), database,... instead of being hardcoded...
        self.load_invader(INVADER_ONE)
        self.load_invader(INVADER_TWO)

        # Work with arguments
        arguments_parser = argparse.ArgumentParser()
        arguments_parser.add_argument("-f", "--sample_file", help="Filename with radar image, e.g: radar_sample.txt")

        # Read arguments from the command line
        args = arguments_parser.parse_args()

        # Load radar image from file
        if args.sample_file:
            file_radar_image = args.sample_file
        else:
            file_radar_image = RADAR_FILE

        try:
            radar_image = []
            with open(file_radar_image, 'r') as radar_file:
                for line in radar_file:
                    radar_image.append(line.strip())
            self.load_radar_image(radar_image)
        except OSError:
            print("Problem reading radar image from", file_radar_image)
            exit()

    def load_radar_image(self, image: List):
        """
        Create Radar object with provided image and make it accessible by loading it into self.radar variable.

        :param image: Radar image
        """
        if len(image) < 10 or len(image[0]) < 10:
            print("Provided radar sample is too small (required is at least 10x10)")
            exit()

        self.radar = Radar(image)

    def load_invader(self, invader_data: List):
        """
        Create Invader object from provided invader pattern (within invader_data),
        then upload invader into list of known invaders.

        :param invader_data: List with pattern of invader.
        """
        invader = Invader(invader_data)
        self.known_invaders.append(invader)

    @staticmethod
    def calculate_samples_similarity(needle: str, haystack: str) -> float:
        """
        Calculate similarity between provided text samples (haystack, needle) using 'difflib' library.

        :param needle: First sample string for similarity matching
        :param haystack: Second sample string for similarity matching
        :return float: Value between 0-1 representing similarity of provided samples between 0-100%
        """
        return difflib.SequenceMatcher(None, needle, haystack).ratio()

    def calculate_total_similarity(self, row_start: int, col_start: int, invader: Invader) -> Union[float, int]:
        """
        On radar image, starting from provided row_start and col_start point/coordinates,
        Search for similarity of samples withing boundaries of invader (height, width)
        and calculate match/similarity each line one by one using calculate_samples_similarity()
        Total similarity value is then calculated from similarities from all lines.

        :param row_start: Starting position (for row) within radar image
        :param col_start: Starting position (for column) within radar image
        :param invader
        :return:
        """
        col_offset = col_start + invader.width
        invader_row = 0
        similarity_ratio = []

        for i in range(row_start, row_start + invader.height):
            if i < self.radar.height:
                sample_radar = self.radar.image[i][col_start: col_offset]
                sample_invader = invader.data[invader_row]
                similarity_of_sample = self.calculate_samples_similarity(sample_invader, sample_radar)
                similarity_ratio.append(similarity_of_sample)
            invader_row += 1

        if not similarity_ratio:
            return 0

        return sum(similarity_ratio) / len(similarity_ratio)

    def overlay_radar_with_invader(self, row_start: int, col_start: int, invader: Invader, invader_char: str):
        """
        Highlight (with provided character) pattern matching found invader on the radar image.
        Logic is simple - only "o" characters withing invader boundaries are "highlighted".

        :param row_start: Starting position (for row) within radar image
        :param col_start: Starting position (for column) within radar image
        :param invader: Object with all details about invader
        :param invader_char: Character used for highlighting current invader type withing radar image
        """
        col_offset = col_start + invader.width

        for row in range(row_start, row_start + invader.height):
            if row < self.radar.height:
                sample = self.radar.image[row][col_start: col_offset]
                sample = sample.replace("o", invader_char)

                new_row = str(self.radar.image[row][0:col_start]) \
                      + sample \
                      + str(self.radar.image[row][col_offset:])

                self.radar.image[row] = new_row

    def search_for_invader(self, invader: Invader, char: str = "#") -> int:
        """
        Searching for matches of provided Invader pattern withing Radar image.

        :param invader: Object with all details about invader
        :param char: Character used for highlighting currently searched invader type withing radar image
        :return: int
        """
        current_invaders_found = 0

        for row_start in range(0, self.radar.height):

            # Create iterator from range() so we can skip columns / keep distance between samples with next()
            columns = iter(range(0, self.radar.width - invader.width))

            for col_start in columns:
                col_offset = col_start + invader.width

                if (self.radar.height - row_start) < MINIMUM_HEIGHT:
                    # When remaining lines/rows of image (at the bottom) are less then allowed MINIMUM_HEIGHT then
                    break

                similarity = self.calculate_total_similarity(row_start, col_start, invader)

                if similarity >= RATIO_MATCH:
                    # TODO: Overlaying radar image with found invaders could be made optional
                    self.overlay_radar_with_invader(row_start, col_start, invader, char)

                    # Skip columns / keep distance between searched samples
                    for n in range(0, MINIMUM_DISTANCE):
                        if (col_offset + n) < self.radar.width - 1:
                            next(columns)

                    current_invaders_found += 1
        return current_invaders_found

    def save_output(self, filename: str):
        """
        Save output (radar with invaders overlay) into specified file

        :param filename: Filename for saving output with radar image overlay
        """
        with open(filename, 'w') as out:
            for line in self.radar.image:
                out.write(line + '\n')

    def main(self):
        """
        Main function, executing search for all individual invaders within list of known invaders on the radar image.
        Overlay of found invaders over radar image is then saved into output file for closer examination.
        """
        print('Searching for invaders')
        for index, invader in enumerate(self.known_invaders):
            # Let's search for the invader
            found_current = self.search_for_invader(invader, str(index + 1))
            self.found_invaders += found_current

        # TODO: Saving output to file could be made optional
        self.save_output(OUTPUT_FILE)

        print("With similarity acceptance ratio: {0}%".format(RATIO_MATCH * 100))
        print("Invaders found:", self.found_invaders)
        print("Radar image with identified invaders saved in:", OUTPUT_FILE)


if __name__ == '__main__':
    tracker = Tracker()
    tracker.main()
