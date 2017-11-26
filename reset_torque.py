import pypot.dynamixel

ports = pypot.dynamixel.get_available_ports()

if not ports:
    raise IOError('no port found!')

print('ports found', ports)

print('connecting on the first available port:', ports[0])
dxl_io = pypot.dynamixel.DxlIO(ports[0])

found_ids = dxl_io.scan(range(10))

print("%s found IDS" % found_ids)

led = dxl_io.is_led_on(found_ids)

print("LED", led)

dxl_io.enable_torque(found_ids)
