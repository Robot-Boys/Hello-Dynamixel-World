import time
import easing

from pypot.robot.config import ergo_robot_config
import pypot.robot
import pypot.dynamixel


class MotorTester(object):
    def __init__(self, port=None):
        if port is not None:
            self.port = port
        else:
            self.port = self.getport()

    def getport(self):
        ports = pypot.dynamixel.get_available_ports()
        if not ports:
            raise IOError('no port found!')
        print('connecting on the first available port:', ports[0])
        return ports[0]


    def test_robot(self):
        custom_config = {
            'controllers': {
                'my_dxl_controller': {
                    'sync_read': False,
                    'attached_motors': ['base'],
                    'port': self.port
                }
            },
            'motorgroups': {
                'base': ['m5', 'm4']
            },
            'motors': {
                'm5': {
                    'orientation': 'indirect',
                    'type': 'MX-28',
                    'id': 1,
                    'angle_limit': [-90.0, 90.0],
                    'offset': 0.0
                },
                'm4': {
                    'orientation': 'direct',
                    'type': 'MX-28',
                    'id': 2,
                    'angle_limit': [-90.0, 90.0],
                    'offset': 0.0
                }
            }
        }
        return pypot.robot.from_config(custom_config)

    def scan_motors(self):
        dxl_io = pypot.dynamixel.DxlIO(self.port)
        print(dxl_io.scan())

    def scan_ports(self):
        print(pypot.dynamixel.get_available_ports())

    def robot_move(self, robot, position, duration, type, wait):
        robot.power_up()
        robot.goto_position(position, duration, type, wait)

    def print_motors(self, robot):
        for m in robot.motors:
            print(m)

    def reset_robot(self, robot):
        robot.power_up()  # Sets  compliant to false as sideeffect
        for m in robot.motors:
            # m.compliant = False
            m.goal_position = 0
        print("RESET")
        time.sleep(2)

    def simple_move_test(self, robot):
        robot.power_up()  # Sets  compliant to false as sideeffect
        for m in robot.motors:
            # m.compliant = False
            m.goal_position = 0

        time.sleep(2)

        robot.m4.goal_position = 4095
        robot.m5.goal_position = 4095

        time.sleep(20)

    def ease_move_position(self, robot, goal):
        print("Easing")
        steps = 20000
        for number in range(1, steps):
            self.calculate_ease_degress(goal, number, robot, steps)

        print("STOOOOOOOOOOOP")

        for number in range(steps, 1, -1):
            self.calculate_ease_degress(goal, number, robot, steps)


    def calculate_ease_degress(self, goal, current_position, robot, steps):
        for motor in robot.motors:
            ease_factor = easing.easeInOutSine(current_position, 1, 1, steps) - 1
            ease_pos = (90 - (goal * ease_factor))
            print(ease_pos)
            motor.goal_position = ease_pos
            time.sleep(0.000000000001)
