"""src/utils.py 的单元测试（基于 pytest）。

运行方式：
    python -m pytest tests -v
"""

import pytest

from src.utils import Counter, add, divide, fizzbuzz, is_palindrome


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


# ---------- is_palindrome ----------
class TestIsPalindrome:
    @pytest.mark.parametrize(
        "text, expected",
        [
            ("level", True),
            ("A man a plan a canal Panama", True),
            ("Was it a car or a cat I saw?", True),
            ("hello", False),
            ("", True),          # 空串视为回文
            ("12321", True),     # 数字回文
            ("Racecar", True),   # 忽略大小写
        ],
    )
    def test_is_palindrome(self, text, expected):
        assert is_palindrome(text) is expected


# ---------- fizzbuzz ----------
class TestFizzBuzz:
    def test_basic_sequence(self):
        assert fizzbuzz(1) == "1"
        assert fizzbuzz(5) == "1 2 Fizz 4 Buzz"

    def test_fifteen_is_fizzbuzz(self):
        result = fizzbuzz(15).split()
        assert result[14] == "FizzBuzz"

    def test_full_output_1_to_15(self):
        expected = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
        assert fizzbuzz(15) == expected

    @pytest.mark.parametrize("n", [0, -1, -100])
    def test_invalid_input_raises(self, n):
        with pytest.raises(ValueError):
            fizzbuzz(n)


# ---------- Counter ----------
class TestCounter:
    def test_default_initial_value(self):
        assert Counter().value == 0

    def test_custom_initial_value(self):
        assert Counter(initial=10).value == 10

    def test_increment(self):
        c = Counter()
        assert c.increment() == 1
        assert c.increment(step=5) == 6
        assert c.value == 6

    def test_decrement(self):
        c = Counter(initial=3)
        assert c.decrement() == 2
        assert c.decrement(step=10) == -8

    def test_reset(self):
        c = Counter(initial=100)
        c.reset()
        assert c.value == 0

    def test_fixture_usage(self, counter):
        """使用 conftest.py 中定义的 fixture。"""
        assert counter.value == 0
        counter.increment()
        assert counter.value == 1
