"""src/math_ops.py 的单元测试（基于 pytest）。"""

import pytest

from src.math_ops import add, divide


# ---------- add ----------
class TestAdd:
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
            (2.5, 2.5, 5.0),
            (-3, -7, -10),
        ],
    )
    def test_add(self, a, b, expected):
        assert add(a, b) == expected

    def test_add_is_commutative(self):
        assert add(3, 8) == add(8, 3)


# ---------- divide ----------
class TestDivide:
    def test_divide_normal(self):
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5

    def test_divide_negative(self):
        assert divide(-9, 3) == -3

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="除数不能为 0"):
            divide(1, 0)
