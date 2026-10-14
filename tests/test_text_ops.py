"""src/text_ops.py 的单元测试（基于 pytest）。"""

import pytest

from src.text_ops import fizzbuzz, is_palindrome


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
