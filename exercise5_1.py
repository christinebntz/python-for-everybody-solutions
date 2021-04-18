#!/usr/bin/env python3
"""
Exercise 5.1: Write a program which repeatedly reads numbers until the user
enters "done". Once "done" is entered, print out the total, count, and average
of the numbers. If the user enters anything other than a number, detect their
mistake using try and except and print an error message and skip to the next
number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.33333333333333

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""


print('Please input random numbers. Then, input "done" if you wish to end the loop.')

sum = 0 
ctr = 0
avg = 0

while True:
    try:
        num = input('Input a number: ')
        if num == 'done':
            break
        else:
            num1 = float(num) 
            ctr = ctr + 1 
            sum = sum + num1
            avg = sum / ctr
    except:
        print('Invalid input.')

print('The count is ', ctr)
print('The sum is ', sum)
print('The average is ', avg)
