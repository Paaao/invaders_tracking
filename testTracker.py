#!/usr/bin/env python3
"""
Some simple unit tests with build in unittest library ;)

To run it: python3 testTracker.py
"""
import unittest

import tracker


class TestStringMethods(unittest.TestCase):

    tracker = object

    @classmethod
    def setUpClass(cls) -> None:
        radar_sample = cls.load_radar_sample(cls)
        cls.tracker = tracker.Tracker(radar_sample)

        # Make sure that testing with expected values for options
        cls.tracker.RATIO_MATCH = 0.79
        cls.tracker.MINIMUM_HEIGHT = 5
        cls.tracker.MINIMUM_DISTANCE = 4

    @staticmethod
    def load_radar_sample(cls):
        radar_image = []

        with open(tracker.RADAR_FILE, 'r') as radar_file:
            for line in radar_file:
                radar_image.append(line.strip())
        return radar_image

    def test_radar_is_loaded(self):
        self.assertEqual(self.tracker.radar.width, 100)
        self.assertEqual(self.tracker.radar.height, 50)

    def test_invaders_are_loaded(self):
        self.assertEqual(len(self.tracker.known_invaders), 2)

        self.assertEqual(self.tracker.known_invaders[0].width, 11)
        self.assertEqual(self.tracker.known_invaders[0].height, 8)

        self.assertEqual(self.tracker.known_invaders[1].width, 8)
        self.assertEqual(self.tracker.known_invaders[1].height, 8)

    def test_match_ratio_100_percent(self):
        ratio = self.tracker.calculate_samples_similarity('---oo---', '---oo---')
        self.assertEqual(ratio, 1)

    def test_match_ratio_zero_percent(self):
        ratio = self.tracker.calculate_samples_similarity('--------', 'oooooooo')
        self.assertEqual(ratio, 0)

    def test_calculate_total_similarity(self):
        invader = self.tracker.known_invaders[0]
        row_start = 1
        col_start = 73

        expected_similarity = 0.84
        calculated_similarity = self.tracker.calculate_total_similarity(row_start, col_start, invader)
        calculated_similarity = round(calculated_similarity, 2)

        self.assertEqual(expected_similarity, calculated_similarity)

    def test_search_for_invader(self):
        """
        With RATIO_MATCH=0.79 both invader types are found 4x
        """

        invader1 = self.tracker.known_invaders[0]
        invader1_found = self.tracker.search_for_invader(invader1)

        self.assertEqual(invader1_found, 4)

        invader2 = self.tracker.known_invaders[1]
        invader2_found = self.tracker.search_for_invader(invader2)

        self.assertEqual(invader2_found, 4)

    def test_overlay_radar_with_invader(self):
        invader = self.tracker.known_invaders[0]
        row_start = 3
        col_start = 73
        invader_char = '#'

        image = self.tracker.radar.image.copy()

        # Make sure there is no overlay, yet
        num_of_invader_chars = self.tracker.radar.image[row_start].count(invader_char)
        self.assertEqual(num_of_invader_chars, 0)

        self.tracker.overlay_radar_with_invader(row_start, col_start, invader, invader_char)

        num_of_invader_chars = self.tracker.radar.image[row_start].count(invader_char)

        # Restore image with clean one again
        self.tracker.radar.image = image

        self.assertEqual(num_of_invader_chars, 6)


if __name__ == '__main__':
    unittest.main()