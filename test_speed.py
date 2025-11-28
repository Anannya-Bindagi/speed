import pytest
from speed import cal_speed 

def test_speed():
    distance = 200
    time = 5
    #expected output
    expected_output = 40
    #validation
    assert cal_speed(distance,time) == expected_output