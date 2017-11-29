import time
from MotorTester import MotorTester

#my_config = dict(ergo_robot_config)
#my_config['controllers']['port'] = 'COM6' # For Windows' users

#custom_config = {'motors': {'m1': {'angle_limit': [-90.0, 90.0], 'type': 'MX-28', 'orientation': 'direct', 'offset': 0.0, 'id': 1}, 'm2': {'angle_limit': [-90.0, 90.0], 'type': 'MX-28', 'orientation': 'indirect', 'offset': 0.0, 'id': 2}}, 'motorgroups': {'base': ['m1', 'm2']}, 'controllers': {'my_dxl_controller': {'port': '/dev/ttyACM3', 'sync_read': False, 'attached_motors': ['base']}}}

tester = MotorTester()
#tester.scan_ports()
my_robot = tester.test_robot()
my_robot.start_sync()

#start_pos = {'m4': 0, 'm5': 0}
#end_pos = {'m4': 90, 'm5': -90}
#tester.robot_move(my_robot, start_pos, 1, None, True)
#tester.robot_move(my_robot, end_pos, 10, None, True)
#scan_motors()

tester.reset_robot(my_robot)

tester.ease_by_speed(my_robot.m5, 10, 2)

time.sleep(1)

tester.ease_by_speed(my_robot.m5, -50, 2)

time.sleep(1)

tester.ease_by_speed(my_robot.m5, 70, 2)

time.sleep(1)


tester.reset_robot(my_robot)
for i in range(1, 1000):
    tester.ease_move_position(my_robot, 160)


my_robot.close()
