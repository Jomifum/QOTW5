#Question of the Week 5
#Question 1:
class StringReverser:
    def __init__(self):
        self.input_string = input("Enter a string: ")  # Takes input from the user

    def reverse_words(self):
        words = self.input_string.split()  # Split the string by spaces
        reversed_words = words[::-1]       # Reverse the list of words
        print(' '.join(reversed_words))    # Print the reversed string


# Create an instance of the class to run the functionality
reverser = StringReverser()
reverser.reverse_words()

#question 2:
import math

class Circle:
    def __init__(self):
        self.radius = float(input("Enter the radius of the circle: "))  # Take radius input from the user

    def compute_area(self):
        area = math.pi * (self.radius ** 2)  # Calculate area using πr²
        return area

    def compute_perimeter(self):
        perimeter = 2 * math.pi * self.radius  # Calculate perimeter using 2πr
        return perimeter


# Create an instance of the class and print area and perimeter
circle = Circle()
print(f"Area of the circle: {circle.compute_area():.2f}")
print(f"Perimeter of the circle: {circle.compute_perimeter():.2f}")
