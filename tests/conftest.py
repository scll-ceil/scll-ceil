"""pytest 公共配置与 fixture。"""

import sys
from pathlib import Path

# 确保可以从项目根目录导入 src 包
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from src.utils import Counter


@pytest.fixture
def counter() -> Counter:
    """提供一个初始值为 0 的计数器。"""
    return Counter()
