import math
number = int(input("Enter the number of items: "))
itmPerBox = int(input("Enter the number of items per box: "))
print(f"For {number} items, packing {itmPerBox} items in each box, you will need {math.ceil(number/itmPerBox)} boxes.")