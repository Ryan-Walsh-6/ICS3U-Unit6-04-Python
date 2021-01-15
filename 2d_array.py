#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program generate a 2-D array and finds average of all numbers in array

import random


def average_of_numbers(passed_in_2d_list):
    # this function adds up and calculates the average all the elements
    # in a 2D array

    total = 0
    length_of_list = 0
    for row_value in passed_in_2d_list:
        for single_element in row_value:
            total += single_element
            length_of_list += 1
    average = total / length_of_list

    return average


def main():
    # this program generate a 2-D array and finds average of all numbers in
    # array

    a_2d_list = []

    # input
    while True:
        try:
            rows_from_user = input("How many row would you like: ")
            rows_from_user = int(rows_from_user)
            columns_from_user = input("How many columns would you like: ")
            print("\n", end="")
            columns_from_user = int(columns_from_user)
            if rows_from_user < 0 or columns_from_user < 0:
                print("Please ensure all values are positive.")
                print("\n", end="")
            else:
                break
        except Exception:
            print("Please enter a valid number.")
            print("\n", end="")
    for loop_counter_rows in range(0, rows_from_user):
        temp_column = []
        for loop_counter_columns in range(0, columns_from_user):
            a_random_number = random.randint(0, 50)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    average = average_of_numbers(a_2d_list)
    print("\n", end="")
    print("The average of all the numbers is: {0:,.2f} ".format(average))


if __name__ == "__main__":
    main()
