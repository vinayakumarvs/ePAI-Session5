import pytest
import random
import string
import session5
import os
import decimal
from decimal import Decimal
import math
import inspect
import re


README_CONTENT_CHECK_FOR = [
        'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_are_defined():
    content = inspect.getsource(session5)
    AllFUNCTIONSDEFINED = True
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            AllFUNCTIONSDEFINED = False
            pass
    assert AllFUNCTIONSDEFINED == True, "You have not defined all the required functions"

# Test for print

def test_print():
	q = session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=5)
	assert q != 0, 'print is not working'

# Test for squared_power_list()
def test_squared_power_list():
    q=session5.squared_power_list(2,start=0,end=6)
    assert q == [1, 2, 4, 8, 16, 32],'Wrong Result'

def test_squared_power_list_input():
    q = session5.squared_power_list(2,start=0,end=5)
    assert q[1] > 0, 'Negative values not acceptable in squared_power_list'

def test_squared_power_list_zeroinput():
    with pytest.raises(ValueError):
        session5.squared_power_list(0, start=0, end=5), 'Zero is not acceptable in squared_power_list'

def test_squared_power_list_start():
    with pytest.raises(ValueError):
        session5.squared_power_list(0, start=6, end=5), 'start > end is not acceptable in squared_power_list'

def test_squared_power_list_invalid_number():
    with pytest.raises(TypeError):
        session5.squared_power_list('2', start=0, end=5), 'Invalid Type of input value in squared_power_list'

def test_squared_power_list_invalid_startnumber():
    with pytest.raises(TypeError):
        session5.squared_power_list(2, start='1', end=5), 'Invalid Type of start value in squared_power_list'

def test_squared_power_list_invalid_endnumber():
    with pytest.raises(TypeError):
        session5.squared_power_list(2, start=0, end='5'), 'Invalid Type of end value in squared_power_list'

def test_squared_power_list_negative_startnumber():
    with pytest.raises(ValueError):
        session5.squared_power_list(2, start=-1, end=5), 'Negative Start is not acceptable in squared_power_list'

def test_squared_power_list_negative_endnumber():
    with pytest.raises(ValueError):
        session5.squared_power_list(2, start=1, end=-5), 'Negative End is not acceptable in squared_power_list'

# Test for Polygon Area

def test_polygon_area_extra_arg():
    with pytest.raises(TypeError):
        session5.polygon_area(15, 20, sides = 5), 'Extra args are not allowed in polygon_area'

def test_polygon_area_extra_kwarg():
    with pytest.raises(TypeError):
        session5.polygon_area(15, s_length = 20, sides = 5), 'kwargs are not allowed in polygon_area'

def test_polygon_area_invalid_sides():
    with pytest.raises(TypeError):
        session5.polygon_area(15, sides = 2), 'Minimum Traingle is needed to calculate area!'

def test_polygon_area_invalidmax_sides():
    with pytest.raises(TypeError):
        session5.polygon_area(15, sides = 7), 'Maximum Hexagonal is allowed to calculate area!'

def test_polygon_area_invalid_s_length():
    with pytest.raises(TypeError):
        session5.polygon_area(0, sides = 2), 'Polygon side length cannot be Zero!'

def test_polygon_area_negative_side():
    with pytest.raises(TypeError):
        session5.polygon_area(0, sides = -2), 'Polygon side cannot be Negative!'

def test_polygon_area_invalid_length():
    with pytest.raises(TypeError):
        session5.polygon_area(-10, sides = 5), 'Invalid length of side!'

# test for temp_converter
def test_temp_converter_extra_args():
    with pytest.raises(TypeError):
        session5.temp_converter(56,0,temp_given_in='f'), 'Extra args are not allowed in temp_converter'

def test_temp_converter_extra_kwargs():
    with pytest.raises(TypeError):
        session5.temp_converter(56,0,temp_given_in='f', temp_given_inn='c'), 'kwargs are not allowed in temp_converter'

def test_temp_converter_wrong_temp_given_in():
    with pytest.raises(ValueError):
        session5.temp_converter(56,temp_given_in='a'), 'Only c or f is allowed at temp_given_in in temp_converter'

def test_temp_converter_wrongtype_temp():
    with pytest.raises(TypeError):
        session5.temp_converter('56',temp_given_in='c'), 'Temperature input type error in temp_converter'

def test_temp_converter_temp_decimal():
        assert 13.3 != session5.temp_converter(56,temp_given_in='c'), 'float of farenheit will not match with default float in temp_converter'

def test_temp_converter_negative_temp():
    with pytest.raises(ValueError):
        session5.temp_converter(-56,temp_given_in='c'), 'Negative temperature is not allowed in temp_converter'

def test_temp_converter_nonstringin_temp_given_in():
    with pytest.raises(ValueError):
        session5.temp_converter(56,temp_given_in=0), 'Temperature unit cannot be anything other than string in temp_converter'

# tests for speed converter
def test_speed_converter_extra_args():
    with pytest.raises(TypeError):
        session5.speed_converter(70,40, dist='km', time='min'), 'Extra args are not allowed'

def test_speed_converter_extra_kwargs():
    with pytest.raises(TypeError):
        session5.speed_converter(70, dist='km', time='min', velocity = 56), 'kwargs are not allowed'

def test_speed_converter_invalid_value_speed_given():
    with pytest.raises(ValueError):
        session5.speed_converter(-70, dist='km', time='min'), 'Speed cannot be negative!'

def test_speed_converter_invalid_type_speed_given():
    with pytest.raises(TypeError):
        session5.speed_converter('70', dist='km', time='min'), 'Invalid speed type!'

def test_speed_converter_invalid_value_dist():
    with pytest.raises(ValueError):
        session5.speed_converter(70, dist='miles', time='min'), 'Invalid distnace unit'

def test_speed_converter_invalid_value_time():
    with pytest.raises(ValueError):
        session5.speed_converter(70, dist='km', time='hour'), 'Invalid time unit'

def test_speed_converter_invalid_type_dist():
    with pytest.raises(ValueError):
        session5.speed_converter(70, dist=0, time='min'), 'Invalid distnace type'

def test_speed_converter_invalid_type_time():
    with pytest.raises(ValueError):
        session5.speed_converter(70, dist='km', time=9), 'Invalid time type'

def test_speed_converter_name_error_dist():
    with pytest.raises(NameError):
        session5.speed_converter(70, dist=km, time='min'), 'distance name error'

def test_speed_converter_name_error_time():
    with pytest.raises(NameError):
        session5.speed_converter(70, dist='km', time=hr), 'time name error'

def test_speed_converter_to_m_ms():
    assert 1 == session5.speed_converter(3600, dist='m', time='ms'), "speed_converter is not correct for m/ms"

def test_speed_converter_to_m_s():
    assert 1000 == session5.speed_converter(3600, dist='m', time='s'), "speed_converter is not correct for m/s"

def test_speed_converter_to_m_min():
    assert 60000 == session5.speed_converter(3600, dist='m', time='min'), "speed_converter is not correct for m/min"

def test_speed_converter_to_m_hr():
    assert 3600000 == session5.speed_converter(3600, dist='m', time='hr'), "speed_converter is not correct for m/hr"

def test_speed_converter_to_m_day():
    assert 86400000 == session5.speed_converter(3600, dist='m', time='day'), "speed_converter is not correct for km/day"

def test_speed_converter_to_km_ms():
    assert .001 == session5.speed_converter(3600, dist='km', time='ms'), "speed_converter is not correct for km/ms"

def test_speed_converter_to_km_s():
    assert 1 == session5.speed_converter(3600, dist='km', time='s'), "speed_converter is not correct for km/s"

def test_speed_converter_to_km_min():
    assert 60 == session5.speed_converter(3600, dist='km', time='min'), "speed_converter is not correct for km/min"

def test_speed_converter_to_km_hr():
    assert 3600 == session5.speed_converter(3600, dist='km', time='hr'), "speed_converter is not correct for km/hr"

def test_speed_converter_to_km_day():
    assert 86400 == session5.speed_converter(3600, dist='km', time='day'), "speed_converter is not correct for km/day"








