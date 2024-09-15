import numpy as np
import math
import unittest

def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """
    g = 9.81 # acceleration due to gravity (m/s^2)
    
    potential_energy = mass * g * height # potential energy at the top
    
    theta = math.radians(incline) # angle in radians
    
    friction_force = friction * mass * g * math.cos(theta)
    friction_work = friction_force * length
    
    # translational kinetic energy + rotational kinetic energy = potential energy − work done by friction
    # using conservation of energy:
    # mgh = 0.5 * m * v^2 + 0.5 * I * omega^2 + friction_work
    # I = 0.5 * m * r^2, omega = v / r
    # simplifying the energy equation gives:
    # mgh = 0.5 * m * v^2 + 0.25 * m * v^2 + friction_work
    # mgh − friction_work = 0.75 * m * v^2
    # v = sqrt((mgh − friction−work) / (0.75 * m))
    
    kinetic_energy = potential_energy - friction_work
    speed = math.sqrt(kinetic_energy / (mass * 0.75))
    
    return speed

# Unit test class
class TestFinalDiskSpeed(unittest.TestCase):
    
    def test_case_1(self):
        result = final_disk_speed(10, 20, 30, 5, 0.1, 0.5)
        self.assertAlmostEqual(result, 10.40, places=2)
    
    def test_case_2(self):
        result = final_disk_speed(15, 25, 45, 3, 0.05, 0.3)
        self.assertAlmostEqual(result, 13.59, places=2)

if __name__ == '__main__':
    unittest.main()
