from new.conveter14 import convert
from new.parses14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed ['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")


if result < 1:
    print("oh no he is not allowed he is a dinosour tchtch :(")
else:
    print("perfect height !!!")