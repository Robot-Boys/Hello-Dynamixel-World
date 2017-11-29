class AbstractEase(object):

    @classmethod
    def calculate_next_step(self, current_time, start_value, change_in_value, duration):
        raise NotImplementedError("You should have implemented this")

