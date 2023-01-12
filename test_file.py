# utility functions
def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False





# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Write down your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

# Tests (copy to tests/test_user_functions.py)
import pytest
import io
import re

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'

# Do the same for the following functions
# Functions in src/user_functions.py and tests in tests/test_user_functions.py

def get_user_name_from_input():
    """ Not empty string. No spaces. """
    name = input("Create your user name: ")
    if (" " in name):
        print('Email is not valid.')
    else:
        return name

def test_user_name_empty_string(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(' '))
    assert get_user_name_from_input() is None

def test_user_name_no_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra karefle'))
    assert get_user_name_from_input() is None

def test_user_name_no_spaces(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('pkarefle'))
    assert get_user_name_from_input() == 'pkarefle'


def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    return input("Create your password: ")

