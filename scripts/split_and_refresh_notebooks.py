#!/usr/bin/env python3
"""One-off maintainer script: split legacy notebook and normalize cells for execution."""

from __future__ import annotations

import ast
import json
import re
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "LearnPythonEasy.ipynb"
OUT_DIR = ROOT / "notebooks"

CHAPTERS: list[tuple[str, str, int, int]] = [
    ("01", "intro_and_language", 0, 5),
    ("02", "conditionals", 5, 17),
    ("03", "loops", 17, 27),
    ("04", "variables", 27, 37),
    ("05", "functions", 37, 49),
    ("06", "modules", 49, 51),
    ("07", "classes", 51, 57),
    ("08", "datatypes_appendix", 57, 76),
]

PSEUDO_MARKERS = (
    "买西瓜",
    "水果店打折",
    "鲜丰水果",
    "与老板讲价",
    "买[水果名]",
    "实例练习2：",
    "带西瓜回家",
    "休息一天",
)


def is_pseudo_python(source: str) -> bool:
    if any(m in source for m in PSEUDO_MARKERS):
        return True
    try:
        ast.parse(source)
    except SyntaxError:
        return True
    # Parses but uses undefined Chinese identifiers as statements
    if re.search(r"^\s*买", source, re.M):
        return True
    return False


def pseudo_to_markdown(source: str) -> str:
    body = source.rstrip()
    return f"以下为**示意伪代码**（不可直接运行），帮助理解逻辑：\n\n```python\n{body}\n```\n"


def patch_executable_cells(cells: list[dict]) -> list[dict]:
    """Make cells runnable in headless CI without changing teaching intent."""
    out: list[dict] = []
    for cell in cells:
        if cell["cell_type"] != "code":
            out.append(cell)
            continue
        src = "".join(cell.get("source", []))
        if is_pseudo_python(src):
            out.append(
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": pseudo_to_markdown(src).splitlines(keepends=True),
                }
            )
            continue
        if "#tempconvert" in src and "while (True)" in src:
            src = src.replace(
                "while (True):\n    degree = input ",
                "samples = ['36C', '100F', 'bad']\n"
                "for degree in samples:\n    # 课堂演示用固定样例；本地可改回 input()\n    ",
            )
            cell = deepcopy(cell)
            cell["source"] = src.splitlines(keepends=True)
        if "number guessing game" in src.lower() or "secret_number" in src:
            src = (
                "# 演示版：用固定猜测序列代替 input()，便于自动运行\n"
                "import random\n"
                "random.seed(0)\n"
                "secret_number = random.randint(1, 20)\n"
                "print('我想了一个数，在1到20间。')\n"
                "demo_guesses = [10, 15, secret_number]\n"
                "guess = demo_guesses[0]\n"
                "for guesses_taken, guess in enumerate(demo_guesses, start=1):\n"
                "    print(f'演示猜测: {guess}')\n"
                "    if guess < secret_number:\n"
                "        print('小了。')\n"
                "    elif guess > secret_number:\n"
                "        print('大了。')\n"
                "    else:\n"
                "        break\n"
                "if guess == secret_number:\n"
                "    print(f'很好! 你用了{guesses_taken}次猜中了!')\n"
                "else:\n"
                "    print(f'好吧。其实我想的数是{secret_number}。')\n"
            )
            cell = deepcopy(cell)
            cell["source"] = src.splitlines(keepends=True)
        if "What is your age?" in src:
            src = (
                "# 演示版：用变量代替 input()\n"
                "age = '20'\n"
                "print(f'假设年龄输入为 {age}')\n"
                "print('I see. You will be ' + str(int(age) + 1) + ' in a year.')\n"
            )
            cell = deepcopy(cell)
            cell["source"] = src.splitlines(keepends=True)
        if "import turtle" in src and "drawSnake" in src:
            out.append(
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "**实例练习：画 snake（可选）**\n",
                        "\n",
                        "原示例使用 `turtle` 图形库，需要本机安装带 Tk 的 Python。"
                        "在无图形界面的环境（如部分 CI）中无法运行。请在本地 Jupyter 中执行原代码，"
                        "或查阅 [turtle 文档](https://docs.python.org/3/library/turtle.html)。\n",
                    ],
                }
            )
            continue
        out.append(cell)
    return out


def chapter_header(num: str, slug: str, title: str) -> list[str]:
    return [
        f"# {num} · {title}\n",
        "\n",
        "本仓库为[通俗学 Python](https://github.com/rogerjsxu/Python3-Basics) 拆分章节。"
        "原文改编自知乎[水风](https://www.zhihu.com/question/60766946/answer/183072131)。\n",
        "\n",
        f"**文件**：`notebooks/{num}_{slug}.ipynb`\n",
    ]


TITLES = {
    "intro_and_language": "引子与编程语言",
    "conditionals": "判断（if / elif / else）",
    "loops": "循环（for / while）",
    "variables": "变量与作用域",
    "functions": "函数",
    "modules": "模块与文件",
    "classes": "类与对象",
    "datatypes_appendix": "附录：数据类型",
}


def new_notebook(cells: list[dict]) -> dict:
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "pygments_lexer": "ipython3",
            },
        },
        "cells": cells,
    }


def write_nb(path: Path, cells: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(new_notebook(cells), f, ensure_ascii=False, indent=1)
        f.write("\n")


def main() -> None:
    with LEGACY.open(encoding="utf-8") as f:
        legacy = json.load(f)
    all_cells = legacy["cells"]

    for num, slug, start, end in CHAPTERS:
        chunk = deepcopy(all_cells[start:end])
        header = {
            "cell_type": "markdown",
            "metadata": {},
            "source": chapter_header(num, slug, TITLES[slug]),
        }
        chunk = [header] + patch_executable_cells(chunk)
        write_nb(OUT_DIR / f"{num}_{slug}.ipynb", chunk)

    print(f"Wrote {len(CHAPTERS)} notebooks under {OUT_DIR}")


if __name__ == "__main__":
    main()
