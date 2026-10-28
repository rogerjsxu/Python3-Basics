# Python3-Basics

面向**零基础**读者的中文 Python 入门仓库，在保持「通俗、轻量」的前提下，增加了**翻译技术（译技）**方向的示例与练习：平行语料、术语表 CSV、项目路径、轻量字符串清洗等，帮助翻译、本地化相关专业的同学理解「为什么学 Python」。

## 来源与致谢

- 核心叙述改编自知乎 [水风](https://www.zhihu.com/question/60766946/answer/183072131) 的回答，向原作者致谢。
- 原仓库自 2020 年起维护；本次翻新（2026）主要做了：**章节拆分**、**译技向示例**、依赖与许可证、以及可自动运行的 Notebook 整理。详见各 Notebook 首单元与 `legacy/`（若保留旧版单文件）。

## 适合谁

- 从未写过代码的翻译 / 本地化 / 语言服务相关初学者。
- 需要先用通用语法入门，再接触语料、术语、文件路径等**译技常见场景**的同学。
- **不**面向：Web 全栈、深度学习、大型 CAT 二次开发（本仓库不引入重型框架）。

## 环境要求

- **Python 3.10+**（推荐 3.11 或 3.12）
- 可选： [JupyterLab](https://jupyter.org/) 或 VS Code 的 Jupyter 扩展

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

在浏览器中打开 `notebooks/` 下文件，**按文件名序号**学习。

### 其他环境

若使用 Google Colab 等在线 Notebook，请先克隆本仓库再打开 `notebooks/` 下文件；示例数据在 `examples/data/`，Notebook 内 `../examples/...` 相对路径与本地一致。

## 学习顺序

| 顺序 | Notebook | 内容 |
|------|----------|------|
| 01 | `notebooks/01_intro_and_language.ipynb` | 引子、编程语言 |
| 02 | `notebooks/02_conditionals.ipynb` | 判断 |
| 03 | `notebooks/03_loops.ipynb` | 循环 |
| 04 | `notebooks/04_variables.ipynb` | 变量 |
| 05 | `notebooks/05_functions.ipynb` | 函数 |
| 06 | `notebooks/06_modules.ipynb` | 模块与文件（含 pathlib / csv / 清洗） |
| 07 | `notebooks/07_classes.ipynb` | 类与对象 |
| 08 | `notebooks/08_datatypes_appendix.ipynb` | 附录：数据类型 |
| 09 | `notebooks/09_translation_tech_practice.ipynb` | 译技综合小练习 |

配套脚本（可选命令行体验）：

- `examples/read_parallel.py` — 读取示例 TSV 平行句对
- `examples/clean_segment.py` — 简单句段清洗

根目录 `LearnPythonEasy.ipynb` 为**历史单文件版本**（2020 合订本），内容与拆分章节同源；**建议以 `notebooks/` 为准**。

## 译技向定位说明

- 语法讲解仍以通用入门为主（变量、分支、循环、函数等）。
- **领域味道**体现在：术语表、双语 TSV、项目目录结构、MT/PE 场景下的字符串处理，以及 2～3 个短练习（见 02、06、09 章）。
- 示例数据均为虚构或可公开使用的短句，**不包含**任何私有课程资料或凭据。

## 许可

[MIT License](LICENSE)
