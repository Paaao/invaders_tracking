"""
Simple BDD tests with mamba library
https://github.com/nestorsalceda/mamba

Run it from main project directory:
    $ pipenv run mamba tests
"""

from mamba import description, context, before, it
from expects import expect, equal

from tracker.radar import Radar
from tracker.invader import Invader
from tracker.pattern import Pattern
from tracker.radarstorage import RadarStorageManager
from tracker.radarsearch import RadarSearchUsingDiff

with description("Pattern") as self:
    with it("work with empty image"):
        image = []

        pattern = Pattern(image)

        assert pattern.width == 0
        assert pattern.height == 0

    with it("work with image dimensions"):
        image = [
            "OOO",
            "OOO"
        ]

        pattern = Pattern(image)

        assert pattern.width == 3
        assert pattern.height == 2

    with it("get height with get_height method"):
        image = [
            "OOO",
            "OOO"
        ]

        pattern = Pattern(image)
        height = pattern.get_height()

        assert height == 2

    with it("get width with get_width method"):
        image = [
            "OOO",
            "OOO"
        ]

        pattern = Pattern(image)
        width = pattern.get_width()

        assert width == 3


with description("Invader"):
    with before.all:
        self.invader_data = [
            "--o-----o--",
            "---o---o---",
            "--ooooooo--",
            "-oo-ooo-oo-",
            "ooooooooooo",
            "o-ooooooo-o",
            "o-o-----o-o",
            "---oo-oo---"
        ]

        self.invader = Invader(self.invader_data)

    with it("get height"):
        assert self.invader.height == 8

    with it("get width"):
        assert self.invader.width == 11

    with it("work with get_height method"):
        assert self.invader.get_height() == 8

    with it("work with get_width method"):
        assert self.invader.get_width() == 11

with description("Radar"):
    with before.all:
        self.radar = Radar('./data/radar_sample.txt', './data/output.txt')

    with it("get loaded image dimensions"):
        assert self.radar.width == 100
        assert self.radar.height == 50

    with it("use get_height for height"):
        assert self.radar.get_height() == 50

    with it(" use get_width for width"):
        assert self.radar.get_width() == 100

with description("Radar Storage"):

    with before.all:
        self.FILE_INPUT = './data/radar_sample.txt'
        self.FILE_OUTPUT = './data/output.txt'

        self.manager = RadarStorageManager(self.FILE_INPUT, self.FILE_OUTPUT)

    with it("confirm input filename"):
        assert self.manager.filename_input_map == self.FILE_INPUT

    with it("confirm output filename"):
        assert self.manager.filename_output_map == self.FILE_OUTPUT

    with it("load radar image from file"):
        file_data = self.manager.load_radar_map()
        number_of_lines = len(file_data)
        assert number_of_lines == 50

    with it("save radar overlay to file"):
        pass

with description("Radar Search"):

    with before.all:
        self.manager = RadarSearchUsingDiff()

    with context("basic similarity searching functionality"):
        with it("calculate similarity of matching samples"):
            similarity = self.manager.calculate_similarity_of_samples('---oo---', '---oo---')
            assert similarity == 1

        with it("calculate similarity for samples that are NOT matching"):
            similarity = self.manager.calculate_similarity_of_samples('--------', 'oooooooo')
            assert similarity == 0

        with it("calculate similarity for samples matching for 25%"):
            similarity = self.manager.calculate_similarity_of_samples('---oo---', 'oooooooo')
            assert similarity == 0.25

    with context("functionality for matching patterns"):
        with it("calculate 84% similarity for invader in radar map"):
            radar = Radar('./data/radar_sample.txt', './data/output.txt')

            invader_image = [
                "--o-----o--",
                "---o---o---",
                "--ooooooo--",
                "-oo-ooo-oo-",
                "ooooooooooo",
                "o-ooooooo-o",
                "o-o-----o-o",
                "---oo-oo---"
            ]

            invader = Invader(invader_image)
            similarity = self.manager.calculate_similarity_for_pattern(1, 74, radar, invader)
            assert round(similarity, 2) == 0.84

        with it("find 4 invaders of type #1"):
            radar = Radar('./data/radar_sample.txt', './data/output.txt')

            invader_image = [
                "--o-----o--",
                "---o---o---",
                "--ooooooo--",
                "-oo-ooo-oo-",
                "ooooooooooo",
                "o-ooooooo-o",
                "o-o-----o-o",
                "---oo-oo---"
            ]

            invader = Invader(invader_image)
            invaders_found = self.manager.search_for_pattern(radar, invader)

            assert self.manager.RATIO_MATCH == 0.79
            assert invaders_found == 4

        with it("find 5 invaders of type #2"):
            radar = Radar('./data/radar_sample.txt', './data/output.txt')

            invader_image = [
                "---oo---",
                "--oooo--",
                "-oooooo-",
                "oo-oo-oo",
                "oooooooo",
                "--o--o--",
                "-o-oo-o-",
                "o-o--o-o"
            ]

            invader = Invader(invader_image)
            invaders_found = self.manager.search_for_pattern(radar, invader)

            assert self.manager.RATIO_MATCH == 0.79
            assert invaders_found == 5

        with it("overlay radar image with image of invader"):
            row_start = 3
            col_start = 73
            invader_char = '#'

            radar = Radar('./data/radar_sample.txt', './data/output.txt')

            invader_image = [
                "--o-----o--",
                "---o---o---",
                "--ooooooo--",
                "-oo-ooo-oo-",
                "ooooooooooo",
                "o-ooooooo-o",
                "o-o-----o-o",
                "---oo-oo---"
            ]
            invader = Invader(invader_image)

            # Make sure there is no overlay, yet
            num_of_invader_chars = radar.image[row_start].count(invader_char)
            assert num_of_invader_chars == 0

            self.manager.overlay_image_with_pattern(row_start, col_start, radar, invader, invader_char)

            num_of_invader_chars = radar.image[row_start].count(invader_char)
            assert num_of_invader_chars == 6
