def print_pyramid(height):
    """
    Prints a pyramid
    Example for height=5:
        *
       ***
      *****
     *******
    *********
    """
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

print_pyramid(5)