"""计数器类。"""

from __future__ import annotations


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
