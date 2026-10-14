"""src 包：工具函数按职责拆分为 math_ops / text_ops / counters 子模块。

为保持向后兼容，本包同时重新导出所有公共 API，
既有的 ``from src.utils import ...`` 与新的 ``from src import ...`` 均可使用。
"""

from __future__ import annotations

from src.counters import Counter
from src.math_ops import add, divide
from src.text_ops import fizzbuzz, is_palindrome

__all__ = [
    "Counter",
    "add",
    "divide",
    "fizzbuzz",
    "is_palindrome",
]
