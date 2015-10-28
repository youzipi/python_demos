# -*- coding: utf-8 -*- 
# user: youzipi
# date: 15-10-28 下午1:05
import datetime

current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log(func):
    def wrapper(*args, **kwargs):
        print current, ": call %s()" % func.__name__
        print (args, kwargs)
        return func(*args, **kwargs)

    return wrapper


@log
def add(a, b):
    print a + b


add(1, 2)
