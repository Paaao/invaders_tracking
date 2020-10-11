#!/usr/bin/env python3
"""
Application for tracking invaders on provided radar image, revealing possible locations of known types of invaders.
Created as a simple challenge from Marketer.tech

In this version main options are provided as default values,
and only input file (radar sample) can be provided as optional argument:
    python3 -m tracker --sample_file radar_sample.txt
    or
    python3 -m tracker -f radar_sample.txt
    If not provided then default filename is used.

Required input is radar image provided as .txt file (like noted above specified default filename or as an argument)
Output of radar image with found invaders overlay is saved into .txt file.

Author: Pavel Ondra
Email: ondra.pavel@gmail.com
"""

import argparse
from tracker.invader import Invader
from tracker.invadersmanger import InvadersManager
from tracker.radar import Radar


class Tracker:
    """
    Collection of tools for identifying threat from known invaders on provided radar image.
    """
    invaders: InvadersManager
    radar: Radar
    found_invaders = 0

    def __init__(self, input_file, output_file):
        self.invaders = InvadersManager()
        self.radar = Radar(input_file, output_file)
        self.load_invaders()

    def add_invader(self, invader_data):
        invader = Invader(invader_data)
        self.invaders.add_invader(invader)

    def load_invaders(self):
        # TODO: load invaders from file or database, ... next time :)
        invader1 = [
            "--o-----o--",
            "---o---o---",
            "--ooooooo--",
            "-oo-ooo-oo-",
            "ooooooooooo",
            "o-ooooooo-o",
            "o-o-----o-o",
            "---oo-oo---"
        ]

        invader2 = [
            "---oo---",
            "--oooo--",
            "-oooooo-",
            "oo-oo-oo",
            "oooooooo",
            "--o--o--",
            "-o-oo-o-",
            "o-o--o-o"
        ]

        self.add_invader(invader1)
        self.add_invader(invader2)

    def run_search(self):
        """
        Execute search for all individual invaders from list of known invaders on the radar image.
        Overlay of found invaders over radar image is then saved into output file for closer examination.
        """
        print('Searching for invaders')
        for index, invader in enumerate(self.invaders.known_invaders):
            radar_map_overlay_character = str(index + 1)
            found_current = self.radar.search(invader, radar_map_overlay_character)
            self.found_invaders += found_current

        if self.found_invaders > 0:
            self.radar.save_radar_image_with_overlay()

        print("With similarity acceptance ratio: {0}%".format(self.radar.RATIO_MATCH * 100))
        print("Invaders found:", self.found_invaders)
        print("Radar image with identified invaders saved in:", self.radar.manager.filename_output_map)


if __name__ == '__main__':
    print('Run this application from main directory like: $ python3 -m tracker')