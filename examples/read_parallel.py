"""Read a tiny bilingual TSV corpus (teaching example)."""

from __future__ import annotations

from pathlib import Path


def load_parallel_tsv(path: Path) -> list[tuple[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return []
    rows: list[tuple[str, str]] = []
    for line in lines[1:]:
        if not line.strip():
            continue
        source, target = line.split("\t", maxsplit=1)
        rows.append((source, target))
    return rows


def main() -> None:
    data = Path(__file__).resolve().parent / "data" / "parallel_sample.tsv"
    for en, zh in load_parallel_tsv(data):
        print(f"{en}\n  → {zh}\n")


if __name__ == "__main__":
    main()
