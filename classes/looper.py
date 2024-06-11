import pygame
from classes.background import Background

class LoopingVariable:

    def __init__(self, bound):
        self.bound = bound
        self.loopValues = 0

    def increase(self, amount):
        if self.loopValues + amount >= self.bound:
            self.loopValues += amount
            while self.loopValues >= self.bound:
                self.loopValues -= self.bound
        else:
            self.loopValues += amount
        


    # Value getter
    @property
    def value(self):
        return self.loopValues

    # Value setter
    @value.setter
    def valueSet(self, new_value):
        self.loopValues = new_value
