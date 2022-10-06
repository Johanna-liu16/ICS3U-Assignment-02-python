#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program calculates the volume of a cone

import constants


def main():
    # this function calculates the volume of a sphere

    # input
    print("The formula of a cone is V = πr²h÷3 .")
    radius = int(input("Enter the radius of the cone (cm): "))
    height = int(input("Enter the height of the cone (cm): "))

    # process
    volume = constants.PI * radius ** 2 * height / 3

    # output
    print("The volume of the cone is {0} cm³.".format(round(volume, 2)))

    print("\nDone.")


if __name__ == "__main__":
    main()