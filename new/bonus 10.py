try:
    width = float(input("Enter rectangular width:"))
    length = float(input("Enter rectangular length:"))

    if width == length :
        exit("That looks like a square. ")

    area = width*length
    print(area)
except ValueError:
    print("Please enter a number.")