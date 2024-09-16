# Title: Will there be enough space?
# Rank: 8 kyu
# Language Version: Python 3.4.3

## Instructions ##
# The Story:
# Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.
# Task Overview:
# You have to write a function that accepts three parameters:
# cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus.
# wait is the number of people waiting to get on to the bus.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
# Usage Examples:
# enough(10, 5, 5)
# 0 # He can fit all 5 passengers
# enough(100, 60, 50)
# 10 # He can't fit 10 out of 50 waiting
#
## Solution ##
def enough(cap, on, wait):
    return  0 if cap - on - wait > 0 else abs(cap - on - wait)

## Test Case ##
test.describe('Example Tests')
test.assert_equals(enough(10, 5, 5), 0)
test.assert_equals(enough(100, 60, 50), 10)
test.assert_equals(enough(20, 5, 5), 0)