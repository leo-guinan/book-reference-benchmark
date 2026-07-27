from pathlib import Path
import json
import os
import re

ROOT = Path(__file__).parents[1]
default_candidates = [
    ROOT / "benchmarks/art-of-time-and-war",
    ROOT.parent / "book-reference-benchmark" / "benchmarks/art-of-time-and-war",
]
default_contracts = next((path for path in default_candidates if path.exists()), default_candidates[0])
contracts = Path(os.environ.get("BENCHMARK_ROOT", default_contracts))
worksheets = ROOT / "worksheets"

for n in range(1, 14):
    path = worksheets / f"chapter-{n:02d}.md"
    assert path.exists(), path
    contract = json.loads((contracts / f"chapter-{n:02d}" / "benchmark.json").read_text())
    text = path.read_text()
    assert f"# Chapter {n}: {contract['chapter']['title']}" in text
    assert contract["id"] in text
    for item in contract["evaluation_items"]["held_out"]:
        assert item["prompt"] in text, (n, item["id"])
    assert "## 4. Transfer" in text
assert (worksheets / "final-book.md").exists()
assert len(list(worksheets.glob("chapter-*.md"))) == 13
print("reader worksheets validated: 13 chapter worksheets + final-book worksheet")
