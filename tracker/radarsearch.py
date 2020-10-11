import difflib
from tracker.pattern import Pattern


class RadarSearch:
    patterns_found: int = 0

    def search_for_pattern(self, radar_image: Pattern, pattern: Pattern) -> int:
        pass

    @staticmethod
    def overlay_image_with_pattern(row_start: int, col_start: int, radar: Pattern, pattern: Pattern, pattern_char: str):
        pass


class RadarSearchUsingDiff(RadarSearch):
    RATIO_MATCH = 0.79  # Minimal matching ratio to consider as positive similarity match (between 0-1, 0.79 == 79%)
    MINIMUM_HEIGHT = 5  # Minimum rows for matching, so we are not making match with last lines at the bottom of image
    MINIMUM_DISTANCE = 4  # Minimal "distance" between samples, to avoid multiple positive matches from same invader

    @staticmethod
    def calculate_similarity_of_samples(sample_1, sample_2):
        return difflib.SequenceMatcher(None, sample_1, sample_2).ratio()

    def calculate_similarity_for_pattern(self, row_start: int, col_start: int,
                                         radar_image: Pattern, pattern: Pattern) -> float:

        col_offset = col_start + pattern.width
        pattern_row = 0
        similarity_ratio = []

        for i in range(row_start, row_start + pattern.height):
            if i < radar_image.height:
                sample_radar = radar_image.image[i][col_start: col_offset]
                sample_invader = pattern.image[pattern_row]
                similarity_of_sample = self.calculate_similarity_of_samples(sample_invader, sample_radar)
                similarity_ratio.append(similarity_of_sample)
            pattern_row += 1

        if not similarity_ratio:
            return 0

        return sum(similarity_ratio) / len(similarity_ratio)

    def search_for_pattern(self, radar: Pattern, pattern: Pattern, char: str = "#") -> int:
        self.patterns_found = 0
        for row_start in range(0, radar.height):
            columns = iter(range(0, radar.width - pattern.width))

            for col_start in columns:
                col_offset = col_start + pattern.width

                if (radar.height - row_start) < self.MINIMUM_HEIGHT:
                    break

                similarity = self.calculate_similarity_for_pattern(row_start, col_start, radar, pattern)

                if similarity >= self.RATIO_MATCH:
                    self.overlay_image_with_pattern(row_start, col_start, radar, pattern, char)

                    # Skip columns / keep distance between searched samples
                    for n in range(0, self.MINIMUM_DISTANCE):
                        if (col_offset + n) < radar.width - 1:
                            next(columns)

                    self.patterns_found += 1

        return self.patterns_found

    @staticmethod
    def overlay_image_with_pattern(row_start: int, col_start: int, radar: Pattern, pattern: Pattern, pattern_char: str):

        col_offset = col_start + pattern.width

        for row in range(row_start, row_start + pattern.height):
            if row < radar.height:
                sample = radar.image[row][col_start: col_offset]
                sample = sample.replace("o", pattern_char)

                new_row = str(radar.image[row][0:col_start]) + sample + str(radar.image[row][col_offset:])

                radar.image[row] = new_row
