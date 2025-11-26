import numpy as np
import pedal_communication


def test_version():
    assert pedal_communication.__version__ == "0.1.0"


def test_adder():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = pedal_communication.adder(a, b)
    assert np.all(result == np.array([5, 7, 9]))
