from spike import PrimeHub, MotorPair, ColorSensor, DistanceSensor
from spike.control import wait_for_seconds

hub = PrimeHub()

motor_pair = MotorPair('A', 'B')
motor_pair.set_default_speed(50)

distance_sensor = DistanceSensor('C')
color_sensor_d = ColorSensor('D')
color_sensor_e = ColorSensor('E')

try:
    while True:
        dist_cm = distance_sensor.get_distance_cm()
        if dist_cm is not None and dist_cm < 10:
            motor_pair.stop()
            print("Obstacle detected! Stopping car.")
            break

        color_d = color_sensor_d.get_color()
        color_e = color_sensor_e.get_color()

        if color_d == 'red' or color_e == 'red':
            print("Color detected: red")

        motor_pair.start()

except KeyboardInterrupt:
    motor_pair.stop()
    print("Program stopped.")