"""
测试add函数测试的一些测试用例函数
"""
from target.tools import add


def add_integer():
    result = add(6,19)
    #断言add函数的实际返回结果actual等于预期值25
    assert result == 25

def add_integer_float():
    result = add(3,2.73)
    assert result == 5.73


def add():
    result = add(6.17,2.632,2)
    assert result == 8.80