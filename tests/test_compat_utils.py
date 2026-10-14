"""src/utils.py 兼容层的单元测试：验证旧导入路径仍然可用且发出弃用警告。"""

import warnings

import pytest


def test_legacy_import_still_works():
    """旧的 ``from src.utils import ...`` 路径应保持可用。"""
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        from src.utils import Counter, add, divide, fizzbuzz, is_palindrome  # noqa: F401

    assert any(issubclass(w.category, DeprecationWarning) for w in caught)
    assert add(1, 2) == 3
    assert divide(4, 2) == 2
    assert is_palindrome("level")
    assert fizzbuzz(3) == "1 2 Fizz"
    assert Counter().value == 0


def test_package_level_import_matches_submodules():
    """``src`` 包级导出应与各子模块为同一对象。"""
    import src
    import src.counters
    import src.math_ops
    import src.text_ops

    assert src.add is src.math_ops.add
    assert src.divide is src.math_ops.divide
    assert src.is_palindrome is src.text_ops.is_palindrome
    assert src.fizzbuzz is src.text_ops.fizzbuzz
    assert src.Counter is src.counters.Counter


@pytest.mark.parametrize("name", ["add", "divide", "is_palindrome", "fizzbuzz", "Counter"])
def test_all_exports(name):
    import src

    assert name in src.__all__
    assert hasattr(src, name)
