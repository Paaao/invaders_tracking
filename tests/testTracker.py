#!/usr/bin/env python3
"""
Some simple unit tests with build in unittest library ;)

To run it: python3 testTracker.py
"""
import unittest

from tracker.radar import Radar
from tracker.invader import Invader
from tracker.pattern import Pattern
from tracker.radarstorage import RadarStorageManager
from tracker.radarsearch import RadarSearchUsingDiff


class TestPattern(unittest.TestCase):
    def test_pattern_with_empty_image(self):
        image = []

        pattern = Pattern(image)

        self.assertEqual(pattern.width, 0)
        self.assertEqual(pattern.height, 0)

    def test_pattern_with_image(self):
        image = [
            "OOO",
            "OOO"
        ]

        pattern = Pattern(image)

        self.assertEqual(pattern.width, 3)
        self.assertEqual(pattern.height, 2)

    def test_get_height(self):
        image = [
            "OOO",
            "OOO"
        ]

        pattern = Pattern(image)
        height = pattern.get_height()

        self.assertEqual(height, 2)

    def test_get_width(self):
        image = [
            "OOO",
            "OOO"
        ]

        pattern = Pattern(image)
        width = pattern.get_width()

        self.assertEqual(width, 3)


class TestInvader(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.invader_data = [
            "--o-----o--",
            "---o---o---",
            "--ooooooo--",
            "-oo-ooo-oo-",
            "ooooooooooo",
            "o-ooooooo-o",
            "o-o-----o-o",
            "---oo-oo---"
        ]
        cls.invader = Invader(cls.invader_data)

    def test_invader_height_is_correct(self):
        self.assertEqual(self.invader.height, 8)

    def test_invader_width_is_correct(self):
        self.assertEqual(self.invader.width, 11)

    def test_invader_get_height(self):
        height = self.invader.get_height()
        self.assertEqual(height, 8)

    def test_invader_get_width(self):
        width = self.invader.get_width()
        self.assertEqual(width, 11)


class TestRadar(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        storage_manager = RadarStorageManager('./data/radar_sample.txt', './data/output.txt')
        cls.radar = Radar(storage_manager)

    def test_radar_is_loaded(self):
        self.assertEqual(self.radar.width, 100)
        self.assertEqual(self.radar.height, 50)

    def test_radar_get_height(self):
        height = self.radar.get_height()
        self.assertEqual(height, 50)

    def test_radar_get_width(self):
        width = self.radar.get_width()
        self.assertEqual(width, 100)


class TestRadarStorage(unittest.TestCase):
    FILE_INPUT = './data/radar_sample.txt'
    FILE_OUTPUT = './data/output.txt'

    @classmethod
    def setUpClass(cls) -> None:
        cls.manager = RadarStorageManager(cls.FILE_INPUT, cls.FILE_OUTPUT)

    def test_input_filename(self):
        self.assertEqual(self.manager.filename_input_map, self.FILE_INPUT)

    def test_output_filename(self):
        self.assertEqual(self.manager.filename_output_map, self.FILE_OUTPUT)

    def test_loading_radar_from_file(self):
        file_data = self.manager.load_radar_map()
        number_of_lines = len(file_data)
        self.assertEqual(number_of_lines, 50)

    def test_save_radar_with_overlay(self):
        pass


class TestRadarSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manager = RadarSearchUsingDiff()

    def test_calculate_similarity_of_samples_matching(self):
        similarity = self.manager.calculate_similarity_of_samples('---oo---', '---oo---')
        self.assertEqual(similarity, 1)

    def test_calculate_similarity_of_samples_not_matching(self):
        similarity = self.manager.calculate_similarity_of_samples('--------', 'oooooooo')
        self.assertEqual(similarity, 0)

    def test_calculate_similarity_of_samples_matching_0_25(self):
        similarity = self.manager.calculate_similarity_of_samples('---oo---', 'oooooooo')
        self.assertEqual(similarity, 0.25)

    def test_similarity_calculation_for_pattern(self):
        storage_manager = RadarStorageManager('./data/radar_sample.txt', './data/output.txt')
        radar = Radar(storage_manager)

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
        self.assertEqual(round(similarity, 2), 0.84)

    def test_search_for_pattern(self):
        storage_manager = RadarStorageManager('./data/radar_sample.txt', './data/output.txt')
        radar = Radar(storage_manager)

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

        self.assertEqual(self.manager.RATIO_MATCH, 0.79)
        self.assertEqual(invaders_found, 4)

    def test_search_for_pattern_2(self):
        storage_manager = RadarStorageManager('./data/radar_sample.txt', './data/output.txt')
        radar = Radar(storage_manager)

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

        self.assertEqual(self.manager.RATIO_MATCH, 0.79)
        self.assertEqual(invaders_found, 5)

    def test_overlay_radar_with_invader(self):
        row_start = 3
        col_start = 73
        invader_char = '#'

        storage_manager = RadarStorageManager('./data/radar_sample.txt', './data/output.txt')
        radar = Radar(storage_manager)

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
        self.assertEqual(num_of_invader_chars, 0)

        self.manager.overlay_image_with_pattern(row_start, col_start, radar, invader, invader_char)

        num_of_invader_chars = radar.image[row_start].count(invader_char)
        self.assertEqual(num_of_invader_chars, 6)


if __name__ == '__main__':
    unittest.main()