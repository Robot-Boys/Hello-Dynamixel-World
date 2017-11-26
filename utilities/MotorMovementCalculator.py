
class MotorMovementCalculator(object):

    def __init__(self, motor):
        self.motor = motor
        self.reset()

    def reset(self):
        self.current_step = 0;
        self.motor._set_compliancy()

