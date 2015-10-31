# -*- coding: utf-8 -*- 
# user: youzipi
# date: 15-10-28 下午1:05
import datetime
import functools
import time
from decorator import decorator

current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
DEBUG = 'debug'


def log0(func):
    def wrapper(*args, **kwargs):
        print current, ": call %s()" % func.__name__
        print (args, kwargs)
        func(*args, **kwargs)
        # return func(*args, **kwargs)

    return wrapper


def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print current, "call %s()" % func.__name__
        func(*args, **kwargs)
        # return func(*args, **kwargs)

    return wrapper


def log2(suffix='info'):
    def decorator(func):  # equal to log1
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print current, "[%s]: call %s()" % (suffix, func.__name__)
            return func(*args, **kwargs)  # execute target function

        return wrapper

    return decorator


# Flask-like class-based decorator
class Log:
    def __init__(self):
        pass

    @classmethod
    def debug(cls):
        def decorator(func):  # equal to log1
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print current, "[%s]: call %s()" % ("debug", func.__name__)
                return func(*args, **kwargs)  # execute target function

            return wrapper

        return decorator


def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print "timed"
        start = time.clock()
        func(*args, **kwargs)
        end = time.clock()
        print 'used:', end - start
        # return func(*args, **kwargs)

    return wrapper


@decorator
def timed2(func, *args, **kwargs):
        print "timed"
        start = time.clock()
        func(*args, **kwargs)
        end = time.clock()
        print 'used:', end - start
        return func(*args, **kwargs)



log = Log()


@log.debug()
def add(a, b):
    print a + b


@log2('debug')
def add2(a, b):
    print a + b


@log1
@timed2
def multiply(numbers):
    """
    Multiple decorators
    equals to log1( timed( multiply(numbers) ) )
    output>>
        # the outer function execute first
        2015-10-28 16:38:00 call multiply() #log1
        timed   #timed
        120
        used: 2.4e-05   #timed
    """
    print reduce(lambda a, b: a * b, numbers)


# add(1, 2)

# add2(1, 2)

multiply([1, 2, 3, 4, 5])
