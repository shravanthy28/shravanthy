def calculate_area(length, width):
    area = length * width
    return area

# Main program
if __name__ == "__main__":
    # Input length and width from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate the area using the function
    area = calculate_area(length, width)

    # Print the area
    print(f"The area of the rectangle with length {length} and width {width} is {area}.")