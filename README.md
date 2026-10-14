# utils-demo

一个用于单元测试演示的 Python 工具库。原单文件模块 `src/utils.py` 已按职责重构拆分为多个子模块。

## 项目结构

```
src/
├── __init__.py     # 包入口，重新导出全部公共 API（推荐 from src import ...）
├── math_ops.py     # add、divide
├── text_ops.py     # is_palindrome、fizzbuzz
├── counters.py     # Counter 类
└── utils.py        # ⚠️ 兼容层（弃用），仅做转发并触发 DeprecationWarning
tests/
├── conftest.py         # pytest 公共 fixture
├── test_math_ops.py
├── test_text_ops.py
├── test_counters.py
└── test_compat_utils.py  # 验证旧导入路径的向后兼容性
```

## 迁移指南

| 旧写法 | 新写法 |
| ------ | ------ |
| `from src.utils import add, divide` | `from src.math_ops import add, divide` |
| `from src.utils import is_palindrome, fizzbuzz` | `from src.text_ops import is_palindrome, fizzbuzz` |
| `from src.utils import Counter` | `from src.counters import Counter` |

也可以直接从包级导入：`from src import add, Counter`。

`src.utils` 兼容层仍可使用，但会发出 `DeprecationWarning`，将在未来版本移除。

## 运行测试

```bash
python -m pytest tests -v
```
