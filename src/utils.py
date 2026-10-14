"""兼容层：旧版单文件工具模块。

本模块已按职责拆分为：
- :mod:`src.math_ops` —— add、divide
- :mod:`src.text_ops` —— is_palindrome、fizzbuzz
- :mod:`src.counters` —— Counter

请勿在新代码中引用本模块，直接导入对应子模块或 ``src`` 包即可。
"""

from __future__ import annotations

import warnings

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

warnings.warn(
    "src.utils 已拆分至 src.math_ops / src.text_ops / src.counters，"
    "请改用新的模块路径（src.utils 兼容层将在未来版本移除）。",
    DeprecationWarning,
    stacklevel=2,
)
