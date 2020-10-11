"""
Basic type of class used for Radar and Invader, or any other object with image as its base.
"""
from typing import List


class Pattern:
    image: List = []
    height: int = 0
    width: int = 0

    def __init__(self, image):
        self.image = image
        self.set_height()
        self.set_width()

    def set_height(self):
        self.height = len(self.image)

    def set_width(self):
        try:
            self.width = len(self.image[0])
        except IndexError:
            self.width = 0

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width