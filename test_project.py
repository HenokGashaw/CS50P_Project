import pytest
from project import get_user_name, teach_scale, introduce_scales


# Test for get_user_name function
def test_get_user_name(monkeypatch):
    # Test Case 1: Correct name input
    monkeypatch.setattr('builtins.input', lambda _: 'John')
    result = get_user_name()
    assert result == "John"  # Check if the returned name is correct

    # Test Case 2: Empty input (handling empty name)
    monkeypatch.setattr('builtins.input', lambda _: '')
    result = get_user_name()
    assert result == "Learner"  # Adjust this based on your actual handling of empty input


# Test for teach_scale function
def test_teach_scale():
    # Test Case 1: Correct scale input
    result = teach_scale("Selamta")
    assert result == None

def test_introduce_scales(monkeypatch):
    # Test Case 1: Correct scale input
    monkeypatch.setattr('builtins.input', lambda _: 'Tizita')
    result = introduce_scales(name="Henok")
    assert result == "You chose Tizita. Let's start learning!"

    # Test Case 2: Incorrect scale input
    monkeypatch.setattr('builtins.input', lambda _: 'InvalidScale')
    result = introduce_scales(name="Henok")
    assert result == "Invalid input. Please choose a valid scale."
