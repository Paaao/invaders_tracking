from mamba import description, it
from expects import expect, equal

import tracker

with description("Tracker") as self:
    with it("calculate similarity between samples"):
        radar_sample = self.load_radar_sample()
        tr = tracker.Tracker(radar_sample)

        expect(tr.calculate_samples_similarity('---', '---')).to(equal(1))
        expect(tr.calculate_samples_similarity('---', 'ooo')).to(equal(0))

    def load_radar_sample(self):
        radar_image = []

        with open(tracker.RADAR_FILE, 'r') as radar_file:
            for line in radar_file:
                radar_image.append(line.strip())
        return radar_image
