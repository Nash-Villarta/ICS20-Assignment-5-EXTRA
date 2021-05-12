# This inputs math into the python code so that math.pi could function.
import math

# This part calculates the circumference. Just like the JS code, it reads the input and puts it into the variable
# CNTND and runs it through the string and then displaying on the console.
print("Please input diameter for Circumference of a circle")
diameterC = float(input())
diameterC = diameterC / 2
print(2 * math.pi * diameterC)
# Like before, it takes the input and runs it through the string and then prints displaying the area using the diameter.
print("Please input diameter for Area of a circle")
diameterA = float(input())
diameterA = diameterA / 2
print(math.pi * diameterA * diameterA)
