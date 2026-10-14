"""数学运算相关工具函数。"""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """返回两个数之和。"""
    return a + b


def divide(a: float, b: float) -> float:
    """返回 a / b，除数为 0 时抛出 ValueError。"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b
