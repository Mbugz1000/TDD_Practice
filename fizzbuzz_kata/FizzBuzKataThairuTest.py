import pytest

def fizzBuzz(value):
    if isMultiple(value,3) & isMultiple(value,5):
        return "FizzBuzz"
    elif isMultiple(value,3):
        return "Fizz"
    elif isMultiple(value,5):
        return "Buzz"
    else:
        return str(value)

def checkFizzBuzz(value, expextedRetVal):
    assert expextedRetVal == fizzBuzz(value)

def isMultiple(value, mod):
    return (value%mod) == 0

def test_returns1WithPassedIn():
    checkFizzBuzz(1,"1")

def test_returns2WithPassedIn():
    checkFizzBuzz(2, "2")
#
# def test_returnsFizzWith3PassedIn():
#     checkFizzBuzz(3, "Fizz")
#
# def test_returnsBuzzWith5PassedIn():
#     checkFizzBuzz(5, "Buzz")

def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")

def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

def test_returnsBuzzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")

# def setup_function(function):
#     if function == test_returnsBuzzWith15PassedIn:
#         print("Testing Setup Fuctions")
#
# def teardown_function(function):
#     if function == test_returnsBuzzWith15PassedIn:
#         print("Testing Teardown Fuctions")