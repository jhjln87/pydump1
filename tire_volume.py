import math

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspRat = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diamete of the wheel in inches (ex 15): "))

volume = (math.pi * width**2 * aspRat * (width * aspRat + 2540 * diameter)) / 10000000000

print(f"The approximate volume is {volume:.2f} liters")