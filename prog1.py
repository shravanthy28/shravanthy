# Function to calculate the area of a circle
def calculate_area(radius):
    area = 3.14159 * radius ** 2
    return area

# Main program
if __name__ == "__main__":
    # Input radius from the user
    radius = float(input("Enter the radius of the circle: "))
    
    # Calculate the area using the function
    area = calculate_area(radius)
    
    # Print the area
    print(f"The area of a circle with radius {radius} is {area}")
