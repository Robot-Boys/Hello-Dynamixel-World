import time

from pypot.robot.config import ergo_robot_config
import pypot.robot
import pypot.dynamixel

class MotorTester(object):
    def __main__(self):
        pass

    def test_robot(self):
        custom_config = {
        'controllers': {
            'my_dxl_controller': {
                'sync_read': False,
                'attached_motors': ['base'],
                'port': '/dev/ttyACM3'
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
        print(pypot.dynamixel.get_available_ports())
        dxl_io = pypot.dynamixel.DxlIO('/dev/ttyACM3')
        print(dxl_io.scan())

    def robot_move(self, robot, position, duration, type, wait):
        for m in robot.motors:
            print(m)
            m.compliant = False

        robot.goto_position(position, duration, type, wait)

    def simple_move(self, robot):

        for m in robot.motors:
            m.compliant = False
            m.goal_position = 0

        time.sleep(2)

        robot.m4.goal_position = 50
        robot.m5.goal_position = 50


        time.sleep(20)
