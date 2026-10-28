"""Light string cleaning for MT/PE-style segments."""

from __future__ import annotations

import re


def clean_segment(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


if __name__ == "__main__":
    sample = "  Terminology   <i>check</i>\u00a0failed  "
    print(clean_segment(sample))
