from typing import List
from tracker.invader import Invader


class InvadersManager:
    known_invaders: List[Invader] = []

    def get_known_invaders(self):
        return self.known_invaders

    def add_invader(self, invader: Invader):
        self.known_invaders.append(invader)
