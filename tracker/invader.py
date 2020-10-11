"""
Class for storing all important details about invader.
"""
from tracker.pattern import Pattern


class Invader(Pattern):

    def __init__(self, image):
        Pattern.__init__(self, image)
