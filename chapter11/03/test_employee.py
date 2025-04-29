# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5,000 to the
# annual salary by default but also accepts a different raise amount.
#   Write a test file for Employee with two test functions, test_give_default
# _raise() and test_give_custom_raise(). Write your tests once without using a
# fixture, and make sure they both pass. Then write a fixture so you don’t have to
# create a new employee instance in each test function. Run the tests again, and
# make sure both tests still pass.

import pytest

from employee import Employee

@pytest.fixture
def employee():
    return Employee('bob', 'li', 10000)

def test_give_default_raise():
    e = Employee('alice', 'li', 10000)
    e.give_raise()
    assert e.annual_salary == 10000 + 5000

def test_give_custom_raise():
    e = Employee('alice', 'li', 10000)
    e.give_raise(10)
    assert e.annual_salary == 10000 + 10

def test_give_default_raise_with_fixture(employee):
    current = employee.annual_salary

    employee.give_raise()
    assert employee.annual_salary == current + 5000

def test_give_custom_raise_with_fixture(employee):
    current = employee.annual_salary

    employee.give_raise(10)

    assert employee.annual_salary == current + 10
