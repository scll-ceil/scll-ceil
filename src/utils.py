"""常用工具函数模块，供单元测试演示使用。"""

from __future__ import annotations


def add(a: float, b: float) -> float:
    """返回两个数之和。"""
    return a + b


def divide(a: float, b: float) -> float:
    """返回 a / b，除数为 0 时抛出 ValueError。"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


def is_palindrome(text: str) -> bool:
    """判断字符串是否为回文（忽略大小写和非字母数字字符）。"""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def fizzbuzz(n: int) -> str:
    """返回 1..n 的 FizzBuzz 结果，以空格拼接。"""
    if n <= 0:
        raise ValueError("n 必须为正整数")
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return " ".join(result)


class Counter:
    """简单计数器。"""

    def __init__(self, initial: int = 0):
        self._count = initial

    @property
    def value(self) -> int:
        return self._count

    def increment(self, step: int = 1) -> int:
        self._count += step
        return self._count

    def decrement(self, step: int = 1) -> int:
        return self.increment(-step)

    def reset(self) -> None:
        self._count = 0
