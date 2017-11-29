import math

from easing.AbstractEase import AbstractEase


class SinEase(AbstractEase):

    @classmethod
    def calculate_next_step(self, current_time, start_value, change_in_value, duration):
        return -change_in_value / 2 * (math.cos(math.pi * current_time / duration) - 1) + start_value
