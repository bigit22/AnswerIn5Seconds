from random import randint
from time import sleep

class Player:
    def __init__(self, pic_path, name):
        self.pos = 0
        self.pic_path = pic_path
        self.name = name
        self.spare_time = 0

    def make_a_move(self, step):
        self.pos += step

    def add_spare_time(self, time):
        self.spare_time += time

    def roll_a_dice(self):
        self.make_a_move(randint(1, 6))


