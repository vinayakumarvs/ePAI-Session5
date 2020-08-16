import time
from math import tan, pi

def time_it(fn, *args, repetitions = 1, **kwargs):
    # start = time.perf_counter()
    if repetitions < 0:
        raise ValueError('Enter proper repetitions')
    start = time.time()
    for i in range(repetitions):
        fn(*args, **kwargs)
        # return args, kwargs
        # print(fn)
    # end = time.perf_counter()
    end = time.time()
    return (end - start) / repetitions

def squared_power_list(n, *args, start = 0, end):
    results = []
    if n <= 0:
        raise ValueError('Negative values & Zero are not allowed!')
    elif start >= end:
        raise ValueError('End Value should be greater than start value')
    elif start < 0 or end < 0:
        raise ValueError('Negative start or end is not acceptable')
    else:
        for i in range(start, end):
            results.append(n**i)
            # results = print('Power square of {} is {}'.format (n,results))
    return results

def polygon_area(n, *args, sides, length):
    if length <= 0:
        raise ValueError ("Input Valid length of polygon")
    elif sides >= 3 and sides <= 6:
        p_area = sides * (length ** 2) / (4 * tan(pi / sides))
        p_area = print('polygon area is {}'.format (p_area))
    else:
        raise ValueError ("Can find an area for a minimum Triangle to maximum Hexagon")
    return p_area

def temp_converter(n, temp_given_in = 'f'):
    if temp_given_in not in ('c', 'f'):
        raise ValueError("please provide the unit as c or f")
    if temp_given_in == 'f' and n > 0:
        result = (n - 32) / 1.8000
        # result = print('{}F° = {}C°'.format (n, result))
    elif temp_given_in == 'c' and n > 0:
        result = (n * 1.8000) + 32
        # result = print('{}C° = {}F°'.format (n, result))
    else:
        raise ValueError ("Temperature should be either in C°:'c' or F°: 'f' and it cannot be zero or negative")
    return result

def speed_converter(speed, dist, time):
    if dist not in ('km', 'm', 'ft', 'yrd'):
        raise ValueError("Distance units can be only in - km, m, ft, yrd")

    if time not in ('ms', 's', 'min', 'hr', 'day'):
        raise ValueError("Time units can be only in - ms, s, min, hr, day")

    if speed<0:
        raise ValueError("Speed cannot be negative")

    if dist == 'km':
        if time == 'ms':
            result = speed/3600000
        if time == 's':
            result = speed/3600
        if time == 'min':
            result = speed/60
        if time == 'hr':
            result = speed
        if time == 'day':
            result = speed*24

    if dist == 'm':
        if time == 'ms':
            result = speed/3600
        if time == 's':
            result = speed/3.6
        if time == 'min':
            result = speed/.06
        if time == 'hr':
            result = speed*1000
        if time == 'day':
            result = speed*24000

    if dist == 'ft':
        if time == 'ms':
            result = speed*3280.84/3600000
        if time == 's':
            result = speed*3280.84/3600
        if time == 'min':
            result = speed*3280.84/60
        if time == 'hr':
            result = speed*3280.84
        if time == 'day':
            result = speed*3280.84*24

    if dist == 'yrd':
        if time == 'ms':
            result = speed*1093.6132/3600000
        if time == 's':
            result = speed*1093.6132/3600
        if time == 'min':
            result = speed*1093.6132/60
        if time == 'hr':
            result = speed*1093.6132
        if time == 'day':
            result = speed*1093.6132*24
    return result