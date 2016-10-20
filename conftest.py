import pytest

def pytest_itemcollected(item):
    """Set tests docstring into pytest report instead of class::test_name"""
    if item._obj.__doc__: item._nodeid = item.obj.__doc__.strip()
