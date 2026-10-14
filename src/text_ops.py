"""文本处理相关工具函数。"""

from __future__ import annotations


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
