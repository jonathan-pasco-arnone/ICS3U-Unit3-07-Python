#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program determines whether the user can date the grandchild


def main():
    # This function determines whether the user can date the grandchild

    print("")
    print("I am going to determine whether you can date my grandchild")
    print("")
    age = int(input("Please enter your age: "))
    print("")

    if age >= 25 and age <= 40:
        print("You may date my grandchild")

    elif age > 40:
        print("You are too old")

    elif age < 25:
        print("You are too young")

    else:
        print("Please enter an actual age")


if __name__ == "__main__":
    main()
