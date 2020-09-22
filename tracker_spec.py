"""
Simple BDD tests with mamba library
https://github.com/nestorsalceda/mamba
"""
from mamba import description, context, before, it
from expects import expect, equal

import tracker

with description("Tracker") as self:
    with before.all:
        # Load tracker and setup data before starting tests
        radar_image = []

        with open(tracker.RADAR_FILE, 'r') as radar_file:
            for line in radar_file:
                radar_image.append(line.strip())

        self.tracker = tracker.Tracker(radar_image)

    with context("stored data and objects"):
        with it("work with radar"):
            assert self.tracker.radar.width == 100
            assert self.tracker.radar.height == 50

        with it("work with all invaders"):
            assert len(self.tracker.known_invaders) == 2

            assert self.tracker.known_invaders[0].width == 11
            assert self.tracker.known_invaders[0].height == 8

            assert self.tracker.known_invaders[1].width == 8
            assert self.tracker.known_invaders[1].height == 8

    with context("with similarity calculation"):
        with it("calculates similarity between samples"):

            expect(self.tracker.calculate_samples_similarity('---oo---', '---oo---')).to(equal(1))
            expect(self.tracker.calculate_samples_similarity('--------', 'oooooooo')).to(equal(0))

        with it("calculates total similarity for invader"):
            invader = self.tracker.known_invaders[0]
            row_start = 1
            col_start = 73

            expected_similarity = 0.84
            calculated_similarity = self.tracker.calculate_total_similarity(row_start, col_start, invader)
            calculated_similarity = round(calculated_similarity, 2)

            expect(calculated_similarity).to(equal(expected_similarity))

        with it("searches for invader in radar sample"):
            # With RATIO_MATCH=0.79 both invader types are found 4x

            invader1 = self.tracker.known_invaders[0]
            invader1_found = self.tracker.search_for_invader(invader1)

            expect(invader1_found).to(equal(4))

            invader2 = self.tracker.known_invaders[1]
            invader2_found = self.tracker.search_for_invader(invader2)

            expect(invader2_found).to(equal(4))

        with it("overlay radar with invader"):
            invader = self.tracker.known_invaders[0]
            row_start = 3
            col_start = 73
            invader_char = '#'

            self.tracker.overlay_radar_with_invader(row_start, col_start, invader, invader_char)
            num_of_invader_chars = self.tracker.radar.image[row_start].count(invader_char)

            expect(num_of_invader_chars).to(equal(11))
