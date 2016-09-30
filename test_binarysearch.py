import unittest
import numpy as np

from binarysearch import binary_search

def test_output():
    assert binary_search(list(range(10)), 5) == 5

def test_missingval():
    assert binary_search(list(range(10)), 4.5) == -1

def test_output_1():
    assert binary_search([5], 5) == 0

def test_missingval_1():
    assert binary_search([5], 4) == -1

def test_zeroarray():
    assert binary_search([], 1) == -1

def test_infty():
    assert binary_search([1, 2, np.inf], 2) == 1

def test_infty2():
    assert binary_search([1, 2, np.inf], np.inf) == 2

def test_ind1():
    assert binary_search(list(range(10)), 5, 1, 3) == -1

def test_ind2():
    assert binary_search(list(range(10)), 2, 1, 3) == 2

def test_ind3():
    assert binary_search(list(range(10)), 2, 3, 1) == -1

def test_ind4():
    assert binary_search(list(range(10)), 2, 2, 2) == 2

def test_ind5():
    assert binary_search(list(range(10)), 5, 2, 2) == -1
