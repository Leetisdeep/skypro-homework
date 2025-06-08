# tests/test_decorators.py
import os

import pytest

from src.decorators import log


@pytest.fixture
def log_file():
    filename = "test_log_tmp.log"
    yield filename
    # Cleanup after tests
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except PermissionError:
            pass  # File might be locked by another process


def test_log_to_file(log_file):
    @log(log_file)
    def test_func(x):
        return x * 2

    result = test_func(5)
    assert result == 10

    # Verify log file was created and has content
    assert os.path.exists(log_file)
    with open(log_file, "r") as f:
        content = f.read()
    assert "test_func" in content
    assert "5" in content
    assert "10" in content


def test_function_ok(log_file):
    @log(log_file)
    def good_func(a, b):
        return a + b

    result = good_func(2, 3)
    assert result == 5


def test_function_fail(log_file):
    @log(log_file)
    def bad_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        bad_func()

    # Verify the error was logged
    with open(log_file, "r") as f:
        content = f.read()
    assert "bad_func" in content
    assert "Test error" in content
