from winreg import DeleteKey


def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

print()
print("***** Area Perimeter Calculator *****")


keep_going = ""
while keep_going == "":
    print()
    width = num_check("width: ")
    height = num_check("Height: ")

    area = width * height

    perimeter = 2 * (width + height)

    print()
    print("the perimeter of your rectangle is {} units".format(perimeter))
    print("the area of your rectangle is {} square units".format(area))
    print()

    keep_going = input("press <enter> to keep going or any other key to quit")

print()
print("Thanks for using the area / perimeter calculator")