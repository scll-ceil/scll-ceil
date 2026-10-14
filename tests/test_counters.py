"""src/counters.py 的单元测试（基于 pytest）。"""

from src.counters import Counter


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
