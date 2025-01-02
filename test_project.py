import pytest
from project import get_user_name, teach_scale


# Test for get_user_name function
def test_get_user_name(monkeypatch):
    # Test Case 1: Correct name input
    monkeypatch.setattr('builtins.input', lambda _: 'John')
    result = get_user_name()
    assert result == "John"  # Check if the returned name is correct

    # Test Case 2: Empty input (handling empty name)
    monkeypatch.setattr('builtins.input', lambda _: '')
    result = get_user_name()
    assert result == "Please enter a valid name"  # Adjust this based on your actual handling of empty input


# Test for teach_scale function
def test_teach_scale():
    # Test Case 1: Correct scale input
    result = teach_scale("Selamta")
    assert result == "The notes for Selamta are: [C D F G A C], with gaps: [1, 1.5, 1, 1, 1.5]"

    # Test Case 2: Incorrect scale input
    result = teach_scale("InvalidScale")
    assert result == "Invalid scale name, please choose a valid scale."  # Adjust this based on your actual error handling
